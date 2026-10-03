from .additions import HistoryEdit,Notifications
import os


class TextEditor:
  def __init__(self):
    self.text: str = ""
    self.file_path = "file.txt"
    self.history_edit:HistoryEdit = HistoryEdit()
    self.notifications:Notifications = Notifications()

    self.history_edit.set_text(self.text)
    


  
  def insert_text(self, text:str, position = -1):
    
    if abs(position) > len(self.text) +1:
      print("Invalid Position")
      return

    
    if position == -1:
      position = len(self.text)
      self.text += text

    elif position < -1:
      position = len(self.text) + 1 - abs(position)

      self.text = self.text[: position] + text + self.text[position :]

    else:
      self.text = self.text[:position] + text + self.text[position :]
      
    
    action = {
      "type_op":"insert",
      "text":text,
      "position":position
             }
    self.history_edit.push(action=action)
    self.history_edit.set_text(self.text)
    print(self.text)

  
  def delete_text(self, text: str, position: int = -1):
    
    if text not in self.text:
      print(f"Text Not in {self.text}")
      return

    if not self.text:
      print("There No Text To Delete")
      return
      
      
    if abs(position) > len(self.text) +1:
      print("Invalid Position")
      return

      
    
    if position < 0: 
      position = len(self.text) - abs(position)


    if not self.text.startswith(text,position):
      print(f"Text Does Not Match Text Which at Position {position}")
      return


    length = len(text)
    

    if length + position > len(self.text):
      print("Invalid Position Or Text")
      return

    #user = input(f"The Text You Want To Delete Is: {self.text[position: position+length +1]}, Are You Sure('yes' or 'no')? ")

  
    #if user.lower() == "yes":
      #print("Deleted")

    #else:
      #print("Closed Delete")
      #return

    self.text = self.text[: position] + self.text[position+length :]

      
    action = {
      "type_op":"delete",
      "text":text,
      "position":position,
    }
    
    self.history_edit.push(action= action)
    print(self.text)
    self.notifications.add_notification("Deleted")
    self.history_edit.set_text(self.text)

  
  def show_text(self):
    print(self.text if self.text else "(empty)")
    

  
  def clean_file(self, file_path = None):
    if file_path is None:
      file_path = self.file_path
    
    if os.path.exists(file_path):
      with open(file_path, "w") as file:
        print("File Is Cleaned")
        file.write("")

    else:
      print("File Is Not Found")

  def undo(self):
    if self.history_edit.is_undo_available():
      self.history_edit.undo()
      self.text = self.history_edit.get_text()

    else:
      print("Undo Is Not Available, You Did Not Do Any Action \n\n")

  

  def redo(self):
    if self.history_edit.is_redo_available():
      self.history_edit.redo()
      self.text = self.history_edit.get_text()

    else:
      print("Redo Is Not Available, You Did Not Do Any Undo \n\n")

  def save(self,file_path = None, mode= "a"):
    if file_path is None:
      file_path = self.file_path


    try:
      with open(file_path, mode) as file:
        file.write(self.text)

      print("Text Is Saved")

    except (PermissionError,OSError):
      print("the file is unwriteable")

  def load(self, file_path = None):
    if file_path is None:
      file_path = self.file_path
      
    try:
      with open(file_path, "r") as file:
        print("Text Is Loaded")
        self.text = file.read()
        

    except FileNotFoundError:
      print("File Is Not Found")
      self.text = ""

    self.history_edit.set_text(self.text)
    self.history_edit.clear_history()
    

  def quit(self):
    user = input("Do You Want To Save ('yes' or 'no')? ").lower()    
    if user != "yes":
      return
      
    path = input("What Path Do You Want Save In ( Or Skip By Press 'Enter')")
    if not path:
      path = self.file_path
      
    print(f"Path File: {path}")
    self.save(path)
    self.history_edit.clear_history()
    self.text = ""

  # ---------------------------------------------------------

  def search(self, search_word: str):
    if not self.text:
      print("There Is No Text For Search")
      return
      
    if search_word not in self.text:
      print("SEARCH: Word Is Not In Text")
      return

    places = list()
    pos = 0

    count_w = self.text.count(search_word)
    for _ in range(count_w):
      places.append(self.text.find(search_word, pos))
      pos = places[-1] +1

    #print(f"Word: {search_word} {count_w} Time{'s' if count_w > 1 else ''} In: {places}")
    return (2, places)

  def replace(self, old: str, new_str: str):
    if old not in self.text:
      print(f"REPLACE: Word {old} Is Not In Text")
      return
    try:
      count = int(input("Type Num Of Replaces Of The Word (or -1 to replace all)(or Enter To Cancel): "))

    except (TypeError,ValueError):
      print("Wrong Input")
      return 

    if not count:
      print("Cancelled")
      return
      
    elif count != -1 :
      
      if count > self.text.count(old):
        print("Num Is Over What Is Found")
        return
      elif count < -1 or count == 0:
        print("Num Invalid")
        return
        
      
    self.text = self.text.replace(old, new_str, count)
    
    self.history_edit.set_text(self.text)
    
    print("Word Is Replaced")

  def word_count(self):
    if not self.text:
      return 0

    return len(self.text.split())

  def char_count(self):
    if not self.text:
      return 0

    return len(self.text)

  def lines_count(self):
    if not self.text:
      return 0

    return len(self.text.split("\n"))
      
    
