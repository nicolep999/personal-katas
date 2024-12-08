from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def test_init(self):
        student = Student("John Doe")
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.courses, {})

    def test_enroll_new_course(self):
        student = Student("John Doe")
        result = student.enroll("Math", ["note1", "note2"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(student.courses, {"Math": ["note1", "note2"]})

    def test_enroll_existing_course(self):
        student = Student("John Doe")
        student.enroll("Math", ["note1", "note2"])
        result = student.enroll("Math", ["note3", "note4"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(
            student.courses, {"Math": ["note1", "note2", "note3", "note4"]}
        )

    def test_add_notes(self):
        student = Student("John Doe")
        student.enroll("Math", ["note1", "note2"])
        result = student.add_notes("Math", "note3")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(student.courses, {"Math": ["note1", "note2", "note3"]})

    def test_add_notes_to_non_existent_course(self):
        student = Student("John Doe")
        with self.assertRaises(Exception) as ex:
            student.add_notes("Math", "note1")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_course(self):
        student = Student("John Doe")
        student.enroll("Math", ["note1", "note2"])
        result = student.leave_course("Math")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(student.courses, {})

    def test_leave_non_existent_course(self):
        student = Student("John Doe")
        with self.assertRaises(Exception) as ex:
            student.leave_course("Math")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()
