from typing import Optional
from Estruturas import ListNode, create_linked_list, print_linked_list


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        if list2 is None:
            return None
        else:
            return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        return ListNode(list1.val, mergeTwoLists(list1.next, list2))
    return ListNode(list2.val, mergeTwoLists(list1, list2.next))


def main():
    a = [1, 5]
    b = [2, 3, 4]
    lista1 = create_linked_list(a)
    lista2 = create_linked_list(b)

    resposta = mergeTwoLists(lista1, lista2)
    print_linked_list(resposta)


if __name__ == '__main__':
    main()

