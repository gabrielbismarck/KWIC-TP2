import pytest 
from KWIC import keyword_title_tuple_generator, circular_shift

@pytest.fixture
def input_data():
    titles = [
        "The quick brown fox",
        "A brown cat sat",
        "The cat is brown"
    ]
    stop_words = ["the", "a", "is"]
    return titles, stop_words

def test_stop_word_removal(input_data):
  titles, stop_words = input_data
  result = keyword_title_tuple_generator(titles, stop_words)
  
  keywords = [keyword for keyword, _ in result]
  
  for stop in stop_words:
    assert stop not in keywords
  
  for word in ["quick", "brown", "fox", "cat", "sat"]:
    assert word in keywords
    
def test_circular_shift():
    keyword = "quick"
    title = "The quick brown fox"
    shift = circular_shift(keyword, title)
    assert shift == "quick brown fox The"

    title2 = "A brown cat sat"
    keyword2 = "brown"
    shift2 = circular_shift(keyword2, title2)
    assert shift2 == "brown cat sat A"

    keyword_not_in_title = "banana"
    shift3 = circular_shift(keyword_not_in_title, title)
    assert shift3 == "The quick brown fox" 
