import pytest

# @pytest.mark.parametrize('a,b,sum', [
#     (1,2,3),
#     pytest.param(2,3,5, id='My super duper test 1', marks=[pytest.mark.testrail(ids=('C5678',))]),
#     pytest.param(4,5,9, id='My super duper test 2', marks=[pytest.mark.testrail(ids=('C1234',))])
# ])
# def test_params(a,b,sum):
#     assert a+b == sum


def test_config(env, config):
    assert config['database']['hostname'] == f'mysql.db.{env}'
