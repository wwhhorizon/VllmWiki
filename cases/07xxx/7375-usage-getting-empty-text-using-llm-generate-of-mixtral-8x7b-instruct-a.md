# vllm-project/vllm#7375: [Usage]: Getting empty text using llm.generate of mixtral-8X7b-Instruct AWQ model

| 字段 | 值 |
| --- | --- |
| Issue | [#7375](https://github.com/vllm-project/vllm/issues/7375) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Getting empty text using llm.generate of mixtral-8X7b-Instruct AWQ model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a Mixtral-8x7B-Instruct-v0.1-AWQ . Its giving me empty text as generation. I am using the sample code from the model card:? from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?", ] prompt_template=f'''[INST] {prompt} [/INST]''' prompts = [prompt_template.format(prompt=prompt) for prompt in prompts] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ", quantization="awq", tensor_parallel_size=4) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") The output is always empty. Prompt: '[INST] Tell me about AI[/INST]', Generated text: '' Its working as expected for other models. Is there something i am missing while using this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: age]: Getting empty text using llm.generate of mixtral-8X7b-Instruct AWQ model usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run infere...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s generation. I am using the sample code from the model card:? from vllm import LLM, SamplingParams prompts = [ "Tell me about AI", "Write a story about llamas", "What is 291 - 150?", "How much wood would a woodchuck ch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: , top_p=0.95) llm = LLM(model="TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ", quantization="awq", tensor_parallel_size=4) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
