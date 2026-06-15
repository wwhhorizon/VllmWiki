# vllm-project/vllm#15895: [Bug]: TP with external_launcher is not working with vLLM version 0.8.0 and above

| 字段 | 值 |
| --- | --- |
| Issue | [#15895](https://github.com/vllm-project/vllm/issues/15895) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TP with external_launcher is not working with vLLM version 0.8.0 and above

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run the [script](https://github.com/vllm-project/vllm/blob/v0.8.0rc2/examples/offline_inference/torchrun_example.py) with `torchrun --nproc-per-node=2 torchrun_example.py`, ranks have different output (vlllm == 0.8.0 and onward). Whn I try it with 0.7.3, it works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. CC @youkaichao

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e.py) with `torchrun --nproc-per-node=2 torchrun_example.py`, ranks have different output (vlllm == 0.8.0 and onward). Whn I try it with 0.7.3, it works. ### Before submitting a new issue... - [x] Make sure you already...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: TP with external_launcher is not working with vLLM version 0.8.0 and above bug ### Your current environment ### 🐛 Describe the bug When I run the [script](https://github.com/vllm-project/vllm/blob/v0.8.0rc2/examp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. CC @youkaichao

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
