# vllm-project/vllm#2103: When sampling multiple times, the results tend to become significantly longer.

| 字段 | 值 |
| --- | --- |
| Issue | [#2103](https://github.com/vllm-project/vllm/issues/2103) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When sampling multiple times, the results tend to become significantly longer.

### Issue 正文摘录

``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(n=16, temperature=0.8, max_tokens=500) # Create an LLM. llm = LLM(model="facebook/opt-125m") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. generated_texts = [] for output in outputs: sample_one = [] for out in output.outputs: sample_one.append(out.text) # print(f"Sample: {repr(out.text)}") # print("-"*30) generated_texts.append(sample_one) # Print the average length of the generated texts. generated_lengths = [[] for _ in range(len(generated_texts[0]))] for samples in generated_texts: for idx in range(len(samples)): generated_lengths[idx].append(len(samples[idx].split())) for idx, lengths in enumerate(generated_lengths): print(idx, sum(lengths)/len(lengths)) ``` ``` 0 189.75 1 197.75 2 78.0 3 174.25 4 141.75 5 164.0 6 393.5 7 289.25 8 352.25 9 307.5 10 379.5 11 38...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s(n=16, temperature=0.8, max_tokens=500) # Create an LLM. llm = LLM(model="facebook/opt-125m") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: le times, the results tend to become significantly longer. ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /opt-125m") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
