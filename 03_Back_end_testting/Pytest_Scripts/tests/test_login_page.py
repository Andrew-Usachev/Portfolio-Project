'''
This file contains tests for login page. Before you run tests you need to create correct data in database.
You can take SQL scripts from sql folder.
'''

import pytest
from Portfolio_API.pages.login_page import LoginPage
from Portfolio_API.srs.enums import *


class TestPositive:

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    LoginPageCorrectData.HEADER.value,
                    LoginPageCorrectData.BODY.value
            )
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_correct_data(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_correct_data()
        page.check_login_user_response_with_login_user_schema()
        page.check_fail_status()

    def test_check_data_in_find_contactors_base_using(self, get_db_session):
        page = LoginPage()
        page.check_data_in_find_contactors_base(get_db_session)
        page.check_fail_status()

    def test_add_data_in_find_contactors_base_using(self, get_db_session, get_add_method):
        page = LoginPage()
        page.add_data_in_find_contactors_base(get_db_session, get_add_method)
        page.check_fail_status()

    def test_update_data_in_find_contactors_base_using(self, get_db_session, get_update_method):
        page = LoginPage()
        page.update_data_in_find_contactors_base(get_db_session, get_update_method)
        page.check_fail_status()


class TestNegative:
    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    url_enum,
                    LoginPageCorrectData.HEADER.value,
                    LoginPageCorrectData.BODY.value
            )
            for url_enum in LoginPageIncorrectData.negative_url()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_incorrect_url(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_url()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    LoginPageIncorrectData.negative_header(),
                    LoginPageCorrectData.BODY.value
            )
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_incorrect_header(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_header()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    LoginPageCorrectData.HEADER.value,
                    LoginPageIncorrectData.negative_body()[0],
            )
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_incorrect_body_password(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_password()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    LoginPageCorrectData.HEADER.value,
                    LoginPageIncorrectData.negative_body()[1],
            )
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_incorrect_body_login(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_login()
        page.check_fail_status()

    def test_add_negative_data_in_find_contactors_base_using(self, get_db_session, get_add_method):
        page = LoginPage()
        arg1 = FindContractorsBaseBuilder().set_contractor_id(None)
        arg2 = FindContractorsBaseBuilder().set_verified_companies("All verified companies")
        page.add_incorrect_data_in_find_contactors_base(get_db_session, get_add_method, arg1, arg2)
        page.check_fail_status()

    def test_update_negative_data_in_find_contactors_base_using(self, get_db_session, get_update_method):
        page = LoginPage()
        arg1 = FindContractorsBaseBuilder().set_contractor_id(None)
        arg2 = FindContractorsBaseBuilder().set_verified_companies("All verified companies")
        page.update_incorrect_data_in_find_contactors_base(get_db_session, get_update_method, arg1, arg2,
                                                           attribute="Id_Contractors",
                                                           value=1003)
        page.check_fail_status()


class TestAdHoc:
    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    url_enum,
                    LoginPageCorrectData.HEADER.value,
                    LoginPageCorrectData.BODY.value
            )
            for url_enum in LoginPageIncorrectData.adhoc_url()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_adhoc_url(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_url()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    enum_header,
                    LoginPageCorrectData.BODY.value
            )
            for enum_header in LoginPageIncorrectData.adhoc_header()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_adhoc_header(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_header()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    LoginPageCorrectData.HEADER.value,
                    enum_body,
            )
            for enum_body in LoginPageIncorrectData.adhoc_body()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_adhoc_body_login(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_login()
        page.check_fail_status()

    def test_add_adhoc_data_in_find_contactors_base_using(self, get_db_session, get_add_method):
        page = LoginPage()
        arg1 = FindContractorsBaseBuilder().set_contractor_id("!@#$%%^&")
        arg2 = FindContractorsBaseBuilder().set_verified_companies(".")
        page.add_incorrect_data_in_find_contactors_base(get_db_session, get_add_method, arg1, arg2)
        page.check_fail_status()

    def test_update_adhoc_data_in_find_contactors_base_using(self, get_db_session, get_update_method):
        page = LoginPage()
        arg1 = FindContractorsBaseBuilder().set_contractor_id("!@#$%%^&")
        arg2 = FindContractorsBaseBuilder().set_verified_companies(".")
        page.update_incorrect_data_in_find_contactors_base(get_db_session, get_update_method, arg1, arg2,
                                                           attribute="Id_Contractors",
                                                           value=1003)
        page.check_fail_status()


class TestBoundary:
    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    url_enum,
                    LoginPageCorrectData.HEADER.value,
                    LoginPageCorrectData.BODY.value
            )
            for url_enum in LoginPageIncorrectData.boundary_url()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_boundary_url(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_url()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    enum_header,
                    LoginPageCorrectData.BODY.value
            )
            for enum_header in LoginPageIncorrectData.boundary_header()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_boundary_header(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_header()
        page.check_fail_status()

    @pytest.mark.parametrize(
        "test_url, test_headers, test_data",
        [
            (
                    LoginPageCorrectData.URL.value,
                    LoginPageCorrectData.HEADER.value,
                    enum_body,
            )
            for enum_body in LoginPageIncorrectData.boundary_body()
        ],
        indirect=["test_url", "test_headers", "test_data"],
    )
    def test_login_user_with_boundary_body_login(self, test_url, test_headers, test_data):
        page = LoginPage(test_url, test_headers, test_data)
        page.can_login_user_with_incorrect_login()
        page.check_fail_status()

    def test_add_boundary_data_in_find_contactors_base_using(self, get_db_session, get_add_method):
        page = LoginPage()
        arg1 = FindContractorsBaseBuilder().set_contractor_id(-1)
        arg2 = FindContractorsBaseBuilder().set_contractor_id(0)
        arg3 = FindContractorsBaseBuilder().set_contractor_id(10001)
        arg4 = FindContractorsBaseBuilder().set_verified_companies("All companie")
        arg5 = FindContractorsBaseBuilder().set_verified_companies("All companiess")
        page.add_incorrect_data_in_find_contactors_base(get_db_session, get_add_method, arg1, arg2, arg3, arg4, arg5)
        page.check_fail_status()

    def test_update_boundary_data_in_find_contactors_base_using(self, get_db_session, get_update_method):
        page = LoginPage()
        arg1 = FindContractorsBaseBuilder().set_contractor_id(-1)
        arg2 = FindContractorsBaseBuilder().set_contractor_id(0)
        arg3 = FindContractorsBaseBuilder().set_contractor_id(10001)
        arg4 = FindContractorsBaseBuilder().set_verified_companies("All companie")
        arg5 = FindContractorsBaseBuilder().set_verified_companies("All companiess")
        page.update_incorrect_data_in_find_contactors_base(get_db_session, get_update_method, arg1, arg2, arg3, arg4,
                                                           arg5,
                                                           attribute="Id_Contractors",
                                                           value=1003)
        page.check_fail_status()
