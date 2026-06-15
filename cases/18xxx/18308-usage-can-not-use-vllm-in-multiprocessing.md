# vllm-project/vllm#18308: [Usage]: Can not use vLLM in multiprocessing

| 字段 | 值 |
| --- | --- |
| Issue | [#18308](https://github.com/vllm-project/vllm/issues/18308) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can not use vLLM in multiprocessing

### Issue 正文摘录

### Your current environment vllm==0.8.5.post1 ### How would you like to use vllm I want to launch several processes to do vllm inference in parallel on multiple GPUs using multiprocessing.Pool, but this error occurs: ``` AssertionError: daemonic processes are not allowed to have children ``` Is my use case not supported anymore? It worked fine with earlier versions. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n ``` Is my use case not supported anymore? It worked fine with earlier versions. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
