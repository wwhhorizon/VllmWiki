# vllm-project/vllm#42391: [Bug]: `/v1/rerank` ignores `chat_template_kwargs` - Qwen3-Reranker per-task `Instruct` cannot be set per request

| 字段 | 值 |
| --- | --- |
| Issue | [#42391](https://github.com/vllm-project/vllm/issues/42391) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `/v1/rerank` ignores `chat_template_kwargs` - Qwen3-Reranker per-task `Instruct` cannot be set per request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The shipped Qwen3-Reranker chat template (`examples/pooling/score/template/qwen3_reranker.jinja`) contains a placeholder for the per-task Instruct: ```jinja : {{ messages | selectattr("role", "eq", "system") | map(attribute="content") | first | default("Given a web search query, retrieve relevant passages that answer the query") }} ``` But there is **no way** to populate that placeholder per request through `/v1/rerank`: 1. `RerankRequest` inherits `chat_template_kwargs` (via `ClassifyRequestMixin`), so clients can already send it - but the rerank handler **does not forward it** to `apply_chat_template`. See `vllm/entrypoints/pooling/score/utils.py` (`get_score_prompt`): it calls ```python safe_apply_chat_template( model_config, tokenizer, [{"role": "query", "content": prompt_1}, {"role": "document", "content": prompt_2}], chat_template=score_template, tools=None, tokenize=False, ) ``` `request.chat_template_kwargs` is never threaded through. 2. The rerank handler constructs the messages list internally as `[query, document]` only - no `system` role produced. 3. The Qwen3-Reranker model card (https://huggingface.co/Qwen/Qwen3-Rer...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: `/v1/rerank` ignores `chat_template_kwargs` - Qwen3-Reranker per-task `Instruct` cannot be set per request bug ### Your current environment ### 🐛 Describe the bug The shipped Qwen3-Reranker chat template (`exampl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Reranker model card (https://huggingface.co/Qwen/Qwen3-Reranker-4B) explicitly recommends per-task Instructs as a primary feature, and the **offline** example (`examples/pooling/score/qwen3_reranker_offline.py`) formats...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: equest bug ### Your current environment ### 🐛 Describe the bug The shipped Qwen3-Reranker chat template (`examples/pooling/score/template/qwen3_reranker.jinja`) contains a placeholder for the per-task Instruct: ```jinja...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: prompt_2}], chat_template=score_template, tools=None, tokenize=False, ) ``` `request.chat_template_kwargs` is never threaded through. 2. The rerank handler constructs the messages list internally as `[query, document]`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
