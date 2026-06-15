# vllm-project/vllm#5976: [Bug]: New bug in last few days for phi-3-vision. The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (50944)

| 字段 | 值 |
| --- | --- |
| Issue | [#5976](https://github.com/vllm-project/vllm/issues/5976) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: New bug in last few days for phi-3-vision. The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (50944)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Same launching as https://github.com/vllm-project/vllm/issues/5969 Only difference is hash 2cd402e1692417b7645e4ece11bc2ab91072f47c (latest main as of earlier today). GPU is totally free, so just new bug in vLLM between the e9de9dd551ac595a9f3825fcd1507deceef4f332 and 2cd402e1692417b7645e4ece11bc2ab91072f47c hashes ``` INFO 06-28 23:40:03 api_server.py:206] vLLM API server version 0.5.0.post1 INFO 06-28 23:40:03 api_server.py:207] args: Namespace(host='0.0.0.0', port=5063, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, respon> INFO 06-28 23:40:03 llm_engine.py:164] Initializing an LLM engine (v0.5.0.post1) with config: model='microsoft/Phi-3-vision-128k-instruct', speculative_config=None, tokenizer='microsoft/Phi-3-vision-128k-instruct', skip_tokenizer_init=False, tokenizer_mode=auto> Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained. INFO 06-28 23:40:04 selector.py:171] Cannot use FlashAtte...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: New bug in last few days for phi-3-vision. The model's max seq len (131072) is larger than the maximum number of tokens that can be stored in KV cache (50944) bug ### Your current environment ```text The output o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e fine-tuned or trained. INFO 06-28 23:40:04 selector.py:171] Cannot use FlashAttention-2 backend due to sliding window. INFO 06-28 23:40:04 selector.py:53] Using XFormers backend. INFO 06-28 23:40:04 selector.py:171] C...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 2f47c hashes ``` INFO 06-28 23:40:03 api_server.py:206] vLLM API server version 0.5.0.post1 INFO 06-28 23:40:03 api_server.py:207] args: Namespace(host='0.0.0.0', port=5063, uvicorn_log_level='info', allow_credentials=F...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: host='0.0.0.0', port=5063, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, chat_template=None, respon> INFO 06-28...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 31072) is larger than the maximum number of tokens that can be stored in KV cache (50944) bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Same launching as https...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
