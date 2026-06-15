# vllm-project/vllm#7780: [Feature]: Check for presence of files at startup

| 字段 | 值 |
| --- | --- |
| Issue | [#7780](https://github.com/vllm-project/vllm/issues/7780) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Check for presence of files at startup

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Checks for files such as templates etc. should be done right at the start of vLLM loading. Not right at the end after 30 minutes of loading the model. [rank0]: ValueError: The supplied chat template (./chat_template/llama3.jinja) looks like a file path, but it failed to be opened. Reason: [Errno 2] No such file or directory: ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rt of vLLM loading. Not right at the end after 30 minutes of loading the model. [rank0]: ValueError: The supplied chat template (./chat_template/llama3.jinja) looks like a file path, but it failed to be opened. Reason:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Check for presence of files at startup feature request ### 🚀 The feature, motivation and pitch Checks for files such as templates etc. should be done right at the start of vLLM loading. Not right at the end a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
