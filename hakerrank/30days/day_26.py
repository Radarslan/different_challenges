if __name__ == "__main__":
    return_day, return_month, return_year = map(int, input().split())
    due_day, due_month, due_year = map(int, input().split())
    if return_year > due_year:
        print(10000)
    elif return_year == due_year:
        if return_month > due_month:
            print((return_month - due_month) * 500)
        elif return_month == due_month:
            if return_day > due_day:
                print((return_day - due_day) * 15)
            elif return_day < due_day:
                print(0)
        elif return_month < due_month:
            print(0)
    elif return_year < due_year:
        print(0)
