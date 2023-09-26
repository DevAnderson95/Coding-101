my_dict ={
    "name": "Troy Aikmen",
    "position": "QB",
    "team": "Dallas Cowboys",
    "age": 54,
    "weight": 220.,
    "superbowls":["XXVII","XXVIII","XXX"],
    "awards":{
        "superbowl_mvp":"XXVII",
        "probowl":[1991, 1992, 1993, 1994, 1995, 1996],
        "man_of_the_year": 1997

    }
}
print(type(my_dict["team"]))
print(type(my_dict["awards"]))
print(my_dict["awards"]["probowl"][-2])
print(
    my_dict['name'] + " has won ", len(my_dict["superbowls"]))

a_list = []
for k, v in my_dict["awards"].items():
    if k == "superbowl_mvp" or k == "man of the year":
        a_list.append(v)
print(a_list)