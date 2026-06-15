# vllm-project/vllm#17711: [Usage]: Offline multi-node inference

| 字段 | 值 |
| --- | --- |
| Issue | [#17711](https://github.com/vllm-project/vllm/issues/17711) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Offline multi-node inference

### Issue 正文摘录

### Your current environment Hello everybody According to the vLLM documentation, it seems that in order to performe multi-node inference, one has to do this in an online setting. I am working with access to a GPU cluster, where the compute nodes do not have internet access. My goal is to run inference with llama 3.3 70B Instruct on a file using 4 nodes (4 gpus per node), however, if I try to use the LLM class, I get an error saying that data parallelism isn't possible and I should use AsyncEngine instead. However, asyncEngine cannot be used with the chat() method, thus I am currently unable to perform inference on this file containing samples. I hereby wanted to ask if it's possible to perform offline multi-node inference and if so whether there are guides or further documentation on it, thank you ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ou ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: if I try to use the LLM class, I get an error saying that data parallelism isn't possible and I should use AsyncEngine instead. However, asyncEngine cannot be used with the chat() method, thus I am currently unable to p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pute nodes do not have internet access. My goal is to run inference with llama 3.3 70B Instruct on a file using 4 nodes (4 gpus per node), however, if I try to use the LLM class, I get an error saying that data parallel...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Offline multi-node inference usage;stale ### Your current environment Hello everybody According to the vLLM documentation, it seems that in order to performe multi-node inference, one has to do this in an onlin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
