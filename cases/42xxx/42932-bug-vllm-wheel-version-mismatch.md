# vllm-project/vllm#42932: [Bug]: vLLM wheel version mismatch 

| 字段 | 值 |
| --- | --- |
| Issue | [#42932](https://github.com/vllm-project/vllm/issues/42932) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM wheel version mismatch 

### Issue 正文摘录

### Your current environment vLLM wheel that is getting installed is different from that of the branch used. Example Docker is generated using the vllm branch - 0.19.0 , https://github.com/vllm-project/vllm/tree/releases/v0.19.0 But while building the wheel/docker, it generates the wheel which has version 0.19.1 pip3 list -l | grep vllm vllm 0.19.1.dev0+g2a69949bd.d20260417.rocm713 Same applies for vLLM branch - 0.19.1 as well vLLM branch used --- https://github.com/vllm-project/vllm/tree/releases/v0.19.1 Wheel that is generated has the version as pip3 list -l | grep vllm vllm 0.19.2.dev3+g24efb8904.d20260514.rocm713 ### 🐛 Describe the bug There are no crashes or faults, This mismatch should not happen ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: vLLM wheel version mismatch bug ### Your current environment vLLM wheel that is getting installed is different from that of the branch used. Example Docker is generated using the vllm branch - 0.19.0 , https://gi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM wheel version mismatch bug ### Your current environment vLLM wheel that is getting installed is different from that of the branch used. Example Docker is generated using the vllm branch - 0.19.0 , https://gi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: vLLM wheel version mismatch bug ### Your current environment vLLM wheel that is getting installed is different from that of the branch used. Example Docker is generated using the vllm branch - 0.19.0 , https://gi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
