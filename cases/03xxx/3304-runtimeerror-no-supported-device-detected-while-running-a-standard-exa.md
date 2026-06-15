# vllm-project/vllm#3304: RuntimeError: No supported device detected, while running a standard example

| 字段 | 值 |
| --- | --- |
| Issue | [#3304](https://github.com/vllm-project/vllm/issues/3304) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: No supported device detected, while running a standard example

### Issue 正文摘录

Trying to run this standard example ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="facebook/opt-125m") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Or any other way to use vllm gives this error ```bash (nvenv) (nvenv) [prince@pc minimal-flask-api]$ python3 test.py Traceback (most recent call last): File "/home/prince/Desktop/task/minimal-flask-api/test.py", line 33, in llm = LLM(model="facebook/opt-125m") ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/prince/Desktop/task/minimal-flask-api/nvenv/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEn...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="facebook/opt-125m") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: andard example Trying to run this standard example ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /opt-125m") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s error ```bash (nvenv) (nvenv) [prince@pc minimal-flask-api]$ python3 test.py Traceback (most recent call last): File "/home/prince/Desktop/task/minimal-flask-api/test.py", line 33, in llm = LLM(model="facebook/opt-125...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
