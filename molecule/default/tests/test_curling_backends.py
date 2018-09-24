import os

import testinfra.utils.ansible_runner
import requests

# curl https://www.example.com and https://www.beispiel.de | grep $host
# This tests if haproxy correctly proxies the nginx server on :8080

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_proxy_www_beispiel_de(host):
    r = requests.get('https://www.beispiel.de/', verify=False)
    assert r.content == 'www.beispiel.de'


def test_proxy_www_example_com(host):
    r = requests.get('https://www.example.com/', verify=False)
    assert r.content == 'www.example.com'
