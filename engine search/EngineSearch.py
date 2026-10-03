# import nltk, wonderwords,random_word

from .indexer import Indexer

from .searcher import Searcher


class EngineSearch:
  def __init__(self):
    self.indexer: Indexer = Indexer()
    self.searcher: Searcher = Searcher()
    

  def search_text(self, text:str):
    return self.searcher.search_word(text)

  def indexing(self, path_folder:str = "."):
    
    self.indexer.index_files(path_folder)


