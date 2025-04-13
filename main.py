def log_to_file(path, message):
    with open(path, 'a') as file:
        print(message, file=file)

class Node:
    def __init__(self):
        self.next = {}
        self.matches = []
        self.link = None

def create_automaton(words):
    root = Node()

    for word in words:
        curr = root
        for ch in word:
            curr = curr.next.setdefault(ch, Node())
        curr.matches.append(word)

    queue = []
    for child in root.next.values():
        queue.append(child)
        child.link = root

    log_to_file('values/while1.txt', 'before while ' + str(bool(queue)))
    while queue:
        curr = queue.pop(0)
        for ch, child in curr.next.items():
            queue.append(child)
            fallback = curr.link
            log_to_file('values/while2.txt', 'before while ' + f'{str(bool(fallback))}    {ch not in fallback.next}')
            while fallback and ch not in fallback.next:
                fallback = fallback.link
            log_to_file('values/while2.txt', 'after while ' + str(bool(fallback)))
            log_to_file('values/if1.txt', str(bool(fallback)))
            if fallback:
                child.link = fallback.next[ch]
            else:
                child.link = root
            child.matches += child.link.matches

    return root

def search_text(text, keywords):
    root = create_automaton(keywords)
    found = {word: [] for word in keywords}
    curr = root

    for i, ch in enumerate(text):
        log_to_file('values/while3.txt', 'before while ' + f'{str(bool(curr))}    {ch not in curr.next}')
        while curr and ch not in curr.next:
            curr = curr.link
        log_to_file('values/while3.txt', 'after while ' + str(bool(curr)))
        log_to_file('values/if2.txt', str(bool(curr)))
        if not curr:
            curr = root
            continue
        curr = curr.next[ch]
        for word in curr.matches:
            found[word].append(i - len(word) + 1)

    return found