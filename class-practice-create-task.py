res_list = ["McDonalds", "In N Out", "Panda Express", "Subway", "Coldstone", "PHS Cafeteria"]

new_res = input("What restaurant would you like to add to the list? ")

def rank_res(new_res, res_list):

    for i in range(len(res_list)):

        rank = input("Do you like A) " + new_res + " or B)" + res_list[i] + " more? A/B ")
        
        if rank == "A":
            res_list.insert(i, new_res)
            return res_list

        elif rank == "B":
            continue

    res_list.append(new_res)
    return res_list

print("Your new ranking is: ", rank_res(new_res, res_list))