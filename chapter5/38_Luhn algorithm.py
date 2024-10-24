def luhn_algorithm(card):
    card = card.replace(" ", "")
    reverse = card[::-1]
    total_sum = 0
    for i, digit in enumerate(reverse):
        num = int(digit)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num = num - 9
        total_sum += num
    return total_sum % 10 == 0
card = '4799 2739 8713 6272'
if luhn_algorithm(card):
    print(f"Номер карты {card} корректен.")
else:
    print(f"Номер карты {card} некорректен.")