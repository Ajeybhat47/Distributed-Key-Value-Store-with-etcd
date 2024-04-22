import unittest
from unittest.mock import MagicMock

from etcd import *

class TestEtcdFunctions(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock()

    def test_connectToServer(self):
        hosts = (('localhost',22379),)
        client = connect_to_etcd(hosts)
        self.assertIsNotNone(client)

    def test_insertKeyValue(self):
        key = "cc_project"
        value = "ETCD"
        insert_etcd_key_value(self.client, key, value)
        self.client.set.assert_called_once_with(key, value)

    def test_getKeyValue(self):
        key = "cc_project"
        self.client.get.return_value = MagicMock(value="ETCD")
        value = get_etcd_key_value(self.client, key)
        print(value)
        self.assertEqual(value, "ETCD")

    def test_getKeyValue_not_found(self):
        key = "PESUUUUU"
        self.client.get.return_value = None
        value = get_etcd_key_value(self.client, key)
        self.assertIsNone(value)

    def test_deleteKeyValue(self):
        key = "cc_project"
        delete_etcd_key(self.client, key)
        self.client.delete.assert_called_once_with(key)

    def test_listAllKeys(self):
        self.client.get.return_value = MagicMock(leaves=[MagicMock(key="/cc_project")])
        keys = get_all_etcd_keys(self.client)
        print(keys)
        self.assertEqual(keys, ["/cc_project"])

if __name__ == "__main__":
    unittest.main()