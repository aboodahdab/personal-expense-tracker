from tracker import create_table, add_expense, delete_expense, get_expenses, cursor, edit_expense, print_expenses, show_expense, delete_all_expenses
import argparse


def greet():
    print("welcome to personal expense tracker!".title())


greet()


def codeHandler(args):
    choice = args.command

    expenses = get_expenses()
    create_table()
    if choice == "add":
        # adds a new expense
        note = " ".join(args.note)
        add_expense((args.date, args.amount, args.category, note))
        print("expense added successfly!")
    if choice == "print":
        if expenses == []:
            print("nothing to show!".title())
            return
        print_expenses(expenses)

    if choice == "clear":
        delete_all_expenses()
        print("succesfly deleting everything".title())
    if choice == "show":
        expense_ID = args.expenseID
        show_expense(expense_ID)
    if choice == "del":
        expense_ID = args.expenseID
        delete_expense(expense_ID)
        print(f"successfly deleting expense number {expense_ID}!")
    if choice == "edit":
        note = " ".join(args.note)
        print(note)
        edit_expense(expense_ID, (args.date,
                     args.amount, args.category, note))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple personal expense tracker using SQLite. You can add, print,edit, clear,delete, or show expenses.")

    sub = parser.add_subparsers(
        dest="command", required=True, help="Choose a command: add, print,edit, clear,delete, or show")

    print_parser = sub.add_parser(
        "print", help="gets all expenses without notes")

    clear_parser = sub.add_parser("clear", help="removes all expenses")

    show_parser = sub.add_parser(
        "show", help="shows only one expense with it's note ")
    show_parser.add_argument("expenseID", type=str,
                             help="the id of the shown expense with the note")
    delete_parser = sub.add_parser(
        "del", help="deletes one expense ")
    delete_parser.add_argument("expenseID", type=str,
                               help="the id of the deleted  expense with the note")
    edit_parser = sub.add_parser(
        "edit", help="edits the expense")
    edit_parser.add_argument("expenseID", type=str,
                             help="the id of the edited expense  ")
    edit_parser.add_argument("date", help="expense date ")
    edit_parser.add_argument("amount", type=lambda v: int(
        v) if v.isdigit() else float(v))
    edit_parser.add_argument(
        "category", type=str, help="the new expense category like:food party or shopping")
    edit_parser.add_argument("note", nargs='+', type=str,
                             help="thenew expense note")

    add_parser = sub.add_parser("add", help="adds a new expense")
    add_parser.add_argument("date", help="expense date ")
    add_parser.add_argument("amount", type=lambda v: int(
        v) if v.isdigit() else float(v))
    add_parser.add_argument(
        "category", type=str, help="expense category like:food party or shopping")
    add_parser.add_argument("note", nargs='+', type=str, help="expense note")

    args = parser.parse_args()
    codeHandler(args)
    cursor.close()
