def insertion_sort(list):
  for i in range(1, len(list)):
    y = list[i]

    j = i - 1
    while j >=0 and y < list[j]:
      list[j+1] = list[j]
      j -=1
    list[j+1] = y

  return list 

def main():
    list = [6,6,2,5,8,533,11,44,63,1]
    insertion_sort(list)
    print(list)

main()
