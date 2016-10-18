# -- PyPosty --
#
#   Version 2016-10-11 .1
#   by Turtle
#   Send any complaints directly into the nearest shredder
#   or zturnlund@kochava.com
#
# -- PyPosty --

# -- Version Control --
version = 'v.1'
debug = False
# -- Version Control --

# -- Dependencies --
import sys
import time
import PostyUI
import textwrap
import requests
import asyncio
from PyQt5.QtWidgets import QApplication, QMainWindow
# -- Dependencies --


# Payload Send Function
def SendPayload(endpoint, payload, response = True):
    r = requests.post(endpoint, payload)
    while (debug == True):
        try:
            s = requests.get('http://10.0.1.32:8080', payload)
            break
        except ValueError:
            print ('Send failed')
            pass
    while (response == True):
        try:
            return str(r.json())
            break
        except ValueError:
            return None
            pass
    return None


class PostyApp(QMainWindow, PostyUI.Ui_MainWindow):

    endpoint = 'http://control.kochava.com/track/json'
    payload = '{"data":"derp"}'
    currentTab = 'Install'

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect listener for post button
        self.postButton.clicked.connect(self.createPayload)

    def createPayload(self):
        if (self.tabWidget.currentIndex() == 0):
            idfa = '"' + self.installTabUserAgentValue.text() + '"'
            ua = '"' + self.installTabUserAgentValue.text() + '"'
            origip = '"' + self.eventTabIPValue.text() + '"'
            appguid = '"' + self.appGUIDValue.text() + '"'

            PostyApp.payload = """{
                                    "data": {
                                        "usertime": "",
                                        "device_ua": %s,
                                        "conversion_data": {
                                            "utm_campaign": "",
                                            "utm_medium": "",
                                            "utm_source": ""
                                        },
                                        "origination_ip": %s,
                                        "device_ids": {
                                            "udid": "",
                                            "mac": "",
                                            "idfa": %s,
                                            "imei": "",
                                            "adid": "",
                                            "odin": "",
                                            "android_id": ""
                                        }
                                    },
                                    "kochava_app_id": %s,
                                    "action": "install"
                                }""" % (ua, origip, idfa, appguid)
            self.installTabPayloadPreview.clear()
            self.installTabPayloadPreview.setPlainText(PostyApp.payload)

            return PostyApp.payload
        elif (self.tabWidget.currentIndex() == 1):
            appversion = '"1.0"'
            idfa = '"' + self.eventTabUserAgentValue.text() + '"'
            ua = '"' + self.eventTabUserAgentValue.text() + '"'
            deviceversion = '"1.1"'
            eventname = '"' + self.eventTabEventNameValue.text() + '"'
            origip = '"' + self.eventTabIPValue.text() + '"'
            appguid = '"' + self.appGUIDValue.text() + '"'

            PostyApp.payload = """{
                                    "data": {
                                        "app_version": %s,
                                        "device_ids": {
                                            "idfa": %s
                                        },
                                        "device_ua": %s,
                                        "device_ver": %s,
                                        "event_name": %s,
                                        "origination_ip": %s,
                                        "event_data": {
                                            "id": "123",
                                            "name": "Shoes",
                                            "currency": "USD",
                                            "sum": 100
                                        }
                                        },
                                    "action": "event",
                                    "kochava_app_id": %s
                                }""" % (appversion, idfa, ua, deviceversion, eventname, origip, appguid)
            self.eventTabPayloadPreview.clear()
            self.eventTabPayloadPreview.setPlainText(PostyApp.payload)

            return PostyApp.payload
        elif (self.tabWidget.currentIndex() == 2):
            PostyApp.payload = """
{
    "data": {
    },
}"""
            self.customTabPayloadValue.clear()
            self.customTabPayloadValue.setPlainText(PostyApp.payload)

            return PostyApp.payload





    def postButtonClicked(self):
        self.serverResponseCodeAll.clear()
        PostyApp.payload = self.createPayload()
        x = 1
        while x <= self.postQtyValue.value():
            # time.sleep(1)
            if (self.serverResponseCodeAll.toPlainText() == ""):
                self.serverResponseCodeAll.setText(str(SendPayload(PostyApp.endpoint, PostyApp.payload)))
            else:
                self.serverResponseCodeAll.setText(self.serverResponseCodeAll.toPlainText() + '\n' + str(
                    SendPayload(PostyApp.endpoint, PostyApp.payload)))
            x += 1

# Main Loop
if __name__ == '__main__':
    a = QApplication(sys.argv)
    app = PostyApp()
    app.show()

    sys.exit(a.exec_())


