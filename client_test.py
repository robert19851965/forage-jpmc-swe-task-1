import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  
  # Test getDataPoint

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceAskVerySmall(self):
      quotes = [
        {'top_ask': {'price': 19.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 12.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      """ ------------ Add the assertion below ------------ """
      for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceAskVeryLarge(self):
      quotes = [
        {'top_ask': {'price': 780.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 1001.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      """ ------------ Add the assertion below ------------ """
      for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidVerySmall(self):
      quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 3.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 11.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      """ ------------ Add the assertion below ------------ """
      for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidVeryLarge(self):
      quotes = [
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1200.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 560.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      """ ------------ Add the assertion below ------------ """
      for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  # Test getRatio

  def test_getRatio_AGreaterThanB(self):
     prices = [
        {'price_a': 120.78, 'price_b': 118.06},
        {'price_a': 131.08, 'price_b': 116.93}
     ]
     for price in prices:
        self.assertEqual(getRatio(price['price_a'], price['price_b']), price['price_a']/price['price_b'])

  def test_getRatio_BGreaterThanA(self):
     prices = [
        {'price_a': 117.28, 'price_b': 128.06},
        {'price_a': 127.08, 'price_b': 127.93}
     ]
     for price in prices:
        self.assertEqual(getRatio(price['price_a'], price['price_b']), price['price_a']/price['price_b'])

  def test_getRatio_BEqualZero(self):
     prices = [
        {'price_a': 120.78, 'price_b': 0},
        {'price_a': 131.08, 'price_b': 0}
     ]
     for price in prices:
        self.assertEqual(getRatio(price['price_a'], price['price_b']), None)

  def test_getRatio_AEqualZero(self):
     prices = [
        {'price_a': 0, 'price_b': 118.06},
        {'price_a': 0, 'price_b': 126.93}
     ]
     for price in prices:
        self.assertEqual(getRatio(price['price_a'], price['price_b']), 0)

  def test_getRatio_AEqualB(self):
     prices = [
        {'price_a': 120.78, 'price_b': 120.78},
        {'price_a': 116.93, 'price_b': 116.93}
     ]
     for price in prices:
        self.assertEqual(getRatio(price['price_a'], price['price_b']), 1)



if __name__ == '__main__':
    unittest.main()
