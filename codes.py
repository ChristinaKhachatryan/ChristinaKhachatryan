# fibionacci sequence


def fibionacci(num):
    if num <= 0:
        return None
    elif num == 1 or num == 2:
        return 1
    else:
        return fibionacci(num - 1) + fibionacci(num - 2)


num = fibionacci(num=7)
print(num)

lst = []
my_dict = {}


def view_menu():
    print('1. enter do to list')
    print('2. view, check it or edit')
    print('3. remove something from list')
    print('4. marked as done')
    print('5. view tasks marked as done')
    print('6. exit')


def my_menu():
    view_menu()
    while True:
        choice = int(input('Enter one of them'))
        if choice == 1:
            enter_to_list()
        elif choice == 2:
            view_list()
        elif choice == 3:
            remove_from_list()
        elif choice == 4:
            marked_as_done()
        elif choice == 5:
            view_marked_as_done()
        elif choice == 6:
            break
        else:
            print('invalid input')


# working with menu
def enter_to_list():
    walks = 0
    while walks < 4:
        user_input = input('enter task')
        lst.append(user_input)
        my_dict[user_input] = 'Not done'
        walks += 1
    print('tasks successfully added to the list')
    view_menu()


def view_list():
    print("Task in the list")
    for index, task in enumerate(lst, start=1):
        print(f"{index}. {task} - {my_dict[task]}")
    view_menu()


def remove_from_list():
    if not lst:
        print('List is empty')
    else:
        print('Tasks in the list ')
        for index, task in enumerate(lst, 1):
            print(f"{index}. {task} - {my_dict[task]}")
        n = int(input('enter the task you want to remove'))
        if 1 <= n <= len(lst):
            removed_t = lst.pop(n - 1)
            my_dict.pop(removed_t)
            print(f"Task '{removed_t}' removed from the list.")
        else:
            print('Invalid task number')
    view_menu()


def marked_as_done():
    print('Tasks in the list:')
    for index, task in enumerate(lst, 1):
        print(f"{index}. {task} - {my_dict[task]}")
    n = int(input('enter the task you want to mark as done'))
    if 1 <= n <= len(lst):
        task_to_mark = lst[n - 1]
        my_dict[task_to_mark] = 'Done'
        print(f"Task '{task_to_mark}' marked as done. ")
    else:
        print('Invalid task number ')
    view_menu()


def view_marked_as_done():
    print('Tasks marked as done: ')
    for task, status in my_dict.items():
        if status == "Done":
            print(f"{task} - {status}")


my_menu()


# reversed list

def my_list():
    mylist = []
    reversed_list = []
    for i in range(5):
        user_input = int(input())
        mylist.append(user_input)
    reversed_list = mylist[::-1]
    print(mylist)
    print(reversed_list)

# factorial
def my_factorial(n):
    if n == 1:
        return 1
    else:
        return n * (my_factorial(n - 1))


n = int(input('input number'))
print(my_factorial(n))



# palindrom words


def if_palindrom():
    word = input('enter word')
    word = list(word)
    reversed_word = word[::-1]
    for i in word:
        if word == reversed_word:
            return True
        else:
            return False


print(if_palindrom())