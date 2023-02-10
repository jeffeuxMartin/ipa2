import unittest

from ipa2 import IPA2


class Test(unittest.TestCase):
    def test_IPA(self):
        ipa = IPA2('yue')
        self.assertEqual(
            ipa.convert_sent("你好")
            ['lei˩˧hou˧˥', 'nei˩˧hou˧˥'])

    def test_IPA_sentence(self):
        ipa = IPA2('yue')
        self.assertEqual(
            len(ipa.convert_sent(
                "今天天氣不錯")), 6)

    def test_pip(self):
        ipa = IPA2('yue')
        self.assertEqual(
            ipa.convert_sent("你好")
            ['lei˩˧hou˧˥', 'nei˩˧hou˧˥'])

    def test_IPA_NotFound(self):
        ipa = IPA2('yue')
        self.assertEqual(
            ipa.convert_sent("hello"), [''])
