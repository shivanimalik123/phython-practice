# import pandas as pd
# data = [100,200,300]
# series = pd.Series(data)
# print(series)

# import pandas as pd
# data = [100,200,300]
# series = pd.Series(data,index=["a","b","c"])
# print(series)

# import pandas as pd
# data = [100,200,300]
# series = pd.Series(data,index=["a","b","c"])
# print(series.to_string(index=False))

# import pandas as pd
# data = [100,200,300]
# series = pd.Series(data)
# print(series.to_string(index=False))

# import pandas as pd
# data = [5,10,15,20]
# series = pd.Series(data)
# print(series)

# import pandas as pd 
# data = (1,2,3,4)
# series = pd.Series(data)
# print(series.iloc[1])

# import pandas as pd
# data = {
#     "A":10,
#     "B":20,
#     "C":30
# } 
# series = pd.Series(data)
# print(series.loc["B"])

# import pandas as pd
# data = {
#     "A":10,
#     "B":20,
#       "C":30
# }
# series = pd.Series(data)
# series.loc["C"]=35
# print(series)

# import pandas as pd
# data =[5,10,15,20]
# series = pd.Series(data)
# print(series[series>=20]) 

# import pandas as pd
# data = {
#     "Name":["Shivani","Anshu","Rittu"],
#     "Marks":[85,90,75]
# }
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = {
#     "Name":["Shivani","Anshu","Rittu"],
#     "Marks":[85,90,75]
# }
# df = pd.DataFrame(data)
# print(df.head(2))


# import pandas as pd
# data = {
#     "Name":["Shivani","Anshu","Rittu"],
#     "Marks":[85,90,75]
# }
# df = pd.DataFrame(data)
# print(df.tail(1))

# import pandas as pd
# data = {
#     "Name":["Shivani","Anshu","Rittu"],
#     "Marks":[85,90,75]
# }
# df = pd.DataFrame(data)
# print(df.shape)

# print(df.columns)

# print(df.dtypes)

# df.info()

# print(df.describe())

# print(df["Name"])

# print(df[["Name","Marks"]])

# print(df.loc[1])

# print(df.iloc[2])

# print(df[df["Marks"]>80])

# print(df.sort_values("Marks"))

# df["Grade"]=["A","A+","B"]
# print(df)

# df.to_csv("students.csv",index=False)
# print("File Saved Successfully")

# ASSIGNMENT
import pandas as pd
df = pd.DataFrame([
    ["Aman",85],
    ["Shivani",81],
    ["Ritesh",80],
    ["Anshu",79],
    ["Vinay",60],
], columns=["Name","Marks"])
# print(df)

# print(df.head(3))

# print(df.tail(2))

# print(df["Marks"])

# print(df[["Name","Marks"]])

# print(df.loc[1])

# print(df.iloc[2])

# print(df.shape)

# print(df.columns)

# print(df.dtypes)

# print(df.sort_values("Marks",ascending=False))

# df["City"] = ["Delhi","Rohtak","Hisar","Kathura","Chhichhrana"]
# print(df)

# df = df.drop("City",axis=1)
# print(df)

# df = pd.DataFrame([
#     ["Aman",None],
#     ["Shivani",81],
#     ["Ritesh",80],
#     ["Anshu",None],
#     ["Vinay",60],
# ], columns=["Name","Marks"])
# print(df)