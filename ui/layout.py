def get_hand_layout(num_cards, screen_width, card_width, max_spacing, min_spacing):
    if num_cards <= 10:
        rows = [list(range(num_cards))]
    else:
        rows = [list(range(10)), list(range(10, num_cards))]

    def calculate_spacing(x):  #x is no of cards in row
        if x <= 1:
            return 0
        else:
            available_space= screen_width - 2 * 50
            spacing = (available_space - card_width) // (x - 1)
            return(max(min_spacing, min(spacing, max_spacing)))

    spacings = []
    for row in rows:
        spacings.append((calculate_spacing(len(row))))

    return list(zip(rows,spacings))