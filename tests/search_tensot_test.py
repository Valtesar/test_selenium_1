import json
import pytest


@pytest.fixture(scope='session')
def config():
    with open("tests/config.json") as config_file:
        data = json.load(config_file)
        return data
