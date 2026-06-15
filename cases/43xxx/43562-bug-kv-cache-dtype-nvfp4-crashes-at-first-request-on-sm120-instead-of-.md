# vllm-project/vllm#43562: [Bug]: --kv-cache-dtype nvfp4 crashes at first request on SM120 instead of failing fast at init

| 字段 | 值 |
| --- | --- |
| Issue | [#43562](https://github.com/vllm-project/vllm/issues/43562) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: --kv-cache-dtype nvfp4 crashes at first request on SM120 instead of failing fast at init

### Issue 正文摘录

### Environment ``` GPU NVIDIA RTX PRO 6000 Blackwell Workstation Edition (sm_120, 96 GB) Driver 595.71.05 CPU Ampere Altra - ARM Neoverse-N1, 64 cores (aarch64) OS Ubuntu 24.04.4 LTS, kernel 6.17.0-23-generic vllm 0.21.1rc1.dev269+gb06813e87 torch 2.11.0+cu130 (CUDA 13.0) flashinfer 0.6.11.post2 transformers 5.9.0 · triton 3.6.0 ``` (`vllm collect-env` can't run here — it shells out to `pip` and crashes on uv-only envs: `get_pip_packages` -> `'NoneType' object has no attribute 'splitlines'`. Minor, separate.) ### Bug `--kv-cache-dtype nvfp4` on an NVFP4 checkpoint starts up clean, captures graphs, then kills the engine on the **first request** (not at config validation). NVFP4 *weights* are fine; only the NVFP4 *KV-cache attention* path fails. Root cause is upstream — trtllm-gen FP4 FMHA has no sm_120 kernel (NVIDIA/TensorRT-LLM#10241, #11799) — but vLLM in front of it accepts the flag and dies cryptically rather than rejecting it. The first request fails in `flashinfer.prefill.plan`, because vLLM passes the literal string `"nvfp4"` as `kv_data_type` and flashinfer resolves it with `getattr(torch, "nvfp4")`: ``` File ".../vllm/v1/attention/backends/flashinfer.py", line 1170, in b...

## 现有链接修复摘要

#10241 [V1] TPU Prototype | #43669 [Bugfix] flashinfer: fail fast when --kv-cache-dtype nvfp4 used on unsupported arch

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: --kv-cache-dtype nvfp4 crashes at first request on SM120 instead of failing fast at init ### Environment ``` GPU NVIDIA RTX PRO 6000 Blackwell Workstation Edition (sm_120, 96 GB) Driver 595.71.05 CPU Ampere Altra...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: --kv-cache-dtype nvfp4 crashes at first request on SM120 instead of failing fast at init ### Environment ``` GPU NVIDIA RTX PRO 6000 Blackwell Workstation Edition (sm_120, 96 GB) Driver 595.71.05 CPU Ampere
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ``` File ".../vllm/v1/attention/backends/flashinfer.py", line 1170, in build prefill_wrapper.plan(...) File ".../flashinfer/prefill.py", line 1859, in plan kv_data_type = canonicalize_torch_dtype(kv_data_type) File "......
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 0.21.1rc1.dev269+gb06813e87 torch 2.11.0+cu130 (CUDA 13.0) flashinfer 0.6.11.post2 transformers 5.9.0 · triton 3.6.0 ``` (`vllm collect-env` can't run here — it shells out to `pip` and crashes on uv-only envs: `get_pip_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: --kv-cache-dtype nvfp4 crashes at first request on SM120 instead of failing fast at init ### Environment ``` GPU NVIDIA RTX PRO 6000 Blackwell Workstation Edition (sm_120, 96 GB) Driver 595.71.05 CPU Ampere Altra...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10241](https://github.com/vllm-project/vllm/pull/10241) | mentioned | 0.45 | [V1] TPU Prototype | alidation), #2207 (fp4 kv head_dim 128 gap), #2577 (sm120 fp4 gemm) - nvidia/tensorrt-llm#10241, #11799 (sm120 trtllm-gen fp4 fmha kernel / cubins) |
| [#43669](https://github.com/vllm-project/vllm/pull/43669) | closes_keyword | 0.95 | [Bugfix] flashinfer: fail fast when --kv-cache-dtype nvfp4 used on unsupported arch | Fixes #43562 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
