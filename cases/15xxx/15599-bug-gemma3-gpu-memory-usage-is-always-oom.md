# vllm-project/vllm#15599: [Bug]: Gemma3 GPU memory usage is always oom

| 字段 | 值 |
| --- | --- |
| Issue | [#15599](https://github.com/vllm-project/vllm/issues/15599) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma3 GPU memory usage is always oom

### Issue 正文摘录

### Your current environment Why does 4 4090s always crash when loading gemma3-12? ### 🐛 Describe the bug Why does 4 4090s always crash when loading gemma3-12? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Gemma3 GPU memory usage is always oom bug;stale ### Your current environment Why does 4 4090s always crash when loading gemma3-12? ### 🐛 Describe the bug Why does 4 4090s always crash when loading gemma3-12? ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 12? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Gemma3 GPU memory usage is always oom bug;stale ### Your current environment Why does 4 4090s always crash when loading gemma3-12? ### 🐛 Describe the bug Why does 4 4090s always crash when loading gemma3-12? ###...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma3 GPU memory usage is always oom bug;stale ### Your current environment Why does 4 4090s always crash when loading gemma3-12? ### 🐛 Describe the bug Why does 4 4090s always crash when loading gemma3-12? ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Gemma3 GPU memory usage is always oom bug;stale ### Your current environment Why does 4 4090s always crash when loading gemma3-12? ### 🐛 Describe the bug Why does 4 4090s always crash when loading gemma3-12? ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
