# vllm-project/vllm#17119: [Bug]: jinja2 TemplateError should return 422 instead of 500 error code

| 字段 | 值 |
| --- | --- |
| Issue | [#17119](https://github.com/vllm-project/vllm/issues/17119) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: jinja2 TemplateError should return 422 instead of 500 error code

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have users who sometimes send the wrong format of input and this results in `jinja2.exceptions.TemplateError: Conversation roles must alternate user/assistant/user/assistant/...`. This error message makes sense and is expected, but it returns 500 errors which triggers alarms for us. Since this is technically a user error, it should raise 4xx errors, ideally a 422. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 22. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t ### 🐛 Describe the bug We have users who sometimes send the wrong format of input and this results in `jinja2.exceptions.TemplateError: Conversation roles must alternate user/assistant/user/assistant/...`. This error...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: g]: jinja2 TemplateError should return 422 instead of 500 error code bug;stale ### Your current environment ### 🐛 Describe the bug We have users who sometimes send the wrong format of input and this results in `jinja2.e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
