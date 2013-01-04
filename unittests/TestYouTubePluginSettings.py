import nose
import BaseTestCase
import sys
from YouTubePluginSettings import YouTubePluginSettings

class TestYouTubePluginSettings(BaseTestCase.BaseTestCase):

    def test_itemsPerPage_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()
        sys.modules["__main__"].settings.getSetting.return_value = "0"

        settings.itemsPerPage()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("perpage")

    def test_currentRegion_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()
        sys.modules["__main__"].settings.getSetting.return_value = "0"

        settings.currentRegion()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("region_id")

    def test_safeSearchLevel_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()
        sys.modules["__main__"].settings.getSetting.return_value = "0"

        settings.safeSearchLevel()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("safe_search")

    def test_requestTimeout_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()
        sys.modules["__main__"].settings.getSetting.return_value = "0"

        settings.requestTimeout()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("timeout")

    def test_userHasProvidedValidCredentials_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()
        sys.modules["__main__"].settings.getSetting.return_value = "0"

        settings.userHasProvidedValidCredentials()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("username")
        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("oauth2_access_token")


    def test_userName_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()

        settings.userName()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("username")

    def test_userPassword_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()

        settings.userPassword()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("user_password")

    def test_debugModeIsEnabled_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()

        settings.debugModeIsEnabled()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("debug")

    def test_authenticationRefreshRoken_should_call_settings_correctly(self):
        settings = YouTubePluginSettings()

        settings.authenticationRefreshRoken()

        sys.modules[ "__main__" ].settings.getSetting.assert_any_call("oauth2_refresh_token")

if __name__ == "__main__":
    nose.runmodule()
