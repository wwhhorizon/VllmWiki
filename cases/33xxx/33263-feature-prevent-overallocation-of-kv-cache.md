# vllm-project/vllm#33263: [Feature]: Prevent overallocation of kv-cache

| 字段 | 值 |
| --- | --- |
| Issue | [#33263](https://github.com/vllm-project/vllm/issues/33263) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prevent overallocation of kv-cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hello, first of all thank you to the contributors for this awesome and fast inference engine! When I'm running a model with restricted sequence length and sequences, then the KV-cache is still allocated s.t. the entire GPU is used. Example: ``` from vllm import LLM, SamplingParams llm = LLM( model="Qwen/Qwen3-1.7B", max_num_seqs=1, max_model_len=1024, ) ``` results in (24 GB GPU): ``` INFO 01-28 16:08:46 [gpu_worker.py:358] Available KV cache memory: 18.78 GiB INFO 01-28 16:08:46 [kv_cache_utils.py:1305] GPU KV cache size: 175,856 tokens ``` despite never coming close to needing 175k tokens, thus unneccessarily filling up the GPU. I understand that setting `kv_cache_memory_bytes` and `gpu_memory_utilization` can alleviate this, yet both are clumsy as correct settings need to be estimated and adjusted on a per model basis. Instead, shouldn't kv cache automatically be limited to `max_num_seqs * max_model_len`, as this is the maximum possible load? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: Prevent overallocation of kv-cache feature request;unstale ### 🚀 The feature, motivation and pitch Hello, first of all thank you to the contributors for this awesome and fast inference engine! When I'm runnin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ributors for this awesome and fast inference engine! When I'm running a model with restricted sequence length and sequences, then the KV-cache is still allocated s.t. the entire GPU is used. Example: ``` from vllm impor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Prevent overallocation of kv-cache feature request;unstale ### 🚀 The feature, motivation and pitch Hello, first of all thank you to the contributors for this awesome and fast inference engine! When I'm runnin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is still allocated s.t. the entire GPU is used. Example: ``` from vllm import LLM, SamplingParams llm = LLM( model="Qwen/Qwen3-1.7B", max_num_seqs=1, max_model_len=1024, ) ``` results in (24 GB GPU): ``` INFO 01-28 16:0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
