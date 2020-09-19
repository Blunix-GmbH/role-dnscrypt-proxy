import os
import dns.resolver
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dns(host):
    my_resolver = dns.resolver.Resolver()
    my_resolver.nameservers = ['127.0.0.1']
    answer = my_resolver.resolve('gateway')
    assert answer[0] == '172.16.0.5'
