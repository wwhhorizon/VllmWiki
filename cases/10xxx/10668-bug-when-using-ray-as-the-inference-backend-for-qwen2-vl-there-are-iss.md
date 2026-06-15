# vllm-project/vllm#10668: [Bug]: When using Ray as the inference backend for Qwen2-VL, there are issues with the inference results.

| 字段 | 值 |
| --- | --- |
| Issue | [#10668](https://github.com/vllm-project/vllm/issues/10668) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using Ray as the inference backend for Qwen2-VL, there are issues with the inference results.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 使用下面代码初始化VLLM后，推理结果出现截断或者重复的问题，模型用的是Qwen2-VL-7B-Instruct ```python model = LLM( model=generate_config.model_dir, dtype="auto", trust_remote_code=True, gpu_memory_utilization=generate_config.gpu_memory_utilization, max_num_batched_tokens=generate_config.max_num_batched_tokens, max_num_seqs=generate_config.max_num_seqs, tensor_parallel_size=generate_config.tensor_parallel_size, enable_prefix_caching=generate_config.enable_prefix_caching, max_model_len=generate_config.max_model_len, distributed_executor_backend="ray", ) ``` 当我不改变任何代码，仅注释 distributed_executor_backend="ray"后，推理结果恢复正常 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: When using Ray as the inference backend for Qwen2-VL, there are issues with the inference results. bug;ray ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 使用下面代码初始化VLLM后，推理...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: When using Ray as the inference backend for Qwen2-VL, there are issues with the inference results. bug;ray ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug 使用下面代码初始化VLLM后，推理...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ```python model = LLM( model=generate_config.model_dir, dtype="auto", trust_remote_code=True, gpu_memory_utilization=generate_config.gpu_memory_utilization, max_num_batched_tokens=generate_config.max_num_batched_tokens,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 复正常 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
