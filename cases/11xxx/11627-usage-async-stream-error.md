# vllm-project/vllm#11627: [Usage]: async stream error

| 字段 | 值 |
| --- | --- |
| Issue | [#11627](https://github.com/vllm-project/vllm/issues/11627) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: async stream error

### Issue 正文摘录

This is my code: ``` self.model = AsyncLLMEngine.from_engine_args(AsyncEngineArgs(**{ "model": model_name, "trust_remote_code": True, "dtype": 'bfloat16', "enforce_eager": True, "tensor_parallel_size": 2, "gpu_memory_utilization": 0.5, })) ``` then, I have a self.model. If I run something like this ``` async for result in result_generator: xxx yield xx ``` It works well However, If I run ``` self.model.generate() # good self.model.generate() # bad self.model.generate() # bad ... async for result in result_generator: # bad xxx yield xx ``` So, I want to ask that the `self.model.generate` comes from `AsyncLLMEngine`, just can be called once (before yield) in a function? If not, how? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ineArgs(**{ "model": model_name, "trust_remote_code": True, "dtype": 'bfloat16', "enforce_eager": True, "tensor_parallel_size": 2, "gpu_memory_utilization": 0.5, })) ``` then, I have a self.model. If I run something lik...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ow? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: async stream error usage This is my code: ``` self.model = AsyncLLMEngine.from_engine_args(AsyncEngineArgs(**{ "model": model_name, "trust_remote_code": True, "dtype": 'bfloat16', "enforce_eager": True, "tensor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
