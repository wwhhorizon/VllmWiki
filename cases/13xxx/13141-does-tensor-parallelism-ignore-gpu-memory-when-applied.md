# vllm-project/vllm#13141: Does Tensor Parallelism Ignore GPU Memory When Applied?

| 字段 | 值 |
| --- | --- |
| Issue | [#13141](https://github.com/vllm-project/vllm/issues/13141) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Does Tensor Parallelism Ignore GPU Memory When Applied?

### Issue 正文摘录

Hi~ I understand that Tensor Parallelism can be applied at the head level or by splitting the heads. Currently, in vLLM, it seems that the decision to use either v1 or v2 is made when calling the paged_attention kernel. I am curious whether this decision is made without considering the GPU memory(especially, shared memory) information. ```python # NOTE(woosuk): We use a simple heuristic to decide whether to use # PagedAttention V1 or V2. If the number of partitions is 1, we use # V1 to avoid the overhead of reduction. Also, if the number of # sequences or heads is large, we use V1 since there is enough work # to parallelize. # TODO(woosuk): Tune this heuristic. # For context len > 8192, use V2 kernel to avoid shared memory shortage. use_v1 = (max_seq_len 512)) ``` Can most cases be covered with only the above condition?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: level or by splitting the heads. Currently, in vLLM, it seems that the decision to use either v1 or v2 is made when calling the paged_attention kernel. I am curious whether this decision is made without considering the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Does Tensor Parallelism Ignore GPU Memory When Applied? performance;stale Hi~ I understand that Tensor Parallelism can be applied at the head level or by splitting the heads. Currently, in vLLM, it seems that the decisi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Does Tensor Parallelism Ignore GPU Memory When Applied? performance;stale Hi~ I understand that Tensor Parallelism can be applied at the head level or by splitting the heads. Currently, in vLLM, it seems that the decisi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is made without considering the GPU memory(especially, shared memory) information. ```python # NOTE(woosuk): We use a simple heuristic to decide whether to use # PagedAttention V1 or V2. If the number of partitions is 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Does Tensor Parallelism Ignore GPU Memory When Applied? performance;stale Hi~ I understand that Tensor Parallelism can be applied at the head level or by splitting the heads. Currently, in vLLM, it seems that the decisi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
