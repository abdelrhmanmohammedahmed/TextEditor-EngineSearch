import json

from string import punctuation
from pathlib import Path
from json import JSONDecodeError


common_words = set({
    
        "a",
        "an",
        "the",
        "is",
        "are",
        "i",
        "you",
        "we",
        "they",
        "he",
        "she",
        "it",
        "in",
        "on",
        "at",
})

prefixes = ["dis", "un", "im"]
suffixes_v = ["ied", "ies", "ing", "ed", "es", "s"]
#suffixes_ = ["ation", "able", "ful", "er"]
exts = (".txt",".json",".md")

path = "indexes.json"

def get_path():
  return Path(path).resolve()



  
def remove_common_words(text: str):
    
    li: list[str] = [x.strip(punctuation) for x in text.split()]
    li = list(filter(lambda x: x.lower() not in common_words and x, li))

    return li


def normalize_word(word: str):
    if not len(word) > 2:
        return word.lower()

    w = word.lower()

    for i in prefixes:
        if w[: len(i)] in prefixes:
            w = w[len(i) :]
            break

    for i in suffixes_v:
        if w[-1 * len(i) : len(w)] in suffixes_v:
            w = w[: -1 * len(i)]

            if len(w) > 3:
                if w[-1] == w[-2]:
                    w = w[: len(w) - 1]
            break

    if len(w) < 2:
        return word.lower()

    return w.lower()


def load_indexes() -> dict:
    try:
        with open(get_path(), "r", encoding="utf-8") as file:
            return json.load(file)

    except (FileNotFoundError, UnicodeDecodeError, PermissionError,JSONDecodeError):
        return dict()


def save_indexes(indexes: dict):
    if not indexes:
        return False
    try:
        
      with open(get_path(), "w", encoding="utf-8") as file:
          json.dump(indexes, file, indent=4)
          return True
    except (PermissionError, OSError):
        
        return False
    



def set_path(p:str, ext=".txt"):
    global path
    
    if not p.endswith(exts):
        p += ext


    path = p


