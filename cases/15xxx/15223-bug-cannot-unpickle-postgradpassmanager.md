# vllm-project/vllm#15223: [Bug]: Cannot unpickle PostGradPassManager

| 字段 | 值 |
| --- | --- |
| Issue | [#15223](https://github.com/vllm-project/vllm/issues/15223) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot unpickle PostGradPassManager

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This issue doesn't occur when running `vllm serve`. However, when I was trying to extend additional logics to the OpenAI-compatible server from python sdk, it seemed to run into this pickle issue with the compiler ```prolog EngineCore hit an exception: Traceback (most recent call last): File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 332, in run_engine_core engine_core = EngineCoreProc(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 287, in __init__ super().__init__(vllm_config, executor_class, log_stats) File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 62, in __init__ num_gpu_blocks, num_cpu_blocks = self._initialize_kv_caches( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 121, in _initialize_kv_caches available_gpu_memory = self.model_executor.determine_available_memory() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: server from python sdk, it seemed to run into this pickle issue with the compiler ```prolog EngineCore hit an exception: Traceback (most recent call last): File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: vllm/v1/engine/core.py", line 287, in __init__ super().__init__(vllm_config, executor_class, log_stats) File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 62, in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Cannot unpickle PostGradPassManager bug ### Your current environment ### 🐛 Describe the bug This issue doesn't occur when running `vllm serve`. However, when I was trying to extend additional logics to the OpenAI...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: /site-packages/vllm/v1/engine/core.py", line 62, in __init__ num_gpu_blocks, num_cpu_blocks = self._initialize_kv_caches( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: orker.py", line 157, in determine_available_memory self.model_runner.profile_run() File "/home/paperspace/workspace/BentoVLLM/.venv/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 1464, in profile...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
