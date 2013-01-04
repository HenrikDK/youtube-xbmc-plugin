import xml.dom.minidom as minidom
import io


class xbmcSettings():
    def __init__(self):
        self.settingsString = {}
        self.path = ""

    def load_strings(self, path="./resources/settings.xml"):
        print " *** *** loading settings strings *** ***"
        self.path = path
        file = io.open(path).read()
        self.dom = minidom.parseString(file)
        self.strings = self.dom.getElementsByTagName("setting")

        for string in self.strings:
            self.settingsString[string.getAttribute("id")] = string.getAttribute("value")

    def __call__(self, key="", value=""):
        if not self.settingsString:
            self.load_strings()

        if value:
            self.settingsString[key] = value
            if self.path.find("settings-logged-in") > -1:  # This only updates. No insert!
                for string in self.strings:
                    if string.getAttribute("id") == key:
                        string.setAttribute("value", value)
                f = open(self.path, 'w')
                self.dom.writexml(f)
                f.close()

        elif key in self.settingsString:
            return self.settingsString[key]

        return ""

    def __getattr__(self, name):
        return self

if __name__ == "__main__":
    x1 = xbmcSettings()
    print "x1: " + x1.getSetting("downloads")
    print "setting x1 = funkytown"
    x1.setSetting("downloads", "funkytown" )
    x2 = xbmcSettings()
    print "x2: " + x2.getSetting("downloads")
    print "x1: " + x1.getSetting("downloads")
