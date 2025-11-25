# # Task 1. ToDo List Application
class Task:
    def __init__(self, task_title, description, due_date, status):
        self.task_title = task_title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_title} - {self.status} (due: {self.due_date})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, status):
        new_task = Task(title, description, due_date, status)
        self.tasks.append(new_task)
        return f'{title} added to the task list.'

    def mark_as_complete(self, task_name):
        for t in self.tasks:
            if t.task_title.lower() == task_name.lower():
                if t.status.lower() == 'complete':
                    return f'Task "{task_name}" is already completed.'
                else:
                    t.status = 'complete'
                    return f'{task_name} marked as complete.'
        return f'Task "{task_name}" not found.'

    def list_all_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return "All tasks:\n" + "\n".join(str(t) for t in self.tasks)

    def incomplete_task(self):
        incomplete = [t for t in self.tasks if t.status.lower() != 'complete']
        if incomplete:
            return "Incomplete tasks:\n" + "\n".join(str(t) for t in incomplete)
        else:
            return "All tasks are completed."


todo = ToDoList()


def print_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. List all tasks")
    print("2. Add a task")
    print("3. Mark a task as complete")
    print("4. View incomplete tasks")
    print("5. Exit")


while True:
    print_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if choice == 1:
        print(todo.list_all_tasks())

    elif choice == 2:
        title_user = input("Task title: ")
        description_user = input("Description: ")
        due_date_user = input("Due date (yyyy-mm-dd): ")
        status_user = input("Status (pending/incomplete): ").lower()

        print(todo.add_task(title_user, description_user, due_date_user, status_user))

    elif choice == 3:
        task_name_to_mark = input("Enter task name to mark complete: ")
        print(todo.mark_as_complete(task_name_to_mark))

    elif choice == 4:
        print(todo.incomplete_task())

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")


# Task 2. Simple Blog System
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f'"{self.title}" — by {self.author}\n{self.content}'


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post_title, post_content, post_author):
        for p in self.posts:
            if p.title.lower() == post_title.lower():
                return "You already have a post with this title."

        new_post = Post(post_title, post_content, post_author)
        self.posts.append(new_post)
        return f'"{post_title}" added successfully.'

    def list_all_posts(self):
        if not self.posts:
            return "You don't have any posts yet."

        return "All posts:\n" + "\n\n".join(str(p) for p in self.posts)

    def display_by_author(self, author_name):
        result = [p for p in self.posts if p.author.lower() == author_name.lower()]

        if not result:
            return f'No posts found by "{author_name}".'

        return "\n\n".join(str(p) for p in result)


    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                return f'"{title}" deleted successfully.'
        return f'Post titled "{title}" not found.'

    def edit_post(self, old_title, new_title, new_content):
        for post in self.posts:
            if post.title.lower() == old_title.lower():

                for p in self.posts:
                    if p.title.lower() == new_title.lower() and p != post:
                        return "Another post with this title already exists."

                post.title = new_title
                post.content = new_content
                return f'"{old_title}" updated successfully.'

        return f'Post titled "{old_title}" not found.'

    def latest_posts(self, count):
        if not self.posts:
            return "There are no posts yet."

        count = int(count)
        latest = self.posts[-count:][::-1]
        return "\n\n".join(str(p) for p in latest)




blog = Blog()

def print_menu_tsk2():
    print("\n==== BLOG MENU ====")
    print("1. List all posts")
    print("2. Display posts by author")
    print("3. Add post")
    print("4. Delete post")
    print("5. Edit post")
    print("6. Latest posts")
    print("7. Exit\n")


while True:
    print_menu_tsk2()

    try:
        choice2 = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    if choice2 == 1:
        print(blog.list_all_posts())

    elif choice2 == 2:
        name = input("Enter author name: ")
        print(blog.display_by_author(name))

    elif choice2 == 3:
        title = input("Post title: ")
        content = input("Post content: ")
        author = input("Post author: ")
        print(blog.add_post(title, content, author))

    elif choice2 == 4:
        t = input("Enter title to delete: ")
        print(blog.delete_post(t))

    elif choice2 == 5:
        old_t = input("Old title: ")
        new_t = input("New title: ")
        new_c = input("New content: ")
        print(blog.edit_post(old_t, new_t, new_c))

    elif choice2 == 6:
        c = input("How many latest posts? ")
        print(blog.latest_posts(c))

    elif choice2 == 7:
        print("Exiting...")
        break

    else:
        print("Invalid menu option!")


