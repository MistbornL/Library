def append_data(item, library, target):
    data = {"title": item.title, "genre": item.genre, "ID": item.id}
    library[target].append(data)
