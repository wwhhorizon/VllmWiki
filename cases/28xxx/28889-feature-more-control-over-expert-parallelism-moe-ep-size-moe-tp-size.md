# vllm-project/vllm#28889: [Feature]: More control over expert parallelism (--moe_ep_size, --moe_tp_size)

| 字段 | 值 |
| --- | --- |
| Issue | [#28889](https://github.com/vllm-project/vllm/issues/28889) |
| 状态 | open |
| 标签 | feature request;deepseek |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: More control over expert parallelism (--moe_ep_size, --moe_tp_size)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch _More granularity of setting expert parallelism_ For low concurrency use case, sometimes there's a balance between `--enable-expert-parallel=True` and `--enable-expert-parallel=False`. I'm benchmarking ISL/OSL of 1600/600, in vllm there's only either EP=8 or EP=1 (no EP). However, in TRTLLM, there's a control over EP=1, EP=2, EP=4, EP=8. As shown in the chart below, EP=4 is actually faster than EP=8 for concurrencies ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: More control over expert parallelism (--moe_ep_size, --moe_tp_size) feature request;deepseek ### 🚀 The feature, motivation and pitch _More granularity of setting expert parallelism_ For low concurrency use ca...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: More control over expert parallelism (--moe_ep_size, --moe_tp_size) feature request;deepseek ### 🚀 The feature, motivation and pitch _More granularity of setting expert parallelism_ For low concurrency use ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: enable-expert-parallel=True` and `--enable-expert-parallel=False`. I'm benchmarking ISL/OSL of 1600/600, in vllm there's only either EP=8 or EP=1 (no EP). However, in TRTLLM, there's a control over EP=1, EP=2, EP=4, EP=...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: shown in the chart below, EP=4 is actually faster than EP=8 for concurrencies ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: between `--enable-expert-parallel=True` and `--enable-expert-parallel=False`. I'm benchmarking ISL/OSL of 1600/600, in vllm there's only either EP=8 or EP=1 (no EP). However, in TRTLLM, there's a control over EP=1, EP=2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
