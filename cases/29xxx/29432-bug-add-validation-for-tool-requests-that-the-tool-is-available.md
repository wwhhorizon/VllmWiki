# vllm-project/vllm#29432: [Bug]: Add validation for tool requests that the tool is available

| 字段 | 值 |
| --- | --- |
| Issue | [#29432](https://github.com/vllm-project/vllm/issues/29432) |
| 状态 | closed |
| 标签 | bug;good first issue;gpt-oss |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Add validation for tool requests that the tool is available

### Issue 正文摘录

### 🐛 Describe the bug Currently there is no check for this, vLLM will just respond sub-optimally in a "silent" way. We should fail the individual request in this case with appropriate error message. This is a problem in particular for example when using the demo tool server without the `gpt-oss` package installed. See discussion here: https://github.com/vllm-project/vllm/pull/29336#issuecomment-3573053391

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: or example when using the demo tool server without the `gpt-oss` package installed. See discussion here: https://github.com/vllm-project/vllm/pull/29336#issuecomment-3573053391
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dation for tool requests that the tool is available bug;good first issue;gpt-oss ### 🐛 Describe the bug Currently there is no check for this, vLLM will just respond sub-optimally in a "silent" way. We should fail the in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Add validation for tool requests that the tool is available bug;good first issue;gpt-oss ### 🐛 Describe the bug Currently there is no check for this, vLLM will just respond sub-optimally in a "silent" way. We sho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
