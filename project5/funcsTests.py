import unittest
from quakeFuncs import *

class TestCases(unittest.TestCase):

   def test_eq_(self):
      quake1 = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)
      quake2 = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)
      self.assertEqual(quake1, quake2)
          
   def test_earthquake_init(self):
      quake = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)
      self.assertEqual(quake.place, '12km SSW of Idyllwild, CA')
      self.assertAlmostEqual(quake.mag, 0.97)
      self.assertAlmostEqual(quake.longitude, -116.7551651)
      self.assertAlmostEqual(quake.latitude, 33.6391678)
      self.assertEqual(quake.time, 1488177290)  

   def test_earthquakes_equal_0(self):   
      quake1 = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)  
      quake2 = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)  
      self.assertEqual(quake1, quake2)

   def test_earthquakes_equal_1(self):   
      quake1 = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)  
      quake2 = Earthquake('13km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)  
      self.assertNotEqual(quake1, quake2)

   def test_read_file_0(self):
      quakes = []
      quake = Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290)
      quakes.append(Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290))
      quakes.append(Earthquake('5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002, 1488173538))
      # call read_file with 'test0.txt'
      earthquakes = read_quakes_from_file('test0.txt')
      #print()
      #print(earthquakes[0].mag, " ", earthquakes[0].place, " ", earthquakes[0].longitude, " ", earthquakes[0].latitude, " ", earthquakes[0].time)
      #print(quakes[0].mag, " ", quakes[0].place, " ", quakes[0].longitude, " ", quakes[0].latitude, " ", quakes[0].time)
      #print(earthquakes[1].mag, " ", earthquakes[1].place, " ", earthquakes[1].longitude, " ", earthquakes[1].latitude, " ", earthquakes[1].time)
      self.assertEqual(quake, quakes[0])
      self.assertEqual(earthquakes, quakes)

      
   def test_filter_by_mag_0(self):
      quakes = []
      quakes.append(Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290))
      quakes.append(Earthquake('5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002, 1488173538))
      quakes.append(Earthquake('100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548, 1488219604))
      filtered = []
      filtered.append(Earthquake('5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002, 1488173538))
      filtered.append(Earthquake('100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548, 1488219604))
      self.assertEqual(filter_by_mag(quakes, 1, 3), filtered)    
      
   def test_filter_by_place_0(self):
      quakes = []
      quakes.append(Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290))
      quakes.append(Earthquake('5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002, 1488173538))
      quakes.append(Earthquake('100km SE of King Salmon, Alaska', 1.9, -155.2835, 58.1548, 1488219604))
      filtered = []
      filtered.append(Earthquake('12km SSW of Idyllwild, CA', 0.97, -116.7551651, 33.6391678, 1488177290))
      filtered.append(Earthquake('5km S of Gilroy, California', 2.19, -121.5801697, 36.9580002, 1488173538))
      self.assertEqual(filter_by_place(quakes, "ca"), filtered)  
 
  # Use this test when ready to work on the json data. 
   def test_quake_from_feature(self):
      feature = {
            "geometry": {
                "coordinates": [
                    -117.4906667,
                    33.9131667,
                    0.25
                ],
                "type": "Point"
            },
            "id": "ci37814000",
            "properties": {
                "code": "37814000",
                "detail": "http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37814000.geojson",
                "dmin": 0.2836,
                "gap": 87,
                "ids": ",ci37814000,",
                "mag": 1.24,
                "magType": "ml",
                "net": "ci",
                "nst": 8,
                "place": "5km NE of Home Gardens, CA",
                "rms": 0.27,
                "sig": 24,
                "sources": ",ci,",
                "status": "automatic",
                "time": 1488179250520,
                "title": "M 1.2 - 5km NE of Home Gardens, CA",
                "tsunami": 0,
                "type": "earthquake",
                "types": ",geoserve,nearby-cities,origin,phase-data,scitech-link,",
                "tz": -480,
                "updated": 1488179487273,
                "url": "http://earthquake.usgs.gov/earthquakes/eventpage/ci37814000"
            },
            "type": "Feature"
        }
      quake1 = quake_from_feature(feature)
      #print(quake1.mag, " ", quake1.place, " ", quake1.longitude, " " , quake1.latitude, " ", quake1.time)
      quake2 = Earthquake("5km NE of Home Gardens, CA", 1.24, -117.4906667, 33.9131667, 1488179250)
      self.assertEqual(quake1, quake2)

      
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

