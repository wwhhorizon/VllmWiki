# vllm-project/vllm#41849: [Bug]: Engine crashes on startup with 'DeepGEMM backend not available' for standard bf16 models on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#41849](https://github.com/vllm-project/vllm/issues/41849) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;kernel;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine crashes on startup with 'DeepGEMM backend not available' for standard bf16 models on H100

### Issue 正文摘录

## Describe the bug vLLM 0.20.1 crashes during engine initialization with `RuntimeError: DeepGEMM backend is not available` even when running a standard bf16 model with no FP8 quantization. `deep_gemm_warmup` is called unconditionally for all models, making it impossible to start vLLM on H100 without installing the optional `deep_gemm` package. ## Environment - **vLLM version:** 0.20.1 - **Python:** 3.12 - **GPU:** NVIDIA H100 80 GB HBM3 SXM5 - **CUDA:** 13.0 / torch 2.11.0+cu130 - **OS:** Ubuntu 24.04 - **Model:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (bf16, no quantization) - `deep_gemm` **not installed** ## Steps to reproduce ```bash pip install vllm # 0.20.1, without deep_gemm vllm serve TinyLlama/TinyLlama-1.1B-Chat-v1.0 \ --gpu-memory-utilization 0.85 --max-model-len 2048 ``` ## Error ``` (EngineCore pid=...) ERROR [core.py:1136] EngineCore failed to start. (EngineCore pid=...) ERROR [core.py:1136] Traceback (most recent call last): ... File ".../vllm/v1/worker/gpu_worker.py", line 586, in compile_or_warm_up_model kernel_warmup(self) File ".../vllm/model_executor/warmup/kernel_warmup.py", line 37, in kernel_warmup deep_gemm_warmup(model, max_tokens) File ".../vllm/model_execu...

## 现有链接修复摘要

#41850 platforms: handle MIG device UUID in device_id_to_physical_device_id | #41851 warmup: skip deep_gemm warmup when DeepGEMM is not available

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nally for all models, making it impossible to start vLLM on H100 without installing the optional `deep_gemm` package. ## Environment - **vLLM version:** 0.20.1 - **Python:** 3.12 - **GPU:** NVIDIA H100 80 GB HBM3 SXM5 -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ne crashes on startup with 'DeepGEMM backend not available' for standard bf16 models on H100 ## Describe the bug vLLM 0.20.1 crashes during engine initialization with `RuntimeError: DeepGEMM backend is not available` ev...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: p/deep_gemm_warmup.py", line 136, in _fp8_linear_may_use_deep_gemm block_size = get_mk_alignment_for_contiguous_layout()[0] File ".../vllm/utils/deep_gemm.py", line 266, in get_mk_alignment_for_contiguous_layout return...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tartup with 'DeepGEMM backend not available' for standard bf16 models on H100 ## Describe the bug vLLM 0.20.1 crashes during engine initialization with `RuntimeError: DeepGEMM backend is not available` even when running...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ashes on startup with 'DeepGEMM backend not available' for standard bf16 models on H100 ## Describe the bug vLLM 0.20.1 crashes during engine initialization with `RuntimeError: DeepGEMM backend is not available` even wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41850](https://github.com/vllm-project/vllm/pull/41850) | mentioned | 0.6 | platforms: handle MIG device UUID in device_id_to_physical_device_id | tch together with `VLLM_USE_DEEP_GEMM=0` (workaround for the separate #41849), vLLM started successfully on the `2g.20gb` MIG partition and served inference requests: ``` INFO [cu… |
| [#41851](https://github.com/vllm-project/vllm/pull/41851) | closes_keyword | 0.95 | warmup: skip deep_gemm warmup when DeepGEMM is not available | Fixes #41849. `_fp8_linear_may_use_deep_gemm` calls `get_mk_alignment_for_contiguous_layout()` unconditionally **before** the FP8 type check, so it raises `RuntimeError` for every |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
