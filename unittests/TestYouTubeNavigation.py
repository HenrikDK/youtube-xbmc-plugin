# -*- coding: utf-8 -*-
import nose
import BaseTestCase
from mock import Mock
import sys
from YouTubeNavigation import YouTubeNavigation

class TestYouTubeNavigation(BaseTestCase.BaseTestCase):

    def test_listMenu_should_traverse_menustructure_correctly(self):
        sys.argv = ["something", -1, "something_else"]
        sys.modules["__main__"].settings.getSetting.return_value = "true"
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu()

        args = navigation.addListItem.call_args_list
        print repr(args)
        for arg in args:
                assert(arg[0][1]["path"].replace('/root/', '').find('/') < 0)
        assert(navigation.addListItem.call_count > 1)

    def test_listMenu_should_only_list_subfolders_to_a_path(self):
        sys.argv = ["something", -1, "something_else"]
        list = ["", "", "", ""]
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: list.pop()
        navigation = YouTubeNavigation()
        navigation.categories = ({"path": "/root/my_first_level"}, {"path": "/root/my_first_level/my_second_level"}, {"path": "/root/my_other_first_level"}, {"path": "/root/my_other_first_level/my_other_second_level"})
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/my_first_level"})

        navigation.addListItem.assert_called_with({"path": "/root/my_first_level"}, {"path": "/root/my_first_level/my_second_level"})

    def test_listMenu_should_use_visibility_from_settings_to_decide_if_items_are_displayed(self):
        sys.argv = ["something", -1, "something_else"]
        list = ["false", "true", "false", "true"]
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: list.pop()
        navigation = YouTubeNavigation()
        navigation.categories = ({"path": "/root/my_first_level"}, {"path": "/root/my_first_level/my_second_level1"}, {"path": "/root/my_first_level/my_second_level2"}, {"path": "/root/my_first_level/my_second_level3"})
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/my_first_level"})

        navigation.addListItem.assert_any_call({"path": "/root/my_first_level"}, {"path": "/root/my_first_level/my_second_level1"})
        navigation.addListItem.assert_any_call({"path": "/root/my_first_level"}, {"path": "/root/my_first_level/my_second_level3"})

    def test_listMenu_should_check_if_download_path_is_set_to_decide_if_download_folder_is_visible(self):
        sys.argv = ["something", -1, "something_else"]
        list = ["true", "true", "true", "", "true"]
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: list.pop()
        navigation = YouTubeNavigation()
        navigation.categories = ({"path": "/root/my_first_level/my_second_level1", "feed": "downloads"}, {"path": "/root/my_first_level/my_second_level2", "feed": "downloads"})
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/my_first_level"})
        
        navigation.addListItem.assert_called_with({"path": "/root/my_first_level"}, {"path": "/root/my_first_level/my_second_level2", "feed": "downloads"})
        
    def test_listMenu_should_call_list_if_feed_in_params(self):
        sys.argv = ["something", -1, "something_else"]
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/some_other_path", "feed": "some_feed"})
        
        navigation.list.assert_called_with({"path": "/root/some_other_path", "feed": "some_feed"})
        
    def test_listMenu_should_call_list_if_user_feed_in_params(self):
        sys.argv = ["something", -1, "something_else"]
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/some_other_path", "user_feed": "some_feed"})
        
        navigation.list.assert_called_with({"path": "/root/some_other_path", "user_feed": "some_feed"})
        
    def test_listMenu_should_call_list_if_options_in_params(self):
        sys.argv = ["something", -1, "something_else"]
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/some_other_path", "options": "some_options"})
        
        navigation.list.assert_called_with({"path": "/root/some_other_path", "options": "some_options"})
        
    def test_listMenu_should_call_list_if_store_in_params(self):
        sys.argv = ["something", -1, "something_else"]
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/some_other_path", "store": "some_store"})
        
        navigation.list.assert_called_with({"path": "/root/some_other_path", "store": "some_store"})
        
    def test_listMenu_should_call_list_if_scraper_in_params(self):
        sys.argv = ["something", -1, "something_else"]
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/some_other_path", "scraper": "some_scraper"})
        
        navigation.list.assert_called_with({"path": "/root/some_other_path", "scraper": "some_scraper"})
        
    def test_listMenu_should_call_settings_getSetting_to_get_listview(self):
        sys.argv = ["something", -1, "something_else"]
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        navigation.listMenu({"path": "/root/some_other_path"})
        
        sys.modules["__main__"].settings.getSetting.assert_called_with("list_view")

    def test_listMenu_should_call_xbmc_executeBuiltin_correctly_if_list_view_is_set(self):
        sys.argv = ["something", -1, "something_else"]
        settings = ["1", "true", "1"]
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: settings.pop()
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        
        navigation.listMenu({"path": "/root/some_other_path"})
        
        sys.modules["__main__"].xbmc.executebuiltin.assert_called_with('Container.SetViewMode(500)')
        
    def test_listMenu_should_call_xbmc_plugin_end_of_directory_correctly(self):
        sys.argv = ["something", -1, "something_else"]
        settings = ["1", "true", "1"]
        sys.modules["__main__"].settings.getSetting.side_effect = lambda x: settings.pop()
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.addListItem = Mock()
        
        navigation.listMenu({"path": "/root/some_other_path"})
        
        sys.modules["__main__"].xbmcplugin.endOfDirectory.assert_called_with(cacheToDisc=True, handle=-1, succeeded=True)

    def test_executeAction_should_call_login_login_if_action_is_settings(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "settings"})
        
        sys.modules["__main__"].login.login.assert_called_with({"action": "settings"})

    def test_executeAction_should_call_storage_deleteStoredSearch_if_action_is_delete_search(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "delete_search"})
        
        sys.modules["__main__"].storage.deleteStoredSearch.assert_called_with({"action": "delete_search"})

    def test_executeAction_should_call_storage_deleteStoredSearch_if_action_is_delete_disco(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "delete_disco"})
        
        sys.modules["__main__"].storage.deleteStoredSearch.assert_called_with({"action": "delete_disco"})

    def test_executeAction_should_call_storage_editStoredSearch_if_action_is_edit_search(self):
        navigation = YouTubeNavigation()
        navigation.listMenu = Mock()
        
        navigation.executeAction({"action": "edit_search"})
        
        sys.modules["__main__"].storage.editStoredSearch.assert_called_with({"action": "edit_search"})

    def test_executeAction_should_call_storage_editStoredSearch_if_action_is_edit_disco(self):
        navigation = YouTubeNavigation()
        navigation.listMenu = Mock()
        
        navigation.executeAction({"action": "edit_disco"})
        
        sys.modules["__main__"].storage.editStoredSearch.assert_called_with({"action": "edit_disco"})

    def test_executeAction_should_call_listMenu_if_action_is_edit_search(self):
        navigation = YouTubeNavigation()
        navigation.listMenu = Mock()
        
        navigation.executeAction({"action": "edit_search"})
        
        navigation.listMenu.assert_called_with({"action": "edit_search"})

    def test_executeAction_should_call_listMenu_if_action_is_edit_disco(self):
        navigation = YouTubeNavigation()
        navigation.listMenu = Mock()
        
        navigation.executeAction({"action": "edit_disco"})
        
        navigation.listMenu.assert_called_with({"action": "edit_disco"})

    def test_executeAction_should_call_removeFromFavorites_if_action_is_remove_favorite(self):
        navigation = YouTubeNavigation()
        navigation.removeFromFavorites = Mock()
        
        navigation.executeAction({"action": "remove_favorite"})
        
        navigation.removeFromFavorites.assert_called_with({"action": "remove_favorite"})        

    def test_executeAction_should_call_addToFavorites_if_action_is_add_favorite(self):
        navigation = YouTubeNavigation()
        navigation.addToFavorites = Mock()
        
        navigation.executeAction({"action": "add_favorite"})
        
        navigation.addToFavorites.assert_called_with({"action": "add_favorite"})        

    def test_executeAction_should_call_removeContact_if_action_is_remove_contact(self):
        navigation = YouTubeNavigation()
        navigation.removeContact = Mock()
        
        navigation.executeAction({"action": "remove_contact"})
        
        navigation.removeContact.assert_called_with({"action": "remove_contact"})

    def test_executeAction_should_call_addContact_if_action_is_add_contact(self):
        navigation = YouTubeNavigation()
        navigation.addContact = Mock()
        
        navigation.executeAction({"action": "add_contact"})
        
        navigation.addContact.assert_called_with({"action": "add_contact"})

    def test_executeAction_should_call_removeSubscription_if_action_is_remove_subscription(self):
        navigation = YouTubeNavigation()
        navigation.removeSubscription = Mock()
        
        navigation.executeAction({"action": "remove_subscription"})
        
        navigation.removeSubscription.assert_called_with({"action": "remove_subscription"})

    def test_executeAction_should_call_addSubscription_if_action_is_add_subscription(self):
        navigation = YouTubeNavigation()
        navigation.addSubscription = Mock()
        
        navigation.executeAction({"action": "add_subscription"})
        
        navigation.addSubscription.assert_called_with({"action": "add_subscription"})

    def test_executeAction_should_call_downloader_downloadVideo_if_action_is_download(self):
        navigation = YouTubeNavigation()
        navigation.downloadVideo = Mock()

        navigation.executeAction({"action": "download"})

        navigation.downloadVideo.assert_called_with({'action': 'download'})

    def test_downloadVideo_should_exit_cleanly_if_download_path_is_not_set(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        navigation = YouTubeNavigation()

        navigation.downloadVideo({"action": "download"})

        assert (sys.modules["__main__"].player.buildVideoObject.call_count == 0)
        assert (sys.modules["__main__"].downloader.download.call_count == 0)

    def test_downloadVideo_should_notify_user_if_download_path_is_not_set(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        navigation = YouTubeNavigation()

        navigation.downloadVideo({"action": "download"})

        assert (sys.modules["__main__"].utils.showMessage.call_count == 1)

    def test_downloadVideo_should_open_settings_module_so_user_can_enter_new_download_path_if_download_path_is_not_set(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        navigation = YouTubeNavigation()

        navigation.downloadVideo({"action": "download"})

        assert (sys.modules["__main__"].settings.openSettings.call_count == 1)

    def test_downloadVideo_should_call_downloader_downloadVideo_if_action_is_download(self):
        sys.modules["__main__"].player.buildVideoObject = Mock()
        sys.modules["__main__"].player.buildVideoObject.return_value = ({"videoid": "ytvideo1", "video_url": "Mock url", "Title": "Mock Title" }, "mock" )
        sys.modules["__main__"].settings.getSetting.return_value = "some_path"
        navigation = YouTubeNavigation()

        navigation.downloadVideo({"action": "download"})

        sys.modules["__main__"].downloader.download.assert_called_with("Mock Title-[ytvideo1].mp4", {'action': 'download', 'url': 'Mock url', "download_path": "some_path", "Title": "Mock Title"})

    def test_executeAction_should_call_player_playVideo_if_action_is_play_video(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "play_video"})
        
        sys.modules["__main__"].player.playVideo.assert_called_with({"action": "play_video"})

    def test_executeAction_should_call_playlist_queueVideo_if_action_is_queue_video(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "queue_video"})
        
        sys.modules["__main__"].playlist.queueVideo.assert_called_with({"action": "queue_video"})

    def test_executeAction_should_call_storage_changeSubscriptionView_if_action_is_change_subscription_view(self):
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.executeAction({"action": "change_subscription_view"})
        
        sys.modules["__main__"].storage.changeSubscriptionView.assert_called_with({"action": "change_subscription_view"})

    def test_executeAction_should_call_list_if_action_is_change_subscription_view(self):
        navigation = YouTubeNavigation()
        navigation.list = Mock()
        navigation.executeAction({"action": "change_subscription_view"})
        
        navigation.list.assert_called_with({"action": "change_subscription_view"})

    def test_executeAction_should_call_playlist_playAll_if_action_is_play_all(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "play_all"})
        
        sys.modules["__main__"].playlist.playAll.assert_called_with({"action": "play_all"})

    def test_executeAction_should_call_playlist_addToPlaylist_if_action_is_add_to_playlist(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "add_to_playlist"})
        
        sys.modules["__main__"].playlist.addToPlaylist.assert_called_with({"action": "add_to_playlist"})

    def test_executeAction_should_call_playlist_removeFromPlaylist_if_action_is_remove_from_playlist(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "remove_from_playlist"})
        
        sys.modules["__main__"].playlist.removeFromPlaylist.assert_called_with({"action": "remove_from_playlist"})

    def test_executeAction_should_call_playlist_deletePlaylist_if_action_is_delete_playlist(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "delete_playlist"})
        
        sys.modules["__main__"].playlist.deletePlaylist.assert_called_with({"action": "delete_playlist"})

    def test_executeAction_should_call_playlist_createPlaylist_if_action_is_create_playlist(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "create_playlist"})
        
        sys.modules["__main__"].playlist.createPlaylist.assert_called_with({"action": "create_playlist"})

    def test_executeAction_should_call_storage_reversePlaylistOrder_if_action_is_reverse_order(self):
        navigation = YouTubeNavigation()
        
        navigation.executeAction({"action": "reverse_order"})
        
        sys.modules["__main__"].storage.reversePlaylistOrder.assert_called_with({"action": "reverse_order"})

    def test_list_should_ask_user_for_input_if_feed_is_search_and_search_is_missing_from_params(self):
        sys.modules["__main__"].feeds.list.return_value = ([],200)
        sys.modules["__main__"].language.return_value = "some_string"
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"feed": "search"})
        
        sys.modules["__main__"].common.getUserInput.assert_called_with("some_string", "")

    def test_list_should_ask_user_for_input_if_scraper_is_search_disco_and_search_is_missing_from_params(self):
        sys.modules["__main__"].scraper.scrape.return_value = ([],200)
        sys.modules["__main__"].language.return_value = "some_string"
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"scraper": "search_disco"})
        
        sys.modules["__main__"].common.getUserInput.assert_called_with("some_string", "")

    def test_list_should_call_storage_saveStoredSearch_if_feed_is_search(self):
        sys.modules["__main__"].feeds.list.return_value = ([],200)
        sys.modules["__main__"].language.return_value = "some_string"
        sys.modules["__main__"].common.getUserInput.return_value = "some_user_string"
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"feed": "search"})
        
        sys.modules["__main__"].storage.saveStoredSearch.assert_called_with({"feed": "search", "search": "some_user_string"})

    def test_list_should_call_storage_saveStoredSearch_if_scraper_is_search_disco(self):
        sys.modules["__main__"].scraper.scrape.return_value = ([],200)
        sys.modules["__main__"].language.return_value = "some_string"
        sys.modules["__main__"].common.getUserInput.return_value = "some_user_string"
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"scraper": "search_disco"})
        
        sys.modules["__main__"].storage.saveStoredSearch.assert_called_with({"scraper": "search_disco", "search": "some_user_string"})

    def test_list_should_call_scraper_scrape_if_scraper_is_in_params(self):
        sys.modules["__main__"].scraper.scrape.return_value = ([],200)
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"scraper": "some_scraper"})
        
        sys.modules["__main__"].scraper.scrape.assert_called_with({"scraper": "some_scraper"})

    def test_list_should_call_storage_list_if_store_is_in_params(self):
        sys.modules["__main__"].storage.list.return_value = ([],200)
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"store": "some_store"})
        
        sys.modules["__main__"].storage.list.assert_called_with({"store": "some_store"})
        
    def test_list_should_call_feeds_list_if_neither_store_or_scraper_is_in_params(self):
        sys.modules["__main__"].feeds.list.return_value = ([],200)
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({})
        
        sys.modules["__main__"].feeds.list.assert_called_with({})
        
    def test_list_should_call_parseFolderList_if_list_was_successfull_and_folder_is_in_params(self):
        sys.modules["__main__"].feeds.list.return_value = ([],200)
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({"folder": "true"})
        
        navigation.parseFolderList.assert_called_with({"folder": "true"},[])
        
    def test_list_should_call_parseVideoList_if_list_was_successfull_and_folder_is_not_in_params(self):
        sys.modules["__main__"].feeds.list.return_value = ([],200)
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({})
        
        navigation.parseVideoList.assert_called_with({},[])        
        
    def test_list_should_call_showListingError_if_list_was_unsuccessfull(self):
        sys.modules["__main__"].feeds.list.return_value = ([],303)
        navigation = YouTubeNavigation()
        navigation.parseVideoList = Mock()
        navigation.parseFolderList = Mock()
        navigation.showListingError = Mock()
        
        navigation.list({})
        
        navigation.showListingError.assert_called_with({})        
        
    def test_showListingError_should_search_categories_for_folder_name_if_external_is_not_in_params(self):
        sys.modules["__main__"].language.return_value = "some_string"
        navigation = YouTubeNavigation()
        navigation.categories = ({"feed": "my_feed", "Title": "my_category_title"}, {"feed": "not_my_feed", "Title": "not_my_category_title"})
        
        navigation.showListingError({"feed": "my_feed"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("my_category_title", "some_string")
                
    def test_showListingError_should_search_storage_user_options_if_external_is_in_params(self):
        sys.modules["__main__"].language.return_value = "some_string"
        sys.modules["__main__"].storage.user_options = ({"feed": "my_feed", "Title": "my_options_title"}, {"feed": "not_my_feed", "Title": "not_my_options_title"})
        navigation = YouTubeNavigation()
        
        navigation.showListingError({"feed": "my_feed", "external": "true"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("my_options_title", "some_string")
                
    def test_showListingError_should_use_channel_title_if_channel_is_in_params(self):
        sys.modules["__main__"].language.return_value = "some_string"
        navigation = YouTubeNavigation()
        navigation.categories = ({"feed": "my_feed", "Title": "my_category_title"}, {"feed": "not_my_feed", "Title": "not_my_category_title"})
        
        navigation.showListingError({"feed": "my_feed", "channel": "some_channel_title"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("some_channel_title", "some_string")
        
    def test_showListingError_should_use_language_string_if_playlist_is_in_params(self):
        sys.modules["__main__"].language.return_value = "some_string"
        navigation = YouTubeNavigation()
        navigation.categories = ({"feed": "my_feed", "Title": "my_category_title"}, {"feed": "not_my_feed", "Title": "not_my_category_title"})
        
        navigation.showListingError({"feed": "my_feed", "playlist": "some_playlist"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("some_string", "some_string")
        sys.modules["__main__"].language.assert_any_call(30615)
        sys.modules["__main__"].language.assert_any_call(30601)
        
    def test_showListingError_should_call_utils_showMessage_correctly(self):
        sys.modules["__main__"].language.return_value = "some_string"
        navigation = YouTubeNavigation()
        navigation.categories = ({"feed": "my_feed", "Title": "my_category_title"}, {"feed": "not_my_feed", "Title": "not_my_category_title"})
        
        navigation.showListingError({"feed": "my_feed"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("my_category_title", "some_string")
                
    def test_addToFavorites_should_exit_cleanly_if_video_id_is_missing(self):
        navigation = YouTubeNavigation()
        
        navigation.addToFavorites()
        
        assert(sys.modules["__main__"].core.add_favorite.call_count == 0)
        assert(sys.modules["__main__"].utils.showErrorMessage.call_count == 0)
        
    def test_addToFavorites_should_call_core_add_favorite(self):
        sys.modules["__main__"].core.add_favorite.return_value = ("",303)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.addToFavorites({"videoid": "some_id"})
        
        sys.modules["__main__"].core.add_favorite.assert_called_with({"videoid": "some_id"})
        
    def test_addToFavorites_should_show_error_message_on_failure(self):
        sys.modules["__main__"].core.add_favorite.return_value = ("",303)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.addToFavorites({"videoid": "some_id"})
        
        sys.modules["__main__"].utils.showErrorMessage.assert_called_with("some_title", "",303)
        sys.modules["__main__"].language.assert_called_with(30020)
        
    def test_removeFromFavorites_should_exit_cleanly_if_editid_is_missing(self):
        navigation = YouTubeNavigation()
        
        navigation.removeFromFavorites()
        
        assert(sys.modules["__main__"].core.delete_favorite.call_count == 0)
        assert(sys.modules["__main__"].utils.showErrorMessage.call_count == 0)        
        
    def test_removeFromFavorites_should_call_core_delete_favorite(self):
        sys.modules["__main__"].core.delete_favorite.return_value = ("",200)
        navigation = YouTubeNavigation()
        
        navigation.removeFromFavorites({"editid": "some_id"})
        
        sys.modules["__main__"].core.delete_favorite.assert_called_with({"editid": "some_id"})
        
    def test_removeFromFavorites_should_show_error_message_on_failure(self):
        sys.modules["__main__"].core.delete_favorite.return_value = ("",303)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.removeFromFavorites({"editid": "some_id"})
        
        sys.modules["__main__"].utils.showErrorMessage.assert_called_with("some_title", "",303)
        sys.modules["__main__"].language.assert_called_with(30020)
                
    def test_addContact_should_ask_user_for_contact_name_if_missing(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].language.return_value = "some_title"
        sys.modules["__main__"].common.getUserInput.return_value = ""
        
        navigation.addContact()
        
        sys.modules["__main__"].common.getUserInput.assert_called_with("some_title", "")
        
    def test_addContact_should_call_core_add_contact(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].core.add_contact.return_value = ("", 200)
        sys.modules["__main__"].language.return_value = "some_title"
        
        navigation.addContact({"contact": "some_contact"})
        
        sys.modules["__main__"].core.add_contact.assert_called_with({"contact": "some_contact"})
        
    def test_addContact_should_exit_cleanly_if_contact_is_missing_and_no_contact_is_given(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].language.return_value = "some_title"
        sys.modules["__main__"].common.getUserInput.return_value = ""
        
        navigation.addContact()
        
        assert(sys.modules["__main__"].core.add_contact.call_count == 0)
        assert(sys.modules["__main__"].utils.showErrorMessage.call_count == 0)        
        sys.modules["__main__"].common.getUserInput.assert_called_with("some_title", "")
        
    def test_addContact_should_show_error_message_on_failure(self):
        sys.modules["__main__"].core.add_contact.return_value = ("", 303)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.addContact({"contact": "some_contact"})
        
        sys.modules["__main__"].utils.showErrorMessage.assert_called_with("some_title", "",303)
        sys.modules["__main__"].language.assert_any_call(30029)
        
    def test_addContact_should_show_success_message_on_success(self):
        sys.modules["__main__"].core.add_contact.return_value = ("", 200)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.addContact({"contact": "some_contact"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("some_title", "some_contact")
        sys.modules["__main__"].language.assert_any_call(30013)
        
    def test_addContact_should_call_xbmc_executebuiltin_on_success(self):
        sys.modules["__main__"].core.add_contact.return_value = ("", 200)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.addContact({"contact": "some_contact"})
        
        sys.modules["__main__"].xbmc.executebuiltin.assert_called_with('Container.Refresh')
                
    def test_removeContact_should_exit_cleanly_if_contact_is_missing(self):
        navigation = YouTubeNavigation()
        
        navigation.removeContact()
        
        assert(sys.modules["__main__"].core.remove_contact.call_count == 0)
        assert(sys.modules["__main__"].utils.showErrorMessage.call_count == 0)        
        
    def test_removeContact_should_call_core_remove_contact(self):
        sys.modules["__main__"].core.remove_contact.return_value = ("", 200)
        navigation = YouTubeNavigation()
        
        navigation.removeContact({"contact": "some_contact"})
        
        sys.modules["__main__"].core.remove_contact.assert_called_with({"contact": "some_contact"})
        
    def test_removeContact_should_show_error_message_on_failure(self):
        sys.modules["__main__"].core.remove_contact.return_value = ("", 303)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.removeContact({"contact": "some_contact"})
        
        sys.modules["__main__"].utils.showErrorMessage.assert_called_with("some_title", "",303)
        sys.modules["__main__"].language.assert_any_call(30029)
        
    def test_removeContact_should_show_success_message_on_success(self):
        sys.modules["__main__"].core.remove_contact.return_value = ("", 200)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.removeContact({"contact": "some_contact"})
        
        sys.modules["__main__"].utils.showMessage.assert_called_with("some_title", "some_contact")
        sys.modules["__main__"].language.assert_any_call(30013)
        
    def test_removeContact_should_call_xbmc_execute_builtin_on_success(self):
        sys.modules["__main__"].core.remove_contact.return_value = ("", 200)
        sys.modules["__main__"].language.return_value = "some_title"
        navigation = YouTubeNavigation()
        
        navigation.removeContact({"contact": "some_contact"})

        sys.modules["__main__"].xbmc.executebuiltin.assert_called_with('Container.Refresh')        
        
    def test_removeSubscription_should_exit_cleanly_if_editid_is_missing(self):
        navigation = YouTubeNavigation()
        
        navigation.removeSubscription()
        
        assert(sys.modules["__main__"].core.remove_subscription.call_count == 0)
        assert(sys.modules["__main__"].utils.showErrorMessage.call_count == 0)        
        
    def test_removeSubscription_should_call_core_remove_subscription(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].core.remove_subscription.return_value = ("",200)
        
        navigation.removeSubscription({"editid": "some_editid"})
        
        sys.modules["__main__"].core.remove_subscription.assert_called_with({"editid": "some_editid"})
        
    def test_removeSubscription_should_show_error_message_on_failure(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].language.return_value = "some_message"
        sys.modules["__main__"].core.remove_subscription.return_value = ("",303)
        
        navigation.removeSubscription({"editid": "some_editid"})
        
        sys.modules["__main__"].utils.showErrorMessage.assert_called_with("some_message", "",303)
        sys.modules["__main__"].language.assert_called_with(30021)
        
    def test_removeSubscription_should_call_xbmc_execute_builtin_on_success(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].core.remove_subscription.return_value = ("",200)
        
        navigation.removeSubscription({"editid": "some_editid"})
        
        sys.modules["__main__"].xbmc.executebuiltin.assert_called_with('Container.Refresh')
        
    def test_addSubscription_should_exit_cleanly_if_channel_is_missing(self):
        navigation = YouTubeNavigation()
        
        navigation.addSubscription()
        
        assert(sys.modules["__main__"].core.add_subscription.call_count == 0)
        assert(sys.modules["__main__"].utils.showErrorMessage.call_count == 0)
        
    def test_addSubscription_should_call_core_add_subscription(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].core.add_subscription.return_value = ("",200)
        
        navigation.addSubscription({"channel": "some_channel"})
        
        sys.modules["__main__"].core.add_subscription.assert_called_with({"channel": "some_channel"})
        
    def test_addSubscription_should_show_error_message_on_failure(self):
        navigation = YouTubeNavigation()
        sys.modules["__main__"].language.return_value = "some_message"
        sys.modules["__main__"].core.add_subscription.return_value = ("",303)
        
        navigation.addSubscription({"channel": "some_channel"})
        
        sys.modules["__main__"].utils.showErrorMessage.assert_called_with("some_message", "",303)
        sys.modules["__main__"].language.assert_called_with(30021)
        
    def test_addListItem_should_call_addFolderListItem_if_item_is_not_an_action_and_doesnt_require_login(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        navigation = YouTubeNavigation()
        navigation.addFolderListItem = Mock()
        
        navigation.addListItem({}, {"feed": "some_feed", "login": "false"})
        
        navigation.addFolderListItem.assert_called_with({}, {"feed": "some_feed", "login": "false"})
        
    def test_addListItem_should_call_addFolderListItem_if_item_is_not_an_action__requires_login_and_user_is_logged_in(self):
        sys.modules["__main__"].settings.getSetting.return_value = "some_token"
        navigation = YouTubeNavigation()
        navigation.addFolderListItem = Mock()
        
        navigation.addListItem({}, {"feed": "some_feed", "login": "true"})
        
        navigation.addFolderListItem.assert_called_with({}, {"feed": "some_feed", "login": "true"})
        
    def test_addListItem_should_call_addActionListItem_if_item_action_is_settings_user_is_logged_in_and_item_requires_login(self):
        sys.modules["__main__"].settings.getSetting.return_value = "some_token"
        navigation = YouTubeNavigation()
        navigation.addActionListItem = Mock()
        
        navigation.addListItem({}, {"action": "settings", "login": "true"})
        
        navigation.addActionListItem.assert_called_with({}, {"action": "settings", "login": "true"})
        
    def test_addListItem_should_call_addActionListItem_if_item_action_is_settings_user_is_not_logged_in_and_item_doesnt_require_login(self):
        sys.modules["__main__"].settings.getSetting.return_value = ""
        navigation = YouTubeNavigation()
        navigation.addActionListItem = Mock()
        
        navigation.addListItem({}, {"action": "settings", "login": "false"})
        
        navigation.addActionListItem.assert_called_with({}, {"action": "settings", "login": "false"})
        
    def test_addListItem_should_call_addVideoListItem_if_item_action_is_play_video(self):
        navigation = YouTubeNavigation()
        navigation.addVideoListItem = Mock()
        
        navigation.addListItem({}, {"action": "play_video"})
        
        navigation.addVideoListItem.assert_called_with({}, {"action": "play_video"}, 0)
        
    def test_addListItem_should_call_addActionListItem_if_item_has_action(self):
        navigation = YouTubeNavigation()
        navigation.addActionListItem = Mock()
        
        navigation.addListItem({}, {"action": "some_action"})
        
        navigation.addActionListItem.assert_called_with({}, {"action": "some_action"})
        
    def test_addFolderListItem_should_call_utils_get_thumbnail_to_get_icon_path(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"action": "some_action", "icon": "some_icon"})
        
        sys.modules["__main__"].utils.getThumbnail("some_icon")
        
    def test_addFolderListItem_should_call_addFolderContextMenuItems_to_get_context_menu_items(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"action": "some_action", "icon": "some_icon"})
        
        navigation.addFolderContextMenuItems.assert_called_with({}, {"action": "some_action", "icon": "some_icon"})
        
    def test_addFolderListItem_should_call_utils_get_thumbnail_to_get_thumbnail_path(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"action": "some_action", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].utils.getThumbnail.assert_called_with("some_thumbnail")
        
    def test_addFolderListItem_should_call_xbmcgui_ListItem_to_fetch_xbmc_listitem_object(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem.assert_called_with("some_title",iconImage='some_image_path', thumbnailImage='some_image_path')
        
    def test_addFolderListItem_should_call_utils_buildItemUrl_to_get_proper_item_url(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].utils.buildItemUrl({"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
    def test_addFolderListItem_should_call_listitem_addContextMenuItems_to_add_context_menu(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = [1,2]
        
        navigation.addFolderListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem().addContextMenuItems.assert_called_with([1,2],replaceItems=False)
        
    def test_addFolderListItem_should_call_listitem_setProperty_to_inidicate_item_is_a_folder(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem().setProperty.assert_called_with('Folder', 'true')
        
    def test_addFolderListItem_should_call_settings_getSetting_to_fetch_downloadPath_if_item_feed_is_downloads(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"feed": "downloads", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].settings.getSetting.assert_called_with("downloadPath")
        
    def test_addFolderListItem_should_call_xbmcplugin_addDirectoryItem_correctly(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        navigation.addFolderContextMenuItems = Mock()
        navigation.addFolderContextMenuItems.return_value = []
        
        navigation.addFolderListItem({}, {"feed": "downloads", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].settings.getSetting.assert_called_with("downloadPath")
        
    def test_addActionListItem_should_call_utils_get_thumbnail_to_get_thumbnail_path(self):
        sys.argv = ["some_path", -1, "some_params"]
        navigation = YouTubeNavigation()
        
        navigation.addActionListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].utils.getThumbnail.assert_called_with("some_thumbnail")

    def test_addActionListItem_should_call_xbmcgui_ListItem_to_fetch_xbmc_listitem_object(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        
        navigation.addActionListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem.assert_called_with("some_title",iconImage='DefaultFolder.png', thumbnailImage='some_image_path')

    def test_addActionListItem_should_call_listitem_setProperty_to_inidicate_item_is_playable_if_item_action_is_playbyid(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        
        navigation.addActionListItem({}, {"action": "playbyid", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem().setProperty.assert_called_with("IsPlayable", "true")


    def test_addActionListItem_should_call_xbmcplugin_addDirectoryItem_correctly(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].xbmcgui.ListItem.return_value = []
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        
        navigation.addActionListItem({}, {"action": "some_action", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcplugin.addDirectoryItem.assert_called_with(totalItems = 0, url="some_path?path=None&action=some_action&", isFolder=True, listitem = [], handle=-1)

    def test_addVideoListItem_should_set_default_icon_for_disco(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        
        navigation.addVideoListItem({"scraper": "search_disco"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].utils.getThumbnail.assert_called_with("discoball")

    def test_addVideoListItem_should_set_default_icon_for_live(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        
        navigation.addVideoListItem({"feed": "some_live"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].utils.getThumbnail.assert_called_with("live")

    def test_addVideoListItem_should_set_default_icon_for_music(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        
        navigation.addVideoListItem({"scraper": "scraper_music"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].utils.getThumbnail.assert_called_with("music")

    def test_addVideoListItem_should_call_xbmcgui_ListItem_to_fetch_xbmc_listitem_object(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem.assert_called_with("some_title",iconImage="some_image_path",thumbnailImage="some_thumbnail")

    def test_addVideoListItem_should_call_addVideoContextMenuItems_to_get_context_menu_items(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        navigation.addVideoContextMenuItems.assert_called_with({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})

    def test_addVideoListItem_should_call_listitem_addContextMenuItems_to_add_context_menu(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoContextMenuItems.return_value = []
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem().addContextMenuItems.assert_called_with([],replaceItems=True)

    def test_addVideoListItem_should_call_listitem_setProperty_to_indicate_listitem_is_video(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoContextMenuItems.return_value = []
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem().setProperty.assert_any_call("Video", "true")
        sys.modules["__main__"].xbmcgui.ListItem().setProperty.assert_any_call("IsPlayable", "true")

    def test_addVideoListItem_should_call_listitem_setInfo_to_allow_xbmc_to_sort_and_display_video_info(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoContextMenuItems.return_value = []
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcgui.ListItem().setInfo.assert_called_with(infoLabels= {'icon': 'some_icon', 'thumbnail': 'some_thumbnail', 'Title': 'some_title'}, type = 'Video')

    def test_addVideoListItem_should_call_xbmcplugin_addDirectoryItem_correctly(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        list_item = Mock()
        sys.modules["__main__"].xbmcgui.ListItem.return_value = list_item 
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoContextMenuItems.return_value = []
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcplugin.addDirectoryItem.assert_called_with(handle=-1, url = "some_path?path=/root/video&action=play_video&videoid=None", listitem=list_item, isFolder=False, totalItems=1)

    def test_addActionListItem_should_set_default_path_for_videos_correctly(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        list_item = Mock()
        sys.modules["__main__"].xbmcgui.ListItem.return_value = list_item 
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoContextMenuItems.return_value = []
        
        navigation.addVideoListItem({}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"})
        
        sys.modules["__main__"].xbmcplugin.addDirectoryItem.assert_called_with(handle=-1, url = "some_path?path=/root/video&action=play_video&videoid=None", listitem=list_item, isFolder=False, totalItems=1)

    def test_parseFolderList_should_set_cache_false_if_item_is_store_og_user_feed(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseFolderList({"user_feed": "some_feed", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}])
        
        sys.modules["__main__"].xbmcplugin.endOfDirectory.assert_called_with(handle=-1,succeeded=True,cacheToDisc=False)

    def test_parseFolderList_should_call_addFolderListItem_for_each_item(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseFolderList({"user_feed": "some_feed", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}])
        
        assert(navigation.addFolderListItem.call_count == 3)

    def test_parseFolderList_should_call_xbmcplugin_endOfDirectory_correctly(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseFolderList({"user_feed": "some_feed", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}])
        
        sys.modules["__main__"].xbmcplugin.endOfDirectory.assert_called_with(handle=-1,succeeded=True,cacheToDisc=False)

    def test_parseVideoList_should_skip_items_where_videoid_is_false(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 0
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        
        navigation.parseVideoList({"user_feed": "some_feed", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}])
        
        assert(navigation.addVideoListItem.call_count == 2)

    def test_parseVideoList_should_add_index_to_items_from_watch_later_feed(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 0
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}])
        
        navigation.addVideoListItem.assert_called_with({'path': 'some_path', 'scraper': 'watch_later'}, {'path': 'some_path', 'icon': 'some_icon', 'index': '3', 'thumbnail': 'some_thumbnail', 'Title': 'some_title'},3)

    def test_parseVideoList_should_call_addFolderListItem_to_next_item(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 0
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"next": "true", "Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}])
        
        navigation.addFolderListItem.assert_called_with({"scraper": "watch_later", "path": "some_path"}, {"next": "true", 'path': 'some_path', 'icon': 'some_icon', 'index': '3', 'thumbnail': 'some_thumbnail', 'Title': 'some_title'},3)

    def test_parseVideoList_should_call_addVideoListItem_if_item_is_not_next_item(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 0
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "next": "true"}])
        
        navigation.addVideoListItem.assert_called_once_with({'path': 'some_path', 'scraper': 'watch_later'}, {'path': 'some_path', 'icon': 'some_icon', 'index': '1', 'thumbnail': 'some_thumbnail', 'Title': 'some_title'},3)

    def test_parseVideoList_should_call_settings_getSetting_to_get_list_view(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 0
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "next": "true"}])
        
        sys.modules["__main__"].settings.getSetting.assert_called_with("list_view")

    def test_parseVideoList_should_call_xbmc_executebuiltin_if_list_view_is_set(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 1
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "next": "true"}])
        
        sys.modules["__main__"].xbmc.executebuiltin.assert_called_with('Container.SetViewMode(500)')
        
    def test_parseVideoList_should_call_xbmcplugin_addSortMethod_for_valid_sort_methods(self):
        sys.argv = ["some_path", -1, "some_params"]
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 1
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "next": "true"}])
        
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_UNSORTED)
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_LABEL)
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_VIDEO_RATING)
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_DATE)
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_PROGRAM_COUNT)
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_VIDEO_RUNTIME)
        sys.modules["__main__"].xbmcplugin.addSortMethod.assert_any_call(handle=-1,sortMethod=sys.modules["__main__"].xbmcplugin.SORT_METHOD_GENRE)
        
    def test_parseVideoList_should_call_xbmcplugin_endOfDirectory_correctly(self):        
        sys.modules["__main__"].utils.getThumbnail.return_value = "some_image_path"
        sys.modules["__main__"].settings.getSetting.return_value = 1
        navigation = YouTubeNavigation()
        navigation.addVideoContextMenuItems = Mock()
        navigation.addVideoListItem = Mock()
        navigation.addFolderListItem = Mock()
        
        navigation.parseVideoList({"scraper": "watch_later", "path": "some_path"},[{"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "false"}, {"Title": "some_title", "icon": "some_icon", "thumbnail": "some_thumbnail", "next": "true"}])
        
        sys.modules["__main__"].xbmcplugin.endOfDirectory.assert_called_with(cacheToDisc=True,handle=-1,succeeded=True)
        
    def test_addVideoContextMenuItems_should_call_utils_makeAscii_on_Title(self):
        sys.argv = ["some_plugin", -1, "some_path"]
        sys.modules["__main__"].language.return_value = "some_button_string %s"
        sys.modules["__main__"].common.makeAscii.side_effect = lambda x: x
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].common.makeAscii.assert_any_call("some_title")
        
    def test_addVideoContextMenuItems_should_call_utils_makeAscii_on_Studio(self):
        sys.argv = ["some_plugin", -1, "some_path"]
        sys.modules["__main__"].language.return_value = "some_button_string %s"
        sys.modules["__main__"].common.makeAscii.side_effect = lambda x: x
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].common.makeAscii.assert_called_with("Unknown Author")
        
    def prepareContestMenu(self):
        sys.argv = ["some_plugin", -1, "some_path"]
        sys.modules["__main__"].language.return_value = "some_button_string %s"
        sys.modules["__main__"].common.makeAscii.side_effect = lambda x: x
        
    def assert_context_menu_contains(self, cm, title, path):
        found = False
        for (ititle, ipath) in cm:
                if ititle == title and ipath == path :
                        found = True

        if found == False:
                print "Failed to find item in context menu: " + title + " - " + path + "\r\n"
                
                for (title, path) in cm:
                    print "item " + str(cm.index((title, path))) +": " + title + " - " + path
                        
        assert(found)

    def assert_context_menu_doesnt_contain(self, cm, title, path):
        found = False
        for (ititle, ipath) in cm:
                if ititle == title and ipath == path :
                        found = True

        if found == True:
                print "Failed to find item in context menu: " + title + " - " + path + "\r\n"
                
                for (title, path) in cm:
                    print "item " + str(cm.index((title, path))) +": " + title + " - " + path
                        
        assert(found == False)
        
    def test_addVideoContextMenuItems_should_add_play_all_from_video_id_to_items_in_playlists(self):
        self.prepareContestMenu()
        navigation = YouTubeNavigation()
        path_params = {"playlist": "some_playlist"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30512)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&playlist=some_playlist&videoid=some_id&)')
                

    def test_addVideoContextMenuItems_should_add_play_all_from_video_id_to_items_in_new_subscriptions_feed(self):
        self.prepareContestMenu()
        navigation = YouTubeNavigation()
        path_params = {"user_feed": "newsubscriptions"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30521)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=newsubscriptions&contact=default&videoid=some_id&)')

    def test_addVideoContextMenuItems_should_add_download_video_to_all_video_items(self):
        self.prepareContestMenu()
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30501)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=download&videoid=some_id)')

    def test_addVideoContextMenuItems_should_add_add_favorite_option_if_user_is_logged_in_and_item_is_not_in_favorites_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30503)
        sys.modules["__main__"].settings.getSetting.assert_any_call("username")
        sys.modules["__main__"].settings.getSetting.assert_any_call("oauth2_access_token")
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=add_favorite&videoid=some_id&)')

    def test_addVideoContextMenuItems_should_add_add_favorite_option_if_user_is_logged_in_and_item_is_in_external_users_favorites_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"user_feed": "favorites", "contact": "some_contact"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30501)
        sys.modules["__main__"].settings.getSetting.assert_any_call("username")
        sys.modules["__main__"].settings.getSetting.assert_any_call("oauth2_access_token")
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=add_favorite&videoid=some_id&)')
        
    def test_addVideoContextMenuItems_should_add_remove_favorite_option_if_user_is_logged_in_and_item_is_in_favorites_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"user_feed": "favorites"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30506)
        sys.modules["__main__"].settings.getSetting.assert_any_call("username")
        sys.modules["__main__"].settings.getSetting.assert_any_call("oauth2_access_token")
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=remove_favorite&editid=some_id&)')

    def test_addVideoContextMenuItems_should_add_add_subscription_option_to_channels_not_in_subscriptions_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"user_feed": "favorites"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30512)
        self.assert_context_menu_contains(cm, "some_button_string Unknown Author", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=Unknown+Author&action=add_subscription)')        

    def test_addVideoContextMenuItems_should_add_add_subscriptions_option_to_external_users_subscriptions_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"feed": "subscriptions_favorites", "external": "true"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30512)
        self.assert_context_menu_contains(cm, "some_button_string Unknown Author", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=Unknown+Author&action=add_subscription)')        

    def test_addVideoContextMenuItems_should_not_add_add_subscrition_option_to_users_uploads_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"user_feed": "uploads"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        self.assert_context_menu_doesnt_contain(cm, "some_button_string Unknown Author", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=Unknown+Author&action=add_subscription)')        

    def test_addVideoContextMenuItems_should_not_add_add_subscription_option_to_subscription_favorites_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"feed": "subscriptions_favorites"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}

        cm = navigation.addVideoContextMenuItems(path_params, item_params)

        self.assert_context_menu_doesnt_contain(cm, "some_button_string Unknown Author", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=Unknown+Author&action=add_subscription)')

    def test_addVideoContextMenuItems_should_not_add_add_subscription_option_to_subscription_playlists_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"feed": "subscriptions_playlists"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        self.assert_context_menu_doesnt_contain(cm, "some_button_string Unknown Author", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=Unknown+Author&action=add_subscription)')        

    def test_addVideoContextMenuItems_should_not_add_add_subscription_option_to_subscription_uploads_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"feed": "subscriptions_uploads"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "editid": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        self.assert_context_menu_doesnt_contain(cm, "some_button_string Unknown Author", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=Unknown+Author&action=add_subscription)')

    def test_addVideoContextMenuItems_should_add_remove_from_playlist_option_to_items_in_playlists(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"playlist": "some_playlist"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "playlist_entry_id": "some_id"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30530)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=remove_from_playlist&playlist=some_playlist&playlist_entry_id=some_id&)')        

    def test_addVideoContextMenuItems_should_add_add_to_playlist_option_to_video_items_if_user_is_logged_in(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30528)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=None&feed=related&videoid=someid)')        

    def test_addVideoContextMenuItems_should_add_more_videos_by_user_if_item_is_not_in_uploads_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30516)
        self.assert_context_menu_contains(cm, "some_button_string Unknown Author", 'XBMC.Container.Update(some_plugin?path=None&feed=uploads&channel=Unknown+Author)')        

    def test_addVideoContextMenuItems_should_not_add_more_videos_by_user_if_item_is_in_uploads_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"user_feed": "uploads"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        self.assert_context_menu_doesnt_contain(cm, "some_button_string Unknown Author", 'XBMC.Container.Update(some_plugin?path=None&feed=uploads&channel=Unknown+Author)')
        
    def test_addVideoContextMenuItems_should_add_related_videos_option_to_video_items(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30527)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=None&feed=related&videoid=someid)')        

    def test_addVideoContextMenuItems_should_add_find_similar_option_to_video_items(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30514)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=None&feed=search&search=some_title)')        

    def test_addVideoContextMenuItems_should_add_now_playing_option_to_video_items(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30523)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.ActivateWindow(VideoPlaylist)')

    def test_addVideoContextMenuItems_should_add_video_info_option_to_video_items(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid"}
        
        cm = navigation.addVideoContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30523)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Action(Info)')

    def test_addFolderContextMenuItems_should_not_add_any_options_to_next_folders(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "next": "true"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        assert(cm == [])

    def test_addFolderContextMenuItems_should_add_play_all_option_to_newsubsctiptions_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "user_feed": "newsubscriptions"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=newsubscriptions&contact=default&login=true&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&shuffle=true&user_feed=newsubscriptions&contact=default&login=true&)')
        
    def test_addFolderContextMenuItems_should_add_play_all_option_to_favorites_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "user_feed": "favorites"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=favorites&contact=default&login=true&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&shuffle=true&user_feed=favorites&contact=default&login=true&)')

    def test_addFolderContextMenuItems_should_add_playlist_options_to_playlist_items(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "playlist": "some_playlist"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30531)
        sys.modules["__main__"].language.assert_any_call(30539)
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=reverse_order&playlist=some_playlist&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=playlist&playlist=some_playlist&)')
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=playlist&shuffle=true&playlist=some_playlist&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=delete_playlist&playlist=some_playlist&)')
                
    def test_addFolderContextMenuItems_should_add_play_all_option_to_watch_later_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "user_feed": "watch_later"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=watch_later&contact=default&login=true&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&shuffle=true&user_feed=watch_later&contact=default&login=true&)')
                
    def test_addFolderContextMenuItems_should_add_play_all_option_to_recommended_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "user_feed": "recommended"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&user_feed=recommended&contact=default&login=true&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&shuffle=true&user_feed=recommended&contact=default&login=true&)')

    def test_addFolderContextMenuItems_should_add_play_all_option_to_liked_videos_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "scraper": "liked_videos"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&scraper=liked_videos&login=true&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&shuffle=true&scraper=liked_videos&login=true&)')
        
    def test_addFolderContextMenuItems_should_add_play_all_option_to_disco_search(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "scraper": "search_disco", "search": "some_search"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30520)
        sys.modules["__main__"].language.assert_any_call(30522)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&scraper=search_disco&search=some_search&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=play_all&shuffle=true&scraper=search_disco&search=some_search&)')
        
    def test_addFolderContextMenuItems_should_add_edit_and_delete_options_to_disco_searches(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "scraper": "search_disco", "search": "some_search"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30524)
        sys.modules["__main__"].language.assert_any_call(30525)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&action=edit_disco&store=disco_searches&search=some_search&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=delete_disco&store=disco_searches&delete=some_search&)')
        
    def test_addFolderContextMenuItems_should_not_add_edit_and_delete_options_to_dissco_searches_in_the_top_artist_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"scraper": "disco_top_artist"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "scraper": "search_disco", "search": "some_search"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        self.assert_context_menu_doesnt_contain(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&action=edit_disco&store=disco_searches&search=some_search&)')        
        self.assert_context_menu_doesnt_contain(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=delete_disco&store=disco_searches&delete=some_search&)')
        
    def test_addFolderContextMenuItems_should_add_edit_and_delete_options_to_searches(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "feed": "search", "search": "some_search"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30515)
        sys.modules["__main__"].language.assert_any_call(30508)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&action=edit_search&store=searches&search=some_search&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=delete_search&store=searches&delete=some_search&)')

    def test_addFolderContextMenuItems_should_add_correct_view_mode_options_to_subscriptions_favorites_feeds(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "view_mode": "some_view_mode", "user_feed": "favorites"}

        cm = navigation.addFolderContextMenuItems(path_params, item_params)

        sys.modules["__main__"].language.assert_any_call(30511)
        sys.modules["__main__"].language.assert_any_call(30526)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&channel=None&action=change_subscription_view&view_mode=uploads&)')
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&channel=None&action=change_subscription_view&view_mode=playlists&folder=true&)')

    def test_addFolderContextMenuItems_should_add_correct_view_mode_options_to_subscriptions_uploads_feeds(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "view_mode": "some_view_mode", "user_feed": "uploads"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30510)
        sys.modules["__main__"].language.assert_any_call(30526)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&channel=None&action=change_subscription_view&view_mode=favorites&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&channel=None&action=change_subscription_view&view_mode=playlists&folder=true&)')
        
    def test_addFolderContextMenuItems_should_add_correct_view_mode_options_to_subscriptions_playlists_feeds(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "view_mode": "some_view_mode", "user_feed": "playlists"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30511)
        sys.modules["__main__"].language.assert_any_call(30510)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&channel=None&action=change_subscription_view&view_mode=favorites&)')        
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.Container.Update(some_plugin?path=some_path&channel=None&action=change_subscription_view&view_mode=uploads&)')        
        
    def test_addFolderContextMenuItems_should_add_add_subscription_option_to_subscriptions_not_in_users_subscription_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {"external": "true"}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "channel": "some_channel"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30512)        
        self.assert_context_menu_contains(cm, "some_button_string some_channel", 'XBMC.RunPlugin(some_plugin?path=some_path&channel=None&action=add_subscription)')
        
    def test_addFolderContextMenuItems_should_add_remove_subscription_option_to_subscriptions_in_users_subscriptions_feed(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        sys.modules["__main__"].common.makeAscii.side_effect = lambda x: x
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "channel": "some_channel", "editid": "some_editid"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30513)
        self.assert_context_menu_contains(cm, "some_button_string some_channel", 'XBMC.RunPlugin(some_plugin?path=some_path&editid=some_editid&action=remove_subscription)')        
        
    def test_addFolderContextMenuItems_should_add_add_contact_option_to_external_contacts_if_user_is_logged_in(self):
        self.prepareContestMenu()
        sys.modules["__main__"].pluginsettings.userHasProvidedValidCredentials.return_value = True
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "contact": "some_contact", "external": "true"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30026)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=add_contact&contact=some_title&)')        
        
    def test_addFolderContextMenuItems_should_add_remove_contact_options_to_items_in_contact_feed_if_user_is_logged_in(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail", "videoid": "someid", "contact": "some_contact"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30025)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.RunPlugin(some_plugin?path=some_path&action=remove_contact&contact=some_title&)')                
        
    def test_addFolderContextMenuItems_should_add_now_playing_option_to_folder_items(self):
        self.prepareContestMenu()
        sys.modules["__main__"].settings.getSetting.return_value = "something"
        navigation = YouTubeNavigation()
        path_params = {}
        item_params = {"Title": "some_title", "path": "some_path", "icon": "some_icon", "thumbnail": "some_thumbnail"}
        
        cm = navigation.addFolderContextMenuItems(path_params, item_params)
        
        sys.modules["__main__"].language.assert_any_call(30523)
        self.assert_context_menu_contains(cm, "some_button_string %s", 'XBMC.ActivateWindow(VideoPlaylist)')
        
if __name__ == '__main__':
        nose.runmodule()
