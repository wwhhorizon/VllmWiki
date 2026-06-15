# vllm-project/vllm#20715: [Bug] when I run the gemma3-27B model with local attention: global attention=5:1 and input 128K, the program does not interrupt?

| 字段 | 值 |
| --- | --- |
| Issue | [#20715](https://github.com/vllm-project/vllm/issues/20715) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] when I run the gemma3-27B model with local attention: global attention=5:1 and input 128K, the program does not interrupt?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, may I ask if when I run the gemma3-27B model with local attention: global attention=5:1 and input 128K, the program does not interrupt? Through debugging, I found that vllm v1 is divided into: process0 for data preprocessing and post-processing, process1 for model inference, and after data transmission to process1, it enters the run loop but cannot terminate. What is the reason for this? I would like to know the root cause. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ng and post-processing, process1 for model inference, and after data transmission to process1, it enters the run loop but cannot terminate. What is the reason for this? I would like to know the root cause. ### Before su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] when I run the gemma3-27B model with local attention: global attention=5:1 and input 128K, the program does not interrupt? bug ### Your current environment ### 🐛 Describe the bug Hello, may I ask if when I run the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug] when I run the gemma3-27B model with local attention: global attention=5:1 and input 128K, the program does not interrupt? bug ### Your current environment ### 🐛 Describe the bug Hello, may I ask if when I run the...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
