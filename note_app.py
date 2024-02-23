import os

# Define data structure for a note
class Note:
  def __init__(self, title, content):
    self.title = title
    self.content = content

# Data storage (replace with a persistent option in production)
notes = []

def show_help():
  print("\nAvailable commands:")
  print("add <title> <content>  - Add a new note")
  print("list                   - List all note titles")
  print("view <title>           - View content of a specific note")
  print("delete <title>         - Delete a note")
  print("quit                   - Exit the application")

def add_note(title, content):
  notes.append(Note(title, content))
  print(f"Note '{title}' added successfully!")

def list_notes():
  if not notes:
    print("You have no notes yet.")
  else:
    print("\nYour notes:")
    for note in notes:
      print(note.title)

def view_note(title):
  for note in notes:
    if note.title == title:
      print(f"\nNote: {title}")
      print(note.content)
      return
  print(f"No note found with title '{title}'.")

def delete_note(title):
  for i, note in enumerate(notes):
    if note.title == title:
      del notes[i]
      print(f"Note '{title}' deleted successfully!")
      return
  print(f"No note found with title '{title}'.")

def main():
  print("\nWelcome to your CLI Note-Taking App!")
  show_help()

  while True:
    command = input("\nEnter command: ").lower().split()

    if not command:
      continue

    if command[0] == "add":
      if len(command) < 3:
        print("Usage: add <title> <content>")
      else:
        add_note(command[1], " ".join(command[2:]))
    elif command[0] == "list":
      list_notes()
    elif command[0] == "view":
      if len(command) < 2:
        print("Usage: view <title>")
      else:
        view_note(command[1])
    elif command[0] == "delete":
      if len(command) < 2:
        print("Usage: delete <title>")
      else:
        delete_note(command[1])
    elif command[0] == "quit":
      print("Exiting... Goodbye!")
      break
    else:
      print("Invalid command. Please see 'help' for available commands.")
      show_help()

if __name__ == "__main__":
  main()
