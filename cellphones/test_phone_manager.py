import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [testPhone1, testPhone2]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass



    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(2, 'Ryan')

        testEmps = [testEmp1, testEmp2]
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmp1)
        testAssignmentMgr.add_employee(testEmp2)
        self.assertCountEqual(testEmps, testAssignmentMgr.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(1, 'Ryan')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(testEmp1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(testEmp2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(2, 'Ryan')
        testEmp3 = Employee(3, 'Harry')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.add_employee(testEmp1)
        testAssignmentMgr.add_employee(testEmp2)
        testAssignmentMgr.add_employee(testEmp3)

        testAssignmentMgr.assign(testPhone1.id, testEmp1)
        self.assertEqual(testPhone1.employee_id, testEmp1.id)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(2, 'Ryan')
        testEmp3 = Employee(3, 'Harry')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmp1)
        testAssignmentMgr.add_employee(testEmp2)
        testAssignmentMgr.add_employee(testEmp3)

        testAssignmentMgr.assign(testPhone1.id, testEmp1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, testEmp2)

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(2, 'Ryan')
        testEmp3 = Employee(3, 'Harry')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmp1)
        testAssignmentMgr.add_employee(testEmp2)
        testAssignmentMgr.add_employee(testEmp3)

        testAssignmentMgr.assign(testPhone1.id, testEmp1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone2.id, testEmp1)

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(2, 'Ryan')
        testEmp3 = Employee(3, 'Harry')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmp1)
        testAssignmentMgr.add_employee(testEmp2)
        testAssignmentMgr.add_employee(testEmp3)

        testAssignmentMgr.assign(testPhone1.id, testEmp1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testPhone1.id, testEmp1)


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testEmp1 = Employee(1, 'Emily')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_employee(testEmp1)

        testAssignmentMgr.assign(1, testEmp1)
        testAssignmentMgr.un_assign(1)
        self.assertFalse(testAssignmentMgr.phones[0].is_assigned())


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testEmp1 = Employee(1, 'Emily')
        testEmp2 = Employee(2, 'Ryan')
        testEmp3 = Employee(3, 'Harry')

        testAssignmentMgr = PhoneAssignments()

        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        testAssignmentMgr.add_employee(testEmp1)
        testAssignmentMgr.add_employee(testEmp2)
        testAssignmentMgr.add_employee(testEmp3)

        testAssignmentMgr.assign(testPhone1.id, testEmp1)
        testAssignmentMgr.assign(testPhone2.id, testEmp2)

        self.assertEqual(testAssignmentMgr.phone_info(testEmp1), testPhone1)
        self.assertEqual(testAssignmentMgr.phone_info(testEmp2), testPhone2)
        self.assertIsNone(testAssignmentMgr.phone_info(testEmp3))
        with self.assertRaises(PhoneError):
            testAssignmentMgr.assign(testAssignmentMgr.phone_info(None))
