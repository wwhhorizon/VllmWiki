# vllm-project/vllm#11126: [Usage]: how to use EAGLE on vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#11126](https://github.com/vllm-project/vllm/issues/11126) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use EAGLE on vLLM?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to test EAGLE on vllm, but i try so many methods to run EAGLE, fail so many times. The target model is Llama2-chat-hf, and the draft model is EAGLE-Llama2-chat in original EAGLE's author's github. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , but i try so many methods to run EAGLE, fail so many times. The target model is Llama2-chat-hf, and the draft model is EAGLE-Llama2-chat in original EAGLE's author's github. ### Before submitting a new issue... - [X]...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: how to use EAGLE on vLLM? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to test EAGLE on vllm, but i try so many methods to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: b. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ython collect_env.py` ``` ### How would you like to use vllm I want to test EAGLE on vllm, but i try so many methods to run EAGLE, fail so many times. The target model is Llama2-chat-hf, and the draft model is EAGLE-Lla...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
