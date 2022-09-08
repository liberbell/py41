import pytest

@pytest.fixture()
def csv_file():
    yield "csv_file!!!"

def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")