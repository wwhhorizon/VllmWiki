# vllm-project/vllm#18153: [RFC]: Blackwell Enablement for vLLM (SM100)

| 字段 | 值 |
| --- | --- |
| Issue | [#18153](https://github.com/vllm-project/vllm/issues/18153) |
| 状态 | closed |
| 标签 | RFC;stale;nvidia |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;moe;operator |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Blackwell Enablement for vLLM (SM100)

### Issue 正文摘录

### Motivation. We are in the process of making incremental changes for Blackwell Support in vLLM. This issue is a tracker for all the items that are planned. ### Planned or In Progress Features The following items are either planned or currently in progress to enable vLLM support on Blackwell. - [x] Enable NVFP4 Support - [x] (NVIDIA) Add functional support for NVFP4 Kernels for linear layers - [x] (NVIDIA) Add functional support for NVFP4 MoE Kernels - [x] (NVIDIA) Add Model Integration for nvidia/*-FP4 models - [x] Finetune GEMM configurations for Blackwell - [x] (NVIDIA) Optimize MoE for Latency - [x] (NVIDIA) Optimize MoE for Throughput [FI: PR !1113](https://github.com/flashinfer-ai/flashinfer/pull/1113) - [x] (NVIDIA) MoE All Reduce Fusion [FI: PR !1108 ](https://github.com/flashinfer-ai/flashinfer/pull/1108) - [ ] Optimize communication overlap ops - [x] (NVIDIA) Enable NCCL’s symmetric memory https://github.com/vllm-project/vllm/pull/24532 - [ ] (NVIDIA) Add support for Gemm + comm overlap - [x] Blackwell Attention Kernels - [x] (NVIDIA) Integrate Cutlass MLA Kernels #17625 - [x] (NVIDIA) Integrate vLLM v1-compatible Blackwell prefill and decode GQA kernels [FI: PR !1051]...

## 现有链接修复摘要

#17625 [NVIDIA] Add Cutlass MLA backend | #18564 Sm100 blockwise fp8 swap ab | #19825 [Core] Add Flashinfer TRTLLM Backend for Flashinfer decode path (SM100).

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: currently in progress to enable vLLM support on Blackwell. - [x] Enable NVFP4 Support - [x] (NVIDIA) Add functional support for NVFP4 Kernels for linear layers - [x] (NVIDIA) Add functional support for NVFP4 MoE Kernels...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [RFC]: Blackwell Enablement for vLLM (SM100) RFC;stale;nvidia ### Motivation. We are in the process of making incremental changes for Blackwell Support in vLLM. This issue is a tracker for all the items that are planned...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ] (NVIDIA) Optimize MoE for Throughput [FI: PR !1113](https://github.com/flashinfer-ai/flashinfer/pull/1113) - [x] (NVIDIA) MoE All Reduce Fusion [FI: PR !1108 ](https://github.com/flashinfer-ai/flashinfer/pull/1108) -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Blackwell Enablement for vLLM (SM100) RFC;stale;nvidia ### Motivation. We are in the process of making incremental changes for Blackwell Support in vLLM. This issue is a tracker for all the items that are planned...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: une GEMM configurations for Blackwell - [x] (NVIDIA) Optimize MoE for Latency - [x] (NVIDIA) Optimize MoE for Throughput [FI: PR !1113](https://github.com/flashinfer-ai/flashinfer/pull/1113) - [x] (NVIDIA) MoE All Reduc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17625](https://github.com/vllm-project/vllm/pull/17625) | mentioned | 0.45 | [NVIDIA] Add Cutlass MLA backend | ell attention kernels - [x] (nvidia) integrate cutlass mla kernels #17625 - [x] (nvidia) integrate vllm v1-compatible blackwell prefill and decode gqa kernels [fi: pr !1051](https |
| [#18564](https://github.com/vllm-project/vllm/pull/18564) | mentioned | 0.45 | Sm100 blockwise fp8 swap ab | blockscale gemm - [x] (nvidia) fp8 blockscale gemm optimizations: #18564 - [x] (nvidia) fp8 blockscale moe - [x] (nvidia) latency and throughput optimizations - [x] mtp supp |
| [#19825](https://github.com/vllm-project/vllm/pull/19825) | closes_keyword | 0.95 | [Core] Add Flashinfer TRTLLM Backend for Flashinfer decode path (SM100).  | resolve)" : #18153 - [x] The test plan, such as providing test command. - [x] The test results, such as pasting the results comparison before and after, or e2e results - [N/A] (Op |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