# Task 3. Simple Banking System

class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}\n" \
               f"Account Holder: {self.account_holder_name}\n" \
               f"Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = []

    # Helper method: account number bo'yicha topish
    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    # Add account
    def add_account(self, account_number, account_holder_name, balance):
        if self.find_account(account_number):
            return "Account with this number already exists."
        new_acc = Account(account_number, account_holder_name, balance)
        self.accounts.append(new_acc)
        return f"Account {account_number} added successfully."

    # Check balance
    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            return f"Balance: ${account.balance:.2f}"
        return "Account not found."

    # Deposit money
    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount <= 0:
                return "Deposit amount must be positive."
            account.balance += amount
            return f"${amount:.2f} deposited. New balance: ${account.balance:.2f}"
        return "Account not found."

    # Withdraw money (overdraft handled)
    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if not account:
            return "Account not found."

        if amount <= 0:
            return "Withdrawal amount must be positive."

        if account.balance < amount:
            return "Insufficient balance."

        account.balance -= amount
        return f"${amount:.2f} withdrawn. New balance: ${account.balance:.2f}"


    # Transfer money between accounts
    def transfer(self, from_acc_number, to_acc_number, amount):
        from_acc = self.find_account(from_acc_number)
        to_acc = self.find_account(to_acc_number)

        if not from_acc or not to_acc:
            return "One or both accounts not found."
        if amount <= 0:
            return "Transfer amount must be positive."
        if from_acc.balance < amount:
            return "Insufficient balance in sender's account."

        from_acc.balance -= amount
        to_acc.balance += amount
        return f"${amount:.2f} transferred from {from_acc_number} to {to_acc_number}."

    # Display account details
    def account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            return str(account)
        return "Account not found."
    
acc = Bank()

def print_menu_tsk3():
    print("\n===== BANK SYSTEM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer (Account → Account)")
    print("5. Add New Account")
    print("6. View Account Details")
    print("7. Exit")
    print("=============================")


while True:
    print_menu_tsk3()

    try:
        choice3 = int(input("Select an option (1-7): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue


    if choice3 == 1:
        try:
            acc_num = int(input("Enter account number (16 digits): "))
            print(acc.check_balance(acc_num))
        except ValueError:
            print(" Account number must be numeric!")

  
    elif choice3 == 2:
        try:
            acc_num = int(input("Enter account number (16 digits): "))
            amount = float(input("Enter deposit amount: "))
            print(acc.deposit(acc_num, amount))
        except ValueError:
            print("Invalid input! Try again.")

  
    elif choice3 == 3:
        try:
            acc_num = int(input("Enter account number (16 digits): "))
            amount = float(input("Enter withdrawal amount: "))
            print(acc.withdraw(acc_num, amount))
        except ValueError:
            print("Invalid number format!")

    elif choice3 == 4:
        try:
            from_acc = int(input("Transfer FROM account (16 digits): "))
            to_acc = int(input("Transfer TO account (16 digits): "))
            amount = float(input("Enter transfer amount: "))
            print(acc.transfer(from_acc, to_acc, amount))
        except ValueError:
            print("Invalid input!")


    elif choice3 == 5:
        try:
            new_acc = int(input("Enter new 16-digit account number: "))
            holder = input("Enter account holder name: ")
            balance = float(input("Initial deposit (min $100): "))
            print(acc.add_account(new_acc, holder, balance))
        except ValueError:
            print("Invalid input! Try again.")


    elif choice3 == 6:
        try:
            acc_num = int(input("Enter the account number: "))
            print(acc.account_details(acc_num))
        except ValueError:
            print(" Account number must be numeric!")

    elif choice3 == 7:
        print("Thank you for using our Banking System. Goodbye!")
        break

    else:
        print("Invalid option! Choose between 1 and 7.")

