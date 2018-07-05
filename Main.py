# locations
start_point = ["Gweonid", "Lilyut", "Dewstone"]
end_point = ["Solzreed"]
locations = []
locations = locations + start_point
locations = locations + end_point

# pack choice
lil_packs = ["Lilyut Hills Milk Soap", "Lilyut Cooking Oil"]
gwe_packs = ["Gweonid Dyed Feathers", "Gweonid Apple Pie"]
dew_packs = ["Dewstone Fine Thread", "Dewstone Distilled Liquor"]

packs = []
packs = packs + lil_packs
packs = packs + gwe_packs
packs = packs + dew_packs

# prices
gwe_solz_dy_price = 15.9
gwe_solz_ap_price = 14.38
lil_solz_mi_price = 10.79
lil_solz_co_price = 10.27
dew_solz_fi_price = 12.02 #ajutine
dew_solz_di_price = 11.92 #ajutine

materials = ["Gilda", "Orchard Puree", "Goose Down", " Chopped Produce", "Apple", "Ground Spices", "Milk", " Dried Flowers", "Olive", "Chopped Produce", "Milk", "Ground Grain", "Fig"]
amount = [1, 100, 40, 50, 30, 70, 35, 20]

print(start_point)


def input_location_and_validate(user_notification):
    # küsida kasutajalt asukoht
    # tõstutundlikuseta otsing asukohtadest
    # kui kui leidis, siis tagastab asukoha
    # kui ei leidnud või leidis mitu, siis viskame vea
    user_input = input(user_notification)
    user_input_lower = user_input.lower()

    selected_location = []
    for location in locations:
        location_lower = location.lower()
        # kui user_input_lower string on leitav location lower-ist, siis lisa see asukoht selecte_location-ite alla
        if location_lower.find(user_input_lower) != -1:
            selected_location.append(location)
    if len(selected_location) == 0:
        print('No locations found')
        exit()
    if len(selected_location) > 1:
        print('multiple locations selected: ' + ','.join(selected_location))
        exit()
    return selected_location[0]

def input_packs_and_validate(user_notification):
    user_input = input(user_notification)
    user_input_lower = user_input.lower()

    selected_pack = []
    for pack in packs:
        pack_lower = pack.lower()
        # kui user_input_lower string on leitav location lower-ist, siis lisa see asukoht selecte_location-ite alla
        if pack_lower.find(user_input_lower) != -1:
            selected_pack.append(pack)
    if len(selected_pack) == 0:
        print('No packs found')
        exit()
    if len(selected_pack) > 1:
        print('multiple packs selected: ' + ','.join(selected_pack))
        exit()
    return selected_pack[0]

def input_location_and_validate_2(user_notification):
    return input_and_validate(user_notification, locations, 'locations')

def input_packs_and_validate_2(user_notification):
    return input_and_validate(user_notification, packs, 'packs')

def input_and_validate(user_notification, elements, name):
    user_input = input(user_notification)
    user_input_lower = user_input.lower()

    selected_element = []
    for element in elements:
        element_lower = element.lower()
        if element_lower.find(user_input_lower) != -1:
            selected_element.append(element)
    if len(selected_element) == 0:
        print('No ' + name + ' found')
        exit()
    if len(selected_element) > 1:
        print('multiple ' + name + ' selected: ' + ','.join(selected_element))
        exit()
    return selected_element[0]

def ma_ei_tea_mis_ma_teen_1( mats, mat, route, num, nums):
    #pridi toode
    #kasutaja saab sisestada selle hinna
    print("Fill in the current prices for 1 material")
    inputi = float(input(mats))
    inputo = float(input(mat))
    numi = float(num)
    numo = float(nums)
    result = route - inputi * numi - inputo * numo
    print("You will get:", result)

def ma_ei_tea_mis_ma_teen_2():
    return ma_ei_tea_mis_ma_teen_1( materials[11], materials[12],dew_solz_fi_price, amount[5], amount[2])



start = input_location_and_validate('Enter your trip start location: ')
print('Start from: ' + start)
end = input_location_and_validate('Enter your trip end location: ')
print('Destination: ' + end)

# info
error = ('Either you wrote your location wrong or that location does not exist! Start location: ' + start + ' end location: ' + end)

if start == start_point[0] and end == end_point[0]:
    print(gwe_packs)
    gwe_choose = input_packs_and_validate('Choose your pack: ')

    # Gweonid Dyed Feathers
    if gwe_choose == gwe_packs[0]:
        print("Fill in the current prices for 1 material")
        print("Gilda")
        gwe_puree = float(input("Orchard Puree"))
        gwe_down = float(input("Goose down"))
        print(gwe_solz_dy_price)
        gwe_solz_dy = gwe_solz_dy_price - gwe_puree * 100 - gwe_down * 40
        print("You will get:", gwe_solz_dy)

    # Gweonid Apple Pies
    elif gwe_choose == gwe_packs[1]:
        # [] koostisosadest
        # [] koostisosade hulgast
        print("Fill in the current prices for 1 material")
        gwe_meat = float(input("Trimmed meat"))
        gwe_grape = float(input("Grape"))
        # print (gwe_solz_ap_price)
        gwe_solz_ap = gwe_solz_ap_price - gwe_meat * 30 - gwe_grape * 30
        print("You will get:", gwe_solz_ap)

    else:
        print("That pack does not exist")



# Lilyutist solzreedi
elif start == start_point[1] and end == end_point[0]:
    print(lil_packs)
    lil_choose = input_packs_and_validate('Choose your pack: ')

    # Lilyut Hills Milk Soap
    if lil_choose == lil_packs[0]:
        print("Fill in the current prices for 1 material")
        print("Gilda")
        lil_spice = float(input("Ground Spices"))
        lil_milk = float(input("Milk"))
        # print (lil_solz_mi_price)
        lil_solz_mi = lil_solz_mi_price - lil_spice * 70 - lil_milk * 35
        print("You will get:", lil_solz_mi)

    # Lilyut Cooking Oil
    elif lil_choose == lil_packs[1]:
        print("Fill in the current prices for 1 material")
        lil_flowers = float(input("Dried Flowers"))
        lil_olive = float(input("Olive"))
        # print (lil_solz_co_price)
        lil_solz_co = lil_solz_co_price - lil_flowers * 50 - lil_olive * 20
        print("You will get:", lil_solz_co)

    else:
        print("That pack does not exist")

elif start == start_point[2] and end == end_point[0]:
    print(dew_packs)
    dew_choose = input_packs_and_validate('Choose your pack: ')

    if dew_choose == dew_packs[0]:
        ma_ei_tea_mis_ma_teen_2()

    elif dew_choose == dew_packs[1]:
        pass

    else:
        print("That pack does not exist")
else:
    print(error)
# Gweonidist Solzreedi
