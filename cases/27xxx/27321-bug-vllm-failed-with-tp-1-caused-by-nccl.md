# vllm-project/vllm#27321: [Bug]: vllm failed with TP > 1(caused by nccl?)

| 字段 | 值 |
| --- | --- |
| Issue | [#27321](https://github.com/vllm-project/vllm/issues/27321) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm failed with TP > 1(caused by nccl?)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python CUDA_VISIBLE_DEVICES=0,1 VLLM_LOGGING_LEVEL=DEBUG VLLM_TRACE_FUNCTION=1 vllm serve Qwen/Qwen3-0.6B-FP8 --gpu-memory-utilization 0.9 --enforce-eager --tensor-parallel-size 2 ``` ``` /data/lijinghui/uv_projects/.venv/lib/python3.13/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] DEBUG 10-22 15:36:53 [plugins/__init__.py:32] No plugins for group vllm.platform_plugins found. DEBUG 10-22 15:36:53 [platforms/__init__.py:36] Checking if TPU platform is available. DEBUG 10-22 15:36:53 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' DEBUG 10-22 15:36:53 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 10-22 15:36:53 [platforms/__init__.py:84] Confirmed CUDA platform is available. DEBUG 10-22 15:36:53 [platforms/__init__.py:112] Checking if ROCm platform is available. DEBUG 10-22 15:36:53 [platforms/__init__.py:126] ROCm platfor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: /__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: vllm failed with TP > 1(caused by nccl?) bug;stale ### Your current environment ### 🐛 Describe the bug ```python CUDA_VISIBLE_DEVICES=0,1 VLLM_LOGGING_LEVEL=DEBUG VLLM_TRACE_FUNCTION=1 vllm serve Qwen/Qwen3-0.6B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: LLM_LOGGING_LEVEL=DEBUG VLLM_TRACE_FUNCTION=1 vllm serve Qwen/Qwen3-0.6B-FP8 --gpu-memory-utilization 0.9 --enforce-eager --tensor-parallel-size 2 ``` ``` /data/lijinghui/uv_projects/.venv/lib/python3.13/site-packages/t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', enable_in_reasonin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: stale ### Your current environment ### 🐛 Describe the bug ```python CUDA_VISIBLE_DEVICES=0,1 VLLM_LOGGING_LEVEL=DEBUG VLLM_TRACE_FUNCTION=1 vllm serve Qwen/Qwen3-0.6B-FP8 --gpu-memory-utilization 0.9 --enforce-eager --t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
