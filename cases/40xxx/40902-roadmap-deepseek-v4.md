# vllm-project/vllm#40902: [Roadmap] DeepSeek V4

| 字段 | 值 |
| --- | --- |
| Issue | [#40902](https://github.com/vllm-project/vllm/issues/40902) |
| 状态 | open |
| 标签 | RFC;keep-open;deepseek |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;cache;fp8;gemm;kernel;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Roadmap] DeepSeek V4

### Issue 正文摘录

## Implementation The latest implementation updates are tracked in https://github.com/vllm-project/vllm/pull/40860 which is already merged into main. Please layer your work on top of main for further optimizations. ## Performance Dashboard Please refer to InferenceX: https://inferencex.semianalysis.com/inference ## Roadmap ### Core Model Support - [x] FP4 Indexer @zyongye - [x] Done in https://github.com/vllm-project/vllm/pull/40860 - [x] MegaMoE @WoosukKwon - [x] Initial support done in https://github.com/vllm-project/vllm/pull/40860 - [ ] Continue work in https://github.com/vllm-project/vllm/pull/40833 - [ ] NVFP4 support ### Low Latency Optimization - [x] Multi-stream 4 GEMM in C4A and C128A (Compressor WKV+W_S, SWA WQA+WKV, Indexer W, Indexer Compressor WKV+WS) @zyongye #41061 - [ ] Fast topk kernel @WoosukKwon - [x] Faster fp8 group quantization kernel #41326 - [ ] Indexer topk + page table transform fusion @ZJY0516 #41105 - [ ] Specialized pre-Attention GEMM for low BS - [x] Fuse norm and router @jeejeelee #41263 ### PD + High throughput Optimization @liuzijing2014 @ywang96 @esmeetu - [x] Nvlink_one_sided a2a support bf16 and mxfp8 dispatch https://github.com/vllm-project/vl...

## 现有链接修复摘要

#41061 [DSV4] Enable Multi-stream for Pre-Attn GEMM | #41105 [Perf] fuse indexer topk and page table transform fusion for dpskv4 | #41220 [Kernel] Add H20-3e FP8 block-scaled GEMM tuned configs for DeepSeek-V4-Flash expert shapes | #41326 Faster per-token fp8 group quant packed kernel for blackwell | #42985 [PoC] Soft-pin recently-hit prefix-cache entries in get_new_blocks | #43809 [DeepSeekV4][PCP] Enable context-parallel prefill for hybrid KV and MegaMoE

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: ex.semianalysis.com/inference ## Roadmap ### Core Model Support - [x] FP4 Indexer @zyongye - [x] Done in https://github.com/vllm-project/vllm/pull/40860 - [x] MegaMoE @WoosukKwon - [x] Initial support done in https://gi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: - [x] Done in https://github.com/vllm-project/vllm/pull/40860 - [x] MegaMoE @WoosukKwon - [x] Initial support done in https://github.com/vllm-project/vllm/pull/40860 - [ ] Continue work in https://github.com/vllm-projec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: #41263 ### PD + High throughput Optimization @liuzijing2014 @ywang96 @esmeetu - [x] Nvlink_one_sided a2a support bf16 and mxfp8 dispatch https://github.com/vllm-project/vllm/pull/40960 - [ ] Nvlink_one_sided a2a support...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Roadmap] DeepSeek V4 RFC;keep-open;deepseek ## Implementation The latest implementation updates are tracked in https://github.com/vllm-project/vllm/pull/40860 which is already merged into main. Please layer your work o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 014 @ywang96 @esmeetu - [x] Nvlink_one_sided a2a support bf16 and mxfp8 dispatch https://github.com/vllm-project/vllm/pull/40960 - [ ] Nvlink_one_sided a2a support for FP8 quantized combine (waiting for flashinfer to up...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41061](https://github.com/vllm-project/vllm/pull/41061) | mentioned | 0.45 | [DSV4] Enable Multi-stream for Pre-Attn GEMM | wkv+w_s, swa wqa+wkv, indexer w, indexer compressor wkv+ws) @zyongye #41061 - [ ] fast topk kernel @woosukkwon - [x] faster fp8 group quantization kernel #41326 - [ ] indexer topk… |
| [#41105](https://github.com/vllm-project/vllm/pull/41105) | mentioned | 0.45 | [Perf] fuse indexer topk and page table transform fusion for dpskv4 | nel #41326 - [ ] indexer topk + page table transform fusion @zjy0516 #41105 - [ ] specialized pre-attention gemm for low bs - [x] fuse norm and router @jeejeelee #41263 ### pd + h… |
| [#41220](https://github.com/vllm-project/vllm/pull/41220) | closes_keyword | 0.95 | [Kernel] Add H20-3e FP8 block-scaled GEMM tuned configs for DeepSeek-V4-Flash expert shapes | fix for GB10/SM120; "Hopper reviewers welcome") - #40902 (DeepSeek V4 roadmap, "Faster FP8 group quant kernel" item) |
| [#41326](https://github.com/vllm-project/vllm/pull/41326) | mentioned | 0.45 | Faster per-token fp8 group quant packed kernel for blackwell | t topk kernel @woosukkwon - [x] faster fp8 group quantization kernel #41326 - [ ] indexer topk + page table transform fusion @zjy0516 #41105 - [ ] specialized pre-attention gemm f… |
| [#42985](https://github.com/vllm-project/vllm/pull/42985) | closes_keyword | 0.95 | [PoC] Soft-pin recently-hit prefix-cache entries in get_new_blocks | closed by #33524, explicitly defers "more complicated models with multiple attention groups" - #40902 — DeepSeek V4 roadmap (does not currently cover this) |
| [#43809](https://github.com/vllm-project/vllm/pull/43809) | mentioned | 0.6 | [DeepSeekV4][PCP] Enable context-parallel prefill for hybrid KV and MegaMoE | context-parallel prefill for hybrid KV and MegaMoE ## Purpose #40902 Implementation summary: Added PCP-aware hybrid KV handling for DeepSeekV4, covering MLA / SWA / C4 / C128 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
