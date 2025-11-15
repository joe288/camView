from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Plugins.Plugin import PluginDescriptor
from enigma import eServiceReference

class StreamScreen(Screen):
    skin = """
        <screen name="StreamScreen" position="0,0" size="720,576"
        title="RTSP Stream mit ServiceApp" backgroundColor="#000000">
        </screen>"""

    def __init__(self, session, stream_url):
        Screen.__init__(self, session)
        self.stream_url = stream_url

        self["actions"] = ActionMap(["SetupActions"], {
            "ok": self.closeScreen,
            "cancel": self.closeScreen
        }, -1)

        self.playStream()

    def playStream(self):
        ref = eServiceReference(5002, 0, self.stream_url)
        self.session.nav.playService(ref)
        print(f"[ServiceApp] Starte Stream: {self.stream_url}")

    def closeScreen(self):
        self.session.nav.stopService()
        self.close()
def main(session, **kwargs):
    username = "admin"
    password = "computer00"
    ip_address = "192.168.4.97"
    port = "554"  # Standardport für RTSP

    rtsp_url = f"rtsp://{username}:{password}@{ip_address}:{port}/h264Preview_01_main"
    session.open(StreamScreen, rtsp_url)

def Plugins(**kwargs):
    return PluginDescriptor(name="RTSP Stream Viewer", description="Zeigt einen RTSP-Stream in einem Widget", where=PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)
