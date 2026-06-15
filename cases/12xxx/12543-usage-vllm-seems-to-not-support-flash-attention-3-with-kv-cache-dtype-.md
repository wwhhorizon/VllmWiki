# vllm-project/vllm#12543: [Usage]: vLLM seems to not support Flash Attention 3 with kv cache dtype 'fp8'

| 字段 | 值 |
| --- | --- |
| Issue | [#12543](https://github.com/vllm-project/vllm/issues/12543) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: vLLM seems to not support Flash Attention 3 with kv cache dtype 'fp8'

### Issue 正文摘录

### Your current environment I am running a vLLM instance to serve DeepSeek R1 on a 8xH200 node, using docker compose, whose service is defined as: ```yaml vllm: <<: *inference-service-cuda container_name: chat-completions profiles: [chat_completions_vllm] image: vllm/vllm-openai:v0.7.0 environment: # Backend for attention computation # Available options: # - "TORCH_SDPA": use torch.nn.MultiheadAttention # - "FLASH_ATTN": use FlashAttention # - "XFORMERS": use XFormers # - "ROCM_FLASH": use ROCmFlashAttention # - "FLASHINFER": use flashinfer (recommended for fp8 quantized models) - VLLM_ATTENTION_BACKEND=FLASH_ATTN - VLLM_FLASH_ATTN_VERSION=3 ipc: host command: ${DEEPSEEK_VLLM_ENGINE_ARGS} ```` where I specify both `FLASH_ATTN` backend with version `3`. The vLLM engine args is specified to run with `--kv-cache-dtype fp8`. Unfortunately, it seems the current logic does not allow running the model with flash attention backend, even if the version is 3. Here are the logs: ``` ds-chat-completions | INFO 01-29 01:53:21 cuda.py:185] Cannot use FlashAttention-2 backend for FP8 KV cache. ds-chat-completions | WARNING 01-29 01:53:21 cuda.py:187] Please use FlashInfer backend with FP8 KV Ca...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: am running a vLLM instance to serve DeepSeek R1 on a 8xH200 node, using docker compose, whose service is defined as: ```yaml vllm: <<: *inference-service-cuda container_name: chat-completions profiles: [chat_completions...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Usage]: vLLM seems to not support Flash Attention 3 with kv cache dtype 'fp8' usage ### Your current environment I am running a vLLM instance to serve DeepSeek R1 on a 8xH200 node, using docker compose, whose service i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: vLLM seems to not support Flash Attention 3 with kv cache dtype 'fp8' usage ### Your current environment I am running a vLLM instance to serve DeepSeek R1 on a 8xH200 node, using docker compose, whose service i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , whose service is defined as: ```yaml vllm: <<: *inference-service-cuda container_name: chat-completions profiles: [chat_completions_vllm] image: vllm/vllm-openai:v0.7.0 environment: # Backend for attention computation...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Usage]: vLLM seems to not support Flash Attention 3 with kv cache dtype 'fp8' usage ### Your current environment I am running a vLLM instance to serve DeepSeek R1 on a 8xH200 node, using docker compose, whose service i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
