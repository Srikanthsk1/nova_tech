import os
import json

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)

def list_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        for title in notes:
            print(title)

def view_note(notes, title):
    if title in notes:
        print(f"\nTitle: {title}\n{'='*30}\n{notes[title]}\n{'='*30}")
    else:
        print(f"Note '{title}' not found.")

def add_note(notes, title, content):
    notes[title] = content
    save_notes(notes)
    print(f"Note '{title}' added successfully.")

def delete_note(notes, title):
    if title in notes:
        del notes[title]
        save_notes(notes)
        print(f"Note '{title}' deleted successfully.")
    else:
        print(f"Note '{title}' not found.")

def main():
    notes = load_notes()

    while True:
        print("\nCommand options:")
        print("1. List all notes (list)")
        print("2. View a note (view <title>)")
        print("3. Add a new note (add <title> <content>)")
        print("4. Delete a note (delete <title>)")
        print("5. Exit the application (exit)")

        user_input = input("Enter your command: ").split()

        if user_input[0] == "list":
            list_notes(notes)
        elif user_input[0] == "view" and len(user_input) == 2:
            view_note(notes, user_input[1])
        elif user_input[0] == "add" and len(user_input) >= 3:
            title = user_input[1]
            content = " ".join(user_input[2:])
            add_note(notes, title, content)
        elif user_input[0] == "delete" and len(user_input) == 2:
            delete_note(notes, user_input[1])
        elif user_input[0] == "exit":
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
