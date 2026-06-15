# vllm-project/vllm#29298: [Feature]: Prefill mode for PD using cpu+gpu hybrid engine

| 字段 | 值 |
| --- | --- |
| Issue | [#29298](https://github.com/vllm-project/vllm/issues/29298) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Prefill mode for PD using cpu+gpu hybrid engine

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi, don't know if it is possible to implement at all, but in theory it would be useful to have some sort of hybrid cpu/gpu prefill-only worker(e.g. llama.cpp) compatible with vllm, to be able to leverage full server resources(that are typically huge - e.g. cpu computing power). Why i am proposing this request - sglang recently added ktransformers support, so it is possible now to use hybrid cpu/gpu computing mode to launch big models. But this mode uses cpu as a compute unit. But existing cpu offload in vllm just offloads weights and doesn't help in compute(as of my knowledge). And i wondered if similar approach(like ktransformers+sglang) would be applicable to the PD disaggregation improvement in vllm. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Prefill mode for PD using cpu+gpu hybrid engine feature request;stale ### 🚀 The feature, motivation and pitch Hi, don't know if it is possible to implement at all, but in theory it would be useful to have som...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d be useful to have some sort of hybrid cpu/gpu prefill-only worker(e.g. llama.cpp) compatible with vllm, to be able to leverage full server resources(that are typically huge - e.g. cpu computing power). Why i am propos...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: h big models. But this mode uses cpu as a compute unit. But existing cpu offload in vllm just offloads weights and doesn't help in compute(as of my knowledge). And i wondered if similar approach(like ktransformers+sglan...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
