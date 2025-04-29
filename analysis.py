import pandas as pd
from pathlib import Path

# Define the data path
data_path = Path("Data") / "2023LFSData.csv"

# Check if the file exists
if not data_path.exists():
    print(f"Error: The file {data_path} does not exist.")
else:
    # Load the CSV
    df = pd.read_csv(data_path)

    # Verify column names
    print("Columns in the CSV:", df.columns)

    # Filter for California rows
    california_df = df[df["SFA_STATE"] == "CA"]

    # Display the first few rows
    print(california_df.head())

    # Save California data to CSV
    california_df.to_csv("california_data.csv", index=False)

    # List of columns to include
    NSL_columns_to_include = [
       "SFA_NAME", "Q7_A1C1", "Q7_A1C2", "Q7_A1C3", "Q7_A1C4"
    ]

    # Select only the columns you want from the dataframe
    selected_columns_df = california_df[NSL_columns_to_include]

    new_column_names = {
        "Q7_A1C1": "Never",  # Replace with your desired column name
        "Q7_A1C2": "Did before SY 2022-23",  # Replace with your desired column name
        "Q7_A1C3": "Did in SY 2022-23",  # Replace with your desired column name
        "Q7_A1C4": "Doing in SY 2023-24"   # Replace with your desired column name
    }

selected_columns_df.rename(columns=new_column_names, inplace=True)
selected_columns_df.replace({0.0: 'no', 1.0: 'yes'}, inplace=True)

    # Save the selected columns with new names to a new CSV file
selected_columns_df.to_csv("local-food-in-NSL.csv", index=False)

df = pd.read_csv("local-food-in-NSL.csv")

# Count how many people said 'yes' for New_Column_1
yes_count = df["Never"].value_counts().get("no", 0)  # Default to 0 if "yes" is not present

# Print the result
print(f"Number of people who said 'yes' for Never: {yes_count}")


