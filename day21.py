def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return

    top = stack.pop()
    insert_at_bottom(stack, element)

    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return

    top = stack.pop()
    reverse_stack(stack)

    insert_at_bottom(stack, top)


if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    reverse_stack(arr)

    print(arr)
