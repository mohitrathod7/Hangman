def get_word():

    import random

    words = ["BELLIGERENT", "COLLATERAL", "FOSTERING", "VERMONT", "WICHITA", "IMPEDE", "PERNICIOUS", "SUPERFLUOUS",
             "INFIDEL", "EPIDEMIOLOGIST", "TRANSGRESSION", "SUBPOENA", "GRATUITIES", "UNSOLICITED", "LEGITIMATE",
             "NEBRASKA", "TRANQUILITY", "FIBROSIS", "VERACITY", "SOUVENIR", "GLENDALE", "VIETNAM", "MAURITANIA",
             "LESOTHO", "GOA", "KOLLOOR", "COLOMBO", "VELLORE", "AHMEDABAD", "RUN", "URI", "LEH", "KULLU", "AVENGERS",
             "MUMBAI", "BYCULLA", "MOHAMMAD", "GUILT", "GELATIN", "GLUTTEN", "MANGALYAAN", "CHANDRAYAAN", "SPUTNIK",
             "DRIZZLE", "MANCHESTER", "LEONARDO", "KRISHNA", "HYPOCRATUS", "PYTHAGORAS", "ATHNIANS", "SPARTANS", "SUN",
             "GANESHA", "VISHNU", "MAHAVIR", "INTERSTELLAR", "DESPERATE", "KANGAROO", "POLICE", "AMBULANCE", "HOME",
             "HOUSE", "COLONY", "AMBEDKAR", "CAR", "TIN", "PIN", "GYM", "SET", "WET", "YASH", "FAR", "FEAR", "DEAR",
             "IN", "OR", "AS", "AT", "WHERE", "HOW", "MUCH", "WHEN", "WAS", "TOSS", "DIE", "GUY", "BAR", "MARK",
             "ZUCKERBERG", "APPLE", "GOOGLE", "MICROSOFT", "NOKIA", "OUT", "NOT", "HOT", "CLUTCH", "GRANULES", "KING"
             ]

    # print(len(words))

    return random.choice(words).upper()
