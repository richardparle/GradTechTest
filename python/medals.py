medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]


def createMedalTable(results):

    medal_table = {}

    medalists = []
    first_place = []
    second_place = []
    third_place = []

    # Place each medalist into "medalists" array
    for event in results:
        for country in event['podium']:
            medalists.append(country)

    # Seperate 1st, 2nd and 3rd into seperate arrays and remove first 2 characters
    for medalist in medalists:
        if medalist.startswith('1'):
            first_place.append(medalist[2: len(medalist)])
        if medalist.startswith('2'):
            second_place.append(medalist[2: len(medalist)])
        if medalist.startswith('3'):
            third_place.append(medalist[2: len(medalist)])

    # Check if country exists in table, if it does then increament the value by the relavent amount, if not then add it.
    for country in first_place:
        if country in medal_table:
            medal_table[country] += 3
        else:
            medal_table[country] = 3

    for country in second_place:
        if country in medal_table:
            medal_table[country] += 2
        else:
            medal_table[country] = 2

    for country in third_place:
        if country in medal_table:
            medal_table[country] += 1
        else:
            medal_table[country] = 1

    return medal_table


def test_function():
    # This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
