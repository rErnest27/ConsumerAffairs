from selenium import webdriver
import unittest

class ConsumerAffairs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):    
        cls.browser = webdriver.Firefox()
        cls.browser.maximize_window()
    
    def test_disclaimerSearch(self):        
        browser = self.browser
        self.browser.get("https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.webdisclaimer = ("ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers.")
        self.disclaimer = browser.find_element_by_xpath("/html/body/footer/div[2]/div[1]/p[1]").text
        self.assertEqual(self.disclaimer, self.webdisclaimer, "Web page disclaimer doesn't match")
        
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        
if __name__ == '__main__':
    unittest.main()