from contrib.reader import get_line, get_files_list
import os


def test_get_line_unix(tmpdir):
    tmp_file = tmpdir.join("test_slash_n.txt")
    original_lines = list(f"line number {i}" for i in range(5))
    tmp_file.write("".join(f"{line}\n" for line in original_lines))

    lines = list()
    for line in get_line(tmp_file, sep=b"\n"):
        lines.append(line[0].decode())
    assert original_lines == lines


def test_get_file_list(tmpdir):
    correct_files = (
        "test1",
        "test2",
        "test3",

    )

    incorrect_files = ("teest", "est3")
    list(tmpdir.join(
        filename).write("") for filename in correct_files + incorrect_files)

    print(os.listdir(str(tmpdir)))
    files = set(
        d["name"].split("/")[-1] for d in
        get_files_list(str(tmpdir), r"test\d"))

    assert set(correct_files) == files
