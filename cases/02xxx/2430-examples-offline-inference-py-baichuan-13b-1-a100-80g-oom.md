# vllm-project/vllm#2430: examples/offline_inference.py。推理baichuan-13b，1*A100（80G），会OOM？

| 字段 | 值 |
| --- | --- |
| Issue | [#2430](https://github.com/vllm-project/vllm/issues/2430) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> examples/offline_inference.py。推理baichuan-13b，1*A100（80G），会OOM？

### Issue 正文摘录

采用代码examples/offline_inference.py，vllm也这么吃显存吗？

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: examples/offline_inference.py。推理baichuan-13b，1*A100（80G），会OOM？ stale 采用代码examples/offline_inference.py，vllm也这么吃显存吗？
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: examples/offline_inference.py。推理baichuan-13b，1*A100（80G），会OOM？ stale 采用代码examples/offline_inference.py，vllm也这么吃显存吗？
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: examples/offline_inference.py。推理baichuan-13b，1*A100（80G），会OOM？ stale 采用代码examples/offline_inference.py，vllm也这么吃显存吗？

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
