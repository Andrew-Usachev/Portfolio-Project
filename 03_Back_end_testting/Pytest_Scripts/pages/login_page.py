from Portfolio_API.pages.base_page import BasePage
from Portfolio_API.srs.enums import *
from Portfolio_API.srs.pydantic_schemas import LoginResponseSchema
from Portfolio_API.srs import tables
from Portfolio_API.srs.builders import *


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # POSITIVE TESTS METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def can_login_user_with_correct_data(self):
        self.print_method_name()
        self.validate_response_code(self.send_post_request, 200)
        self.validate_response_time(self.send_post_request, 1500)
        self.validate_response_size(self.send_post_request, 1888)
        self.response_to_not_be_error(self.send_post_request, "Error")
        self.validate_response_have_body(self.send_post_request)
        self.validate_response_to_be_json(self.send_post_request)
        self.validate_response_json_body_to_not_be_error(self.send_post_request, "Error")
        self.validate_response_json_body_format(self.send_post_request, dict)
        self.validate_response_text(self.send_post_request, 'user')
        self.validate_response_json_body_key_format(self.send_post_request, 'user', dict)
        self.validate_response_headers(self.send_post_request, LoginPageCorrectData.HEADER_RESPONSE.value)
        self.validate_response_header_and_value(self.send_post_request, "Server", 'nginx')
        self.validate_response_headers_and_values(self.send_post_request,
                                                  LoginPageCorrectData.HEADER_RESPONSE.value, "Skip_check_ON", "Date")
        self.validate_response_header(self.send_post_request, "Date")
        self.validate_response_header_partial_match(self.send_post_request, 'Date',
                                                    formatted_datetime_only_date)

    def check_login_user_response_with_login_user_schema(self):
        self.print_method_name()
        login_user_data = self.send_post_request().json()
        try:
            LoginResponseSchema(**login_user_data["user"])
            print("\033[92mPass:\033[0m Login user response is valid")
        except:
            print("\033[91mFail:\033[0m Login user response is not valid")
            self.print_problem("Login user response")

    def check_data_in_find_contactors_base(self, get_db_session):
        self.print_method_name()
        self.check_row_in_db(get_db_session, tables.FindContactors, "Job_title")
        self.check_value_in_db(get_db_session, tables.FindContactors, "Id_Contractors", 1001)

    def add_data_in_find_contactors_base(self, get_db_session, get_add_method):
        self.print_method_name()
        self.add_new_data_in_db(get_db_session, tables.FindContactors, FindContractorsBaseBuilder(), get_add_method)
        last_row = get_db_session.query(tables.FindContactors).order_by(
            tables.FindContactors.Id_Contractors.desc()).first()
        self.delete_data_in_db(get_db_session, tables.FindContactors,
                               (tables.FindContactors.Id_Contractors == last_row.Id_Contractors))

    def update_data_in_find_contactors_base(self, get_db_session, get_update_method):
        self.print_method_name()
        self.update_data_in_db(get_db_session, tables.FindContactors, "Id_Contractors", 1003,
                               FindContractorsBaseBuilder().set_contractor_id(1003),
                               get_update_method)

    # ------------------------------------------------------------------------------------------------------------------
    # NEGATIVE TESTS METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def can_login_user_with_incorrect_url(self):
        self.print_method_name()
        self.validate_response_code(self.send_post_request, 404)
        self.validate_response_time(self.send_post_request, 6000)
        self.response_to_be_error(self.send_post_request, "Error")
        self.validate_response_have_body(self.send_post_request)
        self.validate_response_html_format(self.send_post_request)
        self.validate_response_text(self.send_post_request, "Cannot")
        self.validate_response_headers(self.send_post_request,
                                       LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_URL.value)
        self.validate_response_header_and_value(self.send_post_request, "Server", 'nginx')
        self.validate_response_headers_and_values(self.send_post_request,
                                                  LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_URL.value,
                                                  "Skip_check_ON",
                                                  ["Date"])
        self.validate_response_header(self.send_post_request, "Date")
        self.validate_response_header_partial_match(self.send_post_request, 'Date',
                                                    formatted_datetime_only_date)

    def can_login_user_with_incorrect_header(self):
        self.print_method_name()
        self.validate_response_code(self.send_post_request, 500)
        self.validate_response_time(self.send_post_request, 6000)
        self.validate_response_size(self.send_post_request, 34)
        self.validate_response_have_body(self.send_post_request)
        self.validate_response_html_format(self.send_post_request)
        self.validate_response_text(self.send_post_request, '{"error":"globals is not defined"}')
        self.validate_response_headers(self.send_post_request,
                                       LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_HEADER.value)
        self.validate_response_headers_and_values(self.send_post_request,
                                                  LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_HEADER.value,
                                                  "Skip_check_ON",
                                                  ["Date"])
        self.validate_response_header(self.send_post_request, "Date")
        self.validate_response_header_partial_match(self.send_post_request, 'Date',
                                                    formatted_datetime_only_date)

    def can_login_user_with_incorrect_password(self):
        self.print_method_name()
        self.validate_response_code(self.send_post_request, 400)
        self.validate_response_time(self.send_post_request, 6000)
        self.validate_response_size(self.send_post_request, 31)
        self.response_to_be_error(self.send_post_request, "error")
        self.validate_response_have_body(self.send_post_request)
        self.validate_response_to_be_json(self.send_post_request)
        self.validate_response_json_body_format(self.send_post_request, dict)
        self.validate_response_text(self.send_post_request, 'Incorrect password.')
        self.validate_response_json_body_key_format(self.send_post_request, 'error', str)
        self.validate_response_headers(self.send_post_request,
                                       LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_BODY.value)
        self.validate_response_header_and_value(self.send_post_request, "Server", 'nginx')
        self.validate_response_headers_and_values(self.send_post_request,
                                                  LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_BODY.value,
                                                  "Skip_check_ON", "Date")
        self.validate_response_header(self.send_post_request, "Date")
        self.validate_response_header_partial_match(self.send_post_request, 'Date',
                                                    formatted_datetime_only_date)

    def can_login_user_with_incorrect_login(self, *args, **kwargs):
        self.print_method_name()
        self.validate_response_code(self.send_post_request, 400)
        self.validate_response_time(self.send_post_request, 6000)
        self.validate_response_size(self.send_post_request, 27)
        self.response_to_be_error(self.send_post_request, "error")
        self.validate_response_have_body(self.send_post_request)
        self.validate_response_to_be_json(self.send_post_request)
        self.validate_response_json_body_format(self.send_post_request, dict)
        self.validate_response_text(self.send_post_request, 'User not found.')
        self.validate_response_json_body_key_format(self.send_post_request, 'error', str)
        self.validate_response_headers(self.send_post_request,
                                       LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_BODY.value)
        self.validate_response_header_and_value(self.send_post_request, "Server", 'nginx')
        self.validate_response_headers_and_values(self.send_post_request,
                                                  LoginPageCorrectData.HEADER_BAD_RESPONSE_INCORRECT_BODY.value,
                                                  "Skip_check_ON", "Date")
        self.validate_response_header(self.send_post_request, "Date")
        self.validate_response_header_partial_match(self.send_post_request, 'Date',
                                                    formatted_datetime_only_date)

    def add_incorrect_data_in_find_contactors_base(self, get_db_session, get_add_method, *args):
        self.print_method_name()
        for arg in args:
            self.add_new_bad_data_in_db(get_db_session, tables.FindContactors, arg, get_add_method)
            get_db_session.close()

    def update_incorrect_data_in_find_contactors_base(self, get_db_session, get_update_method, *args, **kwargs):
        self.print_method_name()
        for arg in args:
            self.update_bad_data_in_db(get_db_session, tables.FindContactors, kwargs["attribute"], kwargs["value"],
                                       arg, get_update_method)
            get_db_session.close()
