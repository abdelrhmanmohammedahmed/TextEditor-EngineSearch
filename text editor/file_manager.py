import os, shutil


class FileManager:
  
  def create_folder(self, name: str, path:str = os.getcwd()):

    if path != os.getcwd():
      if not os.path.exists(path):
        print("The Path Is Not Exists")
        return False
    

    
    path = os.path.join(path,name)

    if os.path.exists(path):
      print(f"Folder '{name}' Is Already Exists")
      return False

    os.mkdir(path)
    print("Folder Created")

    return True

  def create_file(self, name: str, path = os.getcwd(), ext=".txt"):
    if path != os.getcwd():
      if not os.path.exists(path):
        print("Path Is Not Found")
        return False

    name += ext
    path = os.path.join(path,name)
    if os.path.exists(path):
      print("File Is Already Exists")
      return False

    with open(path, 'w') as file:
      file.write("")

    
    print("File Created")
    return True
                
  def remove_folder(self, name: str, path = os.getcwd()):

    if path != os.getcwd():
      if not os.path.exists(path):
        print("Path Is Not Found")
        return False

    path = os.path.join(path,name)
    if not os.path.exists(path):
      print("Folder Is Not Found")
      return False

    if not os.listdir(path):
      os.rmdir(path)

    else:
      user = input("Folder May Have Data, Are You Sure You Want Remove It ('yes' or 'no') ? ").lower()
      if user == 'yes':
        shutil.rmtree(path)
        print("Deleted")
        

      else:
        print("Closed")

    return True
    

  def remove_file(self, name, path = os.getcwd(), ext=".txt"):
    if path != os.getcwd():
      if not os.path.exists(path):
        print("Path Is Not Found")
        return

    name += ext

    path = os.path.join(path,name)

    if not os.path.exists(path):
      print("File Is Not Exists")
      return False

    os.remove(path)

    return True

