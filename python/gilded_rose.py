# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            decrease_qual = 1

            if item.name == 'Sulfuras, Hand of Ragnaros':
                if item.sell_in > 0:
                    item.sell_in -= 1
                continue

            if item.name == 'Aged Brie':
                decrease_qual = -1
            elif item.name.startswith("Backstage passes"):
                if item.sell_in == 0:
                    decrease_qual = item.quality
                elif item.sell_in <= 5:
                    decrease_qual = -3
                elif item.sell_in <= 10:
                    decrease_qual = -2
                else:
                    decrease_qual = -1
            elif item.name.startswith("Conjured"):
                decrease_qual = 2

            if decrease_qual > 0 and item.sell_in == 0:
                    decrease_qual *= 2

            if item.quality > 0:
                item.quality = max(0, item.quality - decrease_qual)

            if item.quality > 50:
                item.quality = 50

            if item.sell_in > 0:
                item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
