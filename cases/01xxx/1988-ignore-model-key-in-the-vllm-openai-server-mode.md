# vllm-project/vllm#1988: Ignore `model` key in the vLLM OpenAI server mode

| 字段 | 值 |
| --- | --- |
| Issue | [#1988](https://github.com/vllm-project/vllm/issues/1988) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Ignore `model` key in the vLLM OpenAI server mode

### Issue 正文摘录

I use vLLM to serve private AI model on dedicate instance that is consumed by existing infra across many languages. If I retrain model and deploy, I need to also update other databases to request the right model. I feel like it'd be great if `model` in the request would actually be ignored. I find this reasonable expectation because vLLM supports serving only one model at a time. That model's name is always shown in the response and thus it's still visible. This way my backend could accept any model that is currently active. Does this sound reasonable? :)

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: is always shown in the response and thus it's still visible. This way my backend could accept any model that is currently active. Does this sound reasonable? :)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Ignore `model` key in the vLLM OpenAI server mode I use vLLM to serve private AI model on dedicate instance that is consumed by existing infra across many languages. If I retrain model and deploy, I need to also update...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: If I retrain model and deploy, I need to also update other databases to request the right model. I feel like it'd be great if `model` in the request would actually be ignored. I find this reasonable expectation because...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
