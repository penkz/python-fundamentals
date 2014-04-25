def merge(L):
  merged = []
  for i in range(0,len(L),3):
    merged.append(L[i] + L[i+1] + L[i+2])
  return merged

#print(merge([1,2,3,4,5,6,7,8,9]))


def shift_right(L):
  last_item = L[-1]
  print(len(L))
  for i in range(1,len(L)):
    L[len(L) - i] = L[len(L) - i - 1]
  L[0] = last_item
  print(L)
shift_right([0,1,2,3,4,5])
