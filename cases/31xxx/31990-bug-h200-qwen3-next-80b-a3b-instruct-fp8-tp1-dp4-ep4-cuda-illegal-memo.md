# vllm-project/vllm#31990: [Bug]: [H200] Qwen3-Next-80B-A3B-Instruct-FP8 TP1 DP4 EP4 CUDA illegal memory error

| 字段 | 值 |
| --- | --- |
| Issue | [#31990](https://github.com/vllm-project/vllm/issues/31990) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [H200] Qwen3-Next-80B-A3B-Instruct-FP8 TP1 DP4 EP4 CUDA illegal memory error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] File "/scratch/vllm-dev/vllm/v1/worker/gpu_model_runner.py", line 2885, in synchronize_input_prep [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] yield [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] File "/scratch/vllm-dev/vllm/v1/worker/gpu_model_runner.py", line 3222, in execute_model [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] self._build_attention_metadata( [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] File "/scratch/vllm-dev/vllm/v1/worker/gpu_model_runner.py", line 1779, in _build_attention_metadata [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] _build_attn_group_metadata(kv_cache_gid, attn_gid, cm) [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] File "/scratch/vllm-dev/vllm/v1/worker/gpu_model_runner.py", line 1730, in _build_attn_group_metadata [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] attn_metadata_i = builder.build( [0;36m(EngineCore_DP1 pid=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: neCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] self._build_attention_metadata( [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py:902] File "/scratch/vllm-dev/vllm/v1/worker/gpu_model_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: [H200] Qwen3-Next-80B-A3B-Instruct-FP8 TP1 DP4 EP4 CUDA illegal memory error bug;stale ### Your current environment ### 🐛 Describe the bug ``` [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [H200] Qwen3-Next-80B-A3B-Instruct-FP8 TP1 DP4 EP4 CUDA illegal memory error bug;stale ### Your current environment ### 🐛 Describe the bug ``` [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [H200] Qwen3-Next-80B-A3B-Instruct-FP8 TP1 DP4 EP4 CUDA illegal memory error bug;stale ### Your current environment ### 🐛 Describe the bug ``` [0;36m(EngineCore_DP1 pid=26051)[0;0m ERROR 01-08 11:27:15 [core.py...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --no-enable-prefix-caching \ --data-parallel-size 4 \ --enable-expert-parallel ``` ``` vllm bench serve --host 0.0.0.0 --port 8001 --max-concurrency 16 --model Qwen3-Next-80B-A3B-Instruct-FP8 --random-input-len 1600 --r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
