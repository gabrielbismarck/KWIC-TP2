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

def lower_stop_words(stop_words: list[str]) -> list[str]:
    return [word.lower() for word in stop_words]

def circular_shift(keyword: str, title: str) -> str:
    words = title.lower().split()
    if keyword not in words:
        return title
    
    index = words.index(keyword)
    shifted = words[index:] +words[:index]
    return ' '.join(shifted)

def generate_shifted( keyword_title_tuple: list[tuple[str, str]]) -> list[tuple[str, str]]:
    shifted = []
    for keyword, title in keyword_title_tuple:
        shifted.append((circular_shift(keyword, title), title))

    return shifted

def sort_shifted(shifted: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return sorted(shifted, key=lambda x: x[0].lower())

def print_shifted(sort_shifted: list[tuple[str, str]]) -> None:
    for shifted_title, title in sort_shifted:
        print(f'{shifted_title}\t\t\tfrom {title}')

def main ():
    file = read_file('input.txt')
    stop_words = read_file('stop_words.txt')
    stop_words = lower_stop_words(stop_words)
    keyword_title_tuple = keyword_title_tuple_generator(file, stop_words)
    shifted = generate_shifted(keyword_title_tuple)
    list_sort_shifted = sort_shifted(shifted)
    print_shifted(list_sort_shifted)
    
  
if __name__ == '__main__':
    main()
