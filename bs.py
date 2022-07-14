def Solution(A,B):
    total = A + B
    long = max(A,B)
    short = min(A,B)

    if total < 4:
        return 0

    while total % 4 == 0:
        total -= 1
    
    maximum = total/4

    while maximum != 0:
        if maximum * 4 <= long:
            return maximum
        if maximum * 3 <= long & maximum <= short:
            return maximum
        if maximum * 2 <= long & maximum * 2 <= short:
            return maximum
        maximum -= 1

        return 0



