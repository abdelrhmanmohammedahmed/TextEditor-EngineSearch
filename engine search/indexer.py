import os
from pathlib import Path
from utils import remove_common_words, normalize_word, save_indexes



class Indexer:
  def __init__(self):
    self.index = dict()
    self.exts = {".txt"}
    self.forbid_folders_or_files = ("__pycache__",".git","venv (deactivated)",".agents",".config",".upm",".pythonlibs",".local")
    

  def read_file(self, path_file:str):
    """read file and get words and clean it from common words"""
    if not path_file:
      return []
   
    try:
      with open(path_file,'r',encoding="utf-8") as file:
        return remove_common_words(file.read())
    except (FileNotFoundError,UnicodeDecodeError,PermissionError):
      return []
    
    

  def index_files(self, path="."):
    """this function indexes the files to get words' information like file which found in ,num times said in"""
    
    for tupl in os.walk(path):
      
      for forbid_f in self.forbid_folders_or_files:
        
        if forbid_f in tupl[1]:
          tupl[1].remove(forbid_f)
      
      for i in [ os.path.join(tupl[0],file) for file in tupl[2] ]:

        self.index_single_file(i)

    save_indexes(self.index)
    self.reset_indexing()
    

  def index_single_file(self, i):
        """get words from read of file and normalize the words"""
        path_identfier = Path(i)
        if not path_identfier.is_file():
          return
        if path_identfier.suffix not in self.exts:
          return
        
        read = list(map(lambda x: normalize_word(x), self.read_file(i)))

    
        for word in read:
          if word not in self.index:
            self.index[word] = {i:1}

          else:
            if i not in self.index[word]:
              self.index[word][i] = 1
            else:
              self.index[word][i] += 1



  def set_index(self, value: dict):
    self.index = value
    

  def reset_indexing(self):
    self.index = dict()


