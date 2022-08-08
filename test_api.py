import requests


def test_get_vshkodin():
  response=requests.get('https://vshkodin.com/')
  assert 200 == response.status_code
