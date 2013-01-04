import BaseTestCase
import nose
import sys

class TestYouTubeUserFeeds(BaseTestCase.BaseTestCase):

    def test_plugin_should_list_user_favorites_video_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].settings.setSetting("perpage", "5")

        self.navigation.listMenu({"feed": "favorites", "login": "true", "path": "/root/favorites"})

        self.assert_directory_count_greater_than_or_equals(20)
        self.assert_directory_count_less_than_or_equals(50)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_favorites_video_list_page_2_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].settings.setSetting("perpage", "2")

        self.navigation.listMenu({"feed": "favorites", "login": "true", "page": "1", "path": "/root/favorites"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_playlists_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "playlists", "login": "true", "path": "/root/playlists", "folder": "true"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_folder_list()
        self.assert_directory_item_urls_contain("playlist")

    def test_plugin_should_list_user_uploads_videos_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"feed": "uploads", 'login': 'true', "path": "/root/uploads"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_uploads_videos_list_page_2_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        sys.modules["__main__"].settings.setSetting("perpage", "0")

        self.navigation.listMenu({"feed": "uploads", 'login': 'true', "page": "1", "path": "/root/uploads"})

        self.assert_directory_count_greater_than_or_equals(5)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_watch_later_video_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "watch_later", 'login': 'true', "path": "/root/watch_later"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()
        self.assert_directory_item_urls_contain("playlist_entry_id")

    def test_plugin_should_list_user_recommended_video_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "recommended", 'login': 'true', "path": "/root/watch_later"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_watch_later_video_list_page_2_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        self.navigation.listMenu({"user_feed": "watch_later", 'login': 'true', "page": "1", "path": "/root/watch_later"})

        self.assert_directory_count_greater_than_or_equals(5)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()
        self.assert_directory_item_urls_contain("playlist_entry_id")

    def test_plugin_should_list_user_playlist_video_list_correctly_(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "playlist", 'login': 'true', "path": "/root/playlist/smokey", "playlist": "E3E0C28746217FA6"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_should_have_next_folder()
        self.assert_directory_is_a_video_list()

    def test_plugin_should_list_user_playlist_video_list_page_2_correctly_(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "playlist", 'login': 'true', "path": "/root/playlist/smokey", "playlist": "E3E0C28746217FA6", "page": "1"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()

    def test_plugin_should_list_user_contacts_folder_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "contacts", 'login': 'true', "path": "/root/contacts/smokey", "folder": "true"})

        self.assert_directory_count_greater_than_or_equals(2)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_folder_list()
        self.assert_directory_item_urls_contain("contact")

    def test_plugin_should_list_user_subscriptions_folder_list_correctly_(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "subscriptions", 'login': 'true', "folder": "true", "path": "/root/subscriptions/something/smokey"})

        self.assert_directory_count_greater_than_or_equals(2)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_folder_list()
        self.assert_directory_item_urls_contain("channel")

    def test_plugin_should_list_newsubscriptions_video_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")

        self.navigation.listMenu({"user_feed": "newsubscriptions", "login": "true", "path": "/root/subscriptions/new"})

        self.assert_directory_count_greater_than_or_equals(10)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_contains_almost_only_unique_video_items()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_watched_history_video_list_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        self.navigation.listMenu({"user_feed": "watch_history", 'login': 'true', "path": "/root/history"})

        self.assert_directory_count_greater_than_or_equals(8)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

    def test_plugin_should_list_user_watched_history_video_list_page_2_correctly(self):
        sys.modules["__main__"].settings.load_strings("./resources/basic-login-settings-logged-in.xml")
        self.navigation.listMenu({"user_feed": "watch_history", 'login': 'true', "page": "1", "path": "/root/history"})

        self.assert_directory_count_greater_than_or_equals(8)
        self.assert_directory_count_less_than_or_equals(51)
        self.assert_directory_is_a_video_list()
        self.assert_directory_items_should_have_external_thumbnails()

if __name__ == "__main__":
    nose.runmodule()
