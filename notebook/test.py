import pickle

with open('notebook/physics_answers.pkl', 'rb') as f:
    data = pickle.load(f)

print(data[1])



