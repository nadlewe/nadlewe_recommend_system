def filter_by_cuisine(places, cuisine):
    return [place for place in places if place['cuisine'] == cuisine]
