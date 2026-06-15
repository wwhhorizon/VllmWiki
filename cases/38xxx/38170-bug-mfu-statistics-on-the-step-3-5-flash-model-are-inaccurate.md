# vllm-project/vllm#38170: [Bug]: MFU statistics on the Step-3.5-Flash model are inaccurate

| 字段 | 值 |
| --- | --- |
| Issue | [#38170](https://github.com/vllm-project/vllm/issues/38170) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MFU statistics on the Step-3.5-Flash model are inaccurate

### Issue 正文摘录

### Your current environment Due to environmental constraints, I was unable to run the script. Here are the details of my testing environment: GPU host: 8 H20 GPUs, each with 141 GB of memory vLLM version: v0.17.1 ### 🐛 Describe the bug I ran performance tests on MinixMax-M2.5 and Step-3.5-Flash using vLLM v0.17.1 on a single machine equipped with 8 H20 GPUs. According to the statistics from `enable-mfu-metrics`, the average MFU for Step-3.5-Flash is 55.81%, while the average MFU for MiniMax-m2.5 is 32.61%. Because the gap is large, I tried to analyze the causes and found the following issues: 1. The current MFU statistics logic does not account for Sliding Window Attention (SWA) 2. The current MFU statistics logic does not account for Multi-Token Prediction (MTP) This causes the MFU reported for Step-3.5-Flash to be higher than the actual value (my guess). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ting environment: GPU host: 8 H20 GPUs, each with 141 GB of memory vLLM version: v0.17.1 ### 🐛 Describe the bug I ran performance tests on MinixMax-M2.5 and Step-3.5-Flash using vLLM v0.17.1 on a single machine equipped...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: MFU statistics on the Step-3.5-Flash model are inaccurate bug ### Your current environment Due to environmental constraints, I was unable to run the script. Here are the details of my testing environment: GPU hos...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: constraints, I was unable to run the script. Here are the details of my testing environment: GPU host: 8 H20 GPUs, each with 141 GB of memory vLLM version: v0.17.1 ### 🐛 Describe the bug I ran performance tests on Minix...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
