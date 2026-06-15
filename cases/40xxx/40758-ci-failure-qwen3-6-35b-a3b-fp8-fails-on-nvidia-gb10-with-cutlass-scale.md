# vllm-project/vllm#40758: [CI Failure]: `Qwen3.6-35B-A3B-FP8` fails on `NVIDIA GB10` with `cutlass_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0

| 字段 | 值 |
| --- | --- |
| Issue | [#40758](https://github.com/vllm-project/vllm/issues/40758) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: `Qwen3.6-35B-A3B-FP8` fails on `NVIDIA GB10` with `cutlass_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0

### Issue 正文摘录

### Name of failing test `Qwen3.6-35B-A3B-FP8` on an `NVIDIA GB10` system ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test # Summary I am testing `Qwen3.6-35B-A3B-FP8` on an `NVIDIA GB10` system with: - `NVIDIA-SMI 580.142` - `Driver Version: 580.142` - `CUDA Version: 13.0` I can reproduce a startup failure in vLLM when launching the FP8 model through the OpenAI server. The failure happens during engine initialization / profile run and crashes inside: - `torch.ops._C.cutlass_scaled_mm.default(...)` - `cutlass_gemm_caller ... Error Internal` ### 📝 History of failing test # Environment - Hardware: `NVIDIA GB10` - Driver: `580.142` - CUDA: `13.0` - Image: `vllm/vllm-openai:nightly` - vLLM in container log: - `0.19.2rc1.dev134+gfe9c3d6c5` - Host Python env: - `torch 2.11.0+cu130` - `vllm 0.19.2rc1.dev142+g4a79262e0` # Model - `Qwen3.6-35B-A3B-FP8` # Launch args Current relevant launch args: ```text --model /models/Qwen3.6-35B-A3B-FP8 --served-model-name Qwen3.6-35B-A3B-FP8 --gpu-memory-utilization 0.7 --max-model-len 4096 --enforce-eager ``` Before adding `--enforce-eager`...

## 现有链接修复摘要

#41215 [Bugfix] Use enable_sm120_family for per-tensor FP8 CUTLASS kernels on SM12.1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: `Qwen3.6-35B-A3B-FP8` fails on `NVIDIA GB10` with `cutlass_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0 ci-failure ### Name of failing test `Qwen3.6-35B-A3B-FP8` on an `N
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [CI Failure]: `Qwen3.6-35B-A3B-FP8` fails on `NVIDIA GB10` with `cutlass_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0 ci-failure ### Name of failing test `Qwen3.6-35B-A3B-FP8` on an `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: `Qwen3.6-35B-A3B-FP8` fails on `NVIDIA GB10` with `cutlass_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0 ci-failure ### Name of failing test `Qwen3.6-35B-A3B-FP8` on an `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [CI Failure]: `Qwen3.6-35B-A3B-FP8` fails on `NVIDIA GB10` with `cutlass_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0 ci-failure ### Name of failing test `Qwen3.6-35B-A3B-FP8` on an `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s_scaled_mm` / `cutlass_gemm_caller Error Internal` under vLLM nightly + CUDA 13.0 ci-failure ### Name of failing test `Qwen3.6-35B-A3B-FP8` on an `NVIDIA GB10` system ### Basic information - [ ] Flaky test - [ ] Can re...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41215](https://github.com/vllm-project/vllm/pull/41215) | closes_keyword | 0.95 | [Bugfix] Use enable_sm120_family for per-tensor FP8 CUTLASS kernels on SM12.1 | fixes #40758. ## Test Plan This is a two line change replacing an architecture guard and so no new tests are required. Existing `test_cutlass_scaled_mm.py` FP8 tests cover this |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
