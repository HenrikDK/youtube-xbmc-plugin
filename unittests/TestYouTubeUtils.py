# -*- coding: utf-8 -*-
import nose
import BaseTestCase
from mock import Mock, patch
import sys
from  YouTubeUtils import YouTubeUtils 


class TestYouTubeUtils(BaseTestCase.BaseTestCase):

    def test_showMessage_should_call_xbmc_execute_builtin_correctly(self):
        sys.modules["__main__"].settings.getSetting.return_value = "3"
        utils = YouTubeUtils()
        
        utils.showMessage("someHeading","someMessage")

        sys.modules["__main__"].xbmc.executebuiltin.assert_called_with('XBMC.Notification("someHeading", "someMessage", 4000)')
        
    def test_getThumbnail_should_call_xbmc_skinHasImage(self):
        sys.modules["__main__"].xbmc.skinHasImage = Mock()
        utils = YouTubeUtils()
        
        result = utils.getThumbnail("someTeading")

        sys.modules["__main__"].xbmc.skinHasImage.assert_called_with('YouTube - Unittest/someTeading.png')
        
    def test_getThumbnail_should_user_default_folder_image_if_no_title_is_given(self):
        sys.modules["__main__"].xbmc.skinHasImage.return_value = False
        utils = YouTubeUtils()
        
        result = utils.getThumbnail("")
        
        sys.modules["__main__"].xbmc.skinHasImage.assert_called_with('YouTube - Unittest/DefaultFolder.png')
        assert(result == "DefaultFolder.png")
	
    def test_getThumbnail_should_user_thumbnail_path_to_resolve_file_paths(self):
        sys.modules["__main__"].settings.getAddonInfo.return_value = "testingPath/"
        sys.modules["__main__"].xbmc.skinHasImage.return_value = False        
        patcher = patch("os.path")
        patcher.start()
        import os
        utils = YouTubeUtils()
        
        result = utils.getThumbnail("")
        call = os.path.join.call_args_list[0]
        patcher.stop()
        
        assert(call == (('testingPath/', 'thumbnails'), {}))
        
    def test_showErrorMessage_should_call_showMessage_with_default(self):
        sys.modules["__main__"].language.return_value = "ERROR"
        utils = YouTubeUtils()
        utils.showMessage = Mock()	
        
        result = utils.showErrorMessage("someTitle","someResult")
        
        utils.showMessage.assert_called_with("someTitle","ERROR")

    def test_showErrorMessage_should_call_showMessage_with_empty_title(self):
        sys.modules["__main__"].language.return_value = "ERROR"
        utils = YouTubeUtils()
        utils.showMessage = Mock()	
        
        result = utils.showErrorMessage("","someResult", 303)
        
        utils.showMessage.assert_called_with("ERROR","someResult")
        sys.modules["__main__"].language.assert_called_with(30600)

    def test_showErrorMessage_should_call_showMessage_with_empty_result(self):
        sys.modules["__main__"].language.return_value = "ERROR"
        utils = YouTubeUtils()
        utils.showMessage = Mock()	
        
        result = utils.showErrorMessage("someTitle","")
        
        utils.showMessage.assert_called_with("someTitle","ERROR")
        sys.modules["__main__"].language.assert_called_with(30617)
	
    def test_showErrorMessage_should_call_showMessage_with_result(self):
        utils = YouTubeUtils()
        utils.showMessage = Mock()	
        
        result = utils.showErrorMessage("someTitle","someResult", 303)
        
        utils.showMessage.assert_called_with("someTitle","someResult")
	
    def test_buildItemUrl_should_ignore_items_in_blacklist(self):
        input = {"path":"FAIL","thumbnail":"FAIL", "Overlay":"FAIL", "icon":"FAIL", "next":"FAIL", "content":"FAIL" , "editid":"FAIL", "summary":"FAIL", "published":"FAIL","count":"FAIL","Rating":"FAIL","Plot":"FAIL","Title":"FAIL","new_results_function":"FAIL","some_other_param":"some_value"}
        utils = YouTubeUtils()
        
        result = utils.buildItemUrl(input)
        
        assert(result.find("FAIL") < 0)
        
    def test_buildItemUrl_should_build_url_from_params_collection(self):
        input = {"some_other_param":"some_value", "some_param":"some_other_value"}
        utils = YouTubeUtils()
        
        result = utils.buildItemUrl(input)
        
        assert(result == "some_param=some_other_value&some_other_param=some_value&")

    def test_buildItemUrl_should_append_to_existing_url(self):
        input = {"some_other_param":"some_value", "some_param":"some_other_value"}
        utils = YouTubeUtils()
        
        result = utils.buildItemUrl(input, "myfirst_url?")
        
        assert(result == "myfirst_url?some_param=some_other_value&some_other_param=some_value&")
        
    def test_addNextFolder_should_ignore_item_Title_thumbnail_page_and_new_results_funtion(self):
        sys.modules["__main__"].language.return_value = "Next"
        input = {"some_other_param":"some_value", "some_param":"some_other_value","page":"1","Title":"My annoying Title", "thumbnail":"someThumbnail","new_results_function":"functionPointer"}
        utils = YouTubeUtils()
        result = []
        
        utils.addNextFolder(result, input)
        
        assert(result[0]["Title"] == "Next")
        assert(result[0]["some_other_param"] == "some_value")
        assert(result[0]["some_param"] == "some_other_value")
        assert(result[0]["page"] == "2")
        assert(result[0]["thumbnail"] == "next")
        assert(result[0]["next"] == "true")
        
    def test_addNextFolder_should_increment_current_page(self):
        sys.modules["__main__"].language.return_value = "Next"
        input = {"some_other_param":"some_value", "some_param":"some_other_value","page":"45"}
        utils = YouTubeUtils()
        result = []
        
        utils.addNextFolder(result, input)
        
        assert(result[0]["page"] == "46")

    def test_extractVID_should_return_id_from_string(self):
        utils = YouTubeUtils()
        result = utils.extractVID("/watch?v=bla-id&amp;feature=artist")
        
        assert(len(result) == 1)
        assert(result[0] == "bla-id")

    def test_extractVID_should_return_ids_from_list(self):
        utils = YouTubeUtils()
        result = utils.extractVID(["&v=bla2", "&v=bla3&w="])
        
        assert(len(result) == 2)
        assert(result[0] == "bla2")
        assert(result[1] == "bla3")
        
    def test_extractVID_should_call_log_twice_with_correct_input(self):
        test = [ "?v=bla2", "&v=bla3&", "&v=bla4&amp;", "&amp;v=bla5&"]
        utils = YouTubeUtils()
        result = utils.extractVID(test)

        print repr(result)
        print repr(sys.modules["__main__"].common.log.call_args_list)

        sys.modules["__main__"].common.log.assert_any_call(repr(test), 4)
        sys.modules["__main__"].common.log.assert_any_call(repr([ "bla2", "bla3", "bla4", "bla5"]), 4)

        assert(len(result) == 4)
        assert(result[0] == "bla2")
        assert(result[1] == "bla3")
        assert(result[2] == "bla4")
        assert(result[3] == "bla5")

if __name__ == '__main__':
	nose.runmodule()
