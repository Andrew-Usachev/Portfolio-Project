'''
THIS FILE CONTAINS THE FIXTURES FOR ALL THE TESTS
'''

import pytest
from Portfolio_API.srs.db import Session


@pytest.fixture(scope="module")
def test_data(request):
    data = request.param
    return data


@pytest.fixture(scope="module")
def test_url(request):
    url = request.param
    return url


@pytest.fixture(scope="module")
def test_headers(request):
    headers = request.param
    return headers


@pytest.fixture
def get_db_session():
    """
    Creating of database session and return it into our autotest.
    """
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_data):
    """
    Example of function for delete test data from database.
    """
    session.query(table).filter(filter_data).delete()
    session.commit()


def add_method(session, item):
    """
    Example of function for add test data from database.
    """
    session.add(item)
    session.commit()


def update_method(session, item):
    """
    Example of function for update test data from database.
    """
    session.merge(item)
    session.commit()


@pytest.fixture
def get_add_method():
    """
    Example of fixture, that returns add method as object into our tests.
    """
    return add_method


@pytest.fixture
def get_update_method():
    """
    Example of fixture, that returns update method as object into our tests.
    """
    return update_method


@pytest.fixture
def get_delete_method():
    """
    Example of fixture, that returns delete method as object into our tests.
    """
    return delete_test_data
