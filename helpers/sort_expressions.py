#Can add more sorting algorithms while using sort_expressions as control function

def sort_expressions(input_list, ascending_check): 
    return mergeSort(input_list, ascending_check)

def mergeSort(input_list, ascending_check):
    if len(input_list) > 1:
        mid = int(len(input_list)/2)
        
        leftHalf = input_list[:mid]
        rightHalf = input_list[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        leftIndex,rightIndex,mergeIndex = 0,0,0
        mergeList = input_list

        #checking for ascend descend
        if ascending_check == 1:
            #sorts ascending
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
                if leftHalf[leftIndex] < rightHalf[rightIndex]:
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
                else:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1 
                mergeIndex+=1
        else:
            #sorts descending
            while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
                if leftHalf[leftIndex] < rightHalf[rightIndex]:
                    mergeList[mergeIndex] = rightHalf[rightIndex]
                    rightIndex+=1
                else:
                    mergeList[mergeIndex] = leftHalf[leftIndex]
                    leftIndex+=1
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