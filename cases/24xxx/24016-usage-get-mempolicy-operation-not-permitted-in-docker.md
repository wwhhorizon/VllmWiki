# vllm-project/vllm#24016: [Usage]: `get_mempolicy: Operation not permitted` in docker

| 字段 | 值 |
| --- | --- |
| Issue | [#24016](https://github.com/vllm-project/vllm/issues/24016) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: `get_mempolicy: Operation not permitted` in docker

### Issue 正文摘录

### Your current environment when docker run vLLM, sometimes you will see warning message ``` get_mempolicy: Operation not permitted ``` it means NUMA policy fetching failure but not impact the functionality , but just impact the NUMA performance optimization code in VLLM. Fix reference : https://docs.docker.com/engine/security/seccomp/ ### How would you like to use vllm I would like to create a doc PR to explain this . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: `get_mempolicy: Operation not permitted` in docker usage ### Your current environment when docker run vLLM, sometimes you will see warning message ``` get_mempolicy: Operation not permitted ``` it means NUMA po...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
