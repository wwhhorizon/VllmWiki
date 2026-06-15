# vllm-project/vllm#37599: [Bug]: cudaErrorIllegalAddress crash when running zai-org/GLM-4.7-FP8 with `--max-num-batched-tokens` < default (e.g. 4K) under

| 字段 | 值 |
| --- | --- |
| Issue | [#37599](https://github.com/vllm-project/vllm/issues/37599) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: cudaErrorIllegalAddress crash when running zai-org/GLM-4.7-FP8 with `--max-num-batched-tokens` < default (e.g. 4K) under

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (`CUDA error: an illegal memory access was encountered`, cudaErrorIllegalAddress) when serving the zai-org/GLM-4.7-FP8 model with `--max-num-batched-tokens` < default value immediately after first requests. The service runs perfectly fine without explicit `--max-num-batched-tokens`. **Steps to Reproduce:** 1. Start the vLLM(0.17.1) server with the zai-org/GLM-4.7-FP8 model and the following speculative decoding configuration: ``` vllm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --async-scheduling \ --enable-prefix-caching \ --max-num-batched-tokens 4K ``` Start benchmark with: ``` vllm bench serve \ --model zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name custom \ --dataset-path SOME_DATASET \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics "ttft,tpot,e2el" \ --result-dir "./vllm_bench_results/" \ --request-rate 1 ``` 2. Send...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #37637 Fix: Add EAGLE/MTP slots calculation in max_num_new_slots_for_drafting

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: with `--max-num-batched-tokens` < default value immediately after first requests. The service runs perfectly fine without explicit `--max-num-batched-tokens`. **Steps to Reproduce:** 1. Start the vLLM(0.17.1) server wit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name custom \ --dataset-path SOME_DATASET \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (`CUDA error: an illegal memory access was encountered`, cudaErrorIllegalAddress) when serving the zai-org/GLM-4.7-FP8 model with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: cudaErrorIllegalAddress crash when running zai-org/GLM-4.7-FP8 with `--max-num-batched-tokens` < default (e.g. 4K) under bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: cudaErrorIllegalAddress crash when running zai-org/GLM-4.7-FP8 with `--max-num-batched-tokens` < default (e.g. 4K) under bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | nknown function> + 0x8b2ea (0x7ff40948b2ea in /lib64/libc.so.6) frame #4: <unknown function> + 0x110b40 (0x7ff409510b40 in /lib64/libc.so.6) ``` </details> **happy path:** start t… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xe77e4 (0x7ff3cb6e77e4 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x8… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n function> + 0xe77e4 (0x7ff3cb6e77e4 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x8b2ea (0x7ff40948b2ea in /lib64/libc.so.6) frame #8: <unknown function> + 0x110b40… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | ker_tp0() [0x1633ab3] frame #11: vllm::worker_tp0() [0x1633ad6] frame #12: vllm::worker_tp0() [0x1633ad6] frame #13: vllm::worker_tp0() [0x1633c27] frame #14: vllm::worker_tp0() [… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | yeval_evalframedefault + 0xe5ec (0x16200ec in vllm::worker_tp0) frame #16: vllm::worker_tp0() [0x161122d] frame #17: vllm::worker_tp0() [0x1740925] frame #18: vllm::worker_tp0() [… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | nknown function> + 0x8b2ea (0x7fe48a88b2ea in /lib64/libc.so.6) frame #20: <unknown function> + 0x110b40 (0x7fe48a910b40 in /lib64/libc.so.6) [rank7]:[e319 19:55:16.880866178 proc… |
| [#37637](https://github.com/vllm-project/vllm/pull/37637) | closes_keyword | 0.95 | Fix: Add EAGLE/MTP slots calculation in max_num_new_slots_for_drafting | Fixes #37599 ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
