# vllm-project/vllm#28883: [Tracking Issue][Performance]: (G)B200/300 performance improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#28883](https://github.com/vllm-project/vllm/issues/28883) |
| 状态 | open |
| 标签 | performance;nvidia |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;fp8;gemm;kernel;moe;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Tracking Issue][Performance]: (G)B200/300 performance improvements

### Issue 正文摘录

Below are some of the performance/functional improvements that help with (G)B200/300 experiences on vLLM. Please feel free to review, suggest and collaborate if you are interested! Point of Contact: @pavanimajety, drafted by @pavanimajety ## Multi Node Serving support - [x] DeepEP low-latency kernel integration https://github.com/vllm-project/vllm/pull/27141 - [x] EPLB for Flashinfer backends https://github.com/vllm-project/vllm/pull/29804 - [ ] Elastic EP ## Consolidated Communications Library - integrations, clean up, and improvements ## Model specific config sweep and performance optimizations - [ ] Qwen3-MoE - [ ] GPT-OSS Disagg - [ ] DSR1/3.2 Disagg - [ ] Kimi K2 Disagg - (NVFP4 possibly) ## Kernels: Cross-link Flashinfer Roadmap https://github.com/flashinfer-ai/flashinfer/issues/1770 - [x] FP8 Prefill Attentions - https://github.com/vllm-project/vllm/pull/30746 - [ ] Deepseek Sparse Attention - [ ] GDN Attention - [ ] Gemm + Compute overlap for both low-latency and high throughput - [ ] BatchPrefillWithRaggedKVCacheWrapper Kernel for MHA/GQA Flashinfer Backend - [ ] Perf improvements for TRTLLM MLA/MHA kernels at very long sequence lengths (128K) ## CI /Build - [ ] CUDA13 su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ications Library - integrations, clean up, and improvements ## Model specific config sweep and performance optimizations - [ ] Qwen3-MoE - [ ] GPT-OSS Disagg - [ ] DSR1/3.2 Disagg - [ ] Kimi K2 Disagg - (NVFP4 possibly)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 3-MoE - [ ] GPT-OSS Disagg - [ ] DSR1/3.2 Disagg - [ ] Kimi K2 Disagg - (NVFP4 possibly) ## Kernels: Cross-link Flashinfer Roadmap https://github.com/flashinfer-ai/flashinfer/issues/1770 - [x] FP8 Prefill Attentions - h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ed Communications Library - integrations, clean up, and improvements ## Model specific config sweep and performance optimizations - [ ] Qwen3-MoE - [ ] GPT-OSS Disagg - [ ] DSR1/3.2 Disagg - [ ] Kimi K2 Disagg - (NVFP4...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: afted by @pavanimajety ## Multi Node Serving support - [x] DeepEP low-latency kernel integration https://github.com/vllm-project/vllm/pull/27141 - [x] EPLB for Flashinfer backends https://github.com/vllm-project/vllm/pu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tegration https://github.com/vllm-project/vllm/pull/27141 - [x] EPLB for Flashinfer backends https://github.com/vllm-project/vllm/pull/29804 - [ ] Elastic EP ## Consolidated Communications Library - integrations, clean...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
