# vllm-project/vllm#19107: [Usage]: intent is added for guided generation

| 字段 | 值 |
| --- | --- |
| Issue | [#19107](https://github.com/vllm-project/vllm/issues/19107) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: intent is added for guided generation

### Issue 正文摘录

### Your current environment `{\n"product":\n"pixel",\n"rating":\n3\n}` response_format + guided generation will add \n. how can we avoid this intent=2 for guided generation? and only force the model to generate via dense json.dumps default. ### How would you like to use vllm - use guided generation without intent ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rrent environment `{\n"product":\n"pixel",\n"rating":\n3\n}` response_format + guided generation will add \n. how can we avoid this intent=2 for guided generation? and only force the model to generate via dense json.dum...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ent ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: intent is added for guided generation usage;stale ### Your current environment `{\n"product":\n"pixel",\n"rating":\n3\n}` response_format + guided generation will add \n. how can we avoid this intent=2 for guid...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
