# vllm-project/vllm#33789: [RFC]: How will vLLM adapt to more diverse KVCacheSpecs?

| 字段 | 值 |
| --- | --- |
| Issue | [#33789](https://github.com/vllm-project/vllm/issues/33789) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: How will vLLM adapt to more diverse KVCacheSpecs?

### Issue 正文摘录

### Motivation. There is a trend toward increasingly complex Attention configurations in LLMs. We have a model that mixes Mamba and different FullAttentions with different kv_hidden_sizes, and it is difficult to find a reasonably sized common multiple across these varying kv_hidden_sizes. For such scenarios, what are the community’s future plans for solutions? ### Proposed Change. There may be several directions: 1. Allocate separate KVCacheTensor and a dedicated BlockPool for each Attention Group, allowing each group to request any kv_hidden_size freely. 2. Maintain the current design of a single global BlockPool, while aligning modules with smaller kv_hidden_sizes via padding to match the global page size (similar to the current approach for Mamba). However, this would require kernels to handle non-contiguous KV cache. 3. Anything else... I would like to know which direction the community intends to take in the future, so that our current work can stay aligned with vLLM’s future technical roadmap. Any comment is appreciated! ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you a...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: several directions: 1. Allocate separate KVCacheTensor and a dedicated BlockPool for each Attention Group, allowing each group to request any kv_hidden_size freely. 2. Maintain the current design of a single global Bloc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current design of a single global BlockPool, while aligning modules with smaller kv_hidden_sizes via padding to match the global page size (similar to the current approach for Mamba). However, this would require kernels...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Motivation. There is a trend toward increasingly complex Attention configurations in LLMs. We have a model that mixes Mamba and different FullAttentions with different kv_hidden_sizes, and it is difficult to find a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: How will vLLM adapt to more diverse KVCacheSpecs? RFC;stale ### Motivation. There is a trend toward increasingly complex Attention configurations in LLMs. We have a model that mixes Mamba and different FullAttent...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n stay aligned with vLLM’s future technical roadmap. Any comment is appreciated! ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
