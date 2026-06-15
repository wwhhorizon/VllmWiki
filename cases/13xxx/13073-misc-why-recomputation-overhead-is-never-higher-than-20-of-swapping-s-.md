# vllm-project/vllm#13073: [Misc]: Why recomputation overhead is never higher than 20% of swapping’s latency

| 字段 | 值 |
| --- | --- |
| Issue | [#13073](https://github.com/vllm-project/vllm/issues/13073) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Why recomputation overhead is never higher than 20% of swapping’s latency

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi, all In the Paper, there is such a paragraph > Thus, recomputation is more efficient when the block size is small, while swapping is more efficient when the block size is large, though recomputation overhead is never higher than 20% of swapping’s latency. For medium block sizes from 16 to 64, the two methods exhibit comparable end-to-end performance. ![Image](https://github.com/user-attachments/assets/bf752ddc-31ce-4fa4-b9b8-2247d44df8f1) I didn't get it, why 20%? Any help is appreciated. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: aragraph > Thus, recomputation is more efficient when the block size is small, while swapping is more efficient when the block size is large, though recomputation overhead is never higher than 20% of swapping’s latency....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: Misc]: Why recomputation overhead is never higher than 20% of swapping’s latency stale ### Anything you want to discuss about vllm. Hi, all In the Paper, there is such a paragraph > Thus, recomputation is more efficient...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the Paper, there is such a paragraph > Thus, recomputation is more efficient when the block size is small, while swapping is more efficient when the block size is large, though recomputation overhead is never higher tha...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: re is such a paragraph > Thus, recomputation is more efficient when the block size is small, while swapping is more efficient when the block size is large, though recomputation overhead is never higher than 20% of swapp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hy recomputation overhead is never higher than 20% of swapping’s latency stale ### Anything you want to discuss about vllm. Hi, all In the Paper, there is such a paragraph > Thus, recomputation is more efficient when th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
