from utils import load_indexes, normalize_word
from .ranker import Ranker

class Searcher:
  
  def __init__(self):
    self.index = dict()
    self.rank: Ranker = Ranker()
    
  
  def search_word(self, word: str):
    
    self.index = load_indexes()
    
    if not self.index:
      return []
    
    find_words = dict()
    word = normalize_word(word.strip())

    
    for i in self.index:
      if word in i:
        find_words[i] = self.index[i]

    return self.rank.rank(find_words)




if __name__ == "__main__":

  print(Searcher().search_word("p"))
