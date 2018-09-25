import os

import testinfra.utils.ansible_runner
import requests

# curl https://www.example.com and https://www.beispiel.de | grep $host
# This tests if haproxy correctly proxies the nginx server on :8080

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_proxy_www_beispiel_de(host):
    headers = {'Host': 'www.beispiel.de'}
    r = requests.get('https://127.0.0.1/', verify=False, headers=headers)
    assert 'www.beispiel.de' in r.content


def test_proxy_www_example_com(host):
    headers = {'Host': 'www.example.com'}
    r = requests.get('https://127.0.0.1/', verify=False, headers=headers)
    assert 'www.example.com' in r.content
