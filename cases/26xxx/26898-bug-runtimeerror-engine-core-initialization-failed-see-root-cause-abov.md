# vllm-project/vllm#26898: [Bug]: RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s)

| 字段 | 值 |
| --- | --- |
| Issue | [#26898](https://github.com/vllm-project/vllm/issues/26898) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **I plan to deploy and autonomously configure Tensor Parallel (TP) dimensions using the VLLM framework based on the local Qwen3-30B-A3B model. At the same time, I will perform performance analysis using NSYS tools. However, after multiple operations, the same error occurs, and when the tensor parallel dimension is set to 2, 4, or 8, the error will reappear.** nsys profile -o ./vllm_profile.qdrep python vllm_profiler.py INFO 10-15 08:32:21 [init.py:216] Automatically detected platform cuda. Loading model: ..../Qwen3-30B-A3B INFO 10-15 08:32:24 [utils.py:233] non-default args: {‘trust_remote_code’: True, ‘tensor_parallel_size’: 4, ‘gpu_memory_utilization’: 0.8, ‘disable_log_stats’: True, ‘model’: ‘..../Qwen3-30B-A3B’} The argument trust_remote_code is to be used with Auto classes. It has no effect here and is ignored. INFO 10-15 08:32:24 [model.py:547] Resolved architecture: Qwen3MoeForCausalLM torch_dtype is deprecated! Use dtype instead! INFO 10-15 08:32:24 [model.py:1510] Using max model len 40960 INFO 10-15 08:32:25 [scheduler.py:205] Chunked prefill is enabled with max_num_batched_tokens=8192. (EngineCore_DP0 pid=59619) INFO 1...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ore initialization failed. See root cause above. Failed core proc(s) bug;stale ### Your current environment ### 🐛 Describe the bug **I plan to deploy and autonomously configure Tensor Parallel (TP) dimensions using the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: er=‘’), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/home/ffc3/yfzhao/models/Qwen3-30B-A3B, enable_p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 08:32:24 [model.py:547] Resolved architecture: Qwen3MoeForCausalLM torch_dtype is deprecated! Use dtype instead! INFO 10-15 08:32:24 [model.py:1510] Using max model len 40960 INFO 10-15 08:32:25 [scheduler.py:205] Chunk...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ironment ### 🐛 Describe the bug **I plan to deploy and autonomously configure Tensor Parallel (TP) dimensions using the VLLM framework based on the local Qwen3-30B-A3B model. At the same time, I will perform performance...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ler.py INFO 10-15 08:32:21 [init.py:216] Automatically detected platform cuda. Loading model: ..../Qwen3-30B-A3B INFO 10-15 08:32:24 [utils.py:233] non-default args: {‘trust_remote_code’: True, ‘tensor_parallel_size’: 4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
