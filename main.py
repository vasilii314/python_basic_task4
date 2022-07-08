dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

dict = {k: v for k, v in dict.items() if v >= 3}

print(dict)
