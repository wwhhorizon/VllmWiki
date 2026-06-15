# vllm-project/vllm#22331: [Bug]: vllm/vllm-openai:gptoss AssertionError: Sinks are only supported in FlashAttention 3 (4090 48gb)

| 字段 | 值 |
| --- | --- |
| Issue | [#22331](https://github.com/vllm-project/vllm/issues/22331) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 72; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai:gptoss AssertionError: Sinks are only supported in FlashAttention 3 (4090 48gb)

### Issue 正文摘录

I run vllm in docker image `vllm/vllm-openai:gptoss` I use this video card 4090(48gb x2) and this docker-compose.yaml ``` services: vllm-server: image: vllm/vllm-openai:gptoss container_name: gpt-oss-120b-vllm-server restart: always shm_size: 40g ports: - "8000:8000" volumes: - ~/.cache/huggingface:/root/.cache/huggingface deploy: resources: reservations: devices: - driver: nvidia device_ids: ["0", "1"] capabilities: [gpu] environment: - HUGGING_FACE_HUB_TOKEN=... - CUDA_VISIBLE_DEVICES=0,1 - TENSOR_PARALLEL_SIZE=2 # - FORCE_BLACKWELL=1 # - VLLM_USE_TRTLLM_ATTENTION=1 # - VLLM_USE_TRTLLM_DECODE_ATTENTION=1 # - VLLM_USE_TRTLLM_CONTEXT_ATTENTION=1 # - VLLM_USE_FLASHINFER_MXFP4_MOE=1 - GPU_MEMORY_UTILIZATION=0.90 - MAX_NUM_BATCHED_TOKENS=1024 - VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 command: [ "--model", "openai/gpt-oss-120b", "--served-model-name", "gpt-oss-120b", "--host", "0.0.0.0", "--port", "8000", "--tensor-parallel-size", "2", "--trust-remote-code", "--enforce-eager", "--disable-custom-all-reduce", "--gpu-memory-utilization", "0.85", "--max-model-len", "16384", "--max-num-seqs", "4", "--distributed-executor-backend", "ray", "--dtype", "auto" ] healthcheck: test: ["CMD", "curl", "-f",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e only supported in FlashAttention 3 (4090 48gb) bug;stale I run vllm in docker image `vllm/vllm-openai:gptoss` I use this video card 4090(48gb x2) and this docker-compose.yaml ``` services: vllm-server: image: vllm/vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ug]: vllm/vllm-openai:gptoss AssertionError: Sinks are only supported in FlashAttention 3 (4090 48gb) bug;stale I run vllm in docker image `vllm/vllm-openai:gptoss` I use this video card 4090(48gb x2) and this docker-co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: # - VLLM_USE_TRTLLM_CONTEXT_ATTENTION=1 # - VLLM_USE_FLASHINFER_MXFP4_MOE=1 - GPU_MEMORY_UTILIZATION=0.90 - MAX_NUM_BATCHED_TOKENS=1024 - VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 command: [ "--model", "openai/gpt-oss-120b", "--s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s: vllm-server: image: vllm/vllm-openai:gptoss container_name: gpt-oss-120b-vllm-server restart: always shm_size: 40g ports: - "8000:8000" volumes: - ~/.cache/huggingface:/root/.cache/huggingface deploy: resources: rese...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ties: [gpu] environment: - HUGGING_FACE_HUB_TOKEN=... - CUDA_VISIBLE_DEVICES=0,1 - TENSOR_PARALLEL_SIZE=2 # - FORCE_BLACKWELL=1 # - VLLM_USE_TRTLLM_ATTENTION=1 # - VLLM_USE_TRTLLM_DECODE_ATTENTION=1 # - VLLM_USE_TRTLLM_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
