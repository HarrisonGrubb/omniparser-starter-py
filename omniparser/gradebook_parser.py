import pandas as pd 
import os

def calculate_average_grade_from_csv(my_csv_filepath):
    dataframe = pd.read_csv(my_csv_filepath)
    avg = dataframe['final_grade'].mean()
    return avg
    #list comprehension follow along
    # rows = df.to_dict(dataframe)
    # grades = [r['final_grade] for r in rows]

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")

    calculate_average_grade_from_csv(gradebook_filepath)