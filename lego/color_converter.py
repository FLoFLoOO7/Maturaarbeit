def converter(x):
    for i in range(6):
        for z in range(9):
            if z == 4:
                continue  # Spalte 4 überspringen

            r, g, b = x[i][z]

            # Grün
            if 2 <= r <= 15 and 21 <= g <= 36 and 45 <= b <= 63:
                x[i][z] = "Gre"

            # Orange
            elif 40 <= r <= 61 and 44 <= g <= 64 and 94 <= b <= 106:
                x[i][z] = "Ora"

            # Blau
            elif 0 <= r <= 12 and 5 <= g <= 19 and 31 <= b <= 53:
                x[i][z] = "Blu"

            # Rot
            elif 28 <= r <= 46 and 11 <= g <= 26 and 15 <= b <= 34:
                x[i][z] = "Rot"

            # Gelb
            elif 42 <= r <= 64 and 43 <= g <= 64 and 94 <= b <= 106:
                x[i][z] = "Gel"

            # Weiß
            elif 46 <= r <= 64 and 45 <= g <= 66 and 74 <= b <= 100:
                x[i][z] = "Wei"

    return x