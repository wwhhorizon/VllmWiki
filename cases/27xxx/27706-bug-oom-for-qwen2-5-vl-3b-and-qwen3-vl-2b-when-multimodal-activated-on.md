# vllm-project/vllm#27706: [Bug]: OOM for Qwen2.5-VL-3B and Qwen3-VL-2B when multimodal activated on RX 7800 XT

| 字段 | 值 |
| --- | --- |
| Issue | [#27706](https://github.com/vllm-project/vllm/issues/27706) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM for Qwen2.5-VL-3B and Qwen3-VL-2B when multimodal activated on RX 7800 XT

### Issue 正文摘录

### Your current environment I built docker image from latest vllm. I tried **Qwen2.5-VL-3B** and **Qwen3-VL-2B** models. Both expecting 256GB when multimodal activated. Seems memory leak because 2B & 3B models should not require 256GB ``` root@cachyos-x8664:/app# vllm serve Qwen/Qwen3-VL-2B-Instruct \ --host 0.0.0.0 \ --port 8000 \ --limit-mm-per-prompt '{"image":1,"video":0}' \ --max-model-len 2K \ --max-num-seqs 1 \ --max-num-batched-tokens 2K DEBUG 10-29 01:56:35 [plugins/__init__.py:32] No plugins for group vllm.platform_plugins found. DEBUG 10-29 01:56:35 [platforms/__init__.py:36] Checking if TPU platform is available. DEBUG 10-29 01:56:35 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' DEBUG 10-29 01:56:35 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 10-29 01:56:35 [platforms/__init__.py:88] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBUG 10-29 01:56:35 [platforms/__init__.py:105] CUDA platform is not available because: NVML Shared Library Not Found DEBUG 10-29 01:56:35 [platforms/__init__.py:112] Checking if ROCm platform is available. DEBUG 10-29 01:56:35 [platforms/...

## 现有链接修复摘要

#38334 [ROCm] Use Triton attention fallback for ViT to avoid SDPA OOM

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ctivated on RX 7800 XT bug;rocm ### Your current environment I built docker image from latest vllm. I tried **Qwen2.5-VL-3B** and **Qwen3-VL-2B** models. Both expecting 256GB when multimodal activated. Seems memory leak...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: OOM for Qwen2.5-VL-3B and Qwen3-VL-2B when multimodal activated on RX 7800 XT bug;rocm ### Your current environment I built docker image from latest vllm. I tried **Qwen2.5-VL-3B** and **Qwen3-VL-2B** models. Bot...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ed on current platform. (APIServer pid=1487) INFO 10-29 01:56:41 [config/scheduler.py:211] Chunked prefill is enabled with max_num_batched_tokens=2048. (APIServer pid=1487) DEBUG 10-29 01:56:41 [config/parallel.py:599]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: y:225] Automatically detected platform rocm. DEBUG 10-29 01:56:37 [utils/flashinfer.py:41] FlashInfer unavailable since package was not found DEBUG 10-29 01:56:39 [entrypoints/utils.py:175] Setting VLLM_WORKER_MULTIPROC...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38334](https://github.com/vllm-project/vllm/pull/38334) | closes_keyword | 0.95 | [ROCm] Use Triton attention fallback for ViT to avoid SDPA OOM | Fixes #36890 Related: #27706 ## Test plan - [ ] Verify Qwen3.5-0.8B starts without OOM on gfx906 - [ ] Verify existing ViT attention tests still pass on MI300X/MI325X - [ ] Verify |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
