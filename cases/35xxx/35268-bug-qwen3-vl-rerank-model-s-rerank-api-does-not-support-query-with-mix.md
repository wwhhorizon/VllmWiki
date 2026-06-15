# vllm-project/vllm#35268: [Bug]: Qwen3-VL-Rerank model’s rerank API does not support query with mixed image and text inputs.

| 字段 | 值 |
| --- | --- |
| Issue | [#35268](https://github.com/vllm-project/vllm/issues/35268) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-Rerank model’s rerank API does not support query with mixed image and text inputs.

### Issue 正文摘录

### Your current environment vllm 0.14.0 ### 🐛 Describe the bug https://github.com/vllm-project/vllm/issues/32378 https://github.com/vllm-project/vllm/issues/33986 I am referring to the example https://github.com/vllm-project/vllm/blob/main/examples/pooling/score/vision_rerank_api_online.py and using qwen3-vl-rerank for reranking. However, in the provided example, the query is always a plain string, while my query is multimodal (image + text). The actual request payload I am sending is as follows: ``` { "model": "qwen3-vl-rerank-2b", "query": { "content": [ { "type": "text", "text": "this is a good thing" }, { "type": "image_url", "image_url": { "url": "..." } }, { "type": "image_url", "image_url": { "url": "..." } } ] }, "documents": [ { "content": [ { "type": "text", "text": "a text" }, { "type": "image_url", "image_url": { "url": "..." } } ] }, { "content": [ { "type": "text", "text": "b text" }, { "type": "image_url", "image_url": { "url": "..." } } ] }, { "content": [ { "type": "text", "text": "c text" }, { "type": "image_url", "image_url": { "url": "..." } } ] } ] } ``` After sending this request, the backend returns a 400 Bad Request error. @noooop

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL-Rerank model’s rerank API does not support query with mixed image and text inputs. bug ### Your current environment vllm 0.14.0 ### 🐛 Describe the bug https://github.com/vllm-project/vllm/issues/32378 ht...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: } } ] } ] } ``` After sending this request, the backend returns a 400 Bad Request error. @noooop
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: a plain string, while my query is multimodal (image + text). The actual request payload I am sending is as follows: ``` { "model": "qwen3-vl-rerank-2b", "query": { "content": [ { "type": "text", "text": "this is a good...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
