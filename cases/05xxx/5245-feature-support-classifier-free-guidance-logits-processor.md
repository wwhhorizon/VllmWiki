# vllm-project/vllm#5245: [Feature]: support Classifier-Free Guidance Logits processor

| 字段 | 值 |
| --- | --- |
| Issue | [#5245](https://github.com/vllm-project/vllm/issues/5245) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support Classifier-Free Guidance Logits processor

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Implementation in transformers: https://github.com/huggingface/transformers/blob/6b22a8f2d8ded6b2a681e1c078b0e1abf27d045c/src/transformers/generation/logits_process.py#L2171 Hi, the Classifier-Free Guidance Logits processor need re-run the model forward process with unconditional_ids in comput_logits process, how to make this happen in vLLM? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: motivation and pitch Implementation in transformers: https://github.com/huggingface/transformers/blob/6b22a8f2d8ded6b2a681e1c078b0e1abf27d045c/src/transformers/generation/logits_process.py#L2171 Hi, the Classifier-Free...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support Classifier-Free Guidance Logits processor feature request;stale ### 🚀 The feature, motivation and pitch Implementation in transformers: https://github.com/huggingface/transformers/blob/6b22a8f2d8ded6b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
