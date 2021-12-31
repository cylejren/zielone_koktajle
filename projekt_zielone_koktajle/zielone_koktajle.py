#!/usr/bin/python3

import csv

def prepare_csv():

    file = open("index_zielone_koktajle.csv", encoding = 'utf-8')
    fh = csv.reader(file)
    csv_data = list(fh)

    # removing commas from the csv lists
    for lista in csv_data:
        for item in lista.copy():
            if item == "":
                lista.remove(item)

    return csv_data


def get_ing_from_csv():
    # return complete dictionary of ingredients and theirs corresponding sites from CSV file

    csv_data = prepare_csv()
    ingredients_dict = {}

    # creating dictionary:key - ingredient, value - sites
    for ingredients_list in csv_data:
        ingredients_dict.setdefault(ingredients_list[1], ingredients_list[2:])
    # print(csv_data)
    return ingredients_dict


def result(ingredients_sites_list, count):
    # return common sites from the list of sites from given ingredients
    # count - nuber of ingredients

    result = []

    for site in ingredients_sites_list:
        if ingredients_sites_list.count(site) == count:
            if site in result:
                continue
            result.append(site)

    return result


def main_loop():
    ingredients_dict = get_ing_from_csv()

    # list of sites from given ingredients
    ingredients_sites_list = []
    count = 0
    
    while True:
        #adding ingredients sites to the list
        ing = input("Podaj składnik lub wciśnij 'K' aby zakończyć: ")
        if ing in "Kk":
            break
        if ing not in ingredients_dict.keys():
            print("'{}' nie wysteępuje w bazie".format(ing.capitalize()))
            continue
        ingredients_sites_list.extend(ingredients_dict.get(ing))
        print(">>> Składnik '{}' został dodany".format(ing))
        count += 1

    return result(ingredients_sites_list, count)


if __name__ == "__main__":
    # print("Zobacz strony: {}".format(main_loop()))
    print(get_ing_from_csv())