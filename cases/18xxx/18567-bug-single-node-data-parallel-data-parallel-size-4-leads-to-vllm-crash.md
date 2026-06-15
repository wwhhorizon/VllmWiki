# vllm-project/vllm#18567: [Bug]: Single-Node data parallel (--data-parallel-size=4) leads to vLLM crash

| 字段 | 值 |
| --- | --- |
| Issue | [#18567](https://github.com/vllm-project/vllm/issues/18567) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Single-Node data parallel (--data-parallel-size=4) leads to vLLM crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running vllm in Data Parallel mode results in crash. This happens on both latest stable version, and on nightly release. Tensor Parallel mode (--tensor-parallel-size=4) works fine and without any problems. To reproduce: ```bash vllm serve --data-parallel-size=4 Qwen/Qwen3-8B ``` Error Trace: ```text DEBUG 05-22 22:30:26 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 05-22 22:30:26 [__init__.py:34] Checking if TPU platform is available. DEBUG 05-22 22:30:26 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 05-22 22:30:26 [__init__.py:52] Checking if CUDA platform is available. DEBUG 05-22 22:30:26 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 05-22 22:30:26 [__init__.py:100] Checking if ROCm platform is available. DEBUG 05-22 22:30:26 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 05-22 22:30:26 [__init__.py:122] Checking if HPU platform is available. DEBUG 05-22 22:30:26 [__init__.py:129] HPU platform is not available because habana_frameworks is not found. DEBUG 05-22 22:30:26 [__init__.py:140] Checking if XPU...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Data Parallel mode results in crash. This happens on both latest stable version, and on nightly release. Tensor Parallel mode (--tensor-parallel-size=4) works fine and without any problems. To reproduce: ```bash vllm se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ngle-Node data parallel (--data-parallel-size=4) leads to vLLM crash bug;stale ### Your current environment ### 🐛 Describe the bug Running vllm in Data Parallel mode results in crash. This happens on both latest stable...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=40960, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 05-22 22:30:26 [__init__.py:52] Checking if CUDA platform is available. DEBUG 05-22 22:30:26 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 05-22 22:30:26 [__init__.py:100] Chec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t any problems. To reproduce: ```bash vllm serve --data-parallel-size=4 Qwen/Qwen3-8B ``` Error Trace: ```text DEBUG 05-22 22:30:26 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 05-22 22:30:26...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
