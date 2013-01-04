import sys
import unittest2, io
from mock import Mock
import MockYouTubeDepends

MockYouTubeDepends.MockYouTubeDepends().mockXBMC()

sys.path.append('../plugin/')
sys.path.append('../xbmc-mocks/')

class BaseTestCase(unittest2.TestCase):#pragma: no cover
	
	def setUp(self):
		MockYouTubeDepends.MockYouTubeDepends().mockXBMC()
		MockYouTubeDepends.MockYouTubeDepends().mock()
	
	def readTestInput(self, filename, should_eval = True):
		try:
			testinput = open("resources/" + filename)
			inputdata = testinput.read()
		except:
			testinput = io.open("resources/" + filename)
			inputdata = testinput.read()

		if should_eval:
			inputdata = eval(inputdata)
		return inputdata
	
	def raiseError(self, exception):
		raise exception
