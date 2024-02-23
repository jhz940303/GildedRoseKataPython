# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_aged_brie_increases_in_quality(self):
        brie_name = "Aged Brie"
        items = [Item(brie_name, 2, 0), Item(brie_name, 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        expected_items = [Item(brie_name, 1, 1), Item(brie_name, -1, 12)]
        for item, expected in zip(gr.items, expected_items):
            with self.subTest(item=item):
                self.assertEqual(item.name, expected.name)
                self.assertEqual(item.sell_in, expected.sell_in)
                self.assertEqual(item.quality, expected.quality)

    def test_backstage_passes_quality_changes(self):
        pass_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(pass_name, 11, 20), Item(pass_name, 10, 20), Item(pass_name, 5, 20), Item(pass_name, 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        expected_items = [
            Item(pass_name, 10, 21),
            Item(pass_name, 9, 22),
            Item(pass_name, 4, 23),
            Item(pass_name, -1, 0)
        ]
        for item, expected in zip(gr.items, expected_items):
            self.assertEqual(item.name, expected.name)
            self.assertEqual(item.sell_in, expected.sell_in)
            self.assertEqual(item.quality, expected.quality)

    def test_sulfuras_never_degrades(self):
        sulfuras_name = "Sulfuras, Hand of Ragnaros"
        initial_quality = 80
        items = [Item(sulfuras_name, 0, initial_quality), Item(sulfuras_name, -1, initial_quality)]
        gr = GildedRose(items)
        gr.update_quality()
        for item in gr.items:
            self.assertEqual(item.quality, initial_quality, f"{sulfuras_name} quality should remain constant.")
            self.assertIn(item.sell_in, [0, -1], f"{sulfuras_name} sell_in should not change.")


if __name__ == '__main__':
    unittest.main()
