import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MinWebTest(unittest.TestCase):
    # execute the test <x = 0, y = 0, z = 0, submitButton = click> and check the output message is correct
    def test0(self):
        driver = webdriver.Safari()
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/jakeyoon/Documents/2020Fall/EE461L/tutorial8/part2/min.html")
        elem = driver.find_element_by_id("x")
        elem.send_keys("0") # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys("0") # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys("0") # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(0, 0, 0) = 0", output)
        time.sleep(2)
        driver.get(r"file:///Users/jakeyoon/Documents/2020Fall/EE461L/tutorial8/part2/min.html")
        elem = driver.find_element_by_id("x")
        elem.send_keys("0") # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys("0") # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys("1") # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(0, 0, 1) = 0", output)
        time.sleep(2)
        driver.get(r"file:///Users/jakeyoon/Documents/2020Fall/EE461L/tutorial8/part2/min.html")
        elem = driver.find_element_by_id("x")
        elem.send_keys("-1") # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys("1") # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys("1") # enter a representative for z
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("", output)
        time.sleep(2)
        driver.get(r"file:///Users/jakeyoon/Documents/2020Fall/EE461L/tutorial8/part2/min.html")
        elem = driver.find_element_by_id("x")
        elem.send_keys("1") # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys("1") # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys("-1") # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(1, 1, -1) = -1", output)
        time.sleep(2)
        driver.get(r"file:///Users/jakeyoon/Documents/2020Fall/EE461L/tutorial8/part2/min.html")
        elem = driver.find_element_by_id("x")
        elem.send_keys("1") # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys("0") # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys("-1") # enter a representative for z
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("", output)
        time.sleep(2)
        driver.get(r"file:///Users/jakeyoon/Documents/2020Fall/EE461L/tutorial8/part2/min.html")
        elem = driver.find_element_by_id("x")
        elem.send_keys("0") # enter a representative for x
        elem = driver.find_element_by_id("y")
        elem.send_keys("-1") # enter a representative for y
        elem = driver.find_element_by_id("z")
        elem.send_keys("-1") # enter a representative for z
        elem = driver.find_element_by_id("computeButton")
        elem.click() #click the button
        result = driver.find_element_by_id("result")
        output = result.text # read the output text
        self.assertEqual("min(1, 1, -1) = -1", output)
        driver.close() # close the browser window

if __name__ == '__main__':
    unittest.main()
