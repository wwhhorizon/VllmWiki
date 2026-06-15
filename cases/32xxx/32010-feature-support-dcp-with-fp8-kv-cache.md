# vllm-project/vllm#32010: [Feature]: Support DCP with FP8 KV Cache

| 字段 | 值 |
| --- | --- |
| Issue | [#32010](https://github.com/vllm-project/vllm/issues/32010) |
| 状态 | open |
| 标签 | help wanted;feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support DCP with FP8 KV Cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch DCP is great Fp8 kv cache is great We should support both at the same time: ```bash (EngineCore_DP0 pid=2734260) ERROR 01-08 23:29:29 [core.py:900] RuntimeError: Worker failed with error 'DCP not support fp8 kvcache now.', please check the stack trace above for the root cause ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Support DCP with FP8 KV Cache help wanted;feature request ### 🚀 The feature, motivation and pitch DCP is great Fp8 kv cache is great We should support both at the same time: ```bash (EngineCore_DP0 pid=273426...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Feature]: Support DCP with FP8 KV Cache help wanted;feature request ### 🚀 The feature, motivation and pitch DCP is great Fp8 kv cache is great We should support both at the same time: ```bash (EngineCore_DP0 pid=273426...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support DCP with FP8 KV Cache help wanted;feature request ### 🚀 The feature, motivation and pitch DCP is great Fp8 kv cache is great We should support both at the same time: ```bash (EngineCore_DP0 pid=273426...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
