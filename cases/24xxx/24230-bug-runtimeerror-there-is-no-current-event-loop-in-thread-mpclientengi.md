# vllm-project/vllm#24230: [Bug]: RuntimeError: There is no current event loop in thread 'MPClientEngineMonitor'.

| 字段 | 值 |
| --- | --- |
| Issue | [#24230](https://github.com/vllm-project/vllm/issues/24230) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: There is no current event loop in thread 'MPClientEngineMonitor'.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash uv run vllm serve meta-llama/Llama-3.1-8B-Instruct --tool-call-parser llama3_json --chat-template custom/tool_chat_template_llama3.1_json.jinja --enable-auto-tool-choice ``` ```python INFO 09-02 17:27:42 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=82793) INFO 09-02 17:27:43 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=82793) INFO 09-02 17:27:43 [utils.py:326] non-default args: {'model_tag': 'meta-llama/Llama-3.1-8B-Instruct', 'chat_template': 'custom/tool_chat_template_llama3.1_json.jinja', 'enable_auto_tool_choice': True, 'tool_call_parser': 'llama3_json', 'model': 'meta-llama/Llama-3.1-8B-Instruct'} (APIServer pid=82793) INFO 09-02 17:27:48 [__init__.py:711] Resolved architecture: LlamaForCausalLM (APIServer pid=82793) INFO 09-02 17:27:48 [__init__.py:1750] Using max model len 131072 (APIServer pid=82793) INFO 09-02 17:27:49 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 09-02 17:27:52 [__init__.py:241] Automatically detected platform cuda. (EngineCore_0 pid=83066) INFO 09-02 17:27:53 [core.py:636] Waiting for init message from fron...

## 现有链接修复摘要

#24422 [Bugfix] Fix 'no event loop' RuntimeError in MPClientEngineMonitor

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rver pid=82793) INFO 09-02 17:27:43 [api_server.py:1805] vLLM API server version 0.10.1.1 (APIServer pid=82793) INFO 09-02 17:27:43 [utils.py:326] non-default args: {'model_tag': 'meta-llama/Llama-3.1-8B-Instruct', 'cha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_al...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment ### 🐛 Describe the bug ```bash uv run vllm serve meta-llama/Llama-3.1-8B-Instruct --tool-call-parser llama3_json --chat-template custom/tool_chat_template_llama3.1_json.jinja --enable-auto-tool-choice ``` ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 0] Using max model len 131072 (APIServer pid=82793) INFO 09-02 17:27:49 [scheduler.py:222] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 09-02 17:27:52 [__init__.py:241] Automatically detected platfo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24422](https://github.com/vllm-project/vllm/pull/24422) | closes_keyword | 0.95 | [Bugfix] Fix 'no event loop' RuntimeError in MPClientEngineMonitor | Resolves #24230 #24305 ## Test Plan 1. Run any model - In my Case: Llama-3.1-8B-Instruct ``` uv run vllm serve meta-llama/Llama-3.1-8B-Instruct --tool-call-parser llama3_json --c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
