'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase


class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    def test_add_and_remove_student_check_student_is_removed(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        test_class.add_student(student)
        test_class.remove_student(student)
        self.assertNotIn(student, test_class.class_list)

    def test_remove_student_not_in_populated_list_check_studentError(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        ghost = "Friendly Casper"
        test_class.add_student(student)
        with self.assertRaises(StudentError):
            test_class.remove_student(ghost)

    def test_remove_student_from_empty_list_check_studentError(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        with self.assertRaises(StudentError):
            test_class.remove_student(student)

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    # TODO test add students, not enrolled. use assertFalse

    def test_IS_ENROLLED_when_student_not_enrolled_in_populated_class_check_return_False(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        ghost = "Friendly Casper"
        test_class.add_student(student)
        self.assertFalse(test_class.is_enrolled(ghost))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    # However, it would be useful to check that index_of_student returns None if a student isn't present.
    def test_INDEX_OF_STUDENT_returns_None_when_student_not_in_empty_list(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        self.assertIsNone(test_class.index_of_student(student))

    def test_INDEX_OF_STUDENT_returns_correct_index_when_student_not_in_list(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        test_class.add_student(student)
        ghost = "Friendly Casper"
        self.assertIsNone(test_class.index_of_student(ghost))

    def test_IS_CLASS_FULL_when_class_is_full_check_return_True(self):
        test_class = ClassList(2)
        student = "Kitty Cat"
        classmate = "Puppy Dog"
        test_class.add_student(student)
        test_class.add_student(classmate)
        self.assertTrue(test_class.is_class_full())

    def test_IS_CLASS_FULL_when_class_is_empty_or_fillable_check_return_False(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_class_full())
        student = "Kitty Cat"
        test_class.add_student(student)
        self.assertFalse(test_class.is_class_full())
