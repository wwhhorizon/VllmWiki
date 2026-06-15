# vllm-project/vllm#31588: [Bug]: vLLM SM 12.1 (Blackwell GB10) V1 Engine Bug Report (Relates to: #28589, #31128, #28621, #27679)

| 字段 | 值 |
| --- | --- |
| Issue | [#31588](https://github.com/vllm-project/vllm/issues/31588) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM SM 12.1 (Blackwell GB10) V1 Engine Bug Report (Relates to: #28589, #31128, #28621, #27679)

### Issue 正文摘录

# vLLM SM 12.1 (Blackwell GB10) V1 Engine Bug Report **Relates to:** [#28589](https://github.com/vllm-project/vllm/issues/28589), [#31128](https://github.com/vllm-project/vllm/issues/31128), [#28621](https://github.com/vllm-project/vllm/issues/28621), [#27679](https://github.com/vllm-project/vllm/issues/27679) --- ## Summary V1 engine crashes with `AttributeError: 'NoneType' object has no attribute 'sampled_token_ids'` on first inference when async scheduling is enabled (default). This affects all SM 12.1 (Blackwell GB10) users and potentially other platforms. **Root Cause:** Missing `None` check in `step_with_batch_queue()` method. --- ## 1. Issue Analysis ### Environment | Component | Version | |-----------|---------| | GPU | NVIDIA GB10 (SM 12.1 / compute_121) | | CUDA | 13.0 | | PyTorch | 2.9.1 (max SM 12.0 support) | | vLLM | 0.14.0rc1+ | | OS | Linux 6.14.0 (ARM64) | ``` Collecting environment information... uv is set /home/ohsono/vllm/.venv/lib/python3.12/site-packages/torch/cuda/__init__.py:283: UserWarning: Found GPU0 NVIDIA GB10 which is of cuda capability 12.1. Minimum and Maximum cuda capability supported by this version of PyTorch is (8.0) - (12.0) warnings.warn( ====...

## 现有链接修复摘要

#31607 [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: eue()` method. --- ## 1. Issue Analysis ### Environment | Component | Version | |-----------|---------| | GPU | NVIDIA GB10 (SM 12.1 / compute_121) | | CUDA | 13.0 | | PyTorch | 2.9.1 (max SM 12.0 support) | | vLLM | 0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: vLLM SM 12.1 (Blackwell GB10) V1 Engine Bug Report (Relates to: #28589, #31128, #28621, #27679) bug # vLLM SM 12.1 (Blackwell GB10) V1 Engine Bug Report **Relates to:** [#28589](https://github.com/vllm-project/vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti ecv afp wfxt Model name: Cortex-A725 Model: 1 Thread(s) per core: 1 Core(s) per socket: 10 S
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: her platforms. **Root Cause:** Missing `None` check in `step_with_batch_queue()` method. --- ## 1. Issue Analysis ### Environment | Component | Version | |-----------|---------| | GPU | NVIDIA GB10 (SM 12.1 / compute_12...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ===== Environment Variables ============================== VLLM_USE_FLASHINFER_MOE_MXFP4_BF16=1 TORCH_CUDA_ARCH_LIST=12.0f PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 ``` ### Error ```python File "vl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31607](https://github.com/vllm-project/vllm/pull/31607) | closes_keyword | 0.95 | [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes | Fixes #31588 - **CUTLASS ops graceful fallback** (`vllm/_custom_ops.py`): `AttributeError` handling for missing CUTLASS ops on incomplete builds - **Compilation ops compatibility* |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
