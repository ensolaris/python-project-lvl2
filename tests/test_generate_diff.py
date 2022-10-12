from gendiff import generate_diff
import pytest


def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = open('tests/fixtures/result_json').read()

    result = generate_diff(file1, file2)
    print(result)
    assert result == expected


def test_generate_diff_with_directory():
    with pytest.raises(IsADirectoryError):
        generate_diff('/tests', '/tests/fixtures/file2.json')


def test_generate_diff_filenotfound():
    with pytest.raises(FileNotFoundError):
        generate_diff('/tests/fixtures/file3.json', '/tests/fixtures/file2.json')