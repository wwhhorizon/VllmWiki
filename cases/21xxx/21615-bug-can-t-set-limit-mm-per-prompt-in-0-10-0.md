# vllm-project/vllm#21615: [Bug]: Can't set limit-mm-per-prompt in 0.10.0

| 字段 | 值 |
| --- | --- |
| Issue | [#21615](https://github.com/vllm-project/vllm/issues/21615) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;gemm;moe;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't set limit-mm-per-prompt in 0.10.0

### Issue 正文摘录

### Your current environment I am trying to set limit-mm-per-prompt, to ensure only 4 images are allowed. This worked with 0.9.2, but no longer in 0.10.0. ### 🐛 Describe the bug ``` $ kubectl logs llm-gemma3-27b-85b98c5ddf-5859g -f Defaulted container "gemma3-27b" out of: gemma3-27b, gemma3-27b-gpu-test (init) usage: api_server.py [-h] [--headless] [--api-server-count API_SERVER_COUNT] [--config CONFIG] [--host HOST] [--port PORT] [--uvicorn-log-level {critical,debug,error,info,trace,warning}] [--disable-uvicorn-access-log | --no-disable-uvicorn-access-log] [--allow-credentials | --no-allow-credentials] [--allowed-origins ALLOWED_ORIGINS] [--allowed-methods ALLOWED_METHODS] [--allowed-headers ALLOWED_HEADERS] [--api-key API_KEY] [--lora-modules LORA_MODULES [LORA_MODULES ...]] [--chat-template CHAT_TEMPLATE] [--chat-template-content-format {auto,openai,string}] [--response-role RESPONSE_ROLE] [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE] [--ssl-ca-certs SSL_CA_CERTS] [--enable-ssl-refresh | --no-enable-ssl-refresh] [--ssl-cert-reqs SSL_CERT_REQS] [--root-path ROOT_PATH] [--middleware MIDDLEWARE] [--return-tokens-as-token-ids | --no-return-tokens-as-token-ids] [--disabl...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: ut no longer in 0.10.0. ### 🐛 Describe the bug ``` $ kubectl logs llm-gemma3-27b-85b98c5ddf-5859g -f Defaulted container "gemma3-27b" out of: gemma3-27b, gemma3-27b-gpu-test (init) usage: api_server.py [-h] [--headless]...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [--trust-remote-code | --no-trust-remote-code] [--dtype {auto,bfloat16,float,float16,float32,half}] [--seed SEED] [--hf-config-path HF_CONFIG_PATH] [--allowed-local-media-path ALLOWED_LOCAL_MEDIA_PATH] [--re
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: | --no-disable-frontend-multiprocessing] [--enable-request-id-headers | --no-enable-request-id-headers] [--enable-auto-tool-choice | --no-enable-auto-tool-choice] [--tool-call-parser {deepseek_v3,glm4_moe,granite-20b-fc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: | --no-enable-multimodal-encoder-data-parallel] [--block-size {1,8,16,32,64,128}] [--gpu-memory-utilization GPU_MEMORY_UTILIZATION] [--swap-space SWAP_SPACE] [--kv-cache-dtype {auto,fp8,fp8_e4m3,fp8_e5m2,fp8_
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ut no longer in 0.10.0. ### 🐛 Describe the bug ``` $ kubectl logs llm-gemma3-27b-85b98c5ddf-5859g -f Defaulted container "gemma3-27b" out of: gemma3-27b, gemma3-27b-gpu-test (init) usage: api_server.py [-h] [--headless]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
