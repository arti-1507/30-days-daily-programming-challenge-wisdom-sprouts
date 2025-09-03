def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    top = stack.pop()
    insert_sorted(stack, element)
    stack.append(top)


def sort_stack(stack):
    if not stack:
        return

    top = stack.pop()

    sort_stack(stack)

    insert_sorted(stack, top)


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))

    sort_stack(arr)

    print(arr)
