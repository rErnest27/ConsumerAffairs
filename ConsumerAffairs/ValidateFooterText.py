# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class ConsumerAffairs2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):    
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
    
    def test_footerSearch(self):        
        browser = self.browser
        self.browser.get("https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.webdisclaimer = ("Copyright © 2021 Consumers Unified LLC. All Rights Reserved. The contents of this site may not be republished, reprinted, rewritten or recirculated without written permission.")
        self.disclaimer = browser.find_element_by_xpath("/html/body/footer/div[2]/div[1]/p[2]").text
        self.assertEqual(self.disclaimer, self.webdisclaimer, "Web page footer doesn't match")
        
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        
if __name__ == '__main__':
    unittest.main()