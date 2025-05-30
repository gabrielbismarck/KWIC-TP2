def read_file(file_path: str) -> list[str]:
    return open(file_path, encoding='utf-8').read().splitlines()

def keyword_title_tuple_generator(titles: list[str], stop_words: list[str]) -> list[tuple[str, str]]:
    keyword_title_tuple = []
    for lines in titles:
        words = lines.lower().split()
        for keyword in words:    
            if keyword not in stop_words:
                keyword_title_tuple.append((keyword, lines))
    return keyword_title_tuple

def circular_shift(keyword: str, title: str) -> str:
    words = title.lower().split()
    if keyword not in title:
        return title
    
    index = words.index(keyword)
    shifted = words[index:] +words[:index]
    return ' '.join(shifted)

file = read_file('input.txt')
stop_words = read_file('stop_words.txt')
keyword_title_tuple = keyword_title_tuple_generator(file, stop_words)

for keyword, title in keyword_title_tuple:
    shifted = circular_shift(keyword, title)
    print(f'2) circular shift: {shifted}')
    print()
