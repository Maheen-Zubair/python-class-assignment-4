def function_for_addition(numbers)-> int:
    initial_state: int = 0
    for number in numbers:
        initial_state += number

    return initial_state


def adding_numbers():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    sum_of_numbers: int = function_for_addition(numbers) 
    print(sum_of_numbers)  
    
adding_numbers()