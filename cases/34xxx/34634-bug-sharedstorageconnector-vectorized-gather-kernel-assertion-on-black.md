# vllm-project/vllm#34634: [Bug]: SharedStorageConnector: vectorized_gather_kernel assertion on Blackwell (B200) GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#34634](https://github.com/vllm-project/vllm/issues/34634) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SharedStorageConnector: vectorized_gather_kernel assertion on Blackwell (B200) GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # SharedStorageConnector: vectorized_gather_kernel assertion on Blackwell (B200) GPUs ## Summary Disaggregated serving with `SharedStorageConnector` crashes with a CUDA `vectorized_gather_kernel` index out-of-bounds assertion on Blackwell (B200, SM 10.0) GPUs. The crash occurs on the very first inference request when the prompt exceeds approximately 1 KV cache block (~16 tokens). Short prompts (~5 tokens) work correctly. ## Environment - **GPU**: NVIDIA B200 (Blackwell, SM 10.0) - **vLLM versions tested**: 0.10.2+9dd9ca32.nv25.10, 0.11.0+582e4e37.nv25.11 - **Container**: `nvcr.io/nvidia/vllm:25.10-py3`, `nvcr.io/nvidia/vllm:25.11-py3` - **Model**: Qwen3-30B-A3B-FP8 (prefill) / Qwen3-30B-A3B-NVFP4 (decode) - **Python**: 3.12 - **PyTorch**: 2.9.0a0 (nv25.10/nv25.11) - **CUDA**: 12.x - **Attention backend**: FlashInfer with HND KV cache layout, TRTLLM attention (query quantized) ## Reproduction ### 1. Start disaggregated servers ```bash # Prefill server (kv_producer, FP8 model) CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server \ --model /path/to/Qwen3-30B-A3B-FP8 \ --served-model-name model \ --host 0.0.0.0 --port...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: m:25.10-py3`, `nvcr.io/nvidia/vllm:25.11-py3` - **Model**: Qwen3-30B-A3B-FP8 (prefill) / Qwen3-30B-A3B-NVFP4 (decode) - **Python**: 3.12 - **PyTorch**: 2.9.0a0 (nv25.10/nv25.11) - **CUDA**: 12.x - **Attention backend**:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: SharedStorageConnector: vectorized_gather_kernel assertion on Blackwell (B200) GPUs bug ### Your current environment ### 🐛 Describe the bug # SharedStorageConnector: vectorized_gather_kernel assertion on Blackwel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: first inference request when the prompt exceeds approximately 1 KV cache block (~16 tokens). Short prompts (~5 tokens) work correctly. ## Environment - **GPU**: NVIDIA B200 (Blackwell, SM 10.0) - **vLLM versions tested*...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: y. ## Environment - **GPU**: NVIDIA B200 (Blackwell, SM 10.0) - **vLLM versions tested**: 0.10.2+9dd9ca32.nv25.10, 0.11.0+582e4e37.nv25.11 - **Container**: `nvcr.io/nvidia/vllm:25.10-py3`, `nvcr.io/nvidia/vllm:25.11-py3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: kwell (B200, SM 10.0) GPUs. The crash occurs on the very first inference request when the prompt exceeds approximately 1 KV cache block (~16 tokens). Short prompts (~5 tokens) work correctly. ## Environment - **GPU**: N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
