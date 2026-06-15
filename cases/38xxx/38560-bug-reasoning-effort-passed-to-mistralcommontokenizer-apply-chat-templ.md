# vllm-project/vllm#38560: [Bug]: reasoning_effort passed to MistralCommonTokenizer.apply_chat_template breaks Mistral Small 4 chat completions on vLLM 0.18.0

| 字段 | 值 |
| --- | --- |
| Issue | [#38560](https://github.com/vllm-project/vllm/issues/38560) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: reasoning_effort passed to MistralCommonTokenizer.apply_chat_template breaks Mistral Small 4 chat completions on vLLM 0.18.0

### Issue 正文摘录

### Your current environment Environment vLLM: 0.18.0 (e.g. Docker image vllm/vllm-openai or internal vllm-audio:v0.18.0) Model: mistralai/Mistral-Small-4-119B-2603 (or equivalent weights served with Mistral tokenizer path) Hardware / stack: (fill in: GPU type, CUDA, --tensor-parallel-size, etc.) ### 🐛 Describe the bug Problem POST /v1/chat/completions fails with 400 and: ValueError: Kwargs ['reasoning_effort'] are not supported by `MistralCommonTokenizer.apply_chat_template`. The failure occurs in vLLM’s Mistral chat rendering path, e.g.: File ".../vllm/entrypoints/openai/chat_completion/serving.py", line 209, in render_chat_request return await self.openai_serving_render.render_chat(request) ... File ".../vllm/renderers/mistral.py", line 125, in render_messages_async prompt_raw = await self._apply_chat_template_async( ... File ".../vllm/renderers/mistral.py", line 34, in safe_apply_chat_template return tokenizer.apply_chat_template(messages, **kwargs) ... File ".../transformers/tokenization_mistral_common.py", line 1432, in apply_chat_template raise ValueError( ValueError: Kwargs ['reasoning_effort'] are not supported by `MistralCommonTokenizer.apply_chat_template`. Reproduction...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 0.18.0 bug ### Your current environment Environment vLLM: 0.18.0 (e.g. Docker image vllm/vllm-openai or internal vllm-audio:v0.18.0) Model: mistralai/Mistral-Small-4-119B-2603 (or equivalent weights served with Mistral...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fort passed to MistralCommonTokenizer.apply_chat_template breaks Mistral Small 4 chat completions on vLLM 0.18.0 bug ### Your current environment Environment vLLM: 0.18.0 (e.g. Docker image vllm/vllm-openai or internal...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: minimal call is enough to trigger the error (LiteLLM is not required—we reproduced with direct HTTP to vLLM). Example: ``` curl -sS "http:// :8000/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 18.0 (e.g. Docker image vllm/vllm-openai or internal vllm-audio:v0.18.0) Model: mistralai/Mistral-Small-4-119B-2603 (or equivalent weights served with Mistral tokenizer path) Hardware / stack: (fill in: GPU type, CUDA,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: entrypoints/openai/chat_completion/serving.py", line 209, in render_chat_request return await self.openai_serving_render.render_chat(request) ... File ".../vllm/renderers/mistral.py", line 125, in render_messages_async...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
