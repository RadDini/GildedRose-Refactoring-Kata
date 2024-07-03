# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == 'Sulfuras, Hand of Ragnaros':
                if item.sell_in > 0:
                    item.sell_in -= 1
                continue

            if item.name == 'Aged Brie':
                item.quality += 1
            elif item.name.startswith("Backstage passes"):
                if item.sell_in == 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in <= 10:
                    item.quality += 2
                else:
                    item.quality += 1
            else:
                # normal item
                if item.quality > 0:
                    item.quality -= 1
                    if item.sell_in == 0:
                        item.quality -= 1


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
