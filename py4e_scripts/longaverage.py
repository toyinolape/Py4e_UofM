def median(inputlist):
  inputlist = sorted(inputlist)
  length = len(inputlist)/2.0
  count = 0
  if inputlist == []:
    return []
  elif len(inputlist) % 2 == 1:
    middle = length - 0.5
    middle = int[middle]
    return inputlist[middle]

  elif len(inputlist) % 2 == 0 :
    first_position = int(length)
    second_position = int(length-1)
    sum_middle = inputlist[first_position] + inputlist[second_position]
    Avg = sum_middle / 2
    return Avg

  elif len(inputlist) == 1:
    return inputlist

print (median([1,2,3,4,6,2,4,4,4,2,7,7,]))
#Codecademy method is below, way shorter
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean

print median([2, 4, 5, 9])
