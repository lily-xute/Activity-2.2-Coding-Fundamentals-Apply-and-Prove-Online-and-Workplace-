"""Homework project tracking system for projects."""

#region Imports
import os
#endregion

#region Functions
def clear_terminal():
	"""Clear the terminal screen on Windows, macOS, or Linux."""
	os.system('cls' if os.name == 'nt' else 'clear')
#endregion

#region Main Function
def main():
	"""Main function for project tracking system."""
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
		choice = input("Enter choice: ")

		match choice:
			case 1:
				print("Add Project selected.")
				# Placeholder for adding project logic
				input("Press Enter to continue...")
			case 2:
				print("View Projects selected.")
				# Placeholder for viewing projects logic
				input("Press Enter to continue...")
			case 3:
				print("Update Project selected.")
				# Placeholder for updating project logic
				input("Press Enter to continue...")
			case 4:
				print("Delete Project selected.")
				# Placeholder for deleting project logic
				input("Press Enter to continue...")
			case 0:
				print("Exiting the program.")
				break
			case _:
				print("Invalid choice! Please try again.")
				input("Press Enter to continue...")
#endregion

# Run the main function
if __name__ == "__main__":
	main()
