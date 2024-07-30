# test_lambda_function.py
import sys
import os

# handler.pyのディレクトリをsys.pathに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from handler import lambda_handler


def test_even_number():
    event = {'number': 2}
    response = lambda_handler(event, None)
    assert response['message'] == 'Even'


def test_odd_number():
    event = {'number': 3}
    response = lambda_handler(event, None)
    assert response['message'] == 'Odd'


def test_no_number_provided():
    event = {}
    response = lambda_handler(event, None)
    assert response['message'] == 'No number provided' 