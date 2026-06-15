# vllm-project/vllm#17505: Issue attempting to serve a model from HF with base model `Llama-3.1-8B-Instruct`

| 字段 | 值 |
| --- | --- |
| Issue | [#17505](https://github.com/vllm-project/vllm/issues/17505) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue attempting to serve a model from HF with base model `Llama-3.1-8B-Instruct`

### Issue 正文摘录

I am attempting to deploy and serve this model from HF: https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-8B The base model is [meta-llama/Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) with Finetuned [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) Based on the model card, it says `vLLM` is supported. I was able to deploy this in a k8s clusters on GKE. I followed the steps outlined here: https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-llama-gpus-vllm ``` INFO: Started server process [145] INFO: Waiting for application startup. INFO: Application startup complete. ``` However, when I attempt to make requests to the model, I keep getting empty response. ``` curl -X POST http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "FreedomIntelligence/HuatuoGPT-o1-8B", "prompt": "Help with my cough and fever", "max_tokens": 2048, "temperature": 0 }' curl: (52) Empty reply from server curl http://localhost:8000/v1/models {"object":"list","data":[{"id":"FreedomIntelligence/HuatuoGPT-o1-8B","object":"model","created":1746054138,"owned_by":"vllm","root":"FreedomIntelligence/Huat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Issue attempting to serve a model from HF with base model `Llama-3.1-8B-Instruct` stale I am attempting to deploy and serve this model from HF: https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-8B The base model i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: empting to serve a model from HF with base model `Llama-3.1-8B-Instruct` stale I am attempting to deploy and serve this model from HF: https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-8B The base model is [meta-l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ## The closest model vllm already supports. The basemodel is fine-tuned version of `Llama-3.1-8B` officially supported by vLLM: https://blog.vllm.ai/2024/07/23/llama31.html ### What's your difficulty of supporting the m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: "object":"model_permission","created":1746054138,"allow_create_engine":false,"allow_sampling":true,"allow_logprobs":true,"allow_search_indices":false,"allow_view":true,"allow_fine_tuning":false,"organization":"*","group...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: reate_engine":false,"allow_sampling":true,"allow_logprobs":true,"allow_search_indices":false,"allow_view":true,"allow_fine_tuning":false,"organization":"*","group":null,"is_blocking":false}]}] ``` ### The closest model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
