
import json
import os
from datetime import datetime

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "leaves.json")


def load_leaves():
    """Load existing leave requests from JSON."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_leaves(leaves):
    """Save leave requests to JSON."""
    os.makedirs(DATA_FOLDER, exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(leaves, file, indent=4)


def apply_leave():
    """Allow an employee to submit a leave request."""

    employee_id = input("Enter Employee ID: ")
    employee_name = input("Enter Employee Name: ")

    try:
        start_date = datetime.strptime(
            input("Enter Start Date (YYYY-MM-DD): "),
            "%Y-%m-%d"
        )

        end_date = datetime.strptime(
            input("Enter End Date (YYYY-MM-DD): "),
            "%Y-%m-%d"
        )

        if end_date < start_date:
            print("End date cannot be before start date.")
            return

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    leave_days = (end_date - start_date).days + 1

    leaves = load_leaves()

    leave_request = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "leave_days": leave_days,
        "status": "Submitted"
    }

    leaves.append(leave_request)
    save_leaves(leaves)

    print("\nLeave request submitted successfully!")
    print("Total Leave Days:", leave_days)


def view_leaves():
    """Display all employee leave requests."""

    leaves = load_leaves()

    if not leaves:
        print("\nNo leave requests found.")
        return

    print("\n----- Employee Leave Requests -----")

    for leave in leaves:
        print("--------------------------------")
        print("Employee ID:", leave["employee_id"])
        print("Employee Name:", leave["employee_name"])
        print("Start Date:", leave["start_date"])
        print("End Date:", leave["end_date"])
        print("Leave Days:", leave["leave_days"])
        print("Status:", leave["status"])


def main():
    while True:
        print("\n===== Employee Leave Management System =====")
        print("1. Apply for Leave")
        print("2. View Leave Requests")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            apply_leave()

        elif choice == "2":
            view_leaves()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

 