# vllm-project/vllm#9187: [Bug]: AttributeError: 'CachedChatGLM4Tokenizer' object has no attribute 'vocab'

| 字段 | 值 |
| --- | --- |
| Issue | [#9187](https://github.com/vllm-project/vllm/issues/9187) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'CachedChatGLM4Tokenizer' object has no attribute 'vocab'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm version is v0.6.2 refer this doc https://docs.vllm.ai/en/v0.6.2/getting_started/cpu-installation.html, build from Dockerfile.cpu. glm-4-9b-chat download from modelscope request /v1/chat/completions debug log: `INFO 10-09 08:57:11 logger.py:36] Received request chat-23a5dc203cc54f79851da3338a215f75: prompt: '[gMASK] \n你是谁 ', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.01, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2000, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [151331, 151333, 151336, 198, 103408, 99668, 151337], lora_request: None, prompt_adapter_request: None. INFO: 192.168.10.77:51198 - "POST /v1/chat/completions HTTP/1.1" 200 OK ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-pac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: t ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm version is v0.6.2 refer this doc https://docs.vllm.ai/en/v0.6.2/getting_started/cpu-installation.html, build from Dockerfile.cpu. glm-4-9b-chat download...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e, sender) | File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ | await self.middleware_stack(scope, receive, send) | File "/usr/local/lib/python3.10/dist-packages/starlette/routi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: temperature=0.01, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=20...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ature=0.01, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2000, mi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: object has no attribute 'vocab' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vllm version is v0.6.2 refer this doc https://docs.vllm.ai/en/v0.6.2/getting_started/cpu-instal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
