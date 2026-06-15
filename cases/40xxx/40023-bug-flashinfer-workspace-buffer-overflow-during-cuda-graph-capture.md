# vllm-project/vllm#40023: [Bug]: FlashInfer workspace buffer overflow during CUDA graph capture

| 字段 | 值 |
| --- | --- |
| Issue | [#40023](https://github.com/vllm-project/vllm/issues/40023) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;quantization |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer workspace buffer overflow during CUDA graph capture

### Issue 正文摘录

### Your current environment - vLLM: `0.19.1rc1.dev231+g9dd5ee011.cu130` - Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` - Hardware: B300 ### 🐛 Describe the bug ## Summary vLLM crashes during server startup with FlashInfer `aligned_alloc` buffer overflow. See error and stack trace below. Related: #25342 ## Reproduce ```bash python3 -m vllm.entrypoints.openai.api_server \ --model nvidia/Qwen3.5-397B-A17B-NVFP4 \ --data-parallel-size 8 \ --kv-cache-dtype fp8_e4m3 \ --max-num-seqs 528 \ --trust-remote-code \ --max-model-len 3072 \ --gpu-memory-utilization 0.85 \ --no-enable-prefix-caching \ --language-model-only \ --async-scheduling \ --attention-backend FLASHINFER \ --enable-expert-parallel \ --quantization modelopt \ --host 0.0.0.0 --port 60000 ``` ## Error ``` RuntimeError: Error in function 'aligned_alloc' at /workspace/include/flashinfer/allocator.h:49: Buffer overflow when allocating memory for batch_prefill_tmp_v with size 536346624 and alignment 16, but only 413138944 bytes available in AlignedAllocator. Increase the workspace buffer size. ``` ## Affected configurations Observed with `nvidia/Qwen3.5-397B-A17B-NVFP4` on B300. Crashes at startup with `--max-num-seqs 528` and above: -...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: : `0.19.1rc1.dev231+g9dd5ee011.cu130` - Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` - Hardware: B300 ### 🐛 Describe the bug ## Summary vLLM crashes during server startup with FlashInfer `aligned_alloc` buffer overflow. See...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ization': 0.85, 'kv_cache_dtype': 'fp8_e4m3', 'enable_prefix_caching': False, 'language_model_only': True, 'max_num_seqs': 528, 'async_scheduling': True} (APIServer pid=1936149) INFO 04-13 17:08:09 [model.py:554] Resolv...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Your current environment - vLLM: `0.19.1rc1.dev231+g9dd5ee011.cu130` - Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` - Hardware: B300 ### 🐛 Describe the bug ## Summary vLLM crashes during server startup with FlashInfer `align...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _GPU_MEMORY_UTILIZATION_ARG='--gpu-memory-utilization 0.85' vLLM runtime version: 0.19.1rc1.dev231+g9dd5ee011.cu130 Starting vLLM server... + python3 -m vllm.entrypoints.openai.api_server --model nvidia/Qwen3.5-397B-A17...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: infer/allocator.h:49: Buffer overflow when allocating memory for batch_prefill_tmp_v with size 536346624 and alignment 16, but only 413138944 bytes available in AlignedAllocator. Increase the workspace buffer size. ```...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
