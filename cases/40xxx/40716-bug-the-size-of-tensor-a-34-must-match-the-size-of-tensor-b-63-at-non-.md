# vllm-project/vllm#40716: [Bug]: The size of tensor a (34) must match the size of tensor b (63) at non-singleton dimension 1

| 字段 | 值 |
| --- | --- |
| Issue | [#40716](https://github.com/vllm-project/vllm/issues/40716) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: The size of tensor a (34) must match the size of tensor b (63) at non-singleton dimension 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Same error run nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 on 4x RTX3090 with https://github.com/vllm-project/vllm/pull/38985 if use `--gpu-memory-utilization` option. Switching to the `--kv-cache-memory-bytes` option to control memory works normal. vLLM version: 0.19.2rc1.dev66+gb47840019 + #40438 + #38985 Test command: ```bash VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 VLLM_MARLIN_USE_ATOMIC_ADD=1 VLLM_FLOAT32_MATMUL_PRECISION=high PYTORCH_ALLOC_CONF=expandable_segments:True CUDA_DEVICE_ORDER=PCI_BUS_ID vllm serve /models/nv-community/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 --served-model-name Nemotron-3-Super --tensor-parallel-size 4 --enable-expert-parallel --trust-remote-code --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser nemotron_v3 --gpu-memory-utilization 0.9 --max-model-len auto --async-scheduling --enable-prefix-caching --enable-chunked-prefill --max-num-seqs 4 --enable-tokenizer-info-endpoint ``` [full-error.log](https://github.com/user-attachments/files/27018584/full-error.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...

## 现有链接修复摘要

#38985 [feat] Support modelopt_mixed for Turing and Ampere via Marlin | #40719 [fix] mismatch dim during capture graph if with --gpu-memory-utilization

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: bug Same error run nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 on 4x RTX3090 with https://github.com/vllm-project/vllm/pull/38985 if use `--gpu-memory-utilization` option. Switching to the `--kv-cache-memory-bytes` o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e `--kv-cache-memory-bytes` option to control memory works normal. vLLM version: 0.19.2rc1.dev66+gb47840019 + #40438 + #38985 Test command: ```bash VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 VLLM_MARLIN_USE_ATOMIC_ADD=1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: escribe the bug Same error run nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 on 4x RTX3090 with https://github.com/vllm-project/vllm/pull/38985 if use `--gpu-memory-utilization` option. Switching to the `--kv-cache-mem...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 4 --served-model-name Nemotron-3-Super --tensor-parallel-size 4 --enable-expert-parallel --trust-remote-code --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser nemotron_v3 --gpu-memory-utilizati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: del-len auto --async-scheduling --enable-prefix-caching --enable-chunked-prefill --max-num-seqs 4 --enable-tokenizer-info-endpoint ``` [full-error.log](https://github.com/user-attachments/files/27018584/full-error.log)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38985](https://github.com/vllm-project/vllm/pull/38985) | mentioned | 0.45 | [feat] Support modelopt_mixed for Turing and Ampere via Marlin | ry works normal. vllm version: 0.19.2rc1.dev66+gb47840019 + #40438 + #38985 test command: ```bash vllm_memory_profiler_estimate_cudagraphs=1 vllm_marlin_use_atomic_add=1 vllm_floa… |
| [#40719](https://github.com/vllm-project/vllm/pull/40719) | closes_keyword | 0.95 | [fix] mismatch dim during capture graph if with --gpu-memory-utilization | Fix #40716. ## Test Plan Test model `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` on 4x RTX3090 with pr #38985 based on version `0.19.2rc1.dev134+gfe9c3d6c5`. Although |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
