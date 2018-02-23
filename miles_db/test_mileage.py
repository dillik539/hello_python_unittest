
import mileage
import sqlite3
from unittest import TestCase

class TestMileageDB(TestCase):

    test_db_url = 'test_miles.db'

    # The name of this method is important - the test runner will look for it
    def setUp(self):
        # Overwrite the mileage
        mileage.db_url = self.test_db_url
        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')
        conn.commit()
        conn.close()


    def test_add_new_vehicle(self):
        mileage.add_miles('Blue Car', 100)
        expected = { 'Blue Car': 100 }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Green Car', 50)
        expected['Green Car'] = 50
        self.compare_db_to_expected(expected)


    def test_increase_miles_for_vehicle(self):
        mileage.add_miles('Red Car', 100)
        expected = { 'Red Car': 100 }
        self.compare_db_to_expected(expected)

        mileage.add_miles('Red Car', 50)
        expected['Red Car'] = 100 + 50
        self.compare_db_to_expected(expected)


    def test_add_new_vehicle_no_vehicle(self):
        with self.assertRaises(Exception):
            mileage.addMiles(None, 100)


    def test_add_new_vehicle_invalid_new_miles(self):
        with self.assertRaises(Exception):
            mileage.addMiles('Car', -100)
        with self.assertRaises(Exception):
            mileage.addMiles('Car', 'abc')
        with self.assertRaises(Exception):
            mileage.addMiles('Car', '12.def')

    def test_vehicle_name_uppercase(self):
        vehicle1 = mileage.change_to_uppercase('yellow car')
        mileage.add_miles(vehicle1, 100)
        vehicle2 = mileage.change_to_uppercase('Yellow car')
        mileage.add_miles(vehicle2, 100)
        vehicle3 = mileage.change_to_uppercase('yElLoW cAr')
        mileage.add_miles(vehicle3, 100)
        vehicle4 = mileage.change_to_uppercase('yELLOW CAR')
        mileage.add_miles(vehicle4, 200)
        expected = 'YELLOW CAR'
        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()
        for r in all_data:
            self.assertEqual(r[0], expected)

    # This is not a test method, instead, it's used by the test methods
    def compare_db_to_expected(self, expected):
        vehicle = mileage.change_to_uppercase('yellow car')
        conn = sqlite3.connect(self.test_db_url)
        cursor = conn.cursor()
        all_data = cursor.execute('SELECT * FROM MILES').fetchall()

        # Same rows in DB as entries in expected dictionary
        self.assertEqual(len(expected.keys()), len(all_data))

        for row in all_data:
            # Vehicle exists, and mileage is correct
            # self.assertEqual(row[0], expected.keys()[0])
            self.assertIn(row[0], expected.keys())
            self.assertEqual(expected[row[0]], row[1])

        conn.close()


class TestSearchVehicle(TestCase):
    test_db_url = 'test_miles.db'

    def setUp(self):
        mileage.db_url = self.test_db_url
        conn = sqlite3.connect(self.test_db_url)
        conn.execute('DELETE FROM miles')
        conn.commit()
        conn.close()

    def test_search_vehicle(self):
        vehicle = mileage.add_miles('BLUE CAR', 100)
        vehicle1 = mileage.add_miles('Green Car', 50)
        vehicle2 = mileage.add_miles('Yellow car', 40)
        search = mileage.search_vehicle('BLUE CAR')
        search1 = mileage.search_vehicle(mileage.change_to_uppercase('Blue car'))
        search2 = mileage.search_vehicle('Blue Car')
        self.assertIsNotNone(search)
        self.assertIsNotNone(search1)
        self.assertIsNone(search2)
