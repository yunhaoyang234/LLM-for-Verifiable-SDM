# Generative Langauage Model for Verifiable Sequential Decision-Making

We design a pipeline to automatically generate natural language instructions for a given task, verify the instruction against user-provided specifications, and ground the instruction to real or simulated robots.


![pipeline](https://github.com/yunhaoyang234/LLM-for-Verifiable-SDM/blob/main/examples/pipeline.png)

Here is a visual demonstration of the pipeline:

![demo](https://github.com/yunhaoyang234/LLM-for-Verifiable-SDM/blob/main/examples/demonstration.png)

## Setup
```bash
$ pip install openai
```

## Instructions
1. Write down the description of the task in ```prompt.txt``` and save the txt file.

2. Provide a System_API file, a LTL.txt file with your task requirements in the form of linear temporal logic, and a Model.smv file to represent your system in NuSMV.

3. Run the following command:

```bash
$ python main.py \
         --task_name TaskName\
         --model_path path_to_Model.smv\
      	 --spec_path path_to_LTL.txt\
      	 --api_path path_to_System_API\
```

The terminal will output the verification outcomes and save the verification results in ```NuSMV/temp/```folder. The executable code will be saved to ```output/``` folder.

## References
[1] Y Yang, C Neary, U Topcu. Multimodal Pretrained Models for Verifiable Sequential Decision-Making: Planning, Grounding, and Perception. NeurIPS 2023 Foundation Models for Decision Making Workshop.

[2] Y Yang, JR Gaglione, C Neary, U Topcu. Large Language Models for Verifiable Sequential Decision-Making in Autonomous Systems. 2nd Workshop on Language and Robot Learning: Language as Grounding.

[3] Y Yang, NP Bhatt, T Ingebrand, W Ward, S Carr, Z Wang, U Topcu. Fine-Tuning Language Models Using Formal Methods Feedback. arXiv preprint.
