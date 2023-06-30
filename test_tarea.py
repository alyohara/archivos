import os
import unittest

from tarea import create_files


class TestCreateFiles(unittest.TestCase):

    def test_create_files(self):
        unab_folder = "unab"
        create_files(unab_folder)

        for letter in "abcdefghijklmnopqrstuvwxyz":
            file_path = os.path.join(unab_folder, f"{letter}.txt")
            self.assertTrue(os.path.exists(file_path))

            with open(file_path, "r") as file:
                content = file.read()

                if letter in ["a", "e", "i", "o", "u"]:
                    self.assertEqual(content, "i am a vowel file")
                else:
                    self.assertEqual(content, "i am a consonant file")


if __name__ == "__main__":
    unittest.main()

