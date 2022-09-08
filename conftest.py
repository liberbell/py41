import pytest

@pytest.fixture()
def csv_file():
    with open("test.csv", "w+") as c:
        print("before test")
        yield c
        print("after test")
    # yield "csv_file!!!"

def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")