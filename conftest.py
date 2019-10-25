from collections import namedtuple
import json

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Pass environment: local or dev or int"
    )


@pytest.fixture(scope='session')
def env(request):
    yield request.config.getoption("--env")


@pytest.fixture(scope='session')
def config(env):
    assert env in ['dev', 'local']
    yield json.load(open('env/{}.json'.format(env)))
    # TODO: add clean up code below


