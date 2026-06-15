# vllm-project/vllm#5423: [RFC]: Improve guided decoding (logit_processor) APIs and performance.

| 字段 | 值 |
| --- | --- |
| Issue | [#5423](https://github.com/vllm-project/vllm/issues/5423) |
| 状态 | closed |
| 标签 | structured-output;RFC;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Improve guided decoding (logit_processor) APIs and performance.

### Issue 正文摘录

### Motivation. Currently, guided decoding & logit processor API is incomplete has has several issues. The RFC is intended to bring up problems and solutions. Some of issues may have been already addressed and there are PRs out already. There are 3 major issues. - It is not supported from SamplingParamters - It is not possible to support batch/async logit processing. - Upon failures, engine will die. ### Proposed Change. API ---- guided decoding parameters are not supported with SamplingParams. It is addressed from https://github.com/vllm-project/vllm/pull/4130 Performance ------------- Currently, logit processors APIs are applied row by row blocking (https://github.com/vllm-project/vllm/blob/246598a6b1e22616630b7f1bf11bd9bcb31dc860/vllm/model_executor/layers/logits_processor.py#L112). Instead, we can use parallel processing (e.g., ray or thread pool) to improve the logit processing performance. We are using this mechanism internally at Anyscale. We'd like to support this feature in OSS, and would like to improve logit processor API to support 1. async. 2. batching. This requires logit processor to be - stateful (to use a tool like Ray or thread pool). I think this PR https://gith...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: com/vllm-project/vllm/blob/246598a6b1e22616630b7f1bf11bd9bcb31dc860/vllm/model_executor/layers/logits_processor.py#L112). Instead, we can use parallel processing (e.g., ray or thread pool) to improve the logit processin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ce ------------- Currently, logit processors APIs are applied row by row blocking (https://github.com/vllm-project/vllm/blob/246598a6b1e22616630b7f1bf11bd9bcb31dc860/vllm/model_executor/layers/logits_processor.py#L112)....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: d decoding (logit_processor) APIs and performance. structured-output;RFC;stale ### Motivation. Currently, guided decoding & logit processor API is incomplete has has several issues. The RFC is intended to bring up probl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nk this PR https://github.com/vllm-project/vllm/pull/5329 is likely sufficient. - async. We'd like to propose "prepare" API which can separate out compute_logits from preparing logits. ``` class LogitPostProcessor: def...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: git processing performance. We are using this mechanism internally at Anyscale. We'd like to support this feature in OSS, and would like to improve logit processor API to support 1. async. 2. batching. This requires log...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
