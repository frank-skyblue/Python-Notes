res = 0


def spam(divBy):
    try:  # run code and test for errors
        global res
        res = 22 / divBy
    # run code when error occurs to handle the error (keep executing)
    except ZeroDivisionError as e:
        res = -1
        print("Error: invalid argument: {}".format(e))
    else:  # run when there is no error
        print("Success: No error")
    finally:  # run regardless of result from try/except
        print("Finished executing...")


spam(2)
print(res)
spam(0)
print(res)
