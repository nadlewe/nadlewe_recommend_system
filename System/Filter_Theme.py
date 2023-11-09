def filter_by_theme(places, theme):
    return [place for place in places if place['type'] == theme]
