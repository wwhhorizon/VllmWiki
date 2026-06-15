# vllm-project/vllm#12012: [Doc]: Performance/Optimization Page doesn't mention Pipeline Parallel Size

| 字段 | 值 |
| --- | --- |
| Issue | [#12012](https://github.com/vllm-project/vllm/issues/12012) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Performance/Optimization Page doesn't mention Pipeline Parallel Size

### Issue 正文摘录

### 📚 The doc issue In the Page https://github.com/vllm-project/vllm/blob/main/docs/source/performance/optimization.md One of the recommended options includes the following: ``` Increase tensor_parallel_size. This approach shards model weights, so each GPU has more memory available for KV cache. ``` This document does not mention increasing `pipeline_parallel_size` which would also result in the model being sharded across more GPUs so their is more memory available for KV cache. ### Suggest a potential alternative/fix Increase `tensor_parallel_size` or `pipeline_parallel_size` (if using Multi-Node Multi-GPU). This approach shards model weights, so each GPU has more memory available for KV cache. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: he. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: approach shards model weights, so each GPU has more memory available for KV cache. ``` This document does not mention increasing `pipeline_parallel_size` which would also result in the model being sharded across more GP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: the following: ``` Increase tensor_parallel_size. This approach shards model weights, so each GPU has more memory available for KV cache. ``` This document does not mention increasing `pipeline_parallel_size` which woul...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
