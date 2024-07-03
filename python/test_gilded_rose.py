# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from python import gilded_rose


class GildedRoseTest(unittest.TestCase):

    def test_normal_item(self):

        items = [Item("no-quality", 0, 0),
                 Item("quality-no-sellin", 0, 2),
                 Item("quality-sellin", 1, 2),
                 Item("sellin-no-quality", 10, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        # normal quality check
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[1].quality)
        self.assertEqual(1, gilded_rose.items[2].quality)
        self.assertEqual(0, gilded_rose.items[3].quality)

        # normal sellin check
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[1].sell_in)
        self.assertEqual(0, gilded_rose.items[2].sell_in)
        self.assertEqual(9, gilded_rose.items[3].sell_in)

    def test_brie(self):
        items = [Item("Aged Brie", 2, 0),
                 Item("Aged Brie", 0, 2),
                 Item("Aged Brie", 1, 50),
                 ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[0].sell_in)

        self.assertEqual(3, gilded_rose.items[1].quality)
        self.assertEqual(0, gilded_rose.items[1].sell_in)

        self.assertEqual(50, gilded_rose.items[2].quality)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80),
                 Item("Sulfuras, Hand of Ragnaros", 0, 80)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(80, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[0].sell_in)

        self.assertEqual(80, gilded_rose.items[1].quality)
        self.assertEqual(0, gilded_rose.items[1].sell_in)

    def test_backstage(self):
        items = [Item("Backstage passes to TAFKAL80 concerts", 20, 0),
                 Item("Backstage passes to a TAFKA", 10, 0),
                 Item("Backstage passes abcd", 6, 0),
                 Item("Backstage passes", 5, 0),
                 Item("Backstage passes", 0, 0),
                 Item("Backstage passes", 0, 10)
                 ]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(19, gilded_rose.items[0].sell_in)

        self.assertEqual(2, gilded_rose.items[1].quality)
        self.assertEqual(9, gilded_rose.items[1].sell_in)

        self.assertEqual(2, gilded_rose.items[2].quality)
        self.assertEqual(5, gilded_rose.items[2].sell_in)

        self.assertEqual(3, gilded_rose.items[3].quality)
        self.assertEqual(4, gilded_rose.items[3].sell_in)

        self.assertEqual(0, gilded_rose.items[4].quality)
        self.assertEqual(0, gilded_rose.items[4].sell_in)

        self.assertEqual(0, gilded_rose.items[5].quality)
        self.assertEqual(0, gilded_rose.items[5].sell_in)

    def test_conjured(self):
        items = [Item("Conjured no-qual",0, 0),
                 Item("Conjured sellin", 2, 0),
                 Item("Conjured qual-normal", 3, 6),
                 Item("Conjured qual-double", 0, 6),]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[0].sell_in)

        self.assertEqual(0, gilded_rose.items[1].quality)
        self.assertEqual(1, gilded_rose.items[1].sell_in)

        self.assertEqual(4, gilded_rose.items[2].quality)
        self.assertEqual(2, gilded_rose.items[2].sell_in)

        self.assertEqual(2, gilded_rose.items[3].quality)
        self.assertEqual(0, gilded_rose.items[3].sell_in)
        
if __name__ == '__main__':
    unittest.main()
