# vllm-project/vllm#8523: [Feature]: APC introspection interface

| 字段 | 值 |
| --- | --- |
| Issue | [#8523](https://github.com/vllm-project/vllm/issues/8523) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: APC introspection interface

### Issue 正文摘录

### 🚀 The feature, motivation and pitch we're working towards using vllm for a large-scale deployment with Automatic Prefix Caching enabled. the issue with that in our use-case we want to have the same vllm instance handle the given blocks so that APC provides any form of throughput. to do that we need to know which blocks are in the given instance for a request, and all the currently cached blocks in the instance. (we can hash parts of a request context ourselves and map internal hash -> block id so we know when a vllm instance has the blocks for a given request). I was thinking about exposing it via some internal function on `LLMEngine` that would give the block hashes for the request id and another for all block hashes, and then we can expose it on our vllm http wrapper in the response headers. for that I've been investigating `vllm` source code to find possible hooks to add those functions, but haven't been successful in understanding the architecture of the APC at the required level to do this. if there's some pointers around how an implementation would look like I likely would be able to PR it. ### Alternatives _No response_ ### Additional context _No response_ ### Before su...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: APC introspection interface feature request;stale ### 🚀 The feature, motivation and pitch we're working towards using vllm for a large-scale deployment with Automatic Prefix Caching enabled. the issue with th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e vllm instance handle the given blocks so that APC provides any form of throughput. to do that we need to know which blocks are in the given instance for a request, and all the currently cached blocks in the instance....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ture, motivation and pitch we're working towards using vllm for a large-scale deployment with Automatic Prefix Caching enabled. the issue with that in our use-case we want to have the same vllm instance handle the given...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to add those functions, but haven't been successful in understanding the architecture of the APC at the required level to do this. if there's some pointers around how an implementation would look like I likely would be...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in our use-case we want to have the same vllm instance handle the given blocks so that APC provides any form of throughput. to do that we need to know which blocks are in the given instance for a request, and all the cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
