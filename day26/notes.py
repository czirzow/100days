# notes on list comprehension.
import pandas

if 0:
    numbers = [1, 2, 3]
    new_list = [i + 1 for i in numbers]
    print(new_list)

    name = "Curt"
    new_list = [c for c in name]
    print(new_list)

    print([i * 2 for i in range(1, 5)])

if 0:
    #new_dict = {key:value for item in list}
    #new_dict = {key:value for (key,value) in dict.items() if test}
    import random
    names = ['Alex', 'Beth', 'Curt']
    scores = {name:random.randint(1,100) for name in names }
    print(scores)
    passed = {k:v for (k,v) in scores.items() if v > 60 }
    print(passed)

if 0:
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    result = {w:len(w) for w in sentence.split() }
    print(result)

if 0:
    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
    def c_to_f(c):
        return (c * 9 / 5) + 32
    weather_f = {w:c_to_f(c) for (w, c) in weather_c.items()}

if 1:
    student_dict = {
            'student': ['Angela', 'James', 'Lily'],
            'score': [56, 76, 98]
            }
    student_data_frame = pandas.DataFrame(student_dict)
    #print(student_data_frame)

    #Loop throught data frame
    #for (key, value) in student_data_frame.items():
    #    print(f"{key}: {value}")

    #for (index, row) in student_data_frame.iterrows():
        #print(index)
        #if row.student == 'Angela':
            #print(f"{row.student}: {row.score}")

    result = {
            r.student:r.score
            for r in student_data_frame.iterrows()
            if r.student == 'Angela'
            }
    print(f"result: {result}")


