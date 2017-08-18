def extractPurchases(events):
    purchases = []

    for event in events:
        if event.type == 'purchase':
            purchases = purchases + [event]

    return purchases
