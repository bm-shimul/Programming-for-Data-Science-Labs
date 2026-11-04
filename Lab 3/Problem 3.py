import pandas as pd      #Shimul Bishwas

df = pd.read_csv('train.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)


print(" Top 10 Passengers by Highest Fare ")
top_fare = df.sort_values(by='Fare', ascending=False).head(10)
print(top_fare[['PassengerId', 'Name', 'Pclass', 'Fare', 'Survived']])


print("\n Average Passenger Age ")
avg_age = df['Age'].mean()
print(f"Average Age: {avg_age:.2f} years")


print("\n Male vs Female Count ")
gender_counts = df['Sex'].value_counts()
print(gender_counts)

print("\n Average Fare by Passenger Class ")
avg_fare_by_class = df.groupby('Pclass')['Fare'].mean()
print(avg_fare_by_class.round(2))


print("\n Survival Rate by Passenger Class ")
survival_by_class = df.groupby('Pclass')['Survived'].mean()
print(survival_by_class.round(4))
print("\nIn percentage:")
print((survival_by_class * 100).round(2).astype(str) + ' %')