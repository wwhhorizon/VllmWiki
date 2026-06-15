# vllm-project/vllm#29643: [Usage]: Enabling Tool call in the Python SDK

| 字段 | 值 |
| --- | --- |
| Issue | [#29643](https://github.com/vllm-project/vllm/issues/29643) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Enabling Tool call in the Python SDK

### Issue 正文摘录

### Your current environment Hi Team, I am currently exploring VLLM to enable tool calling, and I need some support with this. It would be very helpful if you could provide the corresponding Python code. What I’m trying to achieve is to configure the Python package with the same settings that I use when starting the VLLM server. The configuration I’m using is: vllm serve DeepSeek-R1-0528-Qwen3-8B \ --served-model-name deepseek \ --gpu_memory_utilization 0.5 \ --max_num_seqs 20 \ --max_model_len 10000 \ --enable-auto-tool-choice \ --tool-call-parser deepseek_v3 \ --chat-template tool_chat_template_deepseekr1.jinja \ --port 5050 \ --max_num_batched_tokens 5000 I need to replicate this exact configuration in Python. Your support would be greatly appreciated. Please respond at your earliest convenience. If you want, I can also write the **Python code equivalent** for these VLLM configurations. Best Regards Madan ### How would you like to use vllm I want to use vLLM to serve a model with tool-calling support enabled. Specifically, I need to run the model with the same configuration parameters that I currently use when launching the vLLM server from the command line. These settings incl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: provide the corresponding Python code. What I’m trying to achieve is to configure the Python package with the same settings that I use when starting the VLLM server. The configuration I’m using is: vllm serve DeepSeek-R...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: s, a custom tool-call parser, and a custom chat template. My goal is to reproduce the following server configuration within a Python environment using the vLLM Python API: vllm serve DeepSeek-R1-0528-Qwen3-8B \ --served...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: this exact configuration in Python. Your support would be greatly appreciated. Please respond at your earliest convenience. If you want, I can also write the **Python code equivalent** for these VLLM configurations. Bes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: launching the vLLM server from the command line. These settings include GPU memory utilization, maximum sequence limits, tool-calling options, a custom tool-call parser, and a custom chat template. My goal is to reprodu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
