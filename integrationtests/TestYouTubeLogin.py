import BaseTestCase
import nose
import sys
import time


class TestYouTubeLogin(BaseTestCase.BaseTestCase):
    totp = ""

    def test_plugin_should_perform_basic_login_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings.xml")

        assert(sys.modules["__main__"].settings.getSetting("auth") == "")
        assert(sys.modules["__main__"].settings.getSetting("oauth2_access_token") == "")

        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + sys.modules["__main__"].settings.getSetting("oauth2_access_token")

        self.navigation.executeAction({"action": "settings"})

        oauth2_access_token = sys.modules["__main__"].settings.getSetting("oauth2_access_token")
        login_cookies = sys.modules["__main__"].settings.getSetting("login_cookies")
        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + oauth2_access_token + " - " + str(len(oauth2_access_token))
        print "login_cookies: " + login_cookies + " - " + str(len(login_cookies))
        assert(len(oauth2_access_token) > 40)

    def test_plugin_should_perform_unlinked_login_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/unlinked-login-settings.xml")

        assert(sys.modules["__main__"].settings.getSetting("auth") == "")
        assert(sys.modules["__main__"].settings.getSetting("oauth2_access_token") == "")

        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + sys.modules["__main__"].settings.getSetting("oauth2_access_token")

        self.navigation.executeAction({"action": "settings"})

        oauth2_access_token = sys.modules["__main__"].settings.getSetting("oauth2_access_token")
        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + oauth2_access_token + " - " + str(len(oauth2_access_token))
        assert(len(oauth2_access_token) > 40)

    def test_plugin_should_perform_basic_2factor_login_correctly(self):
        import pyotp
        self.totp = pyotp.TOTP("fbfkkk27ffmaihzg")
        self.lastpin = False

        sys.modules["__main__"].settings.load_strings("./resources/2factor-login-settings.xml")
        tmp = sys.modules["__main__"].xbmcgui.Dialog()
        tmp.numeric.side_effect = self.generatePin

        assert(sys.modules["__main__"].settings.getSetting("auth") == "")
        assert(sys.modules["__main__"].settings.getSetting("oauth2_access_token") == "")

        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + sys.modules["__main__"].settings.getSetting("oauth2_access_token")

        self.navigation.executeAction({"action": "settings"})

        oauth2_access_token = sys.modules["__main__"].settings.getSetting("oauth2_access_token") 
        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + oauth2_access_token + " - " + str(len(oauth2_access_token))
        assert(len(oauth2_access_token) > 40)

    def test_plugin_should_perform_googleplus_login_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-plus.xml")

        assert(sys.modules["__main__"].settings.getSetting("auth") == "")
        assert(sys.modules["__main__"].settings.getSetting("oauth2_access_token") == "")

        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + sys.modules["__main__"].settings.getSetting("oauth2_access_token")

        self.navigation.executeAction({"action": "settings"})

        oauth2_access_token = sys.modules["__main__"].settings.getSetting("oauth2_access_token")
        print "username: " + sys.modules["__main__"].settings.getSetting("username")
        print "pass: " + sys.modules["__main__"].settings.getSetting("user_password")
        print "oauth2_access_token: " + oauth2_access_token + " - " + str(len(oauth2_access_token))
        assert(len(oauth2_access_token) > 40)

    def generatePin(self, *args, **kwargs):
        userpin = str(self.totp.at(time.time()))
        while len(userpin) < 6:
            userpin = "0" + userpin

        if userpin == self.lastpin:
            time.sleep(15)
            return self.generatePin(args, kwargs)
        print "GENERATED PIN : " + str(userpin)
        return userpin

if __name__ == "__main__":
    nose.runmodule()
