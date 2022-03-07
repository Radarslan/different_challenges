def get_valid_thickness(thickness):
    try:
        thickness = int(thickness)
        if thickness in range(1, 50) and thickness % 2 != 0:
            return thickness
    except Exception as e:
        pass
    return 0


if __name__ == '__main__':
    thickness = get_valid_thickness(input())  # This must be an odd number
    c = 'H'

    # # Top Cone
    # for i in range(thickness):
    #     print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    for i in range(1, thickness+1):3
        print((c * (i*2-1)).center(thickness*2-1))

    # Top Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
    for i in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # # Bottom Cone
    # for i in range(thickness):
    #     print(((c * (thickness - i - 1)).______(thickness) + c + (c * (thickness - i - 1)).______(thickness)).______(
    #         thickness * 6))

    for i in range(thickness, 0, -1):
        print((c * (i*2-1)).center(thickness*2-1).rjust(thickness*6-1))
