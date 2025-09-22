def divide_number(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {str(e)}")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution finished")

divide_number(4, 0)