for i in range(1,11):
    if i == 1:
        sum_current_and_previous = i
    else:
        sum_current_and_previous = i + (i-1)

    print(f"current: {i}, previous: {i-1}, sum: {sum_current_and_previous}")