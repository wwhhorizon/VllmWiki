# vllm-project/vllm#16612: [Bug]: Spec decode not allocating lookahead req for req in WAITING queue

| 字段 | 值 |
| --- | --- |
| Issue | [#16612](https://github.com/vllm-project/vllm/issues/16612) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Spec decode not allocating lookahead req for req in WAITING queue

### Issue 正文摘录

### 🐛 Describe the bug PR #16370 uses num lookahead tokens for computing preallocated kv blocks in EAGLE. However, it skipped for WAITING req which would be req who enter the continous batching for the 1st time or the resumed requests. cc: @LiuXiaoxuanPKU ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Spec decode not allocating lookahead req for req in WAITING queue bug ### 🐛 Describe the bug PR #16370 uses num lookahead tokens for computing preallocated kv blocks in EAGLE. However, it skipped for WAITING req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: KU ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e bug PR #16370 uses num lookahead tokens for computing preallocated kv blocks in EAGLE. However, it skipped for WAITING req which would be req who enter the continous batching for the 1st time or the resumed requests....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
