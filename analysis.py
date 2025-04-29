import pandas as pd
from pathlib import Path

# Define the data path
data_path = Path("Data") / "2023LFSData.csv"
df = pd.read_csv(data_path)

# Create a new CSV with only the California data 
california_df = df[df["SFA_STATE"] == "CA"]
california_df.to_csv("california_data.csv", index=False)

num_rows = california_df.shape[0]
print(f"Number of CA SFAs that answered to the survey: {num_rows}")

# Count the numbers under the columns
num_schools_sum = california_df['NUM_SCHOOLS'].sum()
num_students_sum = california_df['NUM_STUDENTS'].sum()

# Print the counts
print(f"Count of NUM_SCHOOLS: {num_schools_sum}")
print(f"Count of NUM_STUDENTS: {num_students_sum}")

# Create a new CSV with only data about whether schools are using local food in the National School Lunch Program
NSL_columns_to_include = [
    "SFA_NAME", "Q7_A1C1", "Q7_A1C2", "Q7_A1C3", "Q7_A1C4"
    ]
NSL_df = california_df[NSL_columns_to_include]

NSL_new_column_names = {
        "Q7_A1C1": "Never",  
        "Q7_A1C2": "Did before SY 2022-23",  
        "Q7_A1C3": "Did in SY 2022-23", 
        "Q7_A1C4": "Doing in SY 2023-24"   
    }

NSL_df.rename(columns=NSL_new_column_names, inplace=True)
NSL_df.replace({0.0: 'no', 1.0: 'yes'}, inplace=True)
NSL_df.to_csv("local-food-in-NSL.csv", index=False)
df = pd.read_csv("local-food-in-NSL.csv")

# How many SFAs said they have never used local food in their NSLP?
yes_count = df["Never"].value_counts().get("yes", 0)  
no_count = df["Never"].value_counts().get("no", 0)  
print(f"Number of SFAs that have never served local produce in their lunch: {yes_count}")
print(f"Number of SFAs that have served local produce in their lunch: {no_count}")


