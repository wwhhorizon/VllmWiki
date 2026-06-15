# vllm-project/vllm#7677: [Usage]: how to use guided_decoding_backend?

| 字段 | 值 |
| --- | --- |
| Issue | [#7677](https://github.com/vllm-project/vllm/issues/7677) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to use guided_decoding_backend?

### Issue 正文摘录

### Your current environment I found that in EngineArgs, guided_decoding_backend can choose to support outlines or lm-format-enforcer. How can I use it? Specifically, the following code can be executed by outlines ```python import outlines model = outlines.models.transformers(model_path) prompt = "fish is delicious" unstruct_answer = outlines.generate.choice(model,["positive","negative"])(prompt) ``` How can I achieve this in vllm？ ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n choose to support outlines or lm-format-enforcer. How can I use it? Specifically, the following code can be executed by outlines ```python import outlines model = outlines.models.transformers(model_path) prompt = "fis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: EngineArgs, guided_decoding_backend can choose to support outlines or lm-format-enforcer. How can I use it? Specifically, the following code can be executed by outlines ```python import outlines model = outlines.models....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: how to use guided_decoding_backend? usage;stale ### Your current environment I found that in EngineArgs, guided_decoding_backend can choose to support outlines or lm-format-enforcer. How can I use it? Specifica...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to use guided_decoding_backend? usage;stale ### Your current environment I found that in EngineArgs, guided_decoding_backend can choose to support outlines or lm-format-enforcer. How can I use it? Specifica...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
