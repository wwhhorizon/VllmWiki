# vllm-project/vllm#4056: [Feature][Chunked Prefill]: Enable cuda graph for chunked prefill. 

| 字段 | 值 |
| --- | --- |
| Issue | [#4056](https://github.com/vllm-project/vllm/issues/4056) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][Chunked Prefill]: Enable cuda graph for chunked prefill. 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM only enables cuda graph for decoding-only batches (mainly because it didn't see big perf improvement if batched token length > 256). This behavior is preserved even after chunked prefill is enabled, which means when prefill and decodes are batched together (mixed batch) cuda graph is not enabled. Since chunked prefill keeps the max number of batched tokens small (for example, 768), we can ideally turn on cuda graph for mixed batches. Before continuing any efforts, we should make sure this will actually improve the performance. I am planning to do this from our internal repo which already enables cuda graph for prefill. ### Alternatives Not doing it. If the performance improvement is not good enough, we will keep the current behavior rather than adding complexity. ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature][Chunked Prefill]: Enable cuda graph for chunked prefill. feature request;stale ### 🚀 The feature, motivation and pitch vLLM only enables cuda graph for decoding-only batches (mainly because it didn't see big p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature][Chunked Prefill]: Enable cuda graph for chunked prefill. feature request;stale ### 🚀 The feature, motivation and pitch vLLM only enables cuda graph for decoding-only batches (mainly because it didn't see big p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
