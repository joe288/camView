# Ihad.tv enigma2-plugin tutorial 2010
# lesson 1
# by emanuel
# start consolloging: root@dm8000:~# init 4; sleep 4; enigma2
###########################################################################
from Screens.Screen import Screen
from Components.Label import Label
from Components.ActionMap import ActionMap
from Plugins.Plugin import PluginDescriptor
###########################################################################
class HalloWorldScreen(Screen):
    skin = """
        <screen position="130,150" size="460,150" title="Ihad.tv e2-tutorial
        lesson 1" >
        <widget name="myLabel" position="10,60" size="200,40"
        font="Regular;20"/>
        </screen>"""
    def __init__(self, session, args = None):
        self.session = session
        Screen.__init__(self, session)
        self["myLabel"] = Label("Ich Hello World ;-)")
        self["myActionMap"] = ActionMap(["SetupActions"],
        {
            "cancel": self.close # add the RC Command "cancel" to close your Screen
        }, -1)
        
###########################################################################
def main(session, **kwargs):
    print("\n[Hallo World] start\n")
    session.open(HalloWorldScreen)
###########################################################################
def Plugins(**kwargs):
    return PluginDescriptor(
        name="camView", description="enigam2 plugin to display a camera", where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)
