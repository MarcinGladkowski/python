import os.path
import tempfile
import subprocess


def main() -> int:
    """
        The TemporaryName works on descriptor number
        Even as file we can create directories also
        You can add suffix to directory also
    """
    with tempfile.NamedTemporaryFile(mode='w') as tmp_file:
        tmp_file.write("foo\n")
        tmp_file.flush()  # because it's a buffer
        subprocess.check_call(('cat', tmp_file.name))


    tmp_file_example = tempfile.NamedTemporaryFile()
    tmp_file_example.write(b'test')
    tmp_file_example.flush()
    tmp_file_example.close()

    print(tmp_file_example.name)
    print(os.path.isfile(tmp_file_example.name))



if __name__ == '__main__':
    raise SystemExit(main())
