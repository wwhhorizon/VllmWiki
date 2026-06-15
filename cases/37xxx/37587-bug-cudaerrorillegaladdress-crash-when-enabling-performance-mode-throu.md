# vllm-project/vllm#37587: [Bug]: cudaErrorIllegalAddress crash when enabling `--performance-mode throughput` for zai-org/GLM-4.7-FP8 under load

| 字段 | 值 |
| --- | --- |
| Issue | [#37587](https://github.com/vllm-project/vllm/issues/37587) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: cudaErrorIllegalAddress crash when enabling `--performance-mode throughput` for zai-org/GLM-4.7-FP8 under load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (`CUDA error: an illegal memory access was encountered`, cudaErrorIllegalAddress) when serving the zai-org/GLM-4.7-FP8 model with `--performance-mode throughput` even with the first request. The service runs perfectly fine in default and interactivity modes. **Steps to Reproduce:** 1. Start the vLLM(0.17.1) server with the zai-org/GLM-4.7-FP8 model and the following speculative decoding configuration: ``` vllm serve zai-org/GLM-4.7-FP8 \ --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice \ --async-scheduling \ --enable-prefix-caching \ --performance-mode throughput ``` Start benchmark with: ``` vllm bench serve \ --model zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name custom \ --dataset-path SOME_DATASET \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics "ttft,tpot,e2el" \ --result-dir "./vllm_bench_results/" \ --request-rate 1 ``` 2. Send a request to the serve...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: cudaErrorIllegalAddress crash when enabling `--performance-mode throughput` for zai-org/GLM-4.7-FP8 under load bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: zai-org/GLM-4.7-FP8 \ --port 8000 \ --save-result \ --save-detailed \ --backend=vllm \ --dataset-name custom \ --dataset-path SOME_DATASET \ --disable-shuffle \ --metric-percentiles "50,90,95,99" \ --percentile-metrics...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (`CUDA error: an illegal memory access was encountered`, cudaErrorIllegalAddress) when serving the zai-org/GLM-4.7-FP8 model with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: crash when enabling `--performance-mode throughput` for zai-org/GLM-4.7-FP8 under load bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (`CUDA error: an illegal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: cudaErrorIllegalAddress crash when enabling `--performance-mode throughput` for zai-org/GLM-4.7-FP8 under load bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | nknown function> + 0x8b2ea (0x7eff59a8b2ea in /lib64/libc.so.6) frame #4: <unknown function> + 0x110b40 (0x7eff59b10b40 in /lib64/libc.so.6) ``` </details> **happy path:** start th |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xe77e4 (0x7eff1bce77e4 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x8… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n function> + 0xe77e4 (0x7eff1bce77e4 in /lib64/libstdc++.so.6) frame #7: <unknown function> + 0x8b2ea (0x7eff59a8b2ea in /lib64/libc.so.6) frame #8: <unknown function> + 0x110b40… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
