def selection_sort(lst):
    b = len(lst)

  
    for i in range(b-1):
      min = i
      for j in range(i+1, b):
        if lst[j] < lst[min]:
            min = j

      if min!=i:
          lst[i], lst[min] = lst[min], lst[i]

    return lst

def main():
  lst = [10,3,2,22,11,44,6,3,2]
  selection_sort(lst)
  print(lst)

main()


    
