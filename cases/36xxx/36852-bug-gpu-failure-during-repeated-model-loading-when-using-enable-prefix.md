# vllm-project/vllm#36852: [Bug]: GPU failure during repeated model loading when using --enable-prefix-caching with KV transfer (LMCacheConnectorV1)

| 字段 | 值 |
| --- | --- |
| Issue | [#36852](https://github.com/vllm-project/vllm/issues/36852) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: GPU failure during repeated model loading when using --enable-prefix-caching with KV transfer (LMCacheConnectorV1)

### Issue 正文摘录

### Environment Information ### 🐛 Describe the bug The GPUs are entering an error state during the second model load when running vLLM with prefix caching and KV transfer enabled. --enable-prefix-caching --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}' After a system reboot, the model loads successfully and runs without any issues at first time . However, if i try to load again for the second time , the GPUs go into an error state during the second initialization. This behavior is consistently reproducible. **Steps to Reproduce** 1. Run the following command (model loads successfully at first time). 2. unload the model 3. Run the same command again. 4. During the second load, the **GPUs enter an error state**. **Command Used** ```bash export LMCACHE_CONFIG_FILE=/path/to/config.yaml python -m vllm.entrypoints.openai.api_server \ --model /usr/local/models/phi-4 \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.9 \ --max-model-len 16384 \ --enable-chunked-prefill \ --kv-cache-dtype auto \ --host 0.0.0.0 \ --port 8000 \ --trust-remote-code \ --enable-prefix-caching \ --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1","kv_role":"kv_both"}'...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #36905 [WIP][BugFix] Add missing shutdown() to LMCacheConnectorV1 to fix GPU failure on repeated model loading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ring the second initialization. This behavior is consistently reproducible. **Steps to Reproduce** 1. Run the following command (model loads successfully at first time). 2. unload the model 3. Run the same command again...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GPU failure during repeated model loading when using --enable-prefix-caching with KV transfer (LMCacheConnectorV1) bug ### Environment Information ### 🐛 Describe the bug The GPUs are entering an error state durin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: tate during the second initialization. This behavior is consistently reproducible. **Steps to Reproduce** 1. Run the following command (model loads successfully at first time). 2. unload the model 3. Run the same comman...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: GUID 3 Rank 1] Process group watchdog thread terminated with exception: CUDA error: unspecified launch failure Search for `cudaErrorLaunchFailure' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.ht...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --gpu-memory-utilization 0.9 \ --max-model-len 16384 \ --enable-chunked-prefill \ --kv-cache-dtype auto \ --host 0.0.0.0 \ --port 8000 \ --trust-remote-code \ --enable-prefix-caching \ --kv-transfer-config '{"kv_connect...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | xdc253 (0x7697b10b0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7697b9204ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown funct… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | m-venv/lib/python3.10/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdc253 (0x7697b10b0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | xdc253 (0x7697b10b0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7697b9204ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown funct… |
| [#36905](https://github.com/vllm-project/vllm/pull/36905) | closes_keyword | 0.95 | [WIP][BugFix] Add missing shutdown() to LMCacheConnectorV1 to fix GPU failure on repeated model loading | Fixes #36852. `LMCacheConnectorV1` did not override `shutdown()`, inheriting the base class no-op from `KVConnectorBase_V1`. When `GPUWorker.shutdown()` calls `ensure_kv_transfer_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
