# vllm-project/vllm#37644: [Bug]: key error: ‘Layer.34.mlp.experts.gate_up_proj’

| 字段 | 值 |
| --- | --- |
| Issue | [#37644](https://github.com/vllm-project/vllm/issues/37644) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: key error: ‘Layer.34.mlp.experts.gate_up_proj’

### Issue 正文摘录

### Your current environment 0.17 ### 🐛 Describe the bug Hi, which version of cloned is compatible with transformers5.3? I am hitting a key error: Keyerror: ‘Layer.34.mlp.experts.gate_up_proj’ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ug ### Your current environment 0.17 ### 🐛 Describe the bug Hi, which version of cloned is compatible with transformers5.3? I am hitting a key error: Keyerror: ‘Layer.34.mlp.experts.gate_up_proj’ ### Before submitting a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oj’ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: key error: ‘Layer.34.mlp.experts.gate_up_proj’ bug ### Your current environment 0.17 ### 🐛 Describe the bug Hi, which version of cloned is compatible with transformers5.3? I am hitting a key error: Keyerror: ‘Lay...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
