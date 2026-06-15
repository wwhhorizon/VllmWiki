# vllm-project/vllm#5495: [Bug]:  ray not work when tp>=2

| 字段 | 值 |
| --- | --- |
| Issue | [#5495](https://github.com/vllm-project/vllm/issues/5495) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  ray not work when tp>=2

### Issue 正文摘录

### Your current environment The ray version is 2.10.0 and vllm version is 0.5.0+cu117 ### 🐛 Describe the bug Using tp=2 as code listed below: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/cephfs/shared/model/llama-2-7b-hf/", tensor_parallel_size=2) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ray start not work: ```text 2024-06-13 16:11:50,396 INFO worker.py:1752 -- Started a local Ray instance. [2024-06-13 16:11:51,588 E 13261 13261] core_worker.cc:228: Failed to register worker 01000000ffffffffffffffffffffffffffffffffffffffffffffffff to Raylet. IOError: [RayletClient] Unable to register worker with raylet. No such file or directory ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="/cephfs/shared/model/llama-2-7b-hf/", tensor_parallel_size=2) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for outp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ray not work when tp>=2 bug;stale ### Your current environment The ray version is 2.10.0 and vllm version is 0.5.0+cu117 ### 🐛 Describe the bug Using tp=2 as code listed below: ```python from vllm import LLM, SamplingPa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: ray not work when tp>=2 bug;stale ### Your current environment The ray version is 2.10.0 and vllm version is 0.5.0+cu117 ### 🐛 Describe the bug Using tp=2 as code listed below: ```python from vllm import LLM, Sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
