# vllm-project/vllm#8617: [Usage]: Number of requests currently in the queue

| 字段 | 值 |
| --- | --- |
| Issue | [#8617](https://github.com/vllm-project/vllm/issues/8617) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Number of requests currently in the queue

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am running an online inference server via the code: `vllm serve "daryl149/llama-2-7b-chat-hf" --max-model-len 2048` for which I am sending request through a load generator. I want to know if it is possible to find out the number of requests currently in the queue or alternatively number of requests currently being processed in a batch (assume batch size=248 and number of batches=1). ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: running an online inference server via the code: `vllm serve "daryl149/llama-2-7b-chat-hf" --max-model-len 2048` for which I am sending request through a load generator. I want to know if it is possible to find out the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Number of requests currently in the queue usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am running an online inference server via the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ). ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
