def solution(readings):
    lowest = 0
    for reading in readings:
        if reading < lowest:
            lowest = reading
    return lowest
