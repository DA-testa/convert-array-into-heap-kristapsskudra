# python3


def build_heap(data):
    swaps = []
    n = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n // 2 - 1, -1, -1):
        heap(i,data,swaps)

    return swaps

def heap(i,data,swaps):
    n = len(data)
    max = i
    left = 2 * i + 1
    if left < n and data[left] < data[max]:
        max = left
    right = 2 * i + 2
    if right < n and data[right] < data[max]:
        max = right
    
    if i != max:
        data[i], data[max] = data[max], data[i]
        swaps.append((i, max))
        heap(max, data, swaps)
    return swaps
def main():
    # TODO : add input and corresponding checks
    # first two tests are from keyboard, third test is from a file
    # # add another input for I or F
    # input from keyboard
    data = []
    n = 0
    print("Input file type")
    input_method = input()
    if input_method.upper() == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif input_method.upper() == "F":
        filename = input()
        path = open("./tests/" + filename, "r")
        fails = path.read()
        fails = fails.split('\n')
        n = int(fails[0])
        data = list(map(int, fails[1].split()))
        
    else:
        print("Not cerrect input")
        return
    

    # checks if lenght of data is the same as the said lenght
    if len(data) != n:
        print("Imput length not the same as massive length")
        return
 
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
 
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    print("Swap count: ", len(swaps))
    for i, j in swaps:
        print(i,j)
if __name__ == "__main__":
    main()

