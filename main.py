import json

def main():
    # Start block
    fib_num = int(input("Insert a number for [No. 2)] Fibonacci task: "))
    rev_str = input("Insert a word for [No. 5)] reverse string task: ")

    # 1)
    def first_task():
        # CLI spacing
        print("")

        x, sum, k = 13, 0, 0

        while k < x:
            k += 1
            sum += 1

        print(f"The sum result is: {sum}.")

    # Call task
    first_task()

    # 2)
    def second_task(num):
        # CLI spacing
        print("")

        if not isinstance(num, (int, float)):
            raise TypeError("Invalid input!")
        if num < 0:
            raise ValueError("Insert a positive number!")

        x, y, z = 0, 1, 0
        while num > z:
            z = x + y
            x = y
            y = z

        if z == num:
            return print(f"Selected number {num} IS a Fibonacci number!")
        else:
            return print(f"Selected number {num} IS NOT a Fibonacci number!")
    # Call task
    second_task(fib_num)

    # 3)
    def third_task():
        # CLI spacing
        print("")

        with open('arquivo.json', 'r') as file:
            data = json.load(file)
        
        data_dict = {day["dia"]: day["valor"] for day in data if day["valor"] > 0.0}
        
        min_val = min(data_dict, key = data_dict.get)
        max_val = max(data_dict, key = data_dict.get)

        sum_val, days = sum(data_dict.values()), len(data_dict)
        average = sum_val / days

        day_count = 0
        for value in data_dict.values():
            if value > average:
                day_count += 1

        print(f"The lowest revenue was: {min_val}.")
        print(f"The highest revenue was: {max_val}.")
        print(f"Number of days which the daily billing value was higher than the average: {day_count}.")    
    
    # Call task
    third_task()

    # 4)
    def fourth_task(**info):
        # CLI spacing
        print("")

        for value in info.values():
            if not isinstance(value, (int, float)):
                raise TypeError("Please enter a correct type format, like: {state}=numeric_value!")
        
        total_sum = sum(info.values())
        if total_sum <= 0:
            raise ValueError("Value equal or less than zero. Unable to calculate!")

        print("The representation percentage of each given object was:")
        for state, value in info.items():
            percentage = (value / total_sum) * 100
            print(f"{state} - {percentage:.2f}%")

    # Call task
    fourth_task(SP=67836.43, RJ=36678.66, MG=29229.88, ES=27165.48, Outros=19849.53)

    # 5)
    def fifth_task(string):
        # CLI spacing
        print("")
        
        reversed_str = []

        for i in range(len(string) - 1, -1, -1):
            reversed_str.append(string[i])
        
        reversed_str = "".join(reversed_str)
        print(f"Reversed chosen word: {reversed_str}")

    # Call task
    fifth_task(rev_str)

if __name__ == "__main__":
    main()