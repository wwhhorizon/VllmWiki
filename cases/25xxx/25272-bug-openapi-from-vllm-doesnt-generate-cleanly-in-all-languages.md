# vllm-project/vllm#25272: [Bug]: openapi from vllm doesnt generate cleanly in all languages

| 字段 | 值 |
| --- | --- |
| Issue | [#25272](https://github.com/vllm-project/vllm/issues/25272) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: openapi from vllm doesnt generate cleanly in all languages

### Issue 正文摘录

### Your current environment Java ### 🐛 Describe the bug openapi/swagger isnt acceptable for all languages. ``` "stop": { "anyOf": [ { "type": "string" }, { "items": { "type": "string" }, "type": "array" }, { "type": "null" } ], "title": "Stop", "default": [] }, ``` With the out-of the box open-api generator the result is this: ``` public static final String JSON_PROPERTY_STOP = "stop"; @javax.annotation.Nullable private Stop stop = []; ``` This doesn't work in Java: ``` [ERROR] /home/edward/jinference-clients/jinference-client-jersy/target/generated-sources/openapi/src/main/java/io/teknek/jinference/model/ChatCompletionRequest.java:[201,23] illegal start of expression ``` The simple fix is to remove the default Which generates this ``` public static final String JSON_PROPERTY_STOP = "stop"; @javax.annotation.Nullable private Stop stop; ``` This only happens a few places in the API ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: openapi from vllm doesnt generate cleanly in all languages bug;stale ### Your current environment Java ### 🐛 Describe the bug openapi/swagger isnt acceptable for all languages. ``` "stop": { "anyOf": [ { "type":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: API ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ersy/target/generated-sources/openapi/src/main/java/io/teknek/jinference/model/ChatCompletionRequest.java:[201,23] illegal start of expression ``` The simple fix is to remove the default Which generates this ``` public...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
