# vllm-project/vllm#2681: [Roadmap] vLLM Roadmap Q1 2024

| 字段 | 值 |
| --- | --- |
| Issue | [#2681](https://github.com/vllm-project/vllm/issues/2681) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | fp8;kernel;moe;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] vLLM Roadmap Q1 2024

### Issue 正文摘录

This document includes the features in vLLM's roadmap for Q1 2024. Please feel free to discuss and contribute to the specific features at related RFC/Issues/PRs and add anything else you'd like to talk about in this issue. In the future, we will publish our roadmap quarterly and deprecate our old roadmap (#244). - OSS General - [x] Better benchmark scripts and standards (#2433) - [ ] Improve documentation - CI/CD Testing and release process - [ ] Make model and kernel tests working on current CI - [ ] Automate release process - [ ] Dev experience - [ ] Explore Apple Silicon via Torch or MLX or llama cpp - [ ] Cached and parallel build system (#2654) - Frontend - [x] Support structured output (contact: @simon-mo) - [ ] Optimize the performance of the API server - Scheduling - [ ] Chunked prefill / dynamic splitfuse (#1562) - [ ] Speculative decoding (#2188, #2607, [merging plan](https://docs.google.com/document/d/1rE4pr3IdspRw97XbImY4fS9IWYuJJ3HGtL7AdIKGrw8/edit?usp=sharing), contact: @LiuXiaoxuanPKU) - [x] Automatic prefix caching (#2614, contact: @zhuohan123) - [ ] Disaggregated prefill / splitwise (#2472) - Kernel performance optimization - [ ] Quantization kernel optimization -...

## 现有链接修复摘要

#2188 [WIP] Speculative decoding using a draft model | #2378 [Feature][WIP] Prototype of vLLM execution on Intel GPU devices via SYCL. | #2453 DeepseekMoE support with Fused MoE kernel | #2542 Fused MOE for Mixtral

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Optimize the performance of the API server - Scheduling - [ ] Chunked prefill / dynamic splitfuse (#1562) - [ ] Speculative decoding (#2188, #2607, [merging plan](https://docs.google.com/document/d/1rE4pr3IdspRw97XbImY4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oadmap for Q1 2024. Please feel free to discuss and contribute to the specific features at related RFC/Issues/PRs and add anything else you'd like to talk about in this issue. In the future, we will publish our roadmap...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ed prefill / splitwise (#2472) - Kernel performance optimization - [ ] Quantization kernel optimization - [ ] Support FP8 (#2461) - [ ] MoE kernel optimization (#2453, #2542, and more) - [ ] H100 performance (#2107) - [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: #2461) - [ ] MoE kernel optimization (#2453, #2542, and more) - [ ] H100 performance (#2107) - [ ] AMD MI300x Performance - [ ] MQA kernel (#1880) - [ ] Port FlashInfer to vLLM (#2767) - [ ] Kernel for sampler - Hardwar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ove documentation - CI/CD Testing and release process - [ ] Make model and kernel tests working on current CI - [ ] Automate release process - [ ] Dev experience - [ ] Explore Apple Silicon via Torch or MLX or llama cpp...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2188](https://github.com/vllm-project/vllm/pull/2188) | mentioned | 0.45 | [WIP] Speculative decoding using a draft model | ed prefill / dynamic splitfuse (#1562) - [ ] speculative decoding (#2188, #2607, [merging plan](https://docs.google.com/document/d/1re4pr3idsprw97xbimy4fs9iwyujj3hgtl7adikgrw8/edi… |
| [#2378](https://github.com/vllm-project/vllm/pull/2378) | mentioned | 0.45 | [Feature][WIP] Prototype of vLLM execution on Intel GPU devices via SYCL. | ) - [ ] google tpu - [ ] intel gaudi - [ ] intel gpu/cpu (#2378) - model support - [x] multi-modal models (#775, #1265, #2153, #2563) - [ ] encoder-decoder models |
| [#2453](https://github.com/vllm-project/vllm/pull/2453) | mentioned | 0.45 | DeepseekMoE support with Fused MoE kernel | ion - [ ] support fp8 (#2461) - [ ] moe kernel optimization (#2453, #2542, and more) - [ ] h100 performance (#2107) - [ ] amd mi300x performance - [ ] mqa kernel (#188 |
| [#2542](https://github.com/vllm-project/vllm/pull/2542) | mentioned | 0.45 | Fused MOE for Mixtral | - [ ] support fp8 (#2461) - [ ] moe kernel optimization (#2453, #2542, and more) - [ ] h100 performance (#2107) - [ ] amd mi300x performance - [ ] mqa kernel (#1880) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
