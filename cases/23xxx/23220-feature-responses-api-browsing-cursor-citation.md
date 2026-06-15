# vllm-project/vllm#23220: [Feature][Responses API] Browsing Cursor -> Citation

| 字段 | 值 |
| --- | --- |
| Issue | [#23220](https://github.com/vllm-project/vllm/issues/23220) |
| 状态 | closed |
| 标签 | feature request;stale;gpt-oss |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Responses API] Browsing Cursor -> Citation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we do not translate the cursor (indexed by the browsing tool) into Citation format properly. That means users won't be able to access the URL being accessed. Non-streaming mode: https://github.com/vllm-project/vllm/blob/c32e6ad1f63631fd8033f0cca3a35d5e48ccfc7f/vllm/entrypoints/harmony_utils.py#L182-L199 Streaming mode: https://github.com/vllm-project/vllm/blob/c32e6ad1f63631fd8033f0cca3a35d5e48ccfc7f/vllm/entrypoints/openai/serving_responses.py#L1015-L1102 OpenAI docs ``` "content": [ { "type": "output_text", "text": "As of today, March 9, 2025, one notable positive news story...", "annotations": [ { "type": "url_citation", "start_index": 442, "end_index": 557, "url": "https://.../?utm_source=chatgpt.com", "title": "..." }, { "type": "url_citation", "start_index": 962, "end_index": 1077, "url": "https://.../?utm_source=chatgpt.com", "title": "..." }, { "type": "url_citation", "start_index": 1336, "end_index": 1451, "url": "https://.../?utm_source=chatgpt.com", "title": "..." } ] } ] ``` https://platform.openai.com/docs/api-reference/responses/create ### Alternatives _No response_ ### Additional context _No response_ ### Before sub...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eature][Responses API] Browsing Cursor -> Citation feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Currently, we do not translate the cursor (indexed by the browsing tool) into Citation format prop...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][Responses API] Browsing Cursor -> Citation feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Currently, we do not translate the cursor (indexed by the browsing tool) into Citation format pr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature][Responses API] Browsing Cursor -> Citation feature request;stale;gpt-oss ### 🚀 The feature, motivation and pitch Currently, we do not translate the cursor (indexed by the browsing tool) into Citation format pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: { "type": "output_text", "text": "As of today, March 9, 2025, one notable positive news story...", "annotations": [ { "type": "url_citation", "start_index": 442, "end_index": 557, "url": "ht
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
