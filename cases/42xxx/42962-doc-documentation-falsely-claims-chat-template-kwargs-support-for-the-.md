# vllm-project/vllm#42962: [Doc]: Documentation falsely claims chat_template_kwargs support for the Responses API

| 字段 | 值 |
| --- | --- |
| Issue | [#42962](https://github.com/vllm-project/vllm/issues/42962) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Documentation falsely claims chat_template_kwargs support for the Responses API

### Issue 正文摘录

### 📚 The doc issue In the [documentation for the Responses API](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#responses-api), the Extra parameters section claims support for `chat_template_kwargs` in the Response API. However, when I tried to suppress reasoning in `Qwen3.6-27B` by adding ```Python extra_body={"chat_template_kwargs": {"enable_thinking": False}} ``` to the request, it got ignored and I got back the reasoning output as well. The same parameter works fine in the `chat.completions` endpoint. ### Suggest a potential alternative/fix The obviously correct solution would be to implement the functionality. As I understand, there is [an open issue that addresses this](https://github.com/vllm-project/vllm/issues/32850), although it seems to have gone stale. Until that (hopefully) gets implemented, the documentation should be updated to remove the false claim; or better yet, add a warning for arguments not yet (fully) implemented. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ra_body={"chat_template_kwargs": {"enable_thinking": False}} ``` to the request, it got ignored and I got back the reasoning output as well. The same parameter works fine in the `chat.completions` endpoint. ### Suggest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Doc]: Documentation falsely claims chat_template_kwargs support for the Responses API documentation ### 📚 The doc issue In the [documentation for the Responses API](https://docs.vllm.ai/en/latest/serving/openai_compati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gs` in the Response API. However, when I tried to suppress reasoning in `Qwen3.6-27B` by adding ```Python extra_body={"chat_template_kwargs": {"enable_thinking": False}} ``` to the request, it got ignored and I got back...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: In the [documentation for the Responses API](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#responses-api), the Extra parameters section claims support for `chat_template_kwargs` in the Response API. H...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
