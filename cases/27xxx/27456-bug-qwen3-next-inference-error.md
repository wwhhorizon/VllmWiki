# vllm-project/vllm#27456: [Bug]: Qwen3-Next Inference error

| 字段 | 值 |
| --- | --- |
| Issue | [#27456](https://github.com/vllm-project/vllm/issues/27456) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next Inference error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3-Next Inference error ```shell PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.7 \ --disable_custom_all_reduce \ --max-model-len 32000 ``` ```logs No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). (EngineCore_DP0 pid=395) INFO 10-24 11:21:57 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). (EngineCore_DP0 pid=395) INFO 10-24 11:22:57 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). (EngineCore_DP0 pid=395) INFO 10-24 11:23:57 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming wo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: Qwen3-Next Inference error bug;stale ### Your current environment ### 🐛 Describe the bug Qwen3-Next Inference error ```shell PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve Qwen/Qwen3-Next-80B-A3B-I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: er=''), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=Qwen/Qwen3-Next-80B-A3B-Instruct, enable_prefix_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: pandable_segments:True \ vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --dtype bfloat16 \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.7 \ --disable_custom_all_reduce \ --max-model-len 32000 ``` ```logs No avai...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: --max-model-len 32000 ``` ```logs No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). (EngineCore_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-Next Inference error bug;stale ### Your current environment ### 🐛 Describe the bug Qwen3-Next Inference error ```shell PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True \ vllm serve Qwen/Qwen3-Next-80B-A3B-I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
