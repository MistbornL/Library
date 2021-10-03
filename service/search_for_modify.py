def search_to_modify(target, id_to_modify, title, genre):
    for item in target:
        if item['ID'] == id_to_modify:
            item['title'] = title
            item['genre'] = genre