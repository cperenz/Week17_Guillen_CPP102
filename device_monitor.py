def load_default_data():
    return [30, 28, 35, 40, 60]


def check_if_numeric(val_str):
    return val_str.isdigit()


def insert_new_val(data_list):
    user_input = input("Enter new reading: ").strip()

    if not user_input:
        print("\nInvalid input. The reading cannot be empty.")
        return

    if not check_if_numeric(user_input):
        print("\nInvalid input. Enter a positive whole number only.")
        return

    num_val = int(user_input)
    if num_val < 0 or num_val > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return

    data_list.append(num_val)
    print("\nReading added successfully.")


def get_status_level(val, warn_th=60, crit_th=80):
    if val < warn_th:
        return "NORMAL"
    return "WARNING" if val < crit_th else "CRITICAL"


def calc_sum(numbers):
    return sum(numbers)


def calc_mean(numbers):
    return calc_sum(numbers) / len(numbers) if numbers else 0.0


def get_min_val(numbers):
    return min(numbers) if numbers else 0


def get_max_val(numbers):
    return max(numbers) if numbers else 0


def count_status_occurence(numbers, target_status):
    return sum(1 for item in numbers if get_status_level(item) == target_status)


def evaluate_system_state(warn_cnt, crit_cnt):
    if crit_cnt > 0:
        return "ATTENTION REQUIRED SYSTEM OVERHEATING"
    if warn_cnt > 0:
        return "WARNING HEAVY WORK LOAD"
    return "NORMAL LIGHT WORKLOAD"


def print_all_readings(data_list):
    print("\nCURRENT READINGS")
    print("----------------")
    for idx, item in enumerate(data_list, 1):
        print(f"Reading {idx}: {item} °C")


def print_categorization(data_list):
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for item in data_list:
        print(f"{item} °C -> {get_status_level(item)}")


def print_full_report(data_list):
    count_total = len(data_list)
    if count_total == 0:
        print("\nNo database tracking metrics context currently stored.")
        return

    s_total = calc_sum(data_list)
    s_avg = calc_mean(data_list)
    s_min = get_min_val(data_list)
    s_max = get_max_val(data_list)

    n_count = count_status_occurence(data_list, "NORMAL")
    w_count = count_status_occurence(data_