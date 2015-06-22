#!/usr/bin/env python

import unittest
from peeringdb.PeeringDB import PeeringDB


class TestASN(unittest.TestCase):

    PDB = None

    def setUp(self):
        self.PDB = PeeringDB(cache=False)

    # Real networks that exist and have PeeringDB entries

    def test_exists_768(self):
        # JANET UK
        asn = self.PDB.asn(2906)
        self.assertIsNotNone(asn)

    def test_exists_2906(self):
        # Netflix
        asn = self.PDB.asn(2906)
        self.assertIsNotNone(asn)

    # Reserved, private or documentation ASNs

    def test_shouldnt_exist_0(self):
        asn = self.PDB.asn(0)
        self.assertIsNone(asn)

    def test_shouldnt_exist_64496(self):
        asn = self.PDB.asn(64496)
        self.assertIsNone(asn)

if __name__ == '__main__':
    unittest.main()
