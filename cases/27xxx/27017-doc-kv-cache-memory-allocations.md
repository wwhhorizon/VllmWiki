# vllm-project/vllm#27017: [Doc]: KV Cache Memory allocations

| 字段 | 值 |
| --- | --- |
| Issue | [#27017](https://github.com/vllm-project/vllm/issues/27017) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: KV Cache Memory allocations

### Issue 正文摘录

### 📚 The doc issue Hello, When serving a model via vLLM for text(token) generation: 1. Before a new request gets scheduled, does vLLM check if KV cache for a sequence length of `max_model_len` is available for that new request or does it check if KV cache for a sequence length of `input prompt + max_tokens` (if it's less than _max_model_length_) is available for the request? In case the request does not specify a _max_tokens_ does it default to 16? 2. In case the required KV cache memory is not available, does the server wait until it is available to schedule that new request? 3. When exactly is the KV cache allocated for a particular request? Do the KV cache blocks get allocated after computing the number of new blocks required for all current requests after each generation step of the model, as mentioned in this [blog post](https://www.aleksagordic.com/blog/vllm)? i.e. the KV cache block is not fully allocated upfront based on the point [1] calculation instead incrementally allocated since the request could finish before it reaches the _max_tokens_ or _max_model_length_ limit? 4. I am trying to understand if the server concurrency can be more than the one specified in the serve...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ory allocations documentation ### 📚 The doc issue Hello, When serving a model via vLLM for text(token) generation: 1. Before a new request gets scheduled, does vLLM check if KV cache for a sequence length of `max_model_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Doc]: KV Cache Memory allocations documentation ### 📚 The doc issue Hello, When serving a model via vLLM for text(token) generation: 1. Before a new request gets scheduled, does vLLM check if KV cache for a sequence le...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: size` of 8? ``` number of layers * number of KV heads * head dimension * precision/8 * 2 (for K & V) * seq_len bytes OR (number of layers * number of KV heads * head dimension * precision/8 * 2 (for K & V) * seq_len)/te...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l_length_) is available for the request? In case the request does not specify a _max_tokens_ does it default to 16? 2. In case the required KV cache memory is not available, does the server wait until it is available to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
