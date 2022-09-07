from email.policy import default


def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux")