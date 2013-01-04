import xml.dom.minidom as minidom
import io


class xbmcLanguage:
    """
    Borg singleton config object
    """
    _we_are_one = {}
    _languageString = {}

    def __init__(self):
        self.__dict__ = self._we_are_one

    def _load_strings(self):
        print " *** *** loading language strings  *** ***"
        file = io.open("./resources/strings.xml").read()

        dom = minidom.parseString(file)
        strings = dom.getElementsByTagName("string")

        for string in strings:
            if string.firstChild:
                self._languageString[int(string.getAttribute("id"))] = string.firstChild.data

    def __call__(self, id):
        if not self._languageString:
            self._load_strings()

        if id in self._languageString:
            return self._languageString[id]
        return ""

if __name__ == "__main__":
    x = xbmcLanguage()
    print x(30230)
    print x(30232)
    x2 = xbmcLanguage()
    print x2(30232)
    print x2(30230)
