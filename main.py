from engine_search.EngineSearch import EngineSearch
from argparse import ArgumentParser


def main():

    try:
  
      parser = ArgumentParser(description="Engine Search")
      engine = EngineSearch()




      parser.add_argument("-i","--index",help= "For Indexing The Folder You Want",type=str)


      parser.add_argument("-s","--search",help="For Searching Word You Want",type=str)


      args = parser.parse_args()

    
      if args.index:
        engine.indexing(args.index)
      else:
        print("You Typed Nothing To Index")
        return
  
      if args.search:
        print( engine.search_text(args.search) )
      else:
        print("You Type Nothing To Search")
        return
        
    except KeyboardInterrupt:
      print("exit...")
      exit(0)
    
      

if __name__ == "__main__":
  main()
