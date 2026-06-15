# vllm-project/vllm#21906: [Bug]: RuntimeError: Worker failed with error 'Only dense CPU tensors can be pinned'

| 字段 | 值 |
| --- | --- |
| Issue | [#21906](https://github.com/vllm-project/vllm/issues/21906) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Worker failed with error 'Only dense CPU tensors can be pinned'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug How to reproduce the error: ```bash vllm serve Qwen/Qwen2.5-VL-7B-Instruct --port 8000 --host 0.0.0.0 --dtype bfloat16 -mm-processor-kwargs.device cuda ``` Error: ``` 05:56:13 [core.py:515] EngineCore failed to start. ERROR 07-30 05:56:13 [core.py:515] Traceback (most recent call last): ERROR 07-30 05:56:13 [core.py:515] File "/miniconda/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 506, in run_engine_core ERROR 07-30 05:56:13 [core.py:515] engine_core = EngineCoreProc(*args, **kwargs) ERROR 07-30 05:56:13 [core.py:515] File "/miniconda/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 390, in __init__ ERROR 07-30 05:56:13 [core.py:515] super().__init__(vllm_config, executor_class, log_stats, ERROR 07-30 05:56:13 [core.py:515] File "/miniconda/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 83, in __init__ ERROR 07-30 05:56:13 [core.py:515] self._initialize_kv_caches(vllm_config) ERROR 07-30 05:56:13 [core.py:515] File "/miniconda/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 141, in _initialize_kv_caches ERROR 07-30 05:56:13 [core.py:515] available_gpu_memory = self.model_executor.de...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ### 🐛 Describe the bug How to reproduce the error: ```bash vllm serve Qwen/Qwen2.5-VL-7B-Instruct --port 8000 --host 0.0.0.0 --dtype bfloat16 -mm-processor-kwargs.device cuda ``` Error: ``` 05:56:13 [core.py:515] Engine...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm cuda;gemm;triton build_error;crash dtype;env_dependency;s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: bash vllm serve Qwen/Qwen2.5-VL-7B-Instruct --port 8000 --host 0.0.0.0 --dtype bfloat16 -mm-processor-kwargs.device cuda ``` Error: ``` 05:56:13 [core.py:515] EngineCore failed to start. ERROR 07-30 05:56:13 [core.py:51...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --port 8000 --host 0.0.0.0 --dtype bfloat16 -mm-processor-kwargs.device cuda ``` Error: ``` 05:56:13 [core.py:515] EngineCore failed to start. ERROR 07-30 05:56:13 [core.py:515] Traceback (most recent call last): ERROR...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ror: Worker failed with error 'Only dense CPU tensors can be pinned' bug;stale ### Your current environment ### 🐛 Describe the bug How to reproduce the error: ```bash vllm serve Qwen/Qwen2.5-VL-7B-Instruct --port 8000 -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
