# vllm-project/vllm#10761: TypeError: ChatGLMTokenizer._pad() got an unexpected keyword argument 'padding_side'

| 字段 | 值 |
| --- | --- |
| Issue | [#10761](https://github.com/vllm-project/vllm/issues/10761) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: ChatGLMTokenizer._pad() got an unexpected keyword argument 'padding_side'

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm using vllm0.6.2 with chatglm2-6B : TypeError: ChatGLMTokenizer._pad() got an unexpected keyword argument 'padding_side' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: de' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Tokenizer._pad() got an unexpected keyword argument 'padding_side' usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm using vllm0.6.2 with chatg...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
