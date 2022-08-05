import pandas

data = pandas.read_csv("../csv_related/2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_ones = len(data[data["Primary Fur Color"] == "Gray"])
black_ones = len(data[data["Primary Fur Color"] == "Black"])
red_ones = len(data[data["Primary Fur Color"] == "Cinnamon"])

sq_data = {
    "color" : ["Gray","Black","Cinnamon"],
    "count" : [gray_ones,black_ones,red_ones]
}

new_data = pandas.DataFrame(sq_data)
new_data.to_csv("squirrel-count.csv")