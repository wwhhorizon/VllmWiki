# vllm-project/vllm#8383: [Performance]: JSONLogitsProcessor repeats the same `build_regex_from_schema`  again and again

| 字段 | 值 |
| --- | --- |
| Issue | [#8383](https://github.com/vllm-project/vllm/issues/8383) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: JSONLogitsProcessor repeats the same `build_regex_from_schema`  again and again

### Issue 正文摘录

### Proposal to improve performance Why does the regex get recompiled on every request? the object gets instantiated for every request and the regex is rebuilt even though most of the time the schema is likely to remain the same. https://github.com/vllm-project/vllm/blob/b1f3e189586dce42bb3dcda20169a9308c9a25fa/vllm/model_executor/guided_decoding/outlines_logits_processors.py#L142 probably `@lru_cache` should do the trick here? does it work on object constructors? or would it be cleaner to add a wrapper around `build_regex_from_schema` and cache that? This is otherwise similar to https://github.com/vllm-project/vllm/pull/8308?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Performance]: JSONLogitsProcessor repeats the same `build_regex_from_schema` again and again performance;stale ### Proposal to improve performance Why does the regex get recompiled on every request? the object gets ins...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: repeats the same `build_regex_from_schema` again and again performance;stale ### Proposal to improve performance Why does the regex get recompiled on every request? the object gets instantiated for every request and the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/b1f3e189586dce42bb3dcda20169a9308c9a25fa/vllm/model_executor/guided_decoding/outlines_logits_processors.py#L142 probably `@lru_cache` should do the trick here? does it work on object construct...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
