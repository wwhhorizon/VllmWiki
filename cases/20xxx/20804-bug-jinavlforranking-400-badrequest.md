# vllm-project/vllm#20804: [Bug]: JinaVLForRanking 400 BadRequest

| 字段 | 值 |
| --- | --- |
| Issue | [#20804](https://github.com/vllm-project/vllm/issues/20804) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: JinaVLForRanking 400 BadRequest

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This merger adds support for the JinaVL Reranker model ([[#20260](https://github.com/vllm-project/vllm/pull/20260)]). However, when I started the service and ran test calls, it returned a 400 Bad Request error. ### Online Serving ```text vllm serve jinaai/jina-reranker-m0 ``` ### Request ```text curl -X 'POST' \ 'http://127.0.0.1:8000/v1/rerank' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "model": "jinaai/jina-reranker-m0", "query": "slm markdown", "documents": { "content": [ { "type": "image_url", "image_url": { "url": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/handelsblatt-preview.png" } }, { "type": "image_url", "image_url": { "url": "https://raw.githubusercontent.com/jina-ai/multimodal-reranker-test/main/paper-11.png" } } ] } }' ``` ### Response ```text {"object":"error","message":"1 validation error for RerankDocument\nmulti_modal.content\n Field required [type=missing, input_value={'image_url': {'url': 'ht...'}, 'type': 'image_url'}, input_type=dict]\n For further information visit https://errors.pydantic.dev/2.11/v/missing","type":"BadRequestError","param":nul...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### 🐛 Describe the bug This merger adds support for the JinaVL Reranker model ([[#20260](https://github.com/vllm-project/vllm/pull/20260)]). However, when I started the service and ran test calls, it returned a 400 Bad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ou. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ext=documents[idx]) if isinstance( documents, list) else RerankDocument( multi_modal=documents["content"][idx]), relevance_score=classify_res.outputs.score, ) ... ``` For RerankDocument, the multi_modal attribute should...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: JinaVLForRanking 400 BadRequest bug ### Your current environment ### 🐛 Describe the bug This merger adds support for the JinaVL Reranker model ([[#20260](https://github.com/vllm-project/vllm/pull/20260)]). Howeve...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: -project/vllm/pull/20260)]). However, when I started the service and ran test calls, it returned a 400 Bad Request error. ### Online Serving ```text vllm serve jinaai/jina-reranker-m0 ``` ### Request ```text curl -X 'PO...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
