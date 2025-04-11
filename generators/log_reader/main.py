

def log_error_lines(log_path):
    with open(log_path, "r") as f:
        for line in f:
            if line.startswith("[ERROR]"):
                yield line

def paths_from_lines(log_lines):
    for line in log_lines:
        _, path, _ = line.split(" - ", 2)
        yield path


def pages_with_errors(log_path):
    yield from paths_from_lines(log_error_lines(log_path))


print(list(pages_with_errors('webapp.log')))
