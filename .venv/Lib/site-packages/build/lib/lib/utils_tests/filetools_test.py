import platform
import subprocess
import unittest
from unittest.mock import patch
from scripts.addHeaderSlashes.utils.filetools import \
    browse_for_json_file,                            \
    verify_json,                                       \
    read_json_by_lines,                              \
    match_comment,                                   \
    modify_line,                                     \
    open_temp_file                                   \


json_path = 'C:/Users/glenj/AppData/Roaming/Code/User/scripts/addHeaderSlashes/utils_tests/test_file.json'
json_path_with_comments = 'C:/Users/glenj/AppData/Roaming/Code/User/scripts/addHeaderSlashes/utils_tests/test_file_1.json'
test_temp_path = 'C:/Users/glenj/AppData/Roaming/Code/User/scripts/addHeaderSlashes/utils_tests/test_temp_path'


class TestFileBrowsing(unittest.TestCase):
    def test_browse_for_files(self):
        expected_file = "C:/Users/glenj/AppData/Roaming/Code/User/settings.json"
        actual_file = browse_for_json_file()
        self.assertEqual(actual_file, expected_file)


class TestFileLoading(unittest.TestCase):
    def test_load_existing_file(self):
        expected_content = '{\n  "key": "value"\n}'
        loaded_content = verify_json(json_path)
        self.assertEqual(loaded_content, expected_content)

    def test_load_nonexistent_file(self):
        loaded_content = verify_json("nonexistent_file.json")
        self.assertIsNone(loaded_content)


class TestReadFileByLines(unittest.TestCase):
    def test_read_existing_file(self):
        lines = read_json_by_lines(json_path)
        self.assertIsNotNone(lines)
        self.assertEqual(len(lines), 3)

    def test_read_nonexistent_file(self):
        lines = read_json_by_lines("nonexistent_file.txt")
        self.assertIsNone(lines)


class TestMatchCommentLine(unittest.TestCase):
    def test_match_comment_line(self):
        line = "  // This is a comment."
        self.assertTrue(match_comment(line))

    def test_non_match_comment_line(self):
        line = "This is not a comment."
        self.assertFalse(match_comment(line))


class TestModifyCommentLine(unittest.TestCase):
    def test_modify_line(self):
        line = "  ///"
        modified_line = modify_line(line)
        except_line = line + '/' * (120 - len(line))
        self.assertEqual(modified_line, except_line)


class TestOpenInTextEditor(unittest.TestCase):
    @patch('subprocess.Popen')
    @patch('platform.system', return_value='Windows')
    def test_open_in_text_editor_windows(self, mock_system, mock_popen):
        open_temp_file(json_path)
        mock_popen.assert_called_once_with(
            ['C:\\Program Files\\Microsoft VS Code\\Code.exe', json_path])


class TestOpenTempFile(unittest.TestCase):
    def test_open_temp_file_with_vscode(self):
        open_temp_file(test_temp_path)


if __name__ == '__main__':
    unittest.main()
