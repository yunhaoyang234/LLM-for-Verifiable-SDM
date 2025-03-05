import openai
import os 
from openai import OpenAI

OPENAI_API_KEY = input("please enter your OpenAI API_Key:")

openai.api_key = OPENAI_API_KEY
openai_api_key = OPENAI_API_KEY

def gen_steps(model_path, task, max_steps=3):
	f = open(model_path)
	props = f.read()
	props = props[props.find('VAR')+3:]
	props = props[:props.find('ASSIGN')]
	f.close()

	prompt = 'Define ' + str(max_steps) + ' steps for ' + task + ' using the following varibles:\n'
	prompt += props

	client = OpenAI(api_key=openai_api_key)
	completion = client.chat.completions.create(
		model="gpt-4-0613", 
		messages=[ {"role": "user", "content": prompt} ],
		max_tokens=400, 
		temperature=0
	)
	print('\n\n========================LLM OUTPUT========================')
	print('==========================================================')
	print(completion.choices[0].message.content)
	print('==========================================================')
	print('==========================================================\n\n')
	return completion.choices[0].message.content

def text2automaton(steps, model_path, verbose=False):
	os.system('rm -rf NuSMV/temp')
	os.system('mkdir NuSMV/temp')
	fn = open(model_path)
	nusmv_pre = fn.read()

	prompt = 'Complete the following NuSMV: \n' + nusmv_pre +'\n'
	prompt += 'to indicate the following steps:\n' + steps

	client = OpenAI(api_key=openai_api_key)
	completion = client.chat.completions.create(
	      model="gpt-4-0613",
	      messages=[
	        {"role": "user", "content": prompt}
	      ],
	      max_tokens=400,
	      temperature=0
	)
	control = completion.choices[0].message.content
	control = control[control.find('ASSIGN')+6:]
	spec = control.find('SPEC')
	if spec > 0:
		control = control[:spec]
	nusmv = nusmv_pre + '\n' + control
	if verbose:
		print(nusmv)
	f = open('NuSMV/temp/task.smv', 'x')
	f.write(nusmv)
	f.close()
	return nusmv, control

def gen_automaton(task, model_path, verbose=False):
	os.system('rm -rf NuSMV/temp')
	os.system('mkdir NuSMV/temp')
	fn = open(model_path)
	nusmv_pre = fn.read()

	prompt = 'Complete the following NuSMV solving the task ' + task + ':\n' + nusmv_pre +'\n'

	client = OpenAI(api_key=openai_api_key)
	completion = client.chat.completions.create(
	      model="gpt-4o",
	      messages=[
	        {"role": "user", "content": prompt}
	      ],
	      max_tokens=1000,
	      temperature=0
	)
	control = completion.choices[0].message.content
	control = control[control.find('  init(Action)'):]
	spec = control.find('```')
	if spec > 0:
		control = control[:spec]
	nusmv = nusmv_pre + '\n' + control
	if verbose:
		print(nusmv)
		exit()
	f = open('NuSMV/temp/task.smv', 'x')
	f.write(nusmv)
	f.close()
	return nusmv, control, prompt

def text2code(steps, api_path, name):
	f_api = open(api_path)
	api = f_api.read()
	prompt = 'Define a Python function ' + name + '(class_instance) to indicate the following steps: \n' + steps 
	prompt += '\nUsing the provided APIs: \n' + api

	client = OpenAI(api_key=openai_api_key)
	completion = client.chat.completions.create(
	      model="gpt-4-0613",
	      messages=[
	        {"role": "user", "content": prompt}
	      ],
	      max_tokens=400,
	      temperature=0
	)
	code = completion.choices[0].message.content
	code = code[code.find('def'):]
	code = code[:code.find("```")]

	with open('output/'+name+'.py', mode="w") as f:
		f.write(code)
		f.close()

def controller2code(controller, api_path, name):
	f_api = open(api_path)
	api = f_api.read()
	prompt = 'Transform the following NuSMV to a Python function ' + name + '(class_instance):\n' + controller 
	prompt += '\nUsing the provided APIs: \n' + api

	client = OpenAI(api_key=openai_api_key)
	completion = client.chat.completions.create(
	      model="gpt-4-0613",
	      messages=[
	        {"role": "user", "content": prompt}
	      ],
	      max_tokens=400,
	      temperature=0
	)
	code = completion.choices[0].message.content
	code = code[code.find('def'):]
	code = code[:code.find("```")]

	with open('output/'+name+'.py', mode="w") as f:
		f.write(code)
		f.close()

# def main():
#     steps = gen_steps('examples/sample_model.smv', 'go straight at an intersection without traffic light', 3)
#     nusmv, control = text2automaton(steps, 'examples/sample_model.smv', False)
#     text2code(steps, 'examples/sample_api.py', 'CrossRoad')
#     controller2code(control, 'examples/sample_api.py', 'CrossRoad')

# if __name__ == "__main__":
#     main()
