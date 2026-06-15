# vllm-project/vllm#8313: [Performance]: guided generation is very slow in offline mode

| 字段 | 值 |
| --- | --- |
| Issue | [#8313](https://github.com/vllm-project/vllm/issues/8313) |
| 状态 | closed |
| 标签 | performance;structured-output;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: guided generation is very slow in offline mode

### Issue 正文摘录

### Proposal to improve performance With a single request / online mode I'm getting: - no guided 300 tok/sec - `outlines` 150 tok/sec (2x slower) - `lm-format-enforcer` 90 tok/sec (~3x slower) with offline mode I get: - `outlines` **is about 10-20x slower than no guided generation** - `lm-format-enforcer` is about 4x faster than `outlines` (note that it is slower than `outlines` for online) for online I was using this schema: ``` json_template = { "type": "object", "properties": { "criteria": {"type": "array", "items": {"type": "string"}, "minItems": 1}, "response": { "type": "string" } }, "required": ["criteria", "response"] } ``` for offline I was using an even simpler schema: ``` { "type":"object", "properties":{ "name":{ "type":"string", "minLength":2, "maxLength":5 }, "age":{ "type":"integer" } }, "required":[ "name", "age"] } ``` the huge performance hit in the offline mode is very strange for both backends. 2x slow down in the online mode is pretty bad too as it's already a huge impact. The offline mode can actually tolerate 2x no problem as there is no human in the loop, but 10-20x is a way impractical. `vllm=0.6.0` and `outlines==0.0.46`

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed generation is very slow in offline mode performance;structured-output;stale ### Proposal to improve performance With a single request / online mode I'm getting: - no guided 300 tok/sec - `outlines` 150 tok/sec (2x sl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `` the huge performance hit in the offline mode is very strange for both backends. 2x slow down in the online mode is pretty bad too as it's already a huge impact. The offline mode can actually tolerate 2x no problem as...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing: - no guided 300 tok/sec - `outlines` 150 tok/sec (2x slower) - `lm-format-enforcer` 90 tok/sec (~3x slower) with offline mode I get: - `outlines` **is about 10-20x slower than no guided generation** - `lm-format-en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
