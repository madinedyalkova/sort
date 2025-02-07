def bubble_sort(list):
    n = len(list)

    for i in range (n-1):
      for j in range (n-1):
        if list[j] > list[j+1]:
          y = list[j]
          list[j] = list [j+1]
          list[j+1] = y

    return list

def main():
  list = [10,8,45,9,2,6,7,5,3]
  bubble_sort(list)
  print(list)
          
main()
