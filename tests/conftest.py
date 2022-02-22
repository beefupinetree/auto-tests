import pytest
import sys


# Here we're changing the default behavior of stdout to get it to append to a buffer during testing and then printing it out at the end.
@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = {"stdout": "", "write_calls": 0}

    def fake_write(s):
        buffer["stdout"] += s
        buffer["write_calls"] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer


# Connection shared between all test files because of the scope. Otherwise, the default behavior is to run it in every function it's called in.
@pytest.fixture(scope="session")
def db_conn():
    db = ...
    url = ...
    with db.connect(url) as conn:  # connection will be torn down after all tests finish
        yield conn  # Use yield instead of return for anything that required tear-down code
