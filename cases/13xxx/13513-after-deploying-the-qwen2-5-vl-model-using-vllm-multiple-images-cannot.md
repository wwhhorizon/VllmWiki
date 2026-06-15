# vllm-project/vllm#13513: After deploying the qwen2.5-vl model using vllm, multiple images cannot be passed in. What is going on?

| 字段 | 值 |
| --- | --- |
| Issue | [#13513](https://github.com/vllm-project/vllm/issues/13513) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> After deploying the qwen2.5-vl model using vllm, multiple images cannot be passed in. What is going on?

### Issue 正文摘录

### Your current environment The output is : openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400} ### 🐛 Describe the bug The output is : openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: After deploying the qwen2.5-vl model using vllm, multiple images cannot be passed in. What is going on? bug;stale ### Your current environment The output is : openai.BadRequestError: Error code: 400 - {'object': 'error'...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: l using vllm, multiple images cannot be passed in. What is going on? bug;stale ### Your current environment The output is : openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 1 image(s) ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 00} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
