from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(a, b):
        return a / b

    my_function(10, 5)
    captured = capsys.readouterr()
    assert captured.out == "Start: my_function ok\n\nFinish: my_function ok\n\n"

    my_function(10, 0)
    captured = capsys.readouterr()
    assert captured.out == "Start: my_function ok\n\nmy_function error: division by zero. Inputs: (10, 0), {}\n\n"

    @log("testlog.txt", "w")
    def test_function(x, y):
        return x + y

    test_function(1, 8)
    with open("testlog.txt", "r", encoding="utf-8") as test_log:
        content = test_log.read()

    assert content == "Start: test_function ok\nFinish: test_function ok\n"

    test_function("one", 4)
    with open("testlog.txt", "r", encoding="utf-8") as test_log:
        content = test_log.read()

    assert content == (
        "Start: test_function ok\ntest_function error:"
        ' can only concatenate str (not "int") to str. '
        "Inputs: ('one', 4), {}\n"
    )
