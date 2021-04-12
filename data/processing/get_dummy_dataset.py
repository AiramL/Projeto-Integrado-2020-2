from pickle import load
from pickle import dump


dummy_file = open("dataset_dummy","rb")
dictionary = load(dummy_file)

with open('..\\dataset.csv','r') as dataset:
    X = []
    first_line = True
    for line in dataset:
        if first_line:
            pass
        else:
            line_split = line[:-1].split(',')
            tmp = []
            for item in line_split:
                if item not in dictionary.keys():
                    if item != "":
                        tmp.append(item)
                    else:
                        tmp.append(0)
                else:
                    tmp.append(dictionary[item])
            X.append(tmp)
        first_line = False
with open("dataset_transformed","wb") as save:
    dump(X,save)
    
