# vllm-project/vllm#36452: [Bug]: Qwen3.5-35B-A3B-FP8 AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#36452](https://github.com/vllm-project/vllm/issues/36452) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-35B-A3B-FP8 AssertionError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM if __name__ == "__main__": llm = LLM( model="Qwen/Qwen3.5-35B-A3B-FP8", trust_remote_code=True, dtype="bfloat16", gpu_memory_utilization=0.9, quantization="fp8", disable_custom_all_reduce=True, tensor_parallel_size=1, enable_prefix_caching=True, language_model_only=True, ) ``` I launch above code by `CUDA_VISIBLE_DEVICES python3 inference_test.py`. And it throws me AssertionError. ```bash EngineCore failed to start. Traceback (most recent call last): File "/A.I_DATA/jbnu/.local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1090, in run_engine_core engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/A.I_DATA/jbnu/.local/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/A.I_DATA/jbnu/.local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 834, in __init__ super().__init__( File "/A.I_DATA/jbnu/.local/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 120, in __init__ num_gpu_blocks, num_cpu_blocks, kv_cache_con...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM if __name__ == "__main__": llm = LLM( model="Qwen/Qwen3.5-35B-A3B-FP8", trust_remote_code=True, dtype="bfloat16", gpu_memory_utilization=0.9...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3.5-35B-A3B-FP8 AssertionError bug ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM if __name__ == "__main__": llm = LLM( model="Qwen/Qwen3.5-35B-A3B-FP8", trust_remote_cod
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-35B-A3B-FP8 AssertionError bug ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM if __name__ == "__main__": llm = LLM( model="Qwen/Qwen3.5-35B-A3B-FP8",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rue, language_model_only=True, ) ``` I launch above code by `CUDA_VISIBLE_DEVICES python3 inference_test.py`. And it throws me AssertionError. ```bash EngineCore failed to start. Traceback (most recent call last): File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
