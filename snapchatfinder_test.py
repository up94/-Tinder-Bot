# Author: Stan Fortoński
# Date: 06.05.2020
# Snapchat Finder Test

import unittest
from time import sleep
from tinderlogin import TinderLogin
from snapchatfinder import SnapchatFinder
from driver import getDriver

class TestSnapchatFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()
        cls.login = TinderLogin(cls.driver)
        cls.login.logIn()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.insta = SnapchatFinder(self.driver)

    def changeNameScript(self, name):
        self.driver.execute_script('document.querySelector("#content > div > div:nth-child(1) > div > main > div:nth-child(1) > div > div > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(3) > div:nth-child(6) > div > div:nth-child(2) > div > div > span").innerHTML = "'+name+'"');

    def testSnapSaving(self):
        testFileName = 'snap_test.txt'
        with open(testFileName, 'w') as file:
            file.write('')

        self.driver.get('https://tinder.com/app/recs')
        sleep(5)
        self.changeNameScript('snap _x_test_x_')
        self.assertTrue(self.insta.findAndSaveSnapchatNick(fileName=testFileName))

        self.changeNameScript('snap: _x_test_x_')
        self.assertTrue(self.insta.findAndSaveSnapchatNick(fileName=testFileName))

        self.changeNameScript('snap:_x_test_x_')
        self.assertTrue(self.insta.findAndSaveSnapchatNick(fileName=testFileName))

        self.changeNameScript('snapchat _x_test_x_')
        self.assertTrue(self.insta.findAndSaveSnapchatNick(fileName=testFileName))

        self.changeNameScript('snapchat: _x_test_x_')
        self.assertTrue(self.insta.findAndSaveSnapchatNick(fileName=testFileName))

        self.changeNameScript('snapchat:_x_test_x_')
        self.assertTrue(self.insta.findAndSaveSnapchatNick(fileName=testFileName))

if __name__ == '__main__':
    unittest.main()