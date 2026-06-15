# vllm-project/vllm#5224: v0.5.0 Release Tracker

| 字段 | 值 |
| --- | --- |
| Issue | [#5224](https://github.com/vllm-project/vllm/issues/5224) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> v0.5.0 Release Tracker

### Issue 正文摘录

ETA Monday 06/10. This is a version bump in minor because we expect the following major features to informally enter beta stage: * Chunked Prefill * Speculative Decode * FP8 * VLM Blockers: - [ ] Optional: - [ ] https://github.com/vllm-project/vllm/pull/4650 - [ ] #4109

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t the following major features to informally enter beta stage: * Chunked Prefill * Speculative Decode * FP8 * VLM Blockers: - [ ] Optional: - [ ] https://github.com/vllm-project/vllm/pull/4650 - [ ] #4109
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: v0.5.0 Release Tracker ETA Monday 06/10. This is a version bump in minor because we expect the following major features to informally enter beta stage: * Chunked Prefill * Speculative Decode * FP8 * VLM Blockers: - [ ]...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: to informally enter beta stage: * Chunked Prefill * Speculative Decode * FP8 * VLM Blockers: - [ ] Optional: - [ ] https://github.com/vllm-project/vllm/pull/4650 - [ ] #4109
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ly enter beta stage: * Chunked Prefill * Speculative Decode * FP8 * VLM Blockers: - [ ] Optional: - [ ] https://github.com/vllm-project/vllm/pull/4650 - [ ] #4109
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ormally enter beta stage: * Chunked Prefill * Speculative Decode * FP8 * VLM Blockers: - [ ] Optional: - [ ] https://github.com/vllm-project/vllm/pull/4650 - [ ] #4109

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
