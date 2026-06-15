# vllm-project/vllm#15132: [Usage]: multiround QA when using qwen2.5vl with the same input image

| 字段 | 值 |
| --- | --- |
| Issue | [#15132](https://github.com/vllm-project/vllm/issues/15132) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: multiround QA when using qwen2.5vl with the same input image

### Issue 正文摘录

### Your current environment ```text 0.7.3 ``` ### How would you like to use vllm Does vllm support multi question answering for one same image? I have multiple questions for one image, now I use ``` outputs = llm.generate( {"prompt": prompt, "multi_modal_data": {"image": image}}, sampling_params=sampling_params ) ``` to get answer for each answer, but this requires model to processing image each time. Is there any better way to do this? Thanks a lot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: multiround QA when using qwen2.5vl with the same input image usage;stale ### Your current environment ```text 0.7.3 ``` ### How would you like to use vllm Does vllm support multi question answering for one same...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: age]: multiround QA when using qwen2.5vl with the same input image usage;stale ### Your current environment ```text 0.7.3 ``` ### How would you like to use vllm Does vllm support multi question answering for one same im...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
