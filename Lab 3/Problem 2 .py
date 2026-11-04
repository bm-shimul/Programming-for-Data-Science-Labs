import pandas as pd

df = pd.read_csv('train.csv')

pd.set_option('display.max_columns', None)  
pd.set_option('display.width', 200)


print(" First Class Passengers (Pclass == 1) ")
first_class = df[df['Pclass'] == 1]
print(first_class.head(15))
print("Total first class passengers:", first_class.shape[0])


print("\n Passengers Younger than 18 ")
young = df[df['Age'] < 18]
print(young[['PassengerId', 'Name', 'Age', 'Sex', 'Survived']].head(15))
print("Total passengers under 18:", young.shape[0])


print("\n Male Passengers Who Survived ")
male_survived = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]
print(male_survived[['PassengerId', 'Name', 'Age', 'Pclass', 'Fare']].head(15))
print("Total male survivors:", male_survived.shape[0])


print("\n  Passengers with Fare > 100 ")
high_fare = df[df['Fare'] > 100]
print(high_fare[['PassengerId', 'Name', 'Pclass', 'Fare', 'Survived']].head(15))
print("Total passengers with Fare > 100:", high_fare.shape[0])