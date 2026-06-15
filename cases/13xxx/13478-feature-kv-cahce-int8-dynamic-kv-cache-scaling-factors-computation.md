# vllm-project/vllm#13478: [Feature]: kv cahce int8：Dynamic kv cache scaling factors computation

| 字段 | 值 |
| --- | --- |
| Issue | [#13478](https://github.com/vllm-project/vllm/issues/13478) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: kv cahce int8：Dynamic kv cache scaling factors computation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Referring to the online quantization of pr(https://github.com/vllm-project/vllm/pull/10354): kv cache int8, there are only scaling parameters. Can online quantification of KV Cahce INT8 also be achieved. Some machines, such as A800, do not support FP8. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: t;stale ### 🚀 The feature, motivation and pitch Referring to the online quantization of pr(https://github.com/vllm-project/vllm/pull/10354): kv cache int8, there are only scaling parameters. Can online quantification of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ure]: kv cahce int8：Dynamic kv cache scaling factors computation feature request;stale ### 🚀 The feature, motivation and pitch Referring to the online quantization of pr(https://github.com/vllm-project/vllm/pull/10354):...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: kv cahce int8：Dynamic kv cache scaling factors computation feature request;stale ### 🚀 The feature, motivation and pitch Referring to the online quantization of pr(https://github.com/vllm-project/vllm/pull/10...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
