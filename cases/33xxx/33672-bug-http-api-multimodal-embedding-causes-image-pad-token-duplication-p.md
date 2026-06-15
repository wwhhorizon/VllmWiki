# vllm-project/vllm#33672: [Bug]: HTTP API multimodal embedding causes image_pad token duplication, producing incorrect results

| 字段 | 值 |
| --- | --- |
| Issue | [#33672](https://github.com/vllm-project/vllm/issues/33672) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;gemm;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HTTP API multimodal embedding causes image_pad token duplication, producing incorrect results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the HTTP API `/v1/embeddings` endpoint with multimodal inputs (e.g., images), the embedding results are **incorrect** due to `image_pad` token duplication. ### Root Cause In `vllm/entrypoints/openai/engine/serving.py`, the `_build_prompt_from_messages_async` function pre-tokenizes the prompt before merging `multi_modal_data`. However, when `InputProcessor` later processes the `TokensPrompt` with `multi_modal_data`, it inserts `image_pad` tokens again, causing duplication. **Problematic code** (`serving.py:_build_prompt_from_messages_async`): ```python if "prompt_token_ids" not in engine_prompt: extra_data = engine_prompt engine_prompt = await self._tokenize_prompt_input_async( request, renderer.get_tokenizer(), engine_prompt["prompt"], add_special_tokens=add_special_tokens, ) # Fill in other keys like MM data engine_prompt.update(extra_data) # " + text vllm_input = {"prompt": prompt, "multi_modal_data": {"image": images[0]}} outputs = llm.embed([vllm_input]) embedding_sdk = outputs[0].outputs.embedding # === Compare === import numpy as np def cosine_similarity(a, b): return np.dot(a, b) / (np.linalg.norm(a) * np.linalg...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : HTTP API multimodal embedding causes image_pad token duplication, producing incorrect results bug;stale ### Your current environment ### 🐛 Describe the bug When using the HTTP API `/v1/embeddings` endpoint with multim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: engine_prompt) ``` ## Before submitting a new issue... - [x] I have searched for relevant issues and found no existing report for this bug - [x] I have verified this is a vLLM issue (not transformers) - [x] The SDK work...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: HTTP API multimodal embedding causes image_pad token duplication, producing incorrect results bug;stale ### Your current environment ### 🐛 Describe the bug When using the HTTP API `/v1/embeddings` endpoint with m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ding causes image_pad token duplication, producing incorrect results bug;stale ### Your current environment ### 🐛 Describe the bug When using the HTTP API `/v1/embeddings` endpoint with multimodal inputs (e.g., images),...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_api;hardware_porting;model_support;multimodal_vlm activation;cuda;gemm;triton build_error;mismatch dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
