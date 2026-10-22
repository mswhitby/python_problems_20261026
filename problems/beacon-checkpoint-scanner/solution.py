def solution(start, end):
    # Write your code here.
    curzon_list = [n for n in range(start, end+1) if curzon(n)]
    return curzon_list
    
def curzon(num):
    is_curzon = (pow(2, num) + 1) % (num * 2 + 1) == 0
    return is_curzon
