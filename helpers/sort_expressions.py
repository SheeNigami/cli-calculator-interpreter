def sort_expressions(list): 
    sorted_exp = []
    return sorted_exp

def mergeSort(input_list):
    if len(input_list) > 1:
        mid = int(len(input_list)/2)
        leftHalf = input_list[:mid]
        rightHalf = input_list[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        leftIndex,rightIndex,mergeIndex = 0,0,0
        mergeList = input_list
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < xrightHalf[rightIndex]:
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex+=1
            else:
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex+=1 
            mergeIndex+=1
        # Handle those items still left in the left Half
        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex+=1
            mergeIndex+=1
        # Handle those items still left in the right Half
        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex+=1
            mergeIndex+=1
        print('merge', input_list) 

input_list = [50, 20, 90, 10, 70, 30, 40, 60, 20]
mergeSort(input_list)
print(input_list)