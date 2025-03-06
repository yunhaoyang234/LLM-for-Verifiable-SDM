from LLM_Interaction import *
from ModelChecking import *
import numpy as np
import json

acts = ['go straight', 'turn left', 'turn right']
pos = ['traffic light', 'stop sign']

def get_train_data(size=10):
    data = []

    for i in range(size):
        task = acts[np.random.randint(len(acts))] + ' at ' + pos[np.random.randint(len(pos))]
        model_path, spec_path = 'examples/model.smv', 'examples/LTL.txt'

        nusmv, control, prompt = gen_automaton(task, model_path, verbose=False)
        automaton_path = 'NuSMV/temp/task.smv'
        model_checking(automaton_path, spec_path)
        num_fail = show_stats(verbose=False)
        print(num_fail)

        if num_fail < 8:
            data_point = {
                'messages': [
                    {
                        "role":"user",
                        "content": prompt
                    },
                    {
                        "role":"assistant",
                        "content": control
                    }
                ]
            }
            data.append(data_point)
    return data

def save_data(data):
    json_string = ''
    for d in data:
        json_str = json.dumps(d, separators=(',', ':'))
        json_string += json_str
        json_string += '\n'
    with open('examples/data.jsonl', 'w') as outfile:
        outfile.write(json_string)

def main():
    save_data(get_train_data())

if __name__ == '__main__':
    main()