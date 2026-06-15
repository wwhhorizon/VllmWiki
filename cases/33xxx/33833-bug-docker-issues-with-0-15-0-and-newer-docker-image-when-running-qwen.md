# vllm-project/vllm#33833: [Bug][Docker]: Issues with 0.15.0 and newer docker image when running Qwen3-Next with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 

| 字段 | 值 |
| --- | --- |
| Issue | [#33833](https://github.com/vllm-project/vllm/issues/33833) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Docker]: Issues with 0.15.0 and newer docker image when running Qwen3-Next with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 

### Issue 正文摘录

### Your current environment On docker images `vllm/vllm-openai:v0.15.0-cu130` and newer H100 node Specifically this is with: `vllm/vllm-openai:cu130-nightly` ### 🐛 Describe the bug ``` VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 \ vllm serve Qwen/Qwen3-Next-80B-A3B-Thinking-FP8 \ --max-num-seqs 512 \ --max-num-batched-tokens 4096 \ --max-model-len 4096 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.9 \ --load-format dummy``` ``` On the cu130 container, this gives compilation errors during the jit compile: ``` (Worker_TP1 pid=1574309) ERROR 02-04 13:21:04 [multiproc_executor.py:852] FAILED: [code=1] /scratch/.cache/flashinfer/0.6.2/90a/cached_ops/fp8_blockscale_gemm_90/fp8_blockscale_gemm_sm90_binding.cuda.o (Worker_TP1 pid=1574309) ERROR 02-04 13:21:04 [multiproc_executor.py:852] /usr/local/cuda/bin/nvcc --generate-dependencies-with-compile --dependency-output /scratch/.cache/flashinfer/0.6.2/90a/cached_ops/fp8_blockscale_gemm_90/fp8_blockscale_gemm_sm90_binding.cuda.o.d -DPy_LIMITED_API=0x03090000 -D_GLIBCXX_USE_CXX11_ABI=1 -I/usr/local/lib/python3.12/dist-packages/flashinfer/data/csrc/nv_internal -I/usr/local/lib/python3.12/dist-packages/flashinfer/data/csrc/nv_internal/incl...

## 现有链接修复摘要

#33929 [Bugfix][Docker] Install CUDA dev packages for JIT compilation headers

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug][Docker]: Issues with 0.15.0 and newer docker image when running Qwen3-Next with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 bug;stale ### Your current environment On docker images `vllm/vllm-openai:v0.15.0-cu130` and ne...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ith 0.15.0 and newer docker image when running Qwen3-Next with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 bug;stale ### Your current environment On docker images `vllm/vllm-openai:v0.15.0-cu130` and newer H100 node Specifica...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: nvironment On docker images `vllm/vllm-openai:v0.15.0-cu130` and newer H100 node Specifically this is with: `vllm/vllm-openai:cu130-nightly` ### 🐛 Describe the bug ``` VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 \ vllm serve...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: newer docker image when running Qwen3-Next with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 bug;stale ### Your current environment On docker images `vllm/vllm-openai:v0.15.0-cu130` and newer H100 node Specifically this is wit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug][Docker]: Issues with 0.15.0 and newer docker image when running Qwen3-Next with VLLM_BLOCKSCALE_FP8_GEMM_FLASHINFER=1 bug;stale ### Your current environment On docker images `vllm/vllm-openai:v0.15.0-cu130` and ne...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33929](https://github.com/vllm-project/vllm/pull/33929) | closes_keyword | 0.95 | [Bugfix][Docker] Install CUDA dev packages for JIT compilation headers | Fixes #33833 <!-- markdownlint-disable --> ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
