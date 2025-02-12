from _functools import reduce, partial

def compose(*functions):
    """
        example: https://github.com/jjeg1979/pyBacktestAnalyzer/blob/main/src/parsegbx/parsegbx.py

        Composes functions into single function

        compose(
            func_1(),
            func_n()
        )
    """
    return reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)

