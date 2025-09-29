import pandas as pd
from io import StringIO

# Titanic-like dataset (20 rows)
data_csv = """
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Fare,Embarked
1,0,3,Braund Mr. Owen Harris,male,22,1,0,7.25,S
2,1,1,Cumings Mrs. John Bradley (Florence Briggs Thayer),female,38,1,0,71.28,C
3,1,3,Heikkinen Miss. Laina,female,26,0,0,7.92,S
4,1,1,Futrelle Mrs. Jacques Heath (Lily May Peel),female,35,1,0,53.10,S
5,0,3,Allen Mr. William Henry,male,35,0,0,8.05,S
6,0,3,Moran Mr. James,male,27,0,0,8.46,Q
7,0,1,McCarthy Mr. Timothy J,male,54,0,0,51.86,S
8,0,3,Palsson Master. Gosta Leonard,male,2,3,1,21.08,S
9,1,3,Johnson Mrs. Oscar W (Elisabeth Vilhelmina Berg),female,27,0,2,11.13,S
10,1,2,Nasser Mrs. Nicholas (Adele Achem),female,14,1,0,30.07,C
11,1,3,Sandstrom Miss. Marguerite Rut,female,4,1,1,16.70,S
12,1,1,Bonnell Miss. Elizabeth,female,58,0,0,26.55,S
13,0,3,Saundercock Mr. William Henry,male,20,0,0,8.05,S
14,0,3,Andersson Mr. Anders Johan,male,39,1,5,31.28,S
15,0,3,Vestrom Miss. Hulda Amanda Adolfina,female,14,0,0,7.85,S
16,1,2,Hewlett Mrs. (Mary D Kingcome),female,55,0,0,16.00,S
17,0,3,Rice Master. Eugene,male,2,4,1,29.13,Q
18,1,2,Williams Mr. Charles Eugene,male,23,0,0,13.00,S
19,0,3,Vander Planke Mrs. Julius (Emelia Maria Vandemoortele),female,31,1,0,18.00,S
20,1,3,Masselmani Mrs. Fatima,female,22,0,0,7.23,C
"""

# Create DataFrame
titanic_sample = pd.read_csv(StringIO(data_csv))

# Preview dataset
print(titanic_sample.head())

print(titanic_sample.describe(include='all'))
print(titanic_sample['Sex'].value_counts())
