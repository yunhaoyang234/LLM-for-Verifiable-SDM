from LLM_Interaction import *
from ModelChecking import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--task_name', type=str, default='CrossRoad')
parser.add_argument('--task_description', type=str, default='go straight at an intersection without traffic light')
parser.add_argument('--model_path', type=str, default='examples/sample_model.smv')
parser.add_argument('--spec_path', type=str, default='examples/sample_ltl.txt')
parser.add_argument('--api_path', type=str, default='examples/sample_api.py')

def main(args):
	task = args.task_description
	model_path, spec_path, api_path = args.model_path, args.spec_path, args.api_path
	f = open('prompt.txt')
	prompt = f.read()
	if len(prompt) > 1:
		task = prompt
	steps = gen_steps(model_path, task, 3)
	nusmv = text2automaton(steps, model_path, False)
	text2code(steps, api_path, args.task_name)

	automaton_path = 'NuSMV/temp/task.smv'
	model_checking(automaton_path, spec_path)
	show_stats()

if __name__ == '__main__':
    main(parser.parse_args())