from time import sleep

from seleniumbase import BaseCase


class Task2(BaseCase):

    def test_task_2(self):
        # Open Google Chrome with website www.google.com
        self.open("www.google.com")

        # Click on the button with ID L2AGLb (Godkan alla)
        self.click("//button[@id='L2AGLb']")

        # Send Keys to the search writing 'automation"
        self.send_keys("#APjFqb", "automation")

        # Click search
        self.click("//div[@class='FPdoLc lJ9FBc']/center/input[@class='gNO89b']")

        # Click the wikipedia entry
        self.click("//*[@href='https://sv.wikipedia.org/wiki/Automation']")
        self.is_element_visible("//a[@class='mw-wiki-logo']")

        # Open Spanish wikipedia website
        self.click("//span[contains(text(),'Español')]")

        self.assert_text_visible("en 1785, convirtiéndose en el primer proceso industrial completamente automatizado.")
        self.save_screenshot("zara_task_2")
        sleep(3)

    def test_task_3(self):
        # Open Google chrome with website www.google.com
        self.open("www.google.com")

        # Click on the button with ID L2AGLb (Godkan alla)
        self.click("//button[@id='L2AGLb']")
