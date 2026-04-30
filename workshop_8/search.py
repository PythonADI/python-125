nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # n

x = 5
def search(lst, x):
    for num in lst:
        if num == x:
            return num

    return None



def binary_search(lst, x, lb = None, ub = None):
    """
    lst დალაგებულია ზრდადობით
    lst თუ ცარიელია ესეიგი ვერ ვიპოვეთ
    ავიღოთ შუა ელემენტი შევადაროთ X
    თუ ვიპოვეთ დავაბრუნოთ

    თუ მეტია x-ზე:
        -> ვეძებთ სიის მარცხნივ
        -> გამოვიძახოთ binary_search(list[:იდექსამდე], x)
    თუ არა და
        -> ვეძებთ მარჯვნივ
        -> გამოვიძახოთ binary_search(lst[ინდექსიდან:], x)
    """
    if len(lst) <= 1:
        return None

    idx = len(lst) // 2
    middle_element = lst[idx]
    if middle_element == x:
        return x

    if middle_element > x:
        return binary_search(lst[lb:idx], x, lb, idx)
    else:
        return binary_search(lst[idx:ub], x, idx, ub)



print(search(nums, x))
print(binary_search(nums, x))
