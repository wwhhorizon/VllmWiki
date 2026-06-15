# vllm-project/vllm#2624: [Bug ] Memory leak on latest release 0.2.7

| 字段 | 值 |
| --- | --- |
| Issue | [#2624](https://github.com/vllm-project/vllm/issues/2624) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug ] Memory leak on latest release 0.2.7

### Issue 正文摘录

I'm able to run TheBloke/dolphin-2.6-mixtral-8x7b-AWQ on 2x 4090s on git hash 1db83e3 but in the new release I receive the following cuda out of memory error: ``` Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/home/user/projects/repos/vllm/vllm/entrypoints/openai/api_server.py", line 217, in engine = AsyncLLMEngine.from_engine_args(engine_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/user/projects/repos/vllm/vllm/engine/async_llm_engine.py", line 617, in from_engine_args engine = cls(parallel_config.worker_use_ray, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/user/projects/repos/vllm/vllm/engine/async_llm_engine.py", line 321, in __init__ self.engine = self._init_engine(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/user/projects/repos/vllm/vllm/engine/async_llm_engine.py", line 366, in _init_engine return engine_class(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/user/projects/repos/vllm/vllm/engine/llm_engine.py", line 112, in __init__ self._init_cache() File "/home/user/projects/repos/vllm/vllm/engine/llm_engine.py", line 339, in _init_cache self._run_workers(...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ght be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1. Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` Command: ``` RAY_memory_usage_threshold=1 python3 -m vllm.entrypoints.open...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4090s on git hash 1db83e3 but in the new release I receive the following cuda out of memory error: ``` Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _llm_engine.py", line 617, in from_engine_args engine = cls(parallel_config.worker_use_ray, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/user/projects/repos/vllm/vllm/engine/async_llm_engine.py", line 321, in __init_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: quantization;scheduler_memory cuda;kernel;quantization build_error;crash;mismatch;oom env_dependency I'm able to run TheBloke/dolphin-2.6-mixtral-8x7b-AWQ on 2x 4090s on git hash 1db83e3 but in the new release I receive...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ``` correctness ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory cuda;kernel;quantization build_error;crash;mismatch;oom env_dependency I'm able to run TheBloke/dolphin-2.6-mixtral-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
