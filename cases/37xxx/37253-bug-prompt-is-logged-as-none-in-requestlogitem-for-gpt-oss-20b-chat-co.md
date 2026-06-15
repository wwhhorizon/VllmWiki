# vllm-project/vllm#37253: [Bug]: prompt is logged as None in RequestLogItem for gpt-oss-20b (Chat Completion API)

| 字段 | 值 |
| --- | --- |
| Issue | [#37253](https://github.com/vllm-project/vllm/issues/37253) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: prompt is logged as None in RequestLogItem for gpt-oss-20b (Chat Completion API)

### Issue 正文摘录

### Description **`prompt` is logged as `None` in `RequestLogItem` for `gpt-oss-20b` (Chat Completion API)** ### Describe the bug When using the `v1/chat/completions` endpoint with the `gpt-oss-20b` model, the debug logs show `prompt: None` in the `RequestLogItem` details. While the `prompt_token_ids` are correctly populated and the model generates responses successfully, the missing text-based `prompt` in the logs makes it difficult to verify the applied chat template. This behavior is inconsistent with other models. For instance, in `Gemma-3`, the full templated prompt string is clearly visible in the logs. ### To Reproduce 1. Launch the vLLM API server with the `gpt-oss-20b` model. 2. Send a request to the `/v1/chat/completions` endpoint. 3. Observe the output in the debug logs (set `VLLM_LOGGING_LEVEL=DEBUG`). ### Observed Logs **Case 1: gpt-oss-20b (Issue)** ```text (APIServer pid=7) DEBUG 03-17 10:54:08 [entrypoints/logger.py:53] Request chatcmpl-847d721608ebc2b7 details: prompt: None, prompt_token_ids: [200006, 17360, 200008, ...], prompt_embeds shape: None.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: prompt is logged as None in RequestLogItem for gpt-oss-20b (Chat Completion API) bug ### Description **`prompt` is logged as `None` in `RequestLogItem` for `gpt-oss-20b` (Chat Completion API)** ### Describe the b...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: the full templated prompt string is clearly visible in the logs. ### To Reproduce 1. Launch the vLLM API server with the `gpt-oss-20b` model. 2. Send a request to the `/v1/chat/completions` endpoint. 3. Observe the outp...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ate. This behavior is inconsistent with other models. For instance, in `Gemma-3`, the full templated prompt string is clearly visible in the logs. ### To Reproduce 1. Launch the vLLM API server with the `gpt-oss-20b` mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: prompt is logged as None in RequestLogItem for gpt-oss-20b (Chat Completion API) bug ### Description **`prompt` is logged as `None` in `RequestLogItem` for `gpt-oss-20b` (Chat Completion API)** ### Describe the b...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
