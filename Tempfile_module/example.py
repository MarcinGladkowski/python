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


if __name__ == '__main__':
    raise SystemExit(main())
