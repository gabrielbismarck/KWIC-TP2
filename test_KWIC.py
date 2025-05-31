import pytest 
from KWIC import keyword_title_tuple_generator, circular_shift

@pytest.fixture
def sample_data():
  titulos = [
    "O poder da mente",
    "A força do hábito"
  ]
  stop_words = ["o", "a", "da", "do"]
  return titulos, stop_words

def test_stop_word_removal(sample_data):
  titulos, stop_words = sample_data
  result = keyword_title_tuple_generator(titulos, stop_words)
  
  keywords = [keywords for keyword, _ in result]
  
  for stop in stop_words:
    assert stop not in keywords
  
  for word in ["poder", "mente", "força", "hábito"]:
    assert word in keywords
    
def test_circular_shift():
    keyword = "poder"
    title = "O poder da mente"
    shift = circular_shift(keyword, title)
    assert shift == "poder da mente o"

    keyword2 = "mente"
    shift2 = circular_shift(keyword2, title)
    assert shift2 == "mente o poder da"

    keyword_not_in_title = "energia"
    shift3 = circular_shift(keyword_not_in_title, title)
    assert shift3 == "O poder da mente" 
