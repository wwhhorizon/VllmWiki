# vllm-project/vllm#34399: [Bug]: Nemotron 3 (all quants) take a LONG time to load

| 字段 | 值 |
| --- | --- |
| Issue | [#34399](https://github.com/vllm-project/vllm/issues/34399) |
| 状态 | open |
| 标签 | bug;torch.compile;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nemotron 3 (all quants) take a LONG time to load

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to load in the Nemotron 3 nano family of models, the model loading takes a crazy amount of time at the torch.compile step (>800 seconds!!!). Tested with both FP8, and NVFP4. See logs below: ``` INFO 02-11 16:42:00 [model.py:541] Resolved architecture: NemotronHForCausalLM INFO 02-11 16:42:00 [model.py:1561] Using max model len 16384 INFO 02-11 16:42:00 [cache.py:216] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scaling factor. INFO 02-11 16:42:00 [arg_utils.py:1443] Using ray runtime env (env vars redacted): {'_ray_commit': '44be7c5099e5cfb88a51d8ef4304a2047cdf798f', 'pip': {'packages': ['s3fs'], 'pip_check': False}, 'env_vars': {'RAY_DEFAULT_OBJECT_STORE_MEMORY_PROPORTION': '***', 'VLLM_FLASHINFER_MOE_BACKEND': '***', 'VLLM_FLOAT32_MATMUL_PRECISION': '***'}} INFO 02-11 16:42:00 [scheduler.py:226] Chunked prefill is enabled with max_num_batched_tokens=16384. INFO 02-11 16:42:00 [config.py:578] Updating mamba_ssm_cache_dtype to 'float32' for NemotronH model INFO 02-11 16:42:00 [config.py:504] Setting attenti...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: [Bug]: Nemotron 3 (all quants) take a LONG time to load bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When trying to load in the Nemotron 3 nano family of models, the model loading takes a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 'env_vars': {'RAY_DEFAULT_OBJECT_STORE_MEMORY_PROPORTION': '***', 'VLLM_FLASHINFER_MOE_BACKEND': '***', 'VLLM_FLOAT32_MATMUL_PRECISION': '***'}} INFO 02-11 16:42:00 [scheduler.py:226] Chunked prefill is enabled with max...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Nemotron 3 (all quants) take a LONG time to load bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When trying to load in the Nemotron 3 nano family of models, the model loading takes a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Bug]: Nemotron 3 (all quants) take a LONG time to load bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When trying to load in the Nemotron 3 nano family of models, the model loading takes a c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: akes a crazy amount of time at the torch.compile step (>800 seconds!!!). Tested with both FP8, and NVFP4. See logs below: ``` INFO 02-11 16:42:00 [model.py:541] Resolved architecture: NemotronHForCausalLM INFO 02-11 16:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
