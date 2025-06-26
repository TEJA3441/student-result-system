def get_valid_int(prompt, min_val=0, max_val=100):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            else:
                print(f"⚠️  Enter a value between {min_val} and {max_val}")
        except ValueError:
            print("⚠️  Invalid input! Enter an integer.")

def get_non_empty_input(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        else:
            print("⚠️  Input cannot be empty.")
