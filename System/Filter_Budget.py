def filter_by_budget(places, budget):
    return [place for place in places if place['average_cost'] <= budget]
