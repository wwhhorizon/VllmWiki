# vllm-project/vllm#41063: [Tracking] DeepGEMM SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10)

| 字段 | 值 |
| --- | --- |
| Issue | [#41063](https://github.com/vllm-project/vllm/issues/41063) |
| 状态 | open |
| 标签 | DSv4 |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;fp8;gemm;kernel;moe;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Tracking] DeepGEMM SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10)

### Issue 正文摘录

# SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10) Filed against `jasl/DeepGEMM` and tracked alongside vLLM #40899. This is a comprehensive map of what's missing to run **DeepSeek-V4-Flash on SM 12.x** end-to-end through DeepGEMM, gathered from a 10-layer end-to-end debugging pass on dual NVIDIA GB10 (DGX Spark, SM 121, aarch64) using `jasl/DeepGEMM@7a7a41a1` + `jasl/vllm:ds4-sm120@8d0ebb76` against vLLM nightly `0.19.2rc1.dev220+g7b1bc0a3e`. ## What works in `jasl/DeepGEMM` today The fork already includes SM 120-native CuTeDSL kernels for these V4 paths: - `sm120_tf32_hc_prenorm_gemm` (mHC pre-norm GEMM — V4's hyper-connection layer) - `sm120_fp8_einsum` - `sm120_fp8_paged_mqa_logits` - `MmaMXF4NVF4Op` (with the `cute_dsl/warp/mma.py` `sm_120a` whitelist patch — NOT in fork) These paths boot end-to-end on RTX Pro 6000 (SM 120) per the PR description. ## What's still missing for V4-Flash on SM 12.x These dispatch sites in the fork still hard-code `arch_major == 9` (Hopper) or `arch_major == 10` (datacenter Blackwell) and reject SM 120/121, OR route to SM 10 kernels that use `tcgen05.*` instructions which SM 12.x silicon does not implement. #...

## 现有链接修复摘要

#40899 DeepSeek V4 support on SM12x with Triton sparse MLA fallback | #40923 [Kernel] Marlin MoE: include SM 12.x in default arch list | #41028 [Kernel] OAITritonExperts MXFP4: include SM 12.x in supported device range | #43044 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | #43047 [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 9: [Tracking] DeepGEMM SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10) DSv4 # SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10) Filed against...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: PR description. ## What's still missing for V4-Flash on SM 12.x These dispatch sites in the fork still hard-code `arch_major == 9` (Hopper) or `arch_major == 10` (datacenter Blackwell) and reject SM 120/121, OR route to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: fix | |---|---|---|---| | `csrc/utils/layout.hpp` | 76 | `get_default_recipe`: SM 10 → `(1, 1, 128)` | accept `arch_major == 12` for the same recipe (verified working on GB10) | | `csrc/apis/layout.hpp` | 48, 56, 106, 1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: prenorm_gemm` (mHC pre-norm GEMM — V4's hyper-connection layer) - `sm120_fp8_einsum` - `sm120_fp8_paged_mqa_logits` - `MmaMXF4NVF4Op` (with the `cute_dsl/warp/mma.py` `sm_120a` whitelist patch — NOT in fork) These paths...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Tracking] DeepGEMM SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10) DSv4 # SM 12.x kernel coverage gaps for DeepSeek-V4-Flash on consumer Blackwell (RTX 50 / GB10) Filed against...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40899](https://github.com/vllm-project/vllm/pull/40899) | mentioned | 0.45 | DeepSeek V4 support on SM12x with Triton sparse MLA fallback | 50 / gb10) filed against `jasl/deepgemm` and tracked alongside vllm #40899. this is a comprehensive map of what's missing to run **deepseek-v4-flash on sm 12.x** end-to-end throug… |
| [#40923](https://github.com/vllm-project/vllm/pull/40923) | mentioned | 0.45 | [Kernel] Marlin MoE: include SM 12.x in default arch list | `vllm/.../csrc cmakelists.txt marlin_*_archs` \| add `12.0f` family \| #40923 (approved by @harry-chen) \| ## reproduction command ```bash # inside vllm/vllm-openai:nightly-aarch64 w… |
| [#41028](https://github.com/vllm-project/vllm/pull/41028) | mentioned | 0.45 | [Kernel] OAITritonExperts MXFP4: include SM 12.x in supported device range | y` \| `_supports_current_device` cap range `< (11, 0)` → `< (13, 0)` \| #41028 \| \| `vllm/.../csrc cmakelists.txt marlin_*_archs` \| add `12.0f` family \| #40923 (approved by @harry-ch… |
| [#43044](https://github.com/vllm-project/vllm/pull/43044) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | n below). Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tuned for the larg… |
| [#43047](https://github.com/vllm-project/vllm/pull/43047) | mentioned | 0.6 | [Core] Add shmem-aware autotune pruner for non-H100 Triton kernels | n below). Partially addresses the same root cause in #38918, #36802, #41063, #32826. ### Motivation Triton kernels in vLLM often ship with autotune config lists tuned for the larg… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
