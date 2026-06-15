# vllm-project/vllm#39819: [Feature]: Render endpoint responses (i.e /v1/chat/completions/render) include the rendered prompt/text

| 字段 | 值 |
| --- | --- |
| Issue | [#39819](https://github.com/vllm-project/vllm/issues/39819) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Render endpoint responses (i.e /v1/chat/completions/render) include the rendered prompt/text

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Recently, `render` endpoints were introduced as part of the disaggregated inference work described in these RFC: https://github.com/vllm-project/vllm/issues/22817 and https://github.com/vllm-project/vllm/issues/34407. These endpoints return a `GenerateRequest` object that can be forwarded directly to a GPU worker. In addition to their primary role, these endpoints are also valuable for debugging/introspection - particularly for understanding how requests are preprocessed before execution with ChatCompletion chat templates. The current response only includes `token_ids`, which makes it difficult to interpret and less user-friendly for debugging purposes. This gh feature request is proposing to include the original `prompt` (or `text`) in the response payload. ``` { "request_id": "chatcmpl-bbe884a5f2e30dce", "token_ids": [ 8948, 198, .... ], "features": null, "sampling_params": { "presence_penalty": 0.0, "frequency_penalty": 0.0, "repetition_penalty": 1.0, "temperature": 0.7, "top_p": 1.0, "min_p": 0.0, "stop": [], "stop_token_ids": [], "max_tokens": 8161, "output_kind": 2, "skip_clone": true, "bad_words": [], "skip_reading_prefix_cache": fals...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ip_clone": true, "bad_words": [], "skip_reading_prefix_cache": false }, "model": "", "stream": false, "stream_options": null, "cache_salt": null, "priority": 0, "kv_transfer_params ``` ### Before submitting a new issue....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rue, "bad_words": [], "skip_reading_prefix_cache": false }, "model": "", "stream": false, "stream_options": null, "cache_salt": null, "priority": 0, "kv_transfer_params ``` ### Before submitting a new issue... - [x] Mak...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: .e /v1/chat/completions/render) include the rendered prompt/text feature request ### 🚀 The feature, motivation and pitch Recently, `render` endpoints were introduced as part of the disaggregated inference work described...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
