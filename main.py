"""Homework project tracking system for projects."""

# region Imports
import os
from db import init_db, add_project, get_project, get_all_projects, update_project, delete_project
# endregion

# region Functions


def clear_terminal():
	"""Clear the terminal screen on Windows, macOS, or Linux."""
	os.system('cls' if os.name == 'nt' else 'clear')
# endregion

# region Main Function


def main():
	"""Main function for project tracking system."""
	# Initialise the database
	init_db()
	# Loop to simulate continuous operation until user decides to exit
	while True:
		clear_terminal()
		print("Project Tracking System")
		print("-----------------------")
		print("Menu:")
		print("1. Add Project")
		print("2. View Projects")
		print("3. Update Project")
		print("4. Delete Project")
		print("0. Exit")

		# Get user choice and handle invalid input
		try:
			choice = int(input("Enter choice: "))
		except ValueError:
			print("Invalid input! Please enter a valid integer.")
			input("Press Enter to continue...")
			continue

		match choice:
			case 1:
				clear_terminal()
				print("Add New Project")
				print("----------------")
				name = input("Project Name: ")
				description = input("Project Description: ")
				status = input("Project Status: ")
				add_project(name, description, status)
				print("Project added successfully!")
				input("Press Enter to continue...")
			case 2:
				clear_terminal()
				print("View Projects")
				print("--------------")

				# ask user if they want to view all projects or a specific one and handle invalid input
				try:
					id = int(input("Enter Project ID to view (or 0 to view all): "))
				except ValueError:
					print("Invalid input! Please enter a valid integer.")
					input("Press Enter to continue...")
					continue

				if id == 0:
					projects = get_all_projects()
					for project in projects:
						output = (f"Project ID: {project[0]}\r\n"
								  f"Name: {project[1]}\r\n"
								  f"Description: {project[2]}\r\n"
								  f"Status: {project[3]}\n"
								  "----------------")
						print(output)
				else:
					project = get_project(id)
					if project:#
						output = (f"Project ID: {project[0]}\r\n"
								  f"Name: {project[1]}\r\n"
								  f"Description: {project[2]}\r\n"
								  f"Status: {project[3]}")
						print(output)
					else:
						print("Project not found.")
						
				input("Press Enter to continue...")

			case 3:
				print("Update Project selected.")
				# Placeholder for updating project logic
				input("Press Enter to continue...")
			case 4:
				print("Delete Project selected.")
				# Placeholder for deleting project logic
				input("Press Enter to continue...")
			# exit case
			case 0:
				print("Exiting the program.")
				break
			# case for invalid choices
			case _:
				print("Invalid choice! Please try again.")
				input("Press Enter to continue...")
# endregion

# Run the main function
if __name__ == "__main__":
	main()
