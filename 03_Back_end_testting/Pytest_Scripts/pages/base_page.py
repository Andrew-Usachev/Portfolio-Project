import requests
import inspect
import sys
import pdb
import traceback
import time
import json
from bs4 import BeautifulSoup

status = 0


class BasePage:

    def __init__(self, *args):
        self.args = args

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
        traceback.print_exc()  # for debug
        status = 1
        return False

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

    def send_post_request(self):
        """
        Send a POST request using the provided arguments.

        :param self: The object instance
        :return: The response from the POST request
        """
        response = requests.post(self.args[0], headers=self.args[1], data=self.args[2])
        return response

    def validate_response_code(self, send_method, expected_code):
        """
        Validate the response code received by the send_method.

        Args:
            self: The object instance
            send_method: The method to send the request
            expected_code: The expected response code

        Returns:
            None
        """
        global status
        response = send_method()
        if response.status_code == expected_code:
            print(
                "\033[92mPass:\033[0m Response code is correct. Code is:", expected_code
            )
        else:
            print(
                "\033[91mFail:\033[0m Response code is not as expected. Correct code is:",
                response.status_code,
            )
            self.print_problem("Response code")

    def validate_response_time(self, send_method, max_response_time):
        """
        Validates the response time of a given send method.

        Args:
            send_method: The method to send the request.
            max_response_time: The maximum acceptable response time in milliseconds.

        Returns:
            The response from the send method.
        """
        global status
        start_time = time.time()
        response = send_method()
        end_time = time.time()
        response_time = (end_time - start_time) * 1000
        if response_time <= max_response_time:
            print("\033[92mPass:\033[0m Response time is within the expected range. Time for method is:", response_time)
        else:
            print("\033[91mFail:\033[0m Response time exceeds the expected range. Time for method is:", response_time)
            self.print_problem("Response time")

        return response

    def validate_response_size(self, send_method, expected_size):
        """
        Validates the size of the response returned by the given send_method.

        Args:
            self: The object instance
            send_method: The method used to send the request
            expected_size: The expected size of the response content

        Returns:
            None
        """
        global status
        response = send_method()
        if len(response.content) == expected_size:
            print(
                "\033[92mPass:\033[0m Response size is correct. Size is:",
                expected_size,
            )
        else:
            print(
                "\033[91mFail:\033[0m Response size is not as expected. Correct size is:",
                len(response.content),
            )
            self.print_problem("Response size")

    def validate_response_text(self, send_method, expected_text):
        """
        Validate the response text for a given send method and expected text.

        Parameters:
            self (object): The object instance
            send_method (function): The method to send the request
            expected_text (str): The expected text in the response

        Returns:
            None
        """
        global status
        response = send_method()
        response_text = response.text
        if expected_text in response_text:
            print("\033[92mPass:\033[0m Response contains the expected text:", expected_text)
        else:
            print("\033[91mFail:\033[0m Response does not contain the expected text:", expected_text,
                  "Correct text is:", response_text)
            self.print_problem("Response text")

    def validate_response_header_partial_match(self, send_method, expected_header, expected_value):
        global status
        response = send_method()
        header_value = response.headers.get(expected_header)
        if expected_value in header_value:
            print("\033[92mPass:\033[0m Header", expected_header, "contains the expected partial value:",
                  expected_value)
        else:
            print("\033[91mFail:\033[0m Header", expected_header, "does not contain the expected partial value:",
                  expected_value, "Correct value is:", header_value)
            self.print_problem("Response header")

    def validate_response_headers_and_values(self, send_method, expected_headers, skip_check_status="Skip_check_OFF",
                                             skip_headers=None):
        """
        Validate the response header for a partial match with the expected value.

        Parameters:
            send_method (function): The method for sending the request.
            expected_header (str): The expected header in the response.
            expected_value (str): The expected partial value in the header.

        Returns:
            None
        """
        global status
        response = send_method()
        headers = response.headers
        if skip_check_status == "Skip_check_OFF":
            skip_headers = []
        else:
            if skip_headers is None:
                skip_headers = []
        for header, value in expected_headers.items():
            if header in skip_headers:
                continue
            if header in headers and headers[header] == value:
                print("\033[92mPass:\033[0m Header", header, "is correct. Value is:", value)
            elif header in headers and headers[header] != value:
                print("\033[91mFail:\033[0m Header", header, "is not as expected. Correct value is:", headers[header])
                self.print_problem("Response headers and values")

    def validate_response_header_and_value(self, send_method, expected_header, expected_value):
        """
        Validate the response header and value.

        Args:
            self: The object instance.
            send_method: The method to send the request.
            expected_header: The expected header in the response.
            expected_value: The expected value for the header.

        Returns:
            None
        """
        global status
        response = send_method()
        header_value = response.headers.get(expected_header)
        if expected_value in header_value:
            print("\033[92mPass:\033[0m Header", expected_header, "contains the expected value:",
                  expected_value)
        else:
            print("\033[91mFail:\033[0m Header", expected_header, "does not contain the expected value:",
                  expected_value)
            self.print_problem("Response header and value")

    def validate_response_headers(self, send_method, expected_headers):
        """
        Validate the response headers from the send_method using the expected_headers.

        Args:
            self: The object instance.
            send_method: The method to send the request.
            expected_headers: The list of headers expected in the response.

        Returns:
            None
        """
        global status
        response = send_method()
        headers = response.headers
        for header in expected_headers:
            if header in headers:
                print("\033[92mPass:\033[0m Header", header, "is correct.")
            else:
                print("\033[91mFail:\033[0m Header", header, "is not as expected. Correct header is:", headers)
                self.print_problem("Response headers")

    def validate_response_header(self, send_method, expected_header):
        """
        Validate the response header of the given send_method against the expected_header.

        Args:
            self: The object itself.
            send_method: The method to send the request.
            expected_header: The expected header to validate against.

        Returns:
            None
        """
        global status
        response = send_method()
        if response.headers[expected_header]:
            print("\033[92mPass:\033[0m Header", expected_header, "is correct."),
        else:
            print("\033[91mFail:\033[0m Header", expected_header, "is not as expected.")
            self.print_problem("Response header")

    def response_to_not_be_error(self, send_method, error_text):
        """
        Checks the response from the send_method for the absence of the specified error text.

        Args:
            self: The object itself.
            send_method: The method used to send the request.
            error_text: The text to check for in the response.

        Returns:
            None
        """
        global status
        response = send_method()
        if error_text not in response.text:
            print("\033[92mPass:\033[0m Response does not contain the error")
        else:
            print("\033[91mFail:\033[0m Response contains the error")
            self.print_problem("Response error")

    def response_to_be_error(self, send_method, error_text):
        """
        Takes in a send_method and error_text to check if the response contains the error.
        Prints a pass message if the error is present, otherwise prints a fail message and calls
        the print_problem method with the argument "Response error".
        """
        global status
        response = send_method()
        if error_text in response.text:
            print("\033[92mPass:\033[0m Response contain the error")
        else:
            print("\033[91mFail:\033[0m Response does not contain the error")
            self.print_problem("Response error")

    def validate_response_have_body(self, send_method):
        """
        Validate if the response contains a body after sending a request.

        Args:
            self: The object itself.
            send_method: The method used to send the request.

        Returns:
            None
        """
        global status
        response = send_method()
        if response.text:
            print("\033[92mPass:\033[0m Response contains a body")
        else:
            print("\033[91mFail:\033[0m Response does not contain a body")
            self.print_problem("Response body")

    def validate_response_to_be_json(self, send_method):
        """
        Validates the response to be a JSON by sending a method and checking if the response is a valid JSON.
        Parameters:
            self: the instance of the class
            send_method: the method to send the request
        Returns:
            None
        """
        global status
        response = send_method()
        try:
            json_data = response.json()
            print("\033[92mPass:\033[0m Response is a valid JSON")
        except json.JSONDecodeError:
            print("\033[91mFail:\033[0m Response is not a valid JSON")
            self.print_problem("Response JSON")

    def validate_response_html_format(self, send_method):
        """
        Validates the HTML format of the response received using the specified send_method.

        Args:
            self: The object instance
            send_method: The method used to send the request

        Returns:
            None
        """
        response = send_method()
        try:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            if soup:
                print("\033[92mPass:\033[0m Response is in HTML format")
            else:
                print("\033[91mFail:\033[0m Response is not in HTML format")
                self.print_problem("Response HTML format")
        except Exception:
            print("\033[91mFail:\033[0m Error occurred while checking HTML format")
            self.print_problem("Response HTML format")

    def validate_response_json_body_to_not_be_error(self, send_method, error_text):
        """
        Validates the response JSON body to ensure it does not contain a specified error text.

        Args:
            self: The object instance
            send_method: The method to send the request
            error_text: The error text to check for in the JSON body

        Returns:
            None
        """
        global status
        response = send_method()
        try:
            json_data = response.json()
            if error_text not in json_data:
                print("\033[92mPass:\033[0m JSON body does not contain the key 'error'")
            else:
                print("\033[91mFail:\033[0m JSON body contains the key 'error'")
                self.print_problem("JSON body error")
        except json.JSONDecodeError:
            print("\033[91mFail:\033[0m Response is not a valid JSON")
            self.print_problem("Response JSON")

    def validate_response_json_body_key_format(self, send_method, response_key, response_key_type):
        """
        Validates the format of the specified key in the JSON response body.

        Args:
            self: The object instance
            send_method: The method to send the request
            response_key: The key in the JSON response body to validate
            response_key_type: The expected type of the response_key

        Returns:
            None
        """
        global status
        response = send_method()
        try:
            json_data = response.json()
            response_date = json_data.get(response_key)
            if isinstance(response_date, response_key_type):
                print(f"\033[92mPass:\033[0m {response_key} in the JSON body is a {response_key_type}")
            else:
                print(
                    f"\033[91mFail:\033[0m {response_key} in the JSON body is not a {response_key_type}. "
                    f"Expected type: {type(response_date).__name__}")
                self.print_problem("JSON body format")
        except json.JSONDecodeError:
            print("\033[91mFail:\033[0m Response is not a valid JSON")
            self.print_problem("Response JSON")

    def validate_response_json_body_format(self, send_method, response_body_type):
        """
        Validates the format of the JSON response body.

        Args:
            self: The object instance
            send_method: The method used to send the request
            response_body_type: The expected type of the response body

        Returns:
            None
        """
        global status
        response = send_method()
        try:
            json_data = response.json()
            if isinstance(json_data, response_body_type):
                print(f"\033[92mPass:\033[0m JSON body is a {response_body_type}")
            else:
                print(
                    f"\033[91mFail:\033[0m JSON body is not a {response_body_type}. Expected type: {type(json_data).__name__}")
                self.print_problem("JSON body format")
        except json.JSONDecodeError:
            print("\033[91mFail:\033[0m Response is not a valid JSON")
            self.print_problem("Response JSON")

    def check_value_in_db(self, get_db_session, table_name, row_name, row_value):
        """
        Check if a specific value exists in the given table in the database.

        Parameters:
            get_db_session (function): A function that returns a database session.
            table_name (str): The name of the table to search the value in.
            row_name (str): The name of the column in the table to search for the value.
            row_value (str): The value to search for in the specified column.

        Returns:
            None
        """
        global status
        try:
            data = get_db_session.query(table_name).all()
            found = False
            for row in data:
                if getattr(row, row_name) == row_value:
                    found = True
                    print("\033[92mPass:\033[0m Row", row_name, "сontains value", row_value)
                    break
            if not found:
                print("\033[91mFail:\033[0m Row", row_name, "does not contain value", row_value)
                self.print_problem("Row in DB")
        except Exception as e:
            print(f"\033[91mFail:\033[0m {e}")
            self.print_problem("Database connection")

    def check_row_in_db(self, get_db_session, table_name, row_name):
        """
        Check if a specific row is present in the given table in the database.

        Args:
            get_db_session: The session to access the database.
            table_name: The name of the table to search in.
            row_name: The name of the row to check for existence.

        Returns:
            None
        """
        global status
        try:
            data = get_db_session.query(table_name).all()
            found = False
            for row in data:
                if hasattr(row, row_name):
                    found = True
                    print(f"\033[92mPass:\033[0m Row {row_name} in table {table_name}")
                    break
            if not found:
                print(f"\033[91mFail:\033[0m Row {row_name} is not in table {table_name}")
                self.print_problem("Row in DB")
        except Exception as e:
            print(f"\033[91mFail:\033[0m Session was not created. {e}")
            self.print_problem("Database connection")

    def add_new_data_in_db(self, get_db_session, table_name, generator, get_add_method):
        """
        Add new data in the database.

        Args:
            get_db_session: Function to get the database session.
            table_name: The table name to add data to.
            generator: The data generator.
            get_add_method: Function to add data to the database.

        Returns:
            None
        """
        global status
        try:
            data = table_name(**generator.build())
            get_add_method(get_db_session, data)
            print(f"\033[92mPass:\033[0m Data {data} was added")
        except Exception as e:
            print(f"\033[91mFail:\033[0m Data was not added. {e}")
            self.print_problem("Database connection")

    def add_new_bad_data_in_db(self, get_db_session, table_name, generator, get_add_method):
        """
        Adds new bad data in the database.

        Args:
            self: The object itself.
            get_db_session: The function to get the database session.
            table_name: The name of the table to add data to.
            generator: The data generator for the new data.
            get_add_method: The method to add data to the database.

        Returns:
            None
        """
        global status
        try:
            data = table_name(**generator.build())
            get_add_method(get_db_session, data)
            print(f"\033[91mFail:\033[0m Data {data} was added")
            self.print_problem("Database connection")
        except Exception as e:
            print(f"\033[92mPass:\033[0m Data {e} was not added.")

    def update_data_in_db(self, get_db_session, table_name, attribute, value, generator, get_update_method):
        """
        Update data in the database.

        Args:
            get_db_session: The function to get the database session.
            table_name: The name of the table in the database.
            attribute: The attribute to filter the data by.
            value: The value of the attribute to filter the data by.
            generator: The generator function to build new data.
            get_update_method: The method to update the database.

        Returns:
            None
        """
        global status
        try:
            data = get_db_session.query(table_name).filter(getattr(table_name, attribute) == value).first()
            if data:
                new_data = generator.build()
                for key, value in new_data.items():
                    setattr(data, key, value)
                get_update_method(get_db_session, data)
                print(f"\033[92mPass:\033[0m Data {data} was updated")
            else:
                print(f"\033[91mFail:\033[0m Data {data} was not updated.")
                self.print_problem("Database update")
        except Exception as e:
            print(f"\033[91mFail:\033[0m No data found with {attribute} = {value} {e}")
            self.print_problem("Data not found")

    def update_bad_data_in_db(self, get_db_session, table_name, attribute, value, generator, get_update_method):
        """
        Update bad data in the database.

        Args:
            self: The object instance.
            get_db_session: The function to get the database session.
            table_name: The name of the table in the database.
            attribute: The attribute to filter the data in the table.
            value: The value of the attribute to filter the data in the table.
            generator: The generator to build new data.
            get_update_method: The method to update the data in the database.

        Returns:
            None
        """
        global status
        try:
            data = get_db_session.query(table_name).filter(getattr(table_name, attribute) == value).first()
            if data:
                new_data = generator.build()
                for key, value in new_data.items():
                    setattr(data, key, value)
                get_update_method(get_db_session, data)
                print(f"\033[91mFail:\033[0m Data {data} was updated")
                self.print_problem("Data found")
        except Exception as e:
            print(f"\033[92mPass:\033[0m Data was not updated. {e}")

    def delete_data_in_db(self, get_db_session, table_name, filter_data):
        """
        Deletes data in the specified table based on the provided filter data.

        Args:
            self: The instance of the class.
            get_db_session: The database session object.
            table_name: The name of the table where the data will be deleted.
            filter_data: The filter criteria for deleting the data.

        Returns:
            None
        """
        global status
        try:
            get_db_session.query(table_name).filter(filter_data).delete()
            get_db_session.commit()
            print(f"\033[92mPass:\033[0m Data {filter_data} was deleted")
        except Exception as e:
            print(f"\033[91mFail:\033[0m Data {filter_data} was not deleted. {e}")
            self.print_problem("Database connection")
