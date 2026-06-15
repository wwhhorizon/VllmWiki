# vllm-project/vllm#19817: [Feature]: `CustomOp` cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#19817](https://github.com/vllm-project/vllm/issues/19817) |
| 状态 | open |
| 标签 | help wanted;good first issue;feature request;keep-open;startup-ux |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;hardware_porting;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;cuda;fp8;kernel;moe;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: `CustomOp` cleanup

### Issue 正文摘录

### 🚀 Motivation Currently, we do not have a consistent plan for "light" custom ops (subclasses of `CustomOp` with both torch-native and GPU implementations). As we work on improved performance on NVIDIA Blackwell and AMD, we should be more intentional with CompilationConfig defaults that control custom op dispatching. This is a parent issue that tracks smaller PRs addressing `CustomOp`s. In vLLM, there are two kinds of custom kernels/ops: 1. "heavy" ops like GEMMs, MoE, and attention, which will mostly use tuned custom kernels for maximum performance. 2. "light" ops like `RMSNorm`, `SiluAndMul`, and `RoPE`, which have both torch-native and custom GPU implementations. This issue only refers to "light" ops, which are (or should be) all subclasses of `CustomOp`. When we enabled `torch.compile` by default in V1, the plan was to reduce our reliance on custom kernels to reduce maintenance costs and code complexity, even with minor performance costs. Recent versions of `torch` actually produce Triton kernels faster than our custom op implementations anyway. However, with startup time concerns (#19824), it seems like we want good performance even with Inductor disabled (more discussion o...

## 现有链接修复摘要

#19830 [Perf][fp8] Use CustomOp abstraction for fp8 quant for better perf | #24604 [torch.compile] Enable attention and allreduce fusion without custom ops enabled | #44381 Refactor RMSNorm vectorized launch checks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: are (or should be) all subclasses of `CustomOp`. When we enabled `torch.compile` by default in V1, the plan was to reduce our reliance on custom kernels to reduce maintenance costs and code complexity, even with minor p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: e and GPU implementations). As we work on improved performance on NVIDIA Blackwell and AMD, we should be more intentional with CompilationConfig defaults that control custom op dispatching. This is a parent issue that t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ne items might have their own issue or get one in the future. 1. [Perf] FP8 quantization not fused with rms_norm/silu_mul (because fp8 quant doesn't have a torch native implementation) 2. [Perf] AMD uses custom ops but...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: In vLLM, there are two kinds of custom kernels/ops: 1. "heavy" ops like GEMMs, MoE, and attention, which will mostly use tuned custom kernels for maximum performance. 2. "light" ops like `RMSNorm`, `SiluAndMul`, and `Ro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: s currently reimplement the same code, and only some are vectorized. 5. [Testing] Custom op tests either don't exist or reimplement Torch naive implementations 6. [Compilation] Current custom passes rely on custom op pa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#19830](https://github.com/vllm-project/vllm/pull/19830) | mentioned | 0.45 | [Perf][fp8] Use CustomOp abstraction for fp8 quant for better perf | detailed solution tracking: 1. ✅ @proexpertprog: fp8 `customop`s in #19830 2. ✅ #19181 removed hardcoded `enable_fusion=false`. 3. 🚧 wip @gshtras and @sagemoore are collecting som… |
| [#24604](https://github.com/vllm-project/vllm/pull/24604) | mentioned | 0.45 | [torch.compile] Enable attention and allreduce fusion without custom ops enabled | r custom ops. 6. ✅ match and perform fusion with custom ops disabled: #24604 #### ➕ other potential improvements - [ ] simplify custom op enablement - [ ] improve custom op docume… |
| [#44381](https://github.com/vllm-project/vllm/pull/44381) | mentioned | 0.6 | Refactor RMSNorm vectorized launch checks | Python API and CustomOp dispatch behavior are unchanged. Related to #19817. ## Test Plan # Unit regression `.venv/bin/python -m pytest tests/kernels/core/test_layernorm. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
