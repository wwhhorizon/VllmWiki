# vllm-project/vllm#33857: [Bug]: Qwen3-Coder-Next fails with Triton allocator error on DGX Spark cluster (GB10, sm121)

| 字段 | 值 |
| --- | --- |
| Issue | [#33857](https://github.com/vllm-project/vllm/issues/33857) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Coder-Next fails with Triton allocator error on DGX Spark cluster (GB10, sm121)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Qwen3-Coder-Next (any variant, I tried FP8, AWQ and NVFP4) on my dual DGX Spark cluster, vLLM fails during inference with the following errror: RuntimeError: Kernel requires a runtime memory allocation, but no allocator was set. Use triton.set_allocator to specify an allocator. This only happens when running in the cluster, the model runs fine on a single node. I haven't tried other Qwen3-Next models in the cluster, but I suspect they would behave the same way. It also doesn't matter whether I use FLASH_ATTN or FLASHINFER, or whether it uses Triton MoE FP8 or Marlin backend - the error is always the same. The only way to get around the error is to run with `--enforce-eager`, but that kills performance. Also doesn't matter whether I use fastsafetensors or not. Here is the example launch command: ```bash vllm serve Qwen/Qwen3-Coder-Next-FP8 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --gpu-memory-utilization 0.8 \ --host 0.0.0.0 --port 8888 \ --load-format fastsafetensors \ --attention-backend flashinfer \ --enable-prefix-caching \ -tp 2 --distributed-executor-backend ray ``` Exception: ```text (Engi...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 🐛 Describe the bug When running Qwen3-Coder-Next (any variant, I tried FP8, AWQ and NVFP4) on my dual DGX Spark cluster, vLLM fails during inference with the following errror: RuntimeError: Kernel requires a runtime mem...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ory allocation, but no allocator was set. Use triton.set_allocator to specify an allocator. This only happens when running in the cluster, the model runs fine on a single node. I haven't tried other Qwen3-Next models in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: :968] return self._execute_dag(scheduler_output, grammar_output, non_block) (EngineCore_DP0 pid=1117) ERROR 02-05 00:58:24 [core.py:968] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-Coder-Next fails with Triton allocator error on DGX Spark cluster (GB10, sm121) bug;stale ### Your current environment ### 🐛 Describe the bug When running Qwen3-Coder-Next (any variant, I tried FP8, AWQ and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Qwen3-Coder-Next fails with Triton allocator error on DGX Spark cluster (GB10, sm121) bug;stale ### Your current environment ### 🐛 Describe the bug When running Qwen3-Coder-Next (any variant, I tried FP8, AWQ and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
