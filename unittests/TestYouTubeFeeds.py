import nose
import BaseTestCase
from mock import Mock
import sys
from YouTubeFeeds import YouTubeFeeds


class TestYouTubeFeeds(BaseTestCase.BaseTestCase):
    def test_createUrl_should_call_getSetting_to_get_videos_pr_page(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        feeds.createUrl()
        
        sys.modules["__main__"].pluginsettings.itemsPerPage.assert_any_call()

    def test_createUrl_should_call_getSetting_to_get_region_id(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        feeds.createUrl()

        sys.modules["__main__"].pluginsettings.currentRegion.assert_any_call()

    def test_createUrl_should_get_correct_feed_url_if_feed_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "favorites"})
        result = result[:result.find("?")]
        url = feeds.urls["favorites"] % ("default")
        sys.modules["__main__"].pluginsettings.currentRegion.assert_any_call()
        assert(result == url)

    def test_createUrl_should_get_correct_user_feed_url_if_user_feed_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"user_feed": "favorites"})
        result = result[:result.find("?")]
        url = feeds.urls["favorites"] % ("default")
        assert(result == url)
        
    def test_createUrl_should_get_correct_search_url_if_search_is_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        sys.modules["__main__"].pluginsettings.safeSearchLevel.return_value = "moderate"
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"search": "some_search"})
        result = result[:result.find("moderate") + 8]
        url = feeds.urls["search"] % ("some_search", "moderate")
        assert(result == url)
        
    def test_createUrl_should_add_contact_name_to_url_if_contact_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "favorites", "contact": "some_contact"})
        
        result = result[:result.find("?")]
        url = feeds.urls["favorites"] % ("some_contact")
        assert(result == url)

    def test_createUrl_should_add_channel_to_url_if_channel_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "favorites", "channel": "some_channel"})
        
        result = result[:result.find("?")]
        url = feeds.urls["favorites"] % ("some_channel")
        assert(result == url)
	
    def test_createUrl_should_add_category_and_time_to_url_if_category_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "feed_category", "category": "some_category"})
        
        result = result[:result.rfind("&")]
        result = result[:result.rfind("&")]
        url = feeds.urls["feed_category"] % (("some_category"), "today")
        assert(result == url)

    def test_createUrl_should_add_playlist_to_url_if_playlist_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "playlist", "channel": "some_playlist"})
        
        result = result[:result.find("?")]
        url = feeds.urls["playlist"] % ("some_playlist")
        assert(result == url)

    def test_createUrl_should_add_videoid_to_url_if_videoid_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""

        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "related", "videoid": "some_videoid"})
        
        result = result[:result.find("?")]
        url = feeds.urls["related"] % ("some_videoid")
        assert(result == url)

    def test_createUrl_should_add_region_if_standard_feed(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = "AU"
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "feed_linked"})
        
        result = result[:result.find("?")]
        assert(result.find("standardfeeds/AU/") > 0)

    def test_createUrl_should_start_index_and_max_results_for_non_folder_non_play_all_feeds(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""

        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "feed_linked"})
        
        result = result[result.find("?"):]
        assert(result == "?time=this_week&start-index=1&max-results=15")
	
    def test_createUrl_should_add_time_if_url_contains_time_param(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].pluginsettings.currentRegion.return_value = ""
        feeds = YouTubeFeeds()
        
        result = feeds.createUrl({"feed": "feed_linked"})
        
        assert(result.find("?time=this_week") > 0)
	
    def test_list_should_call_listFolder_if_folder_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        
        result = feeds.list({"folder": "true"})

        print repr(result)

        feeds.listFolder.assert_called_with({"folder": "true"})
        
    def test_list_should_call_listPlaylist_if_playlist_is_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        
        result = feeds.list({"playlist": "some_playlist"})

        print repr(result)

        feeds.listPlaylist.assert_called_with({"playlist": "some_playlist"})
        
    def test_list_should_call_core_getAuth_to_test_if_login_is_set_if_login_is_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_content", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        result = feeds.list({"login": "true"})

        print repr(result)

        sys.modules["__main__"].core._getAuth.assert_called_with()
	
    def test_list_should_return_error_message_if_login_is_not_set_and_login_is_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_content", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].core._getAuth.return_value = False
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        result = feeds.list({"login": "true"})
        
        assert(result == ("some_string", 303))
        sys.modules["__main__"].language.assert_called_with(30609)
        
    def test_list_should_call_createUrl_to_fetch_url(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_content", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        result = feeds.list()

        print repr(result)

        feeds.createUrl.assert_called_with({})

    def test_list_should_call_core_fetchPage_to_get_feed_content(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_content", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        result = feeds.list()

        print repr(result)

        sys.modules["__main__"].core._fetchPage.assert_called_with({"api": "true", "link": "some_url", "auth": None})
    
    def test_list_should_call_return_content_and_status_if_fetchPage_failed(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 303}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.list()
        
        assert(result == ("some_fail", 303))
	
    def test_list_should_call_core_getVideoInfo_if_fetchPage_succeded_and_folder_is_not_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.list()

        print repr(result)

        sys.modules["__main__"].core.getVideoInfo.assert_called_with("some_fail", {})

    def test_list_should_return_error_status_if_video_list_is_empty(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.list()
        
        assert(result == ([], 303))
                
    def test_list_should_call_storage_store_to_save_first_thumbnail_in_list(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id", "thumbnail": "some_thumb"}]
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listPlaylist = Mock()
        feeds.listFolder = Mock()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.list()

        print repr(result)

        sys.modules["__main__"].storage.store.assert_called_with({}, "some_thumb", "thumbnail")

    def test_listPlaylist_should_call_pluginSettings_to_get_perpage(self):

        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id", "thumbnail": "some_thumb"}]
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()
        print repr(result)

        sys.modules["__main__"].pluginsettings.itemsPerPage.assert_any_call()
                        
    def test_listPlaylist_should_call_storage_retrieve_to_fetch_cached_video_listing(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id", "thumbnail": "some_thumb"}]
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()

        print repr(result)

        sys.modules["__main__"].storage.retrieve.assert_called_with({})
        
    def test_listPlaylist_should_call_getBatchDetailsOverride_to_fetch_video_info_for_stored_video_list(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id", "thumbnail": "some_thumb"}]
        sys.modules["__main__"].language.return_value = "some_string"
        sys.modules["__main__"].storage.retrieve.return_value = [{}, {}]
        sys.modules["__main__"].core.getBatchDetailsOverride.return_value = ([], 200)
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist({"page": "1"})

        print repr(result)

        sys.modules["__main__"].core.getBatchDetailsOverride.assert_called_with([], {"page": "1"})

    def test_listPlaylist_should_call_listAll_if_stored_list_isnt_found(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id", "thumbnail": "some_thumb"}]
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()

        print repr(result)

        feeds.listAll.assert_called_with({})
        
    def test_listPlaylist_should_return_error_status_if_listAll_returns_empty_list(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = [{"videoid": "some_id", "thumbnail": "some_thumb"}]
        sys.modules["__main__"].language.return_value = "some_string"
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()

        assert(result == ([], 303))

    def test_listPlaylist_should_call_storage_store_with_list_of_video_ids_and_entryids(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].language.return_value = "some_string"
        list = [{"videoid": "some_id", "thumbnail": "some_thumb", "playlist_entry_id": "some_id"}]
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = list
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()

        print repr(result)

        sys.modules["__main__"].storage.store.assert_any_call({}, [{"videoid": "some_id", "playlist_entry_id": "some_id"}], )
                
    def test_listPlaylist_should_call_storage_store_with_first_thumbnail_of_list(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].language.return_value = "some_string"
        list = [{"videoid": "some_id", "thumbnail": "some_thumb", "playlist_entry_id": "some_id"}]
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = list
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()

        print repr(result)

        sys.modules["__main__"].storage.store.assert_called_with({}, "some_thumb", "thumbnail")
        
    def test_listPlaylist_should_call_addNextFolder_for_lists_longer_than_perpage(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].language.return_value = "some_string"
        ids = []
        i= 1
        while i < 52:
            ids.append({"videoid": "some_id_" + str(i), "thumbnail": "some_thumb_" + str(i), "playlist_entry_id": "some_id_" + str(i)})
            i += 1
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = ids
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        result = feeds.listPlaylist()

        print repr(result)

        sys.modules["__main__"].utils.addNextFolder.assert_called_with(ids[:15], {})

    def test_listPlaylist_should_limit_list_lengt_to_perpage_count(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].language.return_value = "some_string"
        ids = []
        i= 1
        while i < 52:
            ids.append({"videoid": "some_id_" + str(i), "thumbnail": "some_thumb_" + str(i), "playlist_entry_id": "some_id_" + str(i)})
            i += 1
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.listAll.return_value = ids
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
	
        videos, status = feeds.listPlaylist()
        assert(len(videos) == 15)
        
    def test_listPlaylist_should_starts_list_position_from_page_count_and_perpage_count(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].language.return_value = "some_string"
        ids = []
        i= 1
        while i < 52:
            ids.append({"videoid": "some_id_" + str(i), "thumbnail": "some_thumb_" + str(i), "playlist_entry_id": "some_id_" + str(i)})
            i += 1
        sys.modules["__main__"].core.getBatchDetailsOverride.side_effect = lambda x, y: (x, 200)
        sys.modules["__main__"].storage.retrieve.return_value = ids
        feeds = YouTubeFeeds()
        feeds.listFolder = Mock()
        feeds.listAll = Mock()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"

        videos, status = feeds.listPlaylist({"page": "1"})
        print repr(videos)
        print repr(status)

        assert(len(videos) == 15)
        assert(videos[0]["videoid"] == "some_id_16")
        assert(videos[14]["videoid"] == "some_id_30")
        
    def test_listFolder_should_call_storage_getUserOptionFolder_if_storage_is_contact_options(self):
        feeds = YouTubeFeeds()

        feeds.listFolder({"store": "contact_options"})
        	
        sys.modules["__main__"].storage.getUserOptionFolder.assert_called_with({"store": "contact_options"})
	
    def test_listFolder_should_call_storage_getStoredSearches_if_storage_is_set_but_not_contact_options(self):
        feeds = YouTubeFeeds()

        feeds.listFolder({"store": "some_store"})
        	
        sys.modules["__main__"].storage.getStoredSearches.assert_called_with({"store": "some_store"})

    def test_listFolder_should_call_getSetting_to_get_perpage(self):
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listFolder()
        	
        sys.modules["__main__"].pluginsettings.itemsPerPage.assert_any_call()
        
    def test_listFolder_should_call_storage_retrieve_to_fetch_cached_video_listing_if_page_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = []
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listFolder({"page": "1"})
        	
        sys.modules["__main__"].storage.retrieve.assert_called_with({"page": "1"})

    def test_listFolder_should_call_listAll_page_is_not_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = []
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = []
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listFolder()
        	
        feeds.listAll.assert_called_with({})

    def test_listFolder_should_call_storage_store_to_save_new_list(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = []
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = ["some"]
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listFolder()
        	
        sys.modules["__main__"].storage.store.assert_called_with({}, ["some"])

    def test_listFolder_should_call_addNextFolder_for_lists_longer_than_perpage(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = []
        ids = []
        i= 1
        while i < 52:
            ids.append({"Title": "title_" + str(i), "thumbnail": "some_thumb_" + str(i), "id": "some_id_" + str(i)})
            i += 1
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = ids
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listFolder()
        	
        sys.modules["__main__"].utils.addNextFolder.assert_called_with(ids[:15], {})
        
    def test_listFolder_should_limit_list_lengt_to_perpage_count(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = []
        ids = []
        i= 1
        while i < 52:
            ids.append({"Title": "title_" + str(i), "thumbnail": "some_thumb_" + str(i), "id": "some_id_" + str(i)})
            i += 1
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = ids
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        videos, status = feeds.listFolder()
        	
        assert(len(videos) == 15)
        
    def test_listFolder_should_starts_list_position_from_page_count_and_perpage_count(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        ids = []
        i= 1
        while i < 52:
            ids.append({"Title": "title_" + str(i), "thumbnail": "some_thumb_" + str(i), "id": "some_id_" + str(i)})
            i += 1
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        sys.modules["__main__"].storage.retrieve.return_value = ids
        feeds.listAll.return_value = ids
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        (videos, status) = feeds.listFolder({"page": "1"})
        
        assert(videos[0]["id"] == "some_id_16")
        assert(videos[14]["id"] == "some_id_30")
        
    def test_listFolder_should_call_retrieve_to_get_view_mode_if_feed_is_subscriptions(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = [{"id": "some_item"}]
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = [{"id": "some_item"}]
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        (videos, status) = feeds.listFolder({"user_feed": "subscriptions"})
        
        sys.modules["__main__"].storage.retrieve.assert_called_with({"user_feed": "subscriptions"}, "viewmode", {'user_feed': 'uploads', 'view_mode': 'subscriptions_favorites', 'id': 'some_item'})
	
    def test_listFolder_should_set_correct_view_mode_if_feed_is_subscriptions(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        feeds = YouTubeFeeds()
        feeds.listAll = Mock()
        feeds.listAll.return_value = [{"id": "some_item"}]
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        (videos, status) = feeds.listFolder({"user_feed": "subscriptions"})
        
        assert(videos[0]["user_feed"] == "favorites")
	
    def test_listAll_should_call_getAuth_if_login_is_in_params(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"login": "true"})
        
        sys.modules["__main__"].core._getAuth.assert_called_with()
        
    def test_listAll_should_call_createUrl_to_get_url(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"login": "true"})
        
        feeds.createUrl.assert_called_with({"login": "true"})
	
    def test_listAll_should_call_fetchPage_correctly(self):
        sys.modules["__main__"].pluginsettings.itemsPerPage.return_value = 15
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"login": "true"})
        
        sys.modules["__main__"].core._fetchPage.assert_called_with({"link": "some_urlv=2.1&start-index=1&max-results=50", "auth": "true"})
        
    def test_listAll_should_call_core_getFolderInfo_if_folder_is_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getFolderInfo.return_value = []
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"login": "true", "folder": "true"})
        
        sys.modules["__main__"].core.getFolderInfo.assert_called_with("some_fail", {"login": "true", "folder": "true"})
        
    def test_listAll_should_call_core_getVideoInfo_if_folder_is_not_in_params(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        sys.modules["__main__"].core.getVideoInfo.return_value = []
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"login": "true"})
        
        sys.modules["__main__"].core.getVideoInfo.assert_called_with("some_fail", {"login": "true"})
        
    def test_listAll_should_call_fetchPage_multiple_times_if_feed_requires_it(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        list = [[{"next": "false"}], [{"next": "true"}]]
        sys.modules["__main__"].core.getVideoInfo.side_effect = lambda x, y: list.pop()
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"login": "true"})
        
        assert(sys.modules["__main__"].core._fetchPage.call_count == 2)
        
    def test_listAll_should_call_core_getFolderInfo_multiple_times_if_feed_requires_it(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        list = [[{"next": "false"}], [{"next": "true"}]]
        sys.modules["__main__"].core.getFolderInfo.side_effect = lambda x, y: list.pop()
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        feeds.listAll({"folder": "true"})
        
        assert(sys.modules["__main__"].core.getFolderInfo.call_count == 2)
        
    def test_listAll_should_call_core_getVideoInfo_multiple_times_if_feed_requires_it(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        list = [[{"next": "false"}, {"next": "false"}], [{"next": "false"}, {"next": "true"}]]
        sys.modules["__main__"].core.getVideoInfo.side_effect = lambda x, y: list.pop()
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"
        
        video = feeds.listAll()

        print repr(video)

        assert(sys.modules["__main__"].core.getVideoInfo.call_count == 2)
        
    def test_listAll_should_append_additional_items_to_list(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        list = [[{"next": "false"}, {"next": "false"}], [{"next": "false"}, {"next": "true"}], [{"next": "false"}, {"next": "true"}], [{"next": "false"}, {"next": "true"}]]
        sys.modules["__main__"].core.getVideoInfo.side_effect = lambda x, y: list.pop()
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"

        video = feeds.listAll()

        print repr(video)

        assert(video == [{'next': 'false'}, {'next': 'false'}, {'next': 'false'}, {'next': 'false'}, {'next': 'false'}])

    def test_listAll_should_call_storage_getReversePlaylistOrder_to_reverse_list_if_not_play_all(self):
        sys.modules["__main__"].settings.getSetting.return_value = "1"
        sys.modules["__main__"].storage.retrieve.return_value = "favorites"
        sys.modules["__main__"].core._fetchPage.return_value = {"content": "some_fail", "status": 200}
        list = [[{"next": "false"}], [{"next": "true"}]]
        sys.modules["__main__"].core.getVideoInfo.side_effect = lambda x, y: list.pop()
        feeds = YouTubeFeeds()
        feeds.createUrl = Mock()
        feeds.createUrl.return_value = "some_url"

        feeds.listAll({"user_feed": "playlist"})

        sys.modules["__main__"].storage.getReversePlaylistOrder.assert_called_with({"user_feed": "playlist"})

if __name__ == "__main__":
    nose.runmodule()
