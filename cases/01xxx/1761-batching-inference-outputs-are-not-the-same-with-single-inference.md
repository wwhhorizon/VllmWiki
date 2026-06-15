# vllm-project/vllm#1761: Batching inference outputs are not the same with single inference

| 字段 | 值 |
| --- | --- |
| Issue | [#1761](https://github.com/vllm-project/vllm/issues/1761) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Batching inference outputs are not the same with single inference

### Issue 正文摘录

If I call the llm.generate with a batch prompts and greedy search, the output of batch inference is different to single batch inference. Is this right? A minimum reprodece script looks like this: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0) # Create an LLM. llm = LLM(model="/workdir/hf_models/llama-2-7b-chat-hf/", trust_remote_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") for prompt in prompts: print(prompt) outputs = llm.generate(prompt, sampling_params) for output in outputs: generated_text = output.outputs[0].text print(f"Generated text: {generated_text!r}") ``` ![image](https://github.com/vllm-project/vllm/assets/37237570/1e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: pling_params = SamplingParams(temperature=0) # Create an LLM. llm = LLM(model="/workdir/hf_models/llama-2-7b-chat-hf/", trust_remote_code=True) # Generate texts from the prompts. The output is a list of RequestOutput ob...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s right? A minimum reprodece script looks like this: ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e inference If I call the llm.generate with a batch prompts and greedy search, the output of batch inference is different to single batch inference. Is this right? A minimum reprodece script looks like this: ```python f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: te_code=True) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
