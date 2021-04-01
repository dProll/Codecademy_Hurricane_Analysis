# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# 1
def damages_updated(damages):
    # Update Recorded Damages
    conversion = {"M": 1000000, "B": 1000000000}

    # Function do update the damages-list by the given value
    new_list = list()
    for damage in damages:
        if damage == "Damages not recorded":
            new_list.append(damage)
        if damage.find("M") != -1:
            new_list.append(float(damage[0:damage.find("M")]) * conversion["M"])
        if damage.find("B") != -1:
            new_list.append(float(damage[0:damage.find("B")]) * conversion["B"])
    return new_list


# test function by updating damages
test = damages_updated(damages)


# print(test)


# 2
# Create a Table
def create_dictionary(names, months, years, max_wind, areas, damages_updated, deaths):
    new_dict = {}
    for i in range(len(names)):
        new_dict[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_wind[i],
                              "Areas Affected": areas[i], "Damage": damages_updated[i], "Deaths": deaths[i]}
    return new_dict


# Create and view the hurricanes dictionary
hurricane = create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_updated(damages),
                              deaths)


# print(hurricane["Maria"])

# 3
# Organizing by Year
def year_dictionary(dictionary):
    hurricanes_by_year = dict()
    for hurricane in dictionary:
        current_year = dictionary[hurricane]['Year']
        current_hurricane = dictionary[hurricane]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_hurricane]
        else:
            hurricanes_by_year[current_year].append(current_hurricane)
    return hurricanes_by_year


# create a new dictionary of hurricanes with year and key
new = year_dictionary(hurricane)


# print(new[2005])

# 4
# Counting Damaged Areas
def counting_areas(dictionary):
    areas_dict = dict()
    for hurricane in dictionary.values():
        areas = hurricane["Areas Affected"]
        # print(areas)
        for area in areas:
            if area not in areas_dict:
                areas_dict[area] = 1
            else:
                areas_dict[area] += 1
    return areas_dict


# create dictionary of areas to store the number of hurricanes involved in
area = counting_areas(hurricane)


# print(area)

# 5
# Calculating Maximum Hurricane Count
def max_area_count(area_dictionary):
    saved_area = ""
    counter = 0
    for area, count in area_dictionary.items():
        if saved_area == "":
            saved_area = area
            counter = count
        if count > counter:
            saved_area = area
            counter = count
    return saved_area, counter


# find most frequently affected area and the number of hurricanes involved in
area, count = max_area_count(area)


# print(area + " was hit " + str(count) + " times by hurricanes.")

# 6
# Calculating the Deadliest Hurricane
def deaths(dictionary):
    death = list()
    hurricane = list()
    for count in dictionary.values():
        death.append(count["Deaths"])
        hurricane.append(count["Name"])
    zipped_list = list(zip(death, hurricane))
    max_value = max(zipped_list)
    return max_value


# find highest mortality hurricane and the number of deaths
max_death, hurricane_name = deaths(hurricane)


# print(f"The hurricane {hurricane_name} was the deadliest in history with {max_death} deaths")


# 7
# Rating Hurricanes by Mortality
def mortality_rate(dictionary):
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    for element in dictionary.values():
        # 1 Value
        if element["Deaths"] <= mortality_scale[1]:
            mortality_dict[1].append({"Name": element["Name"], "Month": element["Month"], "Year": element["Year"],
                                      "Max Sustained Wind": element["Max Sustained Wind"],
                                      "Areas Affected": element["Areas Affected"], "Damage": element["Damage"],
                                      "Deaths": element["Deaths"]})
        # 2 Value
        if element["Deaths"] > mortality_scale[1] and element["Deaths"] <= mortality_scale[2]:
            mortality_dict[2].append({"Name": element["Name"], "Month": element["Month"], "Year": element["Year"],
                                      "Max Sustained Wind": element["Max Sustained Wind"],
                                      "Areas Affected": element["Areas Affected"], "Damage": element["Damage"],
                                      "Deaths": element["Deaths"]})
        # 3 Value
        if element["Deaths"] > mortality_scale[2] and element["Deaths"] <= mortality_scale[3]:
            mortality_dict[3].append({"Name": element["Name"], "Month": element["Month"], "Year": element["Year"],
                                      "Max Sustained Wind": element["Max Sustained Wind"],
                                      "Areas Affected": element["Areas Affected"], "Damage": element["Damage"],
                                      "Deaths": element["Deaths"]})
        # 4 Value
        if element["Deaths"] > mortality_scale[3] and element["Deaths"] <= mortality_scale[4]:
            mortality_dict[4].append({"Name": element["Name"], "Month": element["Month"], "Year": element["Year"],
                                      "Max Sustained Wind": element["Max Sustained Wind"],
                                      "Areas Affected": element["Areas Affected"], "Damage": element["Damage"],
                                      "Deaths": element["Deaths"]})
        # 5 Value
        if element["Deaths"] > mortality_scale[4]:
            mortality_dict[5].append({"Name": element["Name"], "Month": element["Month"], "Year": element["Year"],
                                      "Max Sustained Wind": element["Max Sustained Wind"],
                                      "Areas Affected": element["Areas Affected"], "Damage": element["Damage"],
                                      "Deaths": element["Deaths"]})
    return mortality_dict


# categorize hurricanes in new dictionary with mortality severity as key
mort = mortality_rate(hurricane)


# print(mort[4])

# 8 Calculating Hurricane Maximum Damage
def biggest_damage(dictionary):
    cost = 0.0
    hurricane_name = ""
    for element in dictionary.values():
        if element["Damage"] == "Damages not recorded":
            continue
        elif cost == 0:
            cost = element["Damage"]
            hurricane_name = element["Name"]
        elif element["Damage"] > cost:
            cost = element["Damage"]
            hurricane_name = element["Name"]
    return hurricane_name, cost


# find highest damage inducing hurricane and its total cost
biggest_hurricane, biggest_cost = biggest_damage(hurricane)


# print(f"The hurricane {biggest_hurricane} caused the biggest damage of {biggest_cost} $")

# 9
# Rating Hurricanes by Damage
def hurricanes_by_damage(dictionary):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in dictionary:
        total_damage = dictionary[hurricane]["Damage"]
        if total_damage == "Damages not recorded" or total_damage == damage_scale[0]:
            hurricanes_by_damage[0].append(dictionary[hurricane])
        elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
            hurricanes_by_damage[1].append(dictionary[hurricane])
        elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
            hurricanes_by_damage[2].append(dictionary[hurricane])
        elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
            hurricanes_by_damage[3].append(dictionary[hurricane])
        elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
            hurricanes_by_damage[4].append(dictionary[hurricane])
        elif total_damage > damage_scale[4]:
            hurricanes_by_damage[5].append(dictionary[hurricane])
    return hurricanes_by_damage


# categorize hurricanes in new dictionary with damage severity as key

hurri = hurricanes_by_damage(hurricane)
print(hurri[5])