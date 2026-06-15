# vllm-project/vllm#26768: [Performance]: Deepseek-V3 Performance Uplift Plan on ROCm Backend

| 字段 | 值 |
| --- | --- |
| Issue | [#26768](https://github.com/vllm-project/vllm/issues/26768) |
| 状态 | closed |
| 标签 | performance;rocm;stale |
| 评论 | 27; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;fp8;kernel;moe;operator;quantization;sampling |
| 症状 | oom;slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: Deepseek-V3 Performance Uplift Plan on ROCm Backend

### Issue 正文摘录

# Proposal to improve performance ## Stage 1: Low Latency Performance Optimization ### 1. Quantization Recipe We will focus on performance optimization of several quantization recipes. - [ ] FP8 with per-token-group scale activation and per-channel-group scale weight - [ ] FP8 with per-token-group scale activation and block-scale weight - [ ] MXFP4 with block-scale activation and block-scale weight ### 2. Parallel Parallelism Recipe We will focus on the performance optimization of the following two parallel parallelism recipes including TP and EP at the first stage to reduce the latency. ### 3. Attention Backend - [ ] Refactor the ROCm Attention backend to avoid some possible OOM issue https://github.com/vllm-project/vllm/pull/25763 - [ ] Integrate the performant MLA kernels (BF16/FP8) from [AITER](https://github.com/ROCm/aiter) https://github.com/vllm-project/vllm/pull/27380 ### 4. MoE Module Optimization **(1) Support expert related fusion patterns** - [x] Fuse shared expert with routed expert: #24097 - [ ] Fuse the small kernels into shared expert. **(2) Support EPLB for EP parallelism** - [ ] Currently in vLLM v0.11.0, EPLB feature is still not supported on ROCm backend. We wi...

## 现有链接修复摘要

#24097 [ROCm][FEAT] Fuse DeepSeek shared experts into AITER fused_moe ops

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: ove performance ## Stage 1: Low Latency Performance Optimization ### 1. Quantization Recipe We will focus on performance optimization of several quantization recipes. - [ ] FP8 with per-token-group scale activation and...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: .com/ROCm/aiter) https://github.com/vllm-project/vllm/pull/27380 ### 4. MoE Module Optimization **(1) Support expert related fusion patterns** - [x] Fuse shared expert with routed expert: #24097 - [ ] Fuse the small ker...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e]: Deepseek-V3 Performance Uplift Plan on ROCm Backend performance;rocm;stale # Proposal to improve performance ## Stage 1: Low Latency Performance Optimization ### 1. Quantization Recipe We will focus on performance o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Performance]: Deepseek-V3 Performance Uplift Plan on ROCm Backend performance;rocm;stale # Proposal to improve performance ## Stage 1: Low Latency Performance Optimization ### 1. Quantization Recipe We will focus on pe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Deepseek-V3 Performance Uplift Plan on ROCm Backend performance;rocm;stale # Proposal to improve performance ## Stage 1: Low Latency Performance Optimization ### 1. Quantization Recipe We will focus on pe...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24097](https://github.com/vllm-project/vllm/pull/24097) | mentioned | 0.45 | [ROCm][FEAT] Fuse DeepSeek shared experts into AITER fused_moe ops | lated fusion patterns** - [x] fuse shared expert with routed expert: #24097 - [ ] fuse the small kernels into shared expert. **(2) support eplb for ep parallelism** - [ ] currentl… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
