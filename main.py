import pandas
import pandas as pd

data = pd.read_csv("./squirrel_dataset.csv")

black_squirrels_count=len(data[data["Primary Fur Color"] == "black"])
red_squirrels_count =len(data[data["Primary Fur Color"] == "red"])
grey_squirrels_count =len(data[data["Primary Fur Color"] == "grey"])
data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df= pandas.DataFrame(data)
df.to_csv()  #convert to csv file