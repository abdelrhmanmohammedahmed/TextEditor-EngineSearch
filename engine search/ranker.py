
class Ranker:

    def rank(self, index:dict):
        """the sort-1 sorts 'index' according to num of times is said in the files  ||||||||||||||||||  the sort-2 'index' according to num of files that the word said in"""

        
        

        if not index:
            return dict()

        
        index =    dict( sorted(
                index.items(),
                key=lambda item: sum([ item[1][file] for file in item[1] ]),
                reverse=True,
            ))
        
        
        index = dict( sorted( index.items(), key=lambda item: len(item[1]) ) )

    

        return index


if __name__ == "__main__":
  print(__name__+":")
  print(Ranker().rank({'program': {'doc2.txt': 2}, 'pythoni': {'doc1.txt': 1}, 'python': {'doc2.txt': 2, 'doc1.txt': 1}}))


