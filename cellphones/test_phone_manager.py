import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError


class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        test_phone1 = Phone(1, 'Apple', 'iPhone 6')
        test_phone2 = Phone(2, 'Apple', 'iPhone 5')

        test_phones = [test_phone1, test_phone2]

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)
        test_assignment_mgr.add_phone(test_phone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(test_phones, test_assignment_mgr.phones)

    def test_create_and_add_phone_with_duplicate_id(self):
        test_phone1 = Phone(1, 'Apple', 'iPhone 6')
        test_phone2 = Phone(1, 'Apple', 'iPhone 5')

        test_assignment_mgr = PhoneAssignments()
        test_assignment_mgr.add_phone(test_phone1)

        with self.assertRaises(PhoneError):
            test_assignment_mgr.add_phone(test_phone2)

    def test_create_and_add_new_employee(self):
        test_assignment_mgr = PhoneAssignments()

        test_employee1 = Employee(1, 'Kitty')
        test_employee2 = Employee(2, 'Puppy')

        test_assignment_mgr.add_employee(test_employee1)
        test_assignment_mgr.add_employee(test_employee2)

        self.assertTrue(test_employee1 in test_assignment_mgr.employees)
        self.assertTrue(test_employee2 in test_assignment_mgr.employees)

    def test_create_and_add_employee_with_duplicate_id(self):
        test_assignment_mgr = PhoneAssignments()

        test_employee1 = Employee(1, 'Kitty')
        test_employee2 = Employee(1, 'Puppy')

        test_assignment_mgr.add_employee(test_employee1)
        with self.assertRaises(PhoneError):
            test_assignment_mgr.add_employee(test_employee2)

    def test_assign_phone_to_employee(self):
        test_phone1 = Phone(1, "Samsung", "Galaxy S2")
        test_employee1 = Employee(1, "Kitty Cat")

        test_assignments_mgr = PhoneAssignments()
        test_assignments_mgr.add_phone(test_phone1)
        test_assignments_mgr.add_employee(test_employee1)
        test_assignments_mgr.assign(test_phone1.id, test_employee1)

        self.assertEqual(test_phone1.employee_id, test_employee1.id)

    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        test_phone1 = Phone(1, "Samsung", "Galaxy S2")
        test_employee1 = Employee(1, "Kitty Cat")
        test_employee2 = Employee(2, "Puppy Dog")

        test_assignments_mgr = PhoneAssignments()
        test_assignments_mgr.add_phone(test_phone1)
        test_assignments_mgr.add_employee(test_employee1)
        test_assignments_mgr.assign(test_phone1.id, test_employee1)

        with self.assertRaises(PhoneError):
            test_assignments_mgr.assign(test_phone1, test_employee2)

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        test_phone1 = Phone(1, "Samsung", "Galaxy S2")
        test_phone2 = Phone(2, "Bedrock", "Pterodactyl")
        test_employee1 = Employee(1, "Fred Flintstone")

        test_assignments_mgr = PhoneAssignments()
        test_assignments_mgr.add_phone(test_phone1)
        test_assignments_mgr.add_employee(test_employee1)
        test_assignments_mgr.assign(test_phone1.id, test_employee1)

        with self.assertRaises(PhoneError):
            test_assignments_mgr.assign(test_phone2, test_employee1)

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        test_phone1 = Phone(1, "Bedrock", "Pterodactyl")
        test_employee1 = Employee(1, "Fred Flintstone")

        test_assignments_mgr = PhoneAssignments()
        test_assignments_mgr.add_phone(test_phone1)
        test_assignments_mgr.add_employee(test_employee1)
        test_assignments_mgr.assign(test_phone1.id, test_employee1)

        self.assertIsNone(test_assignments_mgr.assign(test_phone1, test_employee1))

    def test_un_assign_phone(self):
        test_phone1 = Phone(1, "Bedrock", "Pterodactyl")
        test_employee1 = Employee(1, "Fred Flintstone")

        test_assignments_mgr = PhoneAssignments()
        test_assignments_mgr.add_phone(test_phone1)
        test_assignments_mgr.add_employee(test_employee1)
        test_assignments_mgr.assign(test_phone1.id, test_employee1)
        test_assignments_mgr.un_assign(test_phone1.id)

        self.assertIsNone(test_assignments_mgr.phones[0].employee_id)

    def test_get_phone_info_for_employee(self):
        test_phone1 = Phone(1, "Samsung", "Galaxy S2")
        test_phone2 = Phone(2, "Bedrock", "Pterodactyl")

        test_employee1 = Employee(1, "Kitty Cat")
        test_employee2 = Employee(2, "Puppy Dog")
        test_employee3 = Employee(3, "Fred Flintstone")

        test_assignments_mgr = PhoneAssignments()
        test_assignments_mgr.add_phone(test_phone1)
        test_assignments_mgr.add_phone(test_phone2)
        test_assignments_mgr.add_employee(test_employee1)
        test_assignments_mgr.add_employee(test_employee2)

        test_assignments_mgr.assign(test_phone1.id, test_employee1)

        self.assertEqual(test_phone1, test_assignments_mgr.phone_info(test_employee1))
        self.assertIsNone(test_assignments_mgr.phone_info(test_employee2))
        with self.assertRaises(PhoneError):
            test_assignments_mgr.phone_info(test_employee3)
