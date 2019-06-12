import pandas as pd 
import os
import json
import statistics

def calculate_average_grade_from_csv(my_csv_filepath):
    dataframe = pd.read_csv(my_csv_filepath)
    avg = dataframe['final_grade'].mean()
    return avg
    #list comprehension follow along
    # rows = df.to_dict(dataframe)
    # grades = [r['final_grade] for r in rows]

# def calculate_average_grade_from_json(my_json_filepath):
#     with open(my_json_filepath, "r") as f:
#         file_contents = f.json_read()  
#     gradebook = json.load(file_contents)
#     print(gradebook)

def calculate_average_grade_from_json(x):
    #breakpoint()

    with open(x, "r") as f:
        print(type(f))
        file_contents = f.read()
        print(type(file_contents)) #> str

    gradebook = json.loads(file_contents)
    students = gradebook['students']
    grades = [r['finalGrade'] for r in students]
    avg_grade = statistics.mean(grades)
    return avg_grade


    #json_avg = json_dataframe['final_grade'].mean()
    #return json_avg

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
                                    #(os.path.dirname gets directory of this file hence __file__)
                        # os.path.join = joins the following commands > .. = go up > data changes to data 
    json_gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.json")

    #print(calculate_average_grade_from_csv(gradebook_filepath))
    print(calculate_average_grade_from_json(json_gradebook_filepath))