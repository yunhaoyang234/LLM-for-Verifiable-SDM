import openai
import os 

OPENAI_API_KEY = "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"

openai.organization = "org-6S5CZI9GpGCluYXm8Sl8zN8n"
openai.api_key = OPENAI_API_KEY

def gen_steps(model_path, task, max_steps=3):
	f = open(model_path)
	props = f.read()
	props = props[props.find('VAR')+3:]
	props = props[:props.find('ASSIGN')]
	f.close()

	prompt = 'Define ' + str(max_steps) + ' steps for ' + task + ' using the following varibles:\n'
	prompt += props
	completion = openai.ChatCompletion.create(
		model="gpt-4", 
		messages=[ {"role": "user", "content": prompt} ],
		max_tokens=200, 
		temperature=0
	)
	print('\n\n========================LLM OUTPUT========================')
	print('==========================================================')
	print(completion.choices[0].message["content"])
	print('==========================================================')
	print('==========================================================\n\n')
	return completion.choices[0].message["content"]

def text2automaton(steps, model_path, verbose=False):
	os.system('rm -rf NuSMV/temp')
	os.system('mkdir NuSMV/temp')
	fn = open(model_path)
	nusmv_pre = fn.read()

	prompt = 'Complete the following NuSMV: \n' + nusmv_pre +'\n'
	prompt += 'to indicate the following steps:\n' + steps

	completion = openai.ChatCompletion.create(
	      model="gpt-4",
	      messages=[
	        {"role": "user", "content": prompt}
	      ],
	      max_tokens=400,
	      temperature=0
	)
	control = completion.choices[0].message["content"]
	control = control[control.find('ASSIGN')+6:]
	nusmv = nusmv_pre + '\n' + control
	if verbose:
		print(nusmv)
	f = open('NuSMV/temp/task.smv', 'x')
	f.write(nusmv)
	f.close()
	return nusmv

def text2code(steps, api_path, name):
	f_api = open(api_path)
	api = f_api.read()
	prompt = 'Define a Python function ' + name + '(class_instance) to indicate the following steps: \n' + steps 
	prompt += '\nUsing the provided APIs: \n' + api
	completion = openai.ChatCompletion.create(
	      model="gpt-4",
	      messages=[
	        {"role": "user", "content": prompt}
	      ],
	      max_tokens=400,
	      temperature=0
	)
	code = completion.choices[0].message["content"]
	code = code[code.find('def'):]
	code = code[:code.find("```")]

	f = open('output/'+name+'.py', 'x')
	f.write(code)
	f.close()

def main():
    steps = gen_steps('examples/sample_model.smv', 'go straight at an intersection without traffic light', 3)
    nusmv = text2automaton(steps, 'examples/sample_model.smv', False)
    text2code(steps, 'examples/sample_api.py', 'CrossRoad')

if __name__ == "__main__":
    main()