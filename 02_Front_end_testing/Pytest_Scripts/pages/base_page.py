import traceback
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import jsonschema
import inspect
import requests
import sys
import pdb
import os

status = 0


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Open the specified URL in the browser.

        This function navigates to the given URL by calling the `get` method of the `browser` object with the `url` parameter.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        self.browser.get(self.url)

    def close(self):
        """
        Close the browser.

        This function closes the browser by calling the `close` method of the `browser` object.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        self.browser.close()

    def quit(self):
        """
        Quit the browser.

        This function closes the browser by calling the `quit` method of the `browser` object.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        self.browser.quit()

    def print_method_name(self):
        """
        Prints the name of the calling method to the console.

        This function uses the `inspect` module to retrieve information about the calling method.
        It then prints the name of the calling method to the console in a formatted message.
        The method name is obtained from the `frame_info` object returned by `inspect.getframeinfo`.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        frame_info = inspect.getframeinfo(inspect.currentframe().f_back)
        method_name = frame_info.function
        print(f"\033[93mStart method:\033[0m \033[92m{method_name}\033[0m")

    def print_problem(self, what):
        """
        A function that is called when an element is not found.

        Args:
            what (str): The name of the locator that was not found.

        Returns:
            bool: False indicating that the element was not found.
        """
        global status
        print(
            "\033[91mFail:\033[0m Warning:",
            what,
            "have a problem! Error is:",
            sys.exc_info()[0],
        )
        # traceback.print_exc()  # for debug
        status = 1
        self.take_screenshot_on_error(what)
        return False

    def check_title(self, expected_title):
        """
        Checks if the actual title of the web page matches the expected title.

        Parameters:
            expected_title (str): The expected title of the web page.

        Returns:
            None
        """
        global status
        actual_title = self.browser.title
        if actual_title == expected_title:
            print(f"\033[92mPass:\033[0m Expected title: {expected_title} is correct")
        else:
            print(
                f"\033[91mFail:\033[0m Expected title: {expected_title} is not correct, title is: ",
                actual_title,
            )
            status = 1

    def check_url(self, expected_url):
        """
        Checks if the current URL matches the expected URL and prints the result.

        Parameters:
            expected_url (str): The URL that is expected to match the current URL.

        Returns:
            None
        """
        global status
        current_url = self.browser.current_url
        if current_url == expected_url:
            print(f"\033[92mPass:\033[0m Expected URL: {expected_url} is correct")
        else:
            print(
                f"\033[91mFail:\033[0m Expected URL: {expected_url} is not correct, URL is",
                current_url,
            )
            status = 1

    def check_API_status_code(self, expected_code):
        """
        Check the status code of the API.

        Parameters:
            expected_code (int): The expected status code.

        Returns:
            None

        Prints the result of the check, indicating whether the status code of the API
        matches the expected code. If the status code does not match, it sets the global
        variable `status` to 1.
        """
        global status
        code = requests.get(self.url).status_code
        if code == expected_code:
            print(
                f"\033[92mPass:\033[0m URL: {self.url} has", code, "as API status code"
            )
        else:
            print(
                f"\033[91mFail:\033[0m Status code for URL: {self.url} is not correct, status code is:",
                code,
            )
            status = 1

    def find_elem(self, locator):
        """
        Find the element located by the given locator.

        Args:
            locator: A tuple representing the locator strategy and value.

        Returns:
            The web element found by the given locator.
        """
        self.browser.implicitly_wait(5)
        element = self.browser.find_element(*locator)
        self.browser.execute_script(
            "return arguments[0].scrollIntoView(true);", element
        )
        return element

    def generate_random_string(self, length):
        """
        Generate a random string of the specified length.

        Parameters:
            self (obj): The object itself
            length (int): The length of the random string to be generated

        Returns:
            str: The randomly generated string
        """
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(length))

    def generate_random_sentence(self, length):
        """
        Generate a random sentence of the specified length using words from a predefined list.

        Args:
            self: The instance of the class.
            length (int): The length of the sentence to be generated.

        Returns:
            str: A randomly generated sentence with the first letter capitalized and ending with a period.
        """
        words = [
            "apple",
            "banana",
            "cherry",
            "date",
            "elderberry",
            "fig",
            "grapefruit",
            "honeydew",
            "kiwi",
            "lemon",
        ]
        sentence = " ".join(random.choice(words) for _ in range(length))
        return sentence.capitalize() + "."

    def generate_random_phone_number(self):
        """
        Generate a random phone number and format it as "X-XXX-XXX-XXXX".
        """
        number = "8" + "".join(random.choice("0123456789") for _ in range(10))
        formatted_number = "{}-{}-{}-{}".format(
            number[:1], number[1:4], number[4:7], number[7:]
        )
        return formatted_number

    def generate_random_text(self, length):
        """
        Generate random text of a specified length.

        Args:
            self: The instance of the class.
            length (int): The length of the random text to generate.

        Returns:
            str: The randomly generated text.
        """
        letters = string.ascii_letters
        return "".join(random.choice(letters) for i in range(length))

    def generate_random_email(self):
        """
        Generate a random email address.

        Parameters:
            self (obj): The object instance.

        Returns:
            str: A randomly generated email address.
        """
        random_name = self.generate_random_string(8)
        random_domain = self.generate_random_string(5)
        email = f"{random_name}@{random_domain}.com"
        return email

    def generate_random_number(self, start, end):
        """
        Generate a random number between the given start and end values.

        :param start: The start of the range for the random number
        :param end: The end of the range for the random number
        :return: A random integer between the start and end values
        """
        return random.randint(start, end)

    def generate_random_date(self, start_date, end_date):
        """
        Generate a random date between the start_date and end_date.

        :param start_date: The start date for the range.
        :type start_date: datetime
        :param end_date: The end date for the range.
        :type end_date: datetime
        :return: A randomly generated date between start_date and end_date.
        :rtype: datetime
        """
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()
        random_timestamp = random.uniform(start_timestamp, end_timestamp)
        random_date = datetime.fromtimestamp(random_timestamp)
        return random_date

    def check_response_body(self, url, schema, schema_name):
        """
        Check the response body against a given schema.

        Args:
            self: The object instance
            url: The URL to send the request to
            schema: The JSON schema to validate against
            schema_name: The name of the schema for logging purposes

        Returns:
            None
        """
        global status
        response = requests.get(url)
        response_body = response.json()
        try:
            jsonschema.validate(response_body, schema)
            print("\033[92mPass:\033[0m Response body for:", schema_name, " is valid")
        except jsonschema.exceptions.ValidationError as e:
            print(
                "\033[91mFail:\033[0m Response body for:", schema_name, " is not valid"
            )
            print("Error is: ", e)
            status = 1

    def is_element_present(self, locator, locator_name):
        """
        Check if the element is present using the provided locator and locator name.
        :param locator: The locator to find the element.
        :param locator_name: The name of the locator for logging purposes.
        :return: True if the element is found, otherwise an exception is handled.
        """
        global status
        try:
            self.find_elem(locator)
            print("\033[92mPass:\033[0m Element:", locator_name, "is found!")
            return True
        except Exception:
            self.print_problem(locator_name)

    def element_click(self, locator, locator_name):
        """
        Clicks on the element identified by the given locator.

        Args:
            locator: The locator of the element to be clicked.
            locator_name: A name or description for the locator.

        Returns:
            bool: True if the element is successfully clicked, False otherwise.
        """
        global status
        try:
            self.find_elem(locator)
            try:
                self.find_elem(locator).is_enabled()
                self.find_elem(locator).is_displayed()
                EC.element_to_be_clickable(locator)
                self.find_elem(locator).click()
                print("\033[92mPass:\033[0m Element:", locator_name, "clicked!")
                return True
            except Exception:
                print("\033[91mFail:\033[0m Element:", locator_name, "not clicked!")
                self.print_problem(locator_name)
        except Exception:
            self.print_problem(locator_name)

    def is_element_send_keys(self, locator, locator_name, text):
        """
        Send specified keys to the web element located by `locator`.

        Args:
            self: The object instance.
            locator: The locator strategy to find the web element.
            locator_name: The name of the locator.
            text: The text to be sent to the web element.

        Returns:
            bool: True if the keys are successfully sent, False otherwise.
        """
        global status
        try:
            self.find_elem(locator).send_keys(text)
            print("\033[92mPass:\033[0m Element:", locator_name, f"sent keys: {text}!")
            return True
        except Exception:
            self.print_problem(locator_name)

    def is_element_clickable(self, locator, locator_name):
        """
        Checks if the element located by the given locator is clickable.

        :param locator: The locator of the element to be checked.
        :param locator_name: The name of the locator for logging purposes.
        :return: True if the element is clickable, False otherwise.
        """
        global status
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(locator)
            )
            self.browser.execute_script(
                "return arguments[0].scrollIntoView(true);", element
            )
            print("\033[92mPass:\033[0m Element:", locator_name, "found and clickable!")
            return True
        except Exception:
            self.print_problem(locator_name)

    def is_element_enabled(self, locator, locator_name):
        """
        Check if the element located by the given locator is enabled.

        Args:
            locator: The locator of the element.
            locator_name: The name of the element locator.

        Returns:
            bool: True if the element is enabled, False otherwise.
        """
        global status
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(locator)
            )
            if element.is_enabled():
                self.browser.execute_script(
                    "return arguments[0].scrollIntoView(true);", element
                )
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "presence and enabled!",
                )
                return True
            else:
                print("\033[91mFail:\033[0m Element:", locator_name, "not enabled!")
        except Exception:
            self.print_problem(locator_name)

    def is_element_or_text_present(self, locator, expected_text):
        """
        Check if the specified element or text is present and matches the expected text.

        Parameters:
            locator (str): The locator for finding the element.
            expected_text (str): The text expected to be present in the element.

        Returns:
            bool: True if the element and text are present and match, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            actual_text = element.text
            if actual_text == expected_text:
                print(
                    "\033[92mPass:\033[0m Element is found and text in element:",
                    expected_text,
                    "is correct!",
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Text in element:",
                    expected_text,
                    "is incorrect! Correct text is: ",
                    actual_text,
                )
                status = 1
                self.take_screenshot_on_error(expected_text)
                return False
        except Exception:
            self.print_problem(expected_text)

    def is_element_animating(self, locator, locator_name):
        """
        Check if the element located by the given locator is animating.

        Args:
            locator: The locator for the element.
            locator_name: The name of the locator for logging purposes.

        Returns:
            bool: True if the element is animating, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            if element.value_of_css_property("transform") != "none":
                print(f"\033[92mPass:\033[0m Element: {locator_name} is animating!")
                return True
            else:
                print(f"\033[91mFail:\033[0m Element: {locator_name} is not animating!")
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_element_video(self, locator, locator_name):
        """
        Check if the element identified by the locator is a video.
        Args:
            locator: The locator of the element.
            locator_name: Name of the element for reporting.
        Returns:
            True if the element is a video, False otherwise.
        """
        global status
        try:
            self.browser.implicitly_wait(5)
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(locator)
            )
            element = self.find_elem(locator)
            if element.tag_name == "video":
                print(f"\033[92mPass:\033[0m Element: {locator_name} is video!")
                return True
            else:
                print(f"\033[91mFail:\033[0m Element: {locator_name} is not video!")
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_video_muted(self, locator, locator_name):
        """
        Check if the video element located by the given locator is muted.

        :param locator: The locator of the video element.
        :param locator_name: The name of the video element for logging purposes.
        :return: True if the video is muted, False otherwise.
        """
        global status
        try:
            self.browser.implicitly_wait(5)
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(locator)
            )
            element = self.find_elem(locator)
            if element.get_attribute("muted") == "true":
                print(f"\033[92mPass:\033[0m Element: {locator_name} is muted!")
                return True
            else:
                print(f"\033[91mFail:\033[0m Element: {locator_name} is not muted!")
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_video_duratation(self, locator, locator_name):
        """
        Check if the video duration is available for the given element locator.

        Args:
            locator: The locator of the element.
            locator_name: The name of the element locator.

        Returns:
            bool: True if the video duration is available, False otherwise.
        """
        global status
        try:
            self.browser.implicitly_wait(5)
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(locator)
            )
            element = self.find_elem(locator)
            duraton = element.get_attribute("duration")
            if duraton != "NaN":
                print(
                    f"\033[92mPass:\033[0m Element: {locator_name} has duration! Video duration is: {duraton}"
                )
                return True
            else:
                print(f"\033[91mFail:\033[0m Element: {locator_name} has no duration!")
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def check_element_size(
            self, locator, locator_name, expected_width, expected_height
    ):
        """
        Check the size of the element identified by the given locator.

        Args:
            locator (str): The locator of the element.
            locator_name (str): The name of the locator.
            expected_width (int): The expected width of the element.
            expected_height (int): The expected height of the element.

        Returns:
            bool: True if the element has the expected size, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            actual_width = element.size["width"]
            actual_height = element.size["height"]

            if actual_width == expected_width and actual_height == expected_height:
                print(f"\033[92mPass:\033[0m Element: {locator_name} has correct size!")
                return True
            else:
                print(
                    f"\033[91mFail:\033[0m Element: {locator_name} has incorrect size! Actual size is: {actual_width}x{actual_height}"
                )
                status = 1
                self.take_screenshot_on_error(locator_name)
                return False
        except Exception:
            self.print_problem(locator_name)

    def select_element_by_value(self, locator, locator_name, value, value_name):
        """
        Selects an element by its value from a dropdown using the provided locator and value.

        Args:
            locator: The locator to find the dropdown element.
            locator_name: The name of the locator for error messaging.
            value: The value of the option to be selected from the dropdown.
            value_name: The name of the value for error messaging.

        Returns:
            bool: True if the value is selected successfully, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            try:
                select = Select(element)
                select.select_by_value(value)
                print(f"\033[92mPass:\033[0m Value: {value_name} is selected!")
                return True
            except Exception:
                print(f"\033[91mFail:\033[0m Value: {value_name} is not selected!")
                self.print_problem(value_name)
        except Exception:
            self.print_problem(locator_name)

    def select_element_by_text(self, locator, locator_name, value, value_name):
        """
        Selects an element by its text using the given locator and value.

        Args:
            locator (str): The locator to find the element.
            locator_name (str): The name of the locator for error printing.
            value (str): The text value to be selected.
            value_name (str): The name of the value for error printing.

        Returns:
            bool: True if the element is successfully selected, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            try:
                select = Select(element)
                select.select_by_visible_text(value)
                print(f"\033[92mPass:\033[0m Value: {value_name} is selected!")
                return True
            except Exception:
                print(f"\033[91mFail:\033[0m Value: {value_name} is not selected!")
                self.print_problem(value_name)
        except Exception:
            self.print_problem(locator_name)

    def select_element_by_index(self, locator, locator_name, value, value_name):
        """
        Selects an element by index using the specified locator and value.

        Args:
            locator: The locator for finding the element.
            locator_name: The name of the locator for error reporting.
            value: The index value to select.
            value_name: The name of the index value for error reporting.

        Returns:
            True if the element is successfully selected, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            try:
                select = Select(element)
                select.select_by_index(value)
                print(f"\033[92mPass:\033[0m Value: {value_name} is selected!")
                return True
            except Exception:
                print(f"\033[91mFail:\033[0m Value: {value_name} is not selected!")
                self.print_problem(value_name)
        except Exception:
            self.print_problem(locator_name)

    def is_attribute_present(self, locator, locator_name, attribute):
        """
        Check if the given attribute is present for the specified element.

        Args:
            locator: str, the locator for finding the element
            locator_name: str, the name of the locator
            attribute: str, the attribute to check for

        Returns:
            bool: True if the attribute is present, False otherwise
        """
        global status
        try:
            element = self.find_elem(locator)
            attribute_value = element.get_attribute(attribute)
            if attribute_value:
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "has attribute:",
                    attribute,
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Element:",
                    locator_name,
                    "does not have attribute:",
                    attribute,
                )
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_attribute_have_correct_value(self, locator, locator_name, attribute, value):
        """
        Check if the specified element attribute has the correct value.

        Args:
            locator: The locator of the element.
            locator_name: The name of the locator.
            attribute: The attribute to check.
            value: The expected value of the attribute.

        Returns:
            bool: True if the attribute has the correct value, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            attribute_value = element.get_attribute(attribute)
            if attribute_value == value:
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "has attribute:",
                    attribute,
                    "with value:",
                    value,
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Element:",
                    locator_name,
                    "does not have attribute:",
                    attribute,
                    "with value:",
                    value,
                )
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def show_all_element_properties(self, locator):
        """
        Retrieves and prints all properties of a specified element identified by the given locator.

        :param locator: The locator used to identify the element.
        :type locator: str
        """
        element = self.find_elem(locator)
        all_properties = element.get_property("attributes")
        for prop in all_properties:
            print(prop["name"], ":", prop["value"])

    def is_property_present(self, locator, locator_name, property):
        """
        Check if a property is present for a given element and return True if present, False otherwise.

        Parameters:
            locator (str): The locator to find the element.
            locator_name (str): The name of the locator for logging purposes.
            property (str): The property to check for.

        Returns:
            bool: True if the property is present, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            property_value = element.get_property(property)
            if property_value:
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "has property:",
                    property,
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Element:",
                    locator_name,
                    "does not have property:",
                    property,
                )
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_property_have_correct_value(self, locator, locator_name, property, value):
        """
        Check if the property of the element located by the given locator has the correct value.

        :param locator: The locator used to find the element.
        :param locator_name: The name of the locator for logging purposes.
        :param property: The property to check.
        :param value: The expected value of the property.
        :return: True if the property has the correct value, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            property_value = element.get_property(property)
            if property_value == value:
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "has property:",
                    property,
                    "with value:",
                    value,
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Element:",
                    locator_name,
                    "does not have property:",
                    property,
                    "with value:",
                    value,
                )
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_css_property_value_present(self, locator, locator_name, property):
        """
        Check if the given CSS property value is present for the specified element.

        Parameters:
            locator (str): The locator for finding the element.
            locator_name (str): The name of the element for logging purposes.
            property (str): The CSS property to check.

        Returns:
            bool: True if the property value is present, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            property_value = element.value_of_css_property(property)
            if property_value:
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "has css property:",
                    property,
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Element:",
                    locator_name,
                    "does not have css property:",
                    property,
                )
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_css_property_value_have_correct_value(
            self, locator, locator_name, property, value
    ):
        """
        Check if the CSS property value of the element located by the given locator has the correct value.

        Args:
            locator: The locator of the element.
            locator_name: The name of the locator for logging purposes.
            property: The CSS property to check.
            value: The expected value of the CSS property.

        Returns:
            bool: True if the CSS property value matches the expected value, False otherwise.
        """
        global status
        try:
            element = self.find_elem(locator)
            property_value = element.value_of_css_property(property)
            if property_value == value:
                print(
                    "\033[92mPass:\033[0m Element:",
                    locator_name,
                    "has css property:",
                    property,
                    "with value:",
                    value,
                )
                return True
            else:
                print(
                    "\033[91mFail:\033[0m Element:",
                    locator_name,
                    "does not have css property:",
                    property,
                    "with value:",
                    value,
                )
                status = 1
                return False
        except Exception:
            self.print_problem(locator_name)

    def is_not_element_present(self, locator, locator_name, timeout=4):
        """
        Check if the element is not present within the specified timeout.

        Args:
            self: the object instance
            locator: the locator of the element
            locator_name: the name of the locator
            timeout: the maximum time to wait for the element to be not present (default is 4)

        Returns:
            bool: True if the element is not present, False otherwise
        """
        global status
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located(locator)
            )
            print("\033[92mPass:\033[0m Element:", locator_name, "is not present!")
            return True
        except TimeoutException:
            print("\033[91mFail:\033[0m Element:", locator_name, "is present!")
            status = 1
            return False

    def is_element_disappeared(self, locator, locator_name, timeout=4):
        """
        Check if the element disappears within a specified timeout.

        :param locator: The locator of the element.
        :param locator_name: The name of the element for identification.
        :param timeout: The maximum time to wait for the element to disappear (default 4 seconds).
        :return: True if the element disappears, False otherwise.
        """
        global status
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located(locator)
            )
            print("\033[92mPass:\033[0m Element:", locator_name, "is disappeared!")
            return True
        except TimeoutException:
            print("\033[91mFail:\033[0m Element:", locator_name, "is not disappeared!")
            status = 1
            return False

    def take_screenshot_on_error(self, screenshot_name):
        """
        Takes a screenshot on error.

        Args:
            self: The class instance.
            screenshot_name (str): The name of the screenshot.

        Returns:
            None
        """
        global status
        if status == 1:
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = os.path.join(
                screenshot_dir, f"{screenshot_name}_{timestamp}.png"
            )
            self.browser.save_screenshot(screenshot_path)
            print("Error screenshot saved:", screenshot_path)

    def debug(self):
        """
        Debugs the program by setting a trace point using the `pdb` module.

        This function is used for debugging purposes. It will pause the program and open an interactive debugger when called.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        pdb.set_trace()

    def check_fail_status(self):
        """
        Check the status of the test and print a message indicating whether the test passed or failed.

        This function takes no parameters.

        Returns:
            None
        """
        global status
        if status:
            print("\033[91mTEST FAILED!\033[0m")
            status = 0
            assert (), "\033[91mWARNING!!! ERROR IN TEST!\033[0m"
        else:
            print("\033[92mTEST PASSED!\033[0m")
        status = 0

    def should_be_main_page(self):
        """
        Check if the current page should be the main page by verifying its URL, title, and API status code.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/")
        self.check_title("iBench.net - Remote Web & App Development Teams for Startups")
        self.check_API_status_code(200)

    def should_be_hireteam_page(self):
        """
        Check if the current page is the 'iBench.net' team search page, and verify the URL,
        title, and API status code.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/team-search")
        self.check_title(
            "iBench.net - Remote Web & App Development Teams for Startups / Development team request form"
        )
        self.check_API_status_code(200)

    def should_be_hiredevelopers_page(self):
        """
        Check if the hire developers page is accessible and returns the correct status code and title.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/hire-developers")
        self.check_title(
            "iBench.net - Remote Web & App Development Teams for Startups / Looking for a developers, UX/UI designer, QA or DevOps...or development agency?"
        )
        self.check_API_status_code(200)

    def should_be_blog_page(self):
        """
        Check if the current page should be the blog page.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/blog/")
        self.check_title("iBench - iBench - real-time developers Hiring")
        self.check_API_status_code(200)

    def should_be_register_page(self):
        """
        Check if the current page should be the register page.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/registration")
        self.check_title(
            "iBench.net - Remote Web & App Development Teams for Startups / Registration"
        )
        self.check_API_status_code(200)

    def should_be_login_page(self):
        """
        Check if the current page should be the login page.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/login")
        self.check_title(
            "iBench.net - Remote Web & App Development Teams for Startups / Log in"
        )
        self.check_API_status_code(200)

    def should_be_recovery_password_page(self):
        """
        Check if the current page should be the recovery password page.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/recovery")
        self.check_title(
            "iBench.net - Remote Web & App Development Teams for Startups / Recovery password"
        )
        self.check_API_status_code(200)

    def should_be_personal_page(self):
        """
        Check if the current page should be the personal page.
        """
        self.print_method_name()
        self.check_url("https://ibench.net/stats")
        self.check_title(
            "Daily updates | iBench.net - Remote Web & App Development Teams for Startups"
        )
        self.check_API_status_code(200)

    def clear_field_data(self, locator, locator_name):
        """
        Clear the field data by sending 'Control + a' keys and then the 'Delete' key.

        :param locator: the locator of the element
        :param locator_name: the name of the locator
        :return: None
        """
        self.print_method_name()
        self.is_element_send_keys(
            locator,
            locator_name,
            Keys.CONTROL + "a",
        )
        self.is_element_send_keys(
            locator,
            locator_name,
            Keys.DELETE,
        )
