# vllm-project/vllm#8188: [Usage]: What's the minimum VRAM needed to use entire context length for Llama 3.1 70B and 405B

| 字段 | 值 |
| --- | --- |
| Issue | [#8188](https://github.com/vllm-project/vllm/issues/8188) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What's the minimum VRAM needed to use entire context length for Llama 3.1 70B and 405B

### Issue 正文摘录

### Your current environment Libraries Installed - ``` "vllm==0.5.5", "torch==2.4.0", "transformers==4.44.2", "ray", "hf-transfer", "huggingface_hub" ``` ### How would you like to use vllm Hi I want to run Llama 3.1 70B and 405B with 120K context length. I have access to several 8xH100 nodes however most tutorial code snippets give errors of the style `ValueError: The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (17840). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine`. I want to get an estimate of how many nodes each having 8 H100s do I need for both the models to get enough VRAM to run both the models at full context length. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: What's the minimum VRAM needed to use entire context length for Llama 3.1 70B and 405B usage;stale ### Your current environment Libraries Installed - ``` "vllm==0.5.5", "torch==2.4.0", "transformers==4.44.2", "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ma 3.1 70B and 405B with 120K context length. I have access to several 8xH100 nodes however most tutorial code snippets give errors of the style `ValueError: The model's max seq len (131072) is larger than the maximum n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ama 3.1 70B and 405B usage;stale ### Your current environment Libraries Installed - ``` "vllm==0.5.5", "torch==2.4.0", "transformers==4.44.2", "ray", "hf-transfer", "huggingface_hub" ``` ### How would you like to use vl...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 31072) is larger than the maximum number of tokens that can be stored in KV cache (17840). Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine`. I want to get an estimate o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: RAM needed to use entire context length for Llama 3.1 70B and 405B usage;stale ### Your current environment Libraries Installed - ``` "vllm==0.5.5", "torch==2.4.0", "transformers==4.44.2", "ray", "hf-transfer", "hugging...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
