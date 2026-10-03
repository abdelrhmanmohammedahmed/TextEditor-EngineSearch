from collections import deque
import os


class HistoryEdit:
    def __init__(self):
      self.ops_undo: list = list()
      self.ops_redo: list = list()
      self.text: str = ""
      
      #action_1 = {
      #  "type_op": "insert",
      #  "text": "hello",
      #  "position": 0,
      #  }

    def push(self, action: dict):

      
      self.ops_undo.append(action)
      self.ops_redo.clear()

  
    def undo(self):
      if not self.is_undo_available():
        print("Nothing To Undo")
        return
      
    # text undo ...
      action = self.ops_undo[-1]
      
      if "position" not in action:
        print("position is not in action")
        return

      if "text" not in action:
        print("text not in action")
        return
        
      pos = action["position"]
      
      match action["type_op"]:
      
        case "insert":

          
          length = len(action["text"])
          self.text = self.text[: pos] + self.text[pos+length:]
          
        case "delete":
                    
          self.text = self.text[: pos] + action["text"] + self.text[pos :]

      

      print("undo: "+self.text)

      
      self.ops_undo.pop()
      self.ops_redo.append(action)

      
    def redo(self):
      if not self.is_redo_available():
        print("Nothing To Redo")
        return
        

      action = self.ops_redo[-1]

      if "position" not in action:
        print("position is not in action")
        return

      if "text" not in action:
        print("text is not in action")
        return
        
      pos = action["position"]

      match action["type_op"]:
        case "insert":

                      
          self.text = self.text[: pos] + action["text"] + self.text[pos :]

        case "delete":
          
                  
          length = len(action["text"])
          self.text = self.text[: pos] + self.text[pos+length :]

      
      print("redo: "+self.text)

      
      self.ops_redo.pop()
      self.ops_undo.append(action)

    def clear_history(self):
      self.ops_undo.clear()
      self.ops_redo.clear()

    def is_undo_available(self):
      return bool(self.ops_undo)

    def is_redo_available(self):
      return bool(self.ops_redo) # Class History Save Operations Happens To Text To Undo, Redo

    def set_text(self,text):
      self.text = text

    def get_text(self):
      return self.text

    def reset_text(self):
      self.text = ""

    # ---------------------------------------------
  
    def search(self, search_word: str):
      if search_word not in self.text:
        print("Word Is Not In Text")
        return

      places = list()
      pos = 0

      count_w = self.text.count(search_word)
      for _ in range(count_w):
        places.append(self.text.find(search_word, pos))
        pos = places[-1] +1

      print(f"Word: {search_word} {count_w} Time{'s' if count_w > 1 else ''} In: {places}")
      



class Notifications:
  
  def __init__(self):
    self.messages: deque = deque()
    self.path = "Notifications.txt"

  

  def add_notification(self,notification:str):
    self.messages.append(notification)
    print(self.messages)

  def delete_notification(self, notification:str):
    if notification in self.messages:
      self.messages.remove(notification)
      print(self.messages)
    

  def show_all_notifications(self):
    for msg in self.messages:
      print(msg)

  def clear(self):
    self.messages.clear()

    
  def show_last(self, n: int):
    if n <= 0:
      return
    elif n > len(self.messages):
      print(f"Num Of Notifications Is {len(self.messages)}")
      return

    start = max(0, len(self.messages) - n)  # 0 if 0 > len(self.messages) - n else len(self.messages) - n
    for i in range(start, len(self.messages)):
      print(self.messages[i])

  def has_notifications(self) -> bool:
    return bool(self.messages)

  def save_messages(self, path_file = None):
    if path_file is None:
      path_file = self.path


    with open(path_file,"w") as file:
      file.write("\n".join(self.messages))

  def load_messages(self,path_file = None):
    if path_file is None:
      path_file = self.path
    try:
      with open(path_file, "r") as file:
        self.messages = deque(file.read().splitlines())

    except FileNotFoundError:
      print("File Is Not Found")
      self.messages = deque()


