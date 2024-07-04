# -*- coding: utf-8 -*-
import random
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='items.log', encoding='utf-8', level=logging.DEBUG)


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

            item.quality = min(50, max(item.quality, 0))

            if item.sell_in > 0:
                item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class SulfurasItem(Item):
    def __init__(self, name, sell_in, quality):
        super(SulfurasItem, self).__init__("Sulfuras, The Hand of Ragnaros", sell_in, 80)


class AgedBrieItem(Item):
    def __init__(self, name, sell_in, quality):
        super(AgedBrieItem, self).__init__("Aged Brie", sell_in, quality)


class BackstageItem(Item):
    def __init__(self, name, sell_in, quality):
        super(BackstageItem, self).__init__("Backstage passes " + name, sell_in, quality)


class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super(ConjuredItem, self).__init__("Conjured " + name, sell_in, quality)


def random_item_factory(type=0, name="Test", n=10, test_start=0,
                        q_begin=0, q_end=100, s_begin=0, s_end=100):
    items = {
        0: Item,
        1: SulfurasItem,
        2: AgedBrieItem,
        3: BackstageItem,
        4: ConjuredItem
    }

    return [items[type](name + str(i + test_start),
                        random.randint(s_begin, s_end),
                        random.randint(q_begin, q_end))
            for i in range(n)]


def log_items(items, num_tests):

    logger.info("generated %d items\n", len(items))
    for test_no, item in enumerate(items):
        if test_no % num_tests == 0:
            logger.info("\n")
        logger.info("%s", str(item))


if __name__ == '__main__':
    items = []
    num_tests = 10
    for type in range(5):
        items += random_item_factory(type=type, test_start=type * 10, n=num_tests)

    log_items(items, num_tests)

    GildedRose(items).update_quality()

    logger.info("\nGildedRose done\n")

    log_items(items, num_tests)






