# vllm-project/vllm#5775: [RFC]: A Flexible Architecture for Distributed Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#5775](https://github.com/vllm-project/vllm/issues/5775) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: A Flexible Architecture for Distributed Inference

### Issue 正文摘录

### Motivation. The current vLLM architecture for distributed inference is not flexible enough. We have a difficult time adding speculative decoding with a different tensor parallel size (see https://github.com/vllm-project/vllm/pull/5414 ). Quite the same problem happens when users want the vLLM processes to collaborate with additional processes, e.g. when RLHF frameworks want to sync weight with vLLM processes (see https://github.com/vllm-project/vllm/issues/5723 ). This RFC tries to improve the distributed inference architecture so that it is flexible enough to support more possibilities. # what's the difference between distributed training and distributed inference? Distributed training is a well-studied area, with many optimized communication primitives vLLM already uses, such as allreduce. Distributed training usually happens at large scale, and follows the SPMD style code: all processes are running the same code. Datasets are sharded before training, iteration steps, batch size, model size and architecture... these are all known information for every processes. As a result, distributed training is essentially a for-loop, all the processes are virtually executing the same co...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: ibuted inference is not flexible enough. We have a difficult time adding speculative decoding with a different tensor parallel size (see https://github.com/vllm-project/vllm/pull/5414 ). Quite the same problem happens w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the vLLM processes to collaborate with additional processes, e.g. when RLHF frameworks want to sync weight with vLLM processes (see https://github.com/vllm-project/vllm/issues/5723 ). This RFC tries to improve the distr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ed inference should look like this: There would be a server process, dispatching requests to different models. Each model will occupy its own process group, and will not have any interference with the rest models. If th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: A Flexible Architecture for Distributed Inference RFC ### Motivation. The current vLLM architecture for distributed inference is not flexible enough. We have a difficult time adding speculative decoding with a di...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: Ideally, we should only send token ids to workers, and workers own their kv cache, block tables. With this, we can even incrementally send token ids, to further reduce the amount of data transferred between server proce...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
