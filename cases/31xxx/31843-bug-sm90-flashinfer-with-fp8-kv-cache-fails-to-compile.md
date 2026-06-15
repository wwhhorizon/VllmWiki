# vllm-project/vllm#31843: [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile

| 字段 | 值 |
| --- | --- |
| Issue | [#31843](https://github.com/vllm-project/vllm/issues/31843) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If I run a simple Qwen model on H100 using the FlashInfer backend with FP8 kv cache, I see this long compilation failure. I've even installed the cubins and jit cache ahead of time with: ``` uv pip install flashinfer-cubin uv pip install flashinfer-jit-cache==0.5.3 --index-url https://flashinfer.ai/whl/cu129 ``` Command and log: ``` vllm serve Qwen/Qwen3-0.6B --enforce-eager --attention-backend flashinfer --kv-cache-dtype fp8 (APIServer pid=2246783) INFO 01-06 23:15:33 [api_server.py:1278] vLLM API server version 0.14.0rc1.dev48+gc02a2705f (APIServer pid=2246783) INFO 01-06 23:15:33 [utils.py:253] non-default args: {'model_tag': 'Qwen/Qwen3-0.6B', 'enforce_eager': True, 'attention_backend': 'flashinfer', 'kv_cache_dtype': 'fp8'} (APIServer pid=2246783) INFO 01-06 23:15:34 [model.py:522] Resolved architecture: Qwen3ForCausalLM (APIServer pid=2246783) INFO 01-06 23:15:34 [model.py:1515] Using max model len 40960 (APIServer pid=2246783) INFO 01-06 23:15:34 [cache.py:205] Using fp8 data type to store kv cache. It reduces the GPU memory footprint and boosts the performance. Meanwhile, it may cause accuracy drop without a proper scalin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile bug;stale ### Your current environment ### 🐛 Describe the bug If I run a simple Qwen model on H100 using the FlashInfer backend with FP8 kv cache, I see this lon...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile bug;stale ### Your current environment ### 🐛 Describe the bug If I run a simple Qwen model on H100 using the FlashInfer backend with FP8 kv cache, I see this lon...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile bug;stale ### Your current environment ### 🐛 Describe the bug If I run a simple Qwen model on H100 using the FlashInfer backend with FP8 kv cache, I see this lon...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile bug;stale ### Your current environment ### 🐛 Describe the bug If I run a simple Qwen model on H100 using the FlashInfer backend with FP8 kv cache, I see this lon...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: SM90 FlashInfer with FP8 kv cache fails to compile bug;stale ### Your current environment ### 🐛 Describe the bug If I run a simple Qwen model on H100 using the FlashInfer backend with FP8 kv cache, I see this lon...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
