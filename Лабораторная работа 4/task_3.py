def delete(list_, index=None):
    if index is not None:
        list_.pop(index)
    else:
        list_.pop()
    return list_

   # С использованием слайсирования
   # if index is not None:
   #      new_list = list_[:index] + list_[index+1:]
   #  else:
   #      new_list = list_[:-1]
   #  return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
