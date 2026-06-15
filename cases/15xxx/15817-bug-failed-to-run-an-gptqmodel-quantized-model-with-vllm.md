# vllm-project/vllm#15817: [Bug]:  Failed to run an GPTQModel quantized model with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#15817](https://github.com/vllm-project/vllm/issues/15817) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Failed to run an GPTQModel quantized model with vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug code: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.6, top_p=0.9) # Create an LLM. llm = LLM(model="InternVL2_5-4B-MPO-4bit") # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` error: ```error ERROR 03-31 21:19:53 [core.py:343] EngineCore hit an exception: Traceback (most recent call last): ERROR 03-31 21:19:53 [core.py:343] File "/usr/local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 335, in run_engine_core ERROR 03-31 21:19:53 [core.py:343] engine_core = EngineCoreProc(*args, **kwargs) ERROR 03-31 21:19:53 [core.py:343] File "/usr/local/lib/python3.10/site-packages/vllm/v1/e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Failed to run an GPTQModel quantized model with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug code: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my nam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Failed to run an GPTQModel quantized model with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug code: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my nam...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: urrent environment ### 🐛 Describe the bug code: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Failed to run an GPTQModel quantized model with vLLM bug;stale ### Your current environment ### 🐛 Describe the bug code: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my nam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
