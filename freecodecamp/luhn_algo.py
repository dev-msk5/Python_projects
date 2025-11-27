def verify_card_number(card: str):
    card = ''.join(ch for ch in card if ch.isdigit())
    if not card:
        return 'INVALID!'
    sum1 = 0
    for i, ch in enumerate(reversed(card)):
        num = int(ch)
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
        sum1 += num
    return 'VALID!' if sum1 % 10 == 0 else 'INVALID!'
