import pandas as pd

###########################Class Data#############################

Class = pd.read_csv("animal_classes.csv", delimiter=",")
print(Class.shape)

########################Training Data#############################

train = pd.read_csv("animals_train.csv", delimiter=",")
print(train.shape)

training_data = [
    "hair",
    "feathers",
    "eggs",
    "milk",
    "airborne",
    "aquatic",
    "predator",
    "toothed",
    "backbone",
    "breathes",
    "venomous",
    "fins",
    "legs",
    "tail",
    "domestic",
    "catsize",
]
target_data = ["class_number"]

print(training_data, target_data)

########################Testing Data#############################

test = pd.read_csv("animals_test.csv", delimiter=",")

target_test = ["animal_name"]

print(test.shape)

##################Create Conversion Dictionary####################

convert = {}
x = 0

for i in Class.Class_Number:
    convert[x + 1] = Class.Class_Type[x]
    x += 1

print(convert)

############################Traning##############################

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X=train[training_data], y=train[target_data])

predicted = knn.predict(test[training_data])
expected = test[target_test]
print(predicted)
print(expected)

##################Finish Conversion Dictionary####################

convert_final = {"animal_name": "prediction"}
animal_names = test["animal_name"]
x = 0

for n in predicted:
    convert_final[animal_names[x]] = convert[n]
    x += 1

print(convert_final)

#########################Produce CSV#############################

with open("Results.csv", "w") as file:
    for key in convert_final.keys():
        file.write("%s,%s\n" % (key, convert_final[key]))
