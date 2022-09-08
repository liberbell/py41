import pytest

@pytest.fixture()
def csv_file():
    with open("test.csv", "w+") as c:
        yield c
    # yield "csv_file!!!"

def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")