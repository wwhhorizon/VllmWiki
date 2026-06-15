# vllm-project/vllm#15647: [Performance]: Update Cascade Attention Heuristics for FA3

| 字段 | 值 |
| --- | --- |
| Issue | [#15647](https://github.com/vllm-project/vllm/issues/15647) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Update Cascade Attention Heuristics for FA3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we use a heuristic (https://github.com/vllm-project/vllm/blob/4098b72210dc10761bb348b373bbd0fc9b23b0e4/vllm/v1/attention/backends/flash_attn.py#L331) to determine whether using cascade attention would improve performance. However, this heuristic was developed prior to the FA3 integration and is therefore optimized only for FA2. The calculation of SM occupancy it uses is no longer accurate for FA3 and needs updating. Specifically, 1. We need to split the case for FA2 and FA3, since FA2 is still used for certain GPUs. 2. Afaik, FA3 uses different heuristics for GQA packing and split kv than FA2. The heuristics in use_cascade should reflect this difference (although it doesn't need to be super accurate). 3. It'd be nice if we can cite specific lines of code in FA3 (and FA2) deciding the tile sizes, scheduling, etc., so that we can easily verify and track. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Performance]: Update Cascade Attention Heuristics for FA3 help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Currently, we use a heuristic (https://github.com/vllm-project/vllm/b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: integration and is therefore optimized only for FA2. The calculation of SM occupancy it uses is no longer accurate for FA3 and needs updating. Specifically, 1. We need to split the case for FA2 and FA3, since FA2 is sti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ascade Attention Heuristics for FA3 help wanted;good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Currently, we use a heuristic (https://github.com/vllm-project/vllm/blob/4098b72210dc10761bb...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: occupancy it uses is no longer accurate for FA3 and needs updating. Specifically, 1. We need to split the case for FA2 and FA3, since FA2 is still used for certain GPUs. 2. Afaik, FA3 uses different heuristics for GQA p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
