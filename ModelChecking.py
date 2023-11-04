import os
import argparse

def model_checking(automaton_path, spec_path):
    os.system('rm -rf NuSMV/temp')
    os.system('mkdir NuSMV/temp')
    spec_file = open(spec_path)
    specs = []
    while True:
        spec = spec_file.readline()
        if len(spec) > 1:
            specs.append(spec)
        if len(spec) == 0:
            break
    command = 'read_model -i '+automaton_path+'\ngo\n'
    idx = 1
    for spec in specs:
        name = '\"' + spec.split(' ')[2] + '\"'
        cmd = 'check_ltlspec -P ' + name + ' -o NuSMV/temp/result' + str(idx) + '.txt \n' 
        command += cmd
        idx += 1
    command += 'quit'
    f = open('NuSMV/temp/script.csh', 'x')
    f.write(command)
    f.close()
    os.system('NuSMV/bin/NuSMV -source NuSMV/temp/script.csh')

def show_stats():
    files = os.listdir('NuSMV/temp/')
    results = []
    for f in files:
        if 'result' in f:
            results.append('NuSMV/temp/' + f)
    result_text = ''
    for r in results:
        f = open(r)
        text = f.read()
        result_text += text + '\n\n'
    num_fails = result_text.count('false')
    print('\n\n' + result_text)
    print('======================Summary=======================')
    print('====================================================')
    print(str(len(results) - num_fails) + ' of ' + str(len(results)) + ' specifications are satisfied.')
    print('====================================================')
    print('====================================================' + '\n\n')

def main():
    automaton_path = 'examples/sample_fsa.smv'
    spec_path = 'examples/sample_ltl.txt'
    model_checking(automaton_path, spec_path)
    show_stats()

if __name__ == "__main__":
    main()