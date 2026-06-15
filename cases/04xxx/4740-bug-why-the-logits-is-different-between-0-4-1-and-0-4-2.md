# vllm-project/vllm#4740: [Bug]: why the logits is different between 0.4.1 and 0.4.2

| 字段 | 值 |
| --- | --- |
| Issue | [#4740](https://github.com/vllm-project/vllm/issues/4740) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: why the logits is different between 0.4.1 and 0.4.2

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0, max_tokens=2048) llm = LLM(model="Llama-3-8B",tensor_parallel_size=4, trust_remote_code=True) outputs = llm.generate(prompts=prompts, sampling_params=sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(prompt + generated_text) ``` I use vllm 0.4.1 and 0.4.2 run this code, and I print logits in sampler.py, but I found the logits is different between 0.4.1 and 0.4.2 when the tensor_parallel_size is 4, but is the same when tensor_parallel_size is 2 or 1. **TP4 first token logits:** 0.4.2 ![image](https://github.com/vllm-project/vllm/assets/71002153/313484a2-3a60-4b91-8243-ada4b49a864f) 0.4.1 ![image](https://github.com/vllm-project/vllm/assets/71002153/20906e58-5568-4cc1-9dc1-4dbd15789c8b) **TP2 first token logits:** 0.4.2 ![image](https://github.com/vllm-project/vllm/assets/71002153/871fb6ce-238b-4752-8adb-f64267302e46) 0.4.1 ![image](https://github.com/vllm-project/vllm/assets/71002153/6c874e36-c90e-47f5-a7af-2f0ec4e6e78e)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mpling_params = SamplingParams(temperature=0, max_tokens=2048) llm = LLM(model="Llama-3-8B",tensor_parallel_size=4, trust_remote_code=True) outputs = llm.generate(prompts=prompts, sampling_params=sampling_params) for ou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ut of `python collect_env.py` ``` ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0, max_tokens=2048) llm = LLM(model="Llama-3-8B",tensor_parallel_size=4, tru...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: why the logits is different between 0.4.1 and 0.4.2 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ``` from vllm import LLM, SamplingParams samplin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
