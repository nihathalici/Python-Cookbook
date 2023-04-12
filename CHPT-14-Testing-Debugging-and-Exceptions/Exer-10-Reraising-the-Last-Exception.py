# Exer-10-Reraising-the-Last-Exception


def example():
    try:
        int("N/A")
    except ValueError:
        print("Didn't work")
        raise


example()  # Prints first: Didn't work, then ValueError

###

try:
    ...
except Exception as e:
    # Process exception information in some way
    ...

    # Propagate the exception
    raise
