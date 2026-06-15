# vllm-project/vllm#30487: [Bug] [CPU Backend]: Wrong L2 cache size on Arm CPU for Attention tiles

| 字段 | 值 |
| --- | --- |
| Issue | [#30487](https://github.com/vllm-project/vllm/issues/30487) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [CPU Backend]: Wrong L2 cache size on Arm CPU for Attention tiles

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On Arm-based instances (e.g. AWS c8g), the CPU attention implementation in vLLM uses: `long l2_size = sysconf(_SC_LEVEL2_CACHE_SIZE);` inside csrc/cpu/cpu_attn_impl.hpp to estimate the L2 cache size and derive tiling parameters for the attention kernel. sysconf(_SC_LEVEL2_CACHE_SIZE) returns 0, which effectively means: • The L2 cache size is treated as 0. • The tiling logic falls back to minimal tile sizes or tile size changes have no effect on performance. • The cache aware code is performing poorly due to missing cache size information. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] [CPU Backend]: Wrong L2 cache size on Arm CPU for Attention tiles bug;cpu ### Your current environment ### 🐛 Describe the bug On Arm-based instances (e.g. AWS c8g), the CPU attention implementation in vLLM uses: `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: • The cache aware code is performing poorly due to missing cache size information. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
