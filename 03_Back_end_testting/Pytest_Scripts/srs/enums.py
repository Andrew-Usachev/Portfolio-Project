'''
This file contains all the constants used in the API.
'''

from enum import Enum
import datetime
from Portfolio_API.srs.builders import *
from faker import Faker
import json
import requests

password = 'Password1234'

current_datetime = datetime.datetime.now()
time_difference = datetime.timedelta(hours=2, minutes=59, seconds=55)
current_datetime_corrected = current_datetime - time_difference
formatted_datetime = current_datetime_corrected.strftime("%a, %d %b %Y %H:%M:%S GMT")
formatted_datetime_only_date = current_datetime_corrected.strftime(
    "%a, %d %b %Y"
)

CONNECTION_ROW = "mysql+pymysql://root:root@localhost:3306/ibench_net_db"

REGISTER_BODY = LoginBodyBuilder().with_email(Faker().email()).with_password(password).with_country(
    'Canada').with_terms_accepted(1).with_type(2).with_company_name(Faker().company()).build()

response = requests.post("https://ibench.net/api/auth/register", REGISTER_BODY)
response_json = json.loads(response.content)
get_email = response_json['user']['email']


class LoginPageCorrectData(Enum):
    URL = LoginUrlBuilder().with_url("https://ibench.net/api/auth/login").build()

    HEADER = (LoginHeaderBuilder()
              .with_sec_ch_ua('"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"')
              .with_sec_ch_ua_platform('"Windows"')
              .with_sec_ch_ua_mobile('?0')
              .with_user_agent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
              .with_content_type('application/x-www-form-urlencoded')
              .with_accept('*/*')
              .with_sec_fetch_site('same-origin')
              .with_sec_fetch_mode('cors')
              .with_sec_fetch_dest('empty')
              .with_host('ibench.net').build())

    BODY = LoginBodyBuilder().with_email(get_email).with_password(
        password).build()

    HEADER_RESPONSE = (LoginHeaderResponseBuilder()
                       .with_server("nginx")
                       .with_date(formatted_datetime)
                       .with_content_type("application/json; charset=utf-8")
                       .with_transfer_encoding("chunked")
                       .with_connection("keep-alive")
                       .with_access_control_allow_origin("*")
                       .with_vary("Accept-Encoding")
                       .with_content_encoding("gzip")
                       .with_x_frame_options("SAMEORIGIN").build())

    HEADER_BAD_RESPONSE_INCORRECT_URL = (LoginHeaderResponseBuilder()
                                         .with_server("nginx")
                                         .with_date(formatted_datetime)
                                         .with_content_type("text/html; charset=utf-8")
                                         .with_transfer_encoding("chunked")
                                         .with_connection("keep-alive")
                                         .with_vary("Accept-Encoding")
                                         .with_content_encoding("gzip").build())

    HEADER_BAD_RESPONSE_INCORRECT_HEADER = (LoginHeaderResponseBuilder()
                                            .with_server("nginx")
                                            .with_date(formatted_datetime)
                                            .with_content_type("application/json; charset=utf-8")
                                            .with_transfer_encoding("chunked")
                                            .with_connection("keep-alive")
                                            .with_access_control_allow_origin("*")
                                            .with_vary("Accept-Encoding").build())

    HEADER_BAD_RESPONSE_INCORRECT_BODY = (LoginHeaderResponseBuilder()
                                          .with_server("nginx")
                                          .with_date(formatted_datetime)
                                          .with_content_type("application/json; charset=utf-8")
                                          .with_transfer_encoding("chunked")
                                          .with_connection("keep-alive")
                                          .with_access_control_allow_origin("*")
                                          .with_vary("Accept-Encoding").build())


class LoginPageIncorrectData(Enum):
    @staticmethod
    def negative_url():
        url = [LoginUrlBuilder().with_url("http://ibench.net/api/auth/login").build(),
               LoginUrlBuilder().with_url("https://ibench.net/api/auth/logis").build()]

        return url

    @staticmethod
    def adhoc_url():
        url = [LoginUrlBuilder().with_url("https://ibench.net/api/!@#$%").build(),
               LoginUrlBuilder().with_url("https://ibench.net/api/auth/+-").build(), ]

        return url

    @staticmethod
    def boundary_url():
        url = [LoginUrlBuilder().with_url("https://ibench.net/api/auth/logi").build(),
               LoginUrlBuilder().with_url("https://ibench.net/api/auth/loginn").build()]

        return url

    @staticmethod
    def negative_header():
        header = (LoginHeaderBuilder()
                  .with_content_type('applicationx-www-form-urlencoded')
                  .with_host('ibenchnet').build())

        return header

    @staticmethod
    def adhoc_header():
        header = [LoginHeaderBuilder()
                  .with_content_type('@')
                  .with_host('@').build(),
                  LoginHeaderBuilder()
                  .with_content_type('!')
                  .with_host('!').build()]

        return header

    @staticmethod
    def boundary_header():
        header = [LoginHeaderBuilder()
                  .with_content_type('applicationx-www-form-urlencode')
                  .with_host('ibench.ne').build(),
                  LoginHeaderBuilder()
                  .with_content_type('applicationx-www-form-urlencodedd')
                  .with_host('ibench.nett').build()]

        return header

    @staticmethod
    def negative_body():
        body = [
            LoginBodyBuilder().with_email(get_email).with_password('Password123').build(),
            LoginBodyBuilder().with_email('A.Crock@atlant.com').with_password(password).build()
        ]
        return body

    @staticmethod
    def adhoc_body():
        body = [
            LoginBodyBuilder().with_email('.').with_password('.').build(),
            LoginBodyBuilder().with_email('!"№;%:?*()_+').with_password('!"№;%:?*()_+').build()
        ]
        return body

    @staticmethod
    def boundary_body():
        body = [
            LoginBodyBuilder().with_email('A.Crock@atlant.comm').with_password('Password12344').build(),
            LoginBodyBuilder().with_email('A.Crock@atlant.co').with_password('Password123').build()
        ]
        return body
