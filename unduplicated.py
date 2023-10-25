import unittest


def remove_duplicates(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Входной аргумент должен быть списком")

    if not all(isinstance(item, (int, float, str)) for item in input_list):
        raise ValueError(
            "Список должен содержать только числа, строки или числовые значения")

    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


class RemoveDuplicatesTest(unittest.TestCase):
    def test_integer_duplicates(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(remove_duplicates(input_list), [1, 2, 3, 4, 5])

    def test_float_duplicates(self):
        input_list = [1.0, 2.5, 2.5, 3.0, 4.5, 4.5, 5.0]
        self.assertEqual(remove_duplicates(input_list),
                         [1.0, 2.5, 3.0, 4.5, 5.0])

    def test_string_duplicates(self):
        input_list = ["apple", "banana", "apple", "cherry", "date", "banana"]
        self.assertEqual(remove_duplicates(input_list), [
                         "apple", "banana", "cherry", "date"])

    def test_mixed_duplicates(self):
        input_list = [1, 2.0, "apple", 2, "banana",
                      3.0, "apple", 4.0, 5, "banana"]
        self.assertEqual(remove_duplicates(input_list), [
                         1, 2.0, "apple", "banana", 3.0, 4.0, 5])

    def test_non_list_input(self):
        with self.assertRaises(ValueError):
            remove_duplicates("not_a_list")


if __name__ == "__main__":
    unittest.main()
