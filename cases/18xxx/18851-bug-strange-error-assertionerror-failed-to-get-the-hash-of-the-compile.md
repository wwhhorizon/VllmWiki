# vllm-project/vllm#18851: [Bug]: Strange error `AssertionError: failed to get the hash of the compiled graph` when running `Qwen/Qwen3-8B` via `LLM` class

| 字段 | 值 |
| --- | --- |
| Issue | [#18851](https://github.com/vllm-project/vllm/issues/18851) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 50; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Strange error `AssertionError: failed to get the hash of the compiled graph` when running `Qwen/Qwen3-8B` via `LLM` class

### Issue 正文摘录

### Your current environment ``` >>> import vllm; vllm.__version__ INFO 05-28 19:02:30 [__init__.py:248] Automatically detected platform cuda. '0.9.1.dev59+gb6a6e7a52' >>> >>> import torch; torch.__version__ '2.7.0+cu126' >>> import transformers; transformers.__version__ '4.52.2' ``` ### 🐛 Describe the bug ``` (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] Traceback (most recent call last): (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] File "/mnt/fs/venv_cu126_py312/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] output = func(*args, **kwargs) (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] File "/mnt/fs/venv_cu126_py312/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] return func(*args, **kwargs) (VllmWorker rank=1 pid=191128) ERROR 05-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Strange error `AssertionError: failed to get the hash of the compiled graph` when running `Qwen/Qwen3-8B` via `LLM` class bug;torch.compile;stale ### Your current environment ``` >>> import vllm; vllm.__version__...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ertionError: failed to get the hash of the compiled graph` when running `Qwen/Qwen3-8B` via `LLM` class bug;torch.compile;stale ### Your current environment ``` >>> import vllm; vllm.__version__ INFO 05-28 19:02:30 [__i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 05-28 18:58:32 [multiproc_executor.py:522] self.model_runner.profile_run() (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] File "/mnt/fs/venv_cu126_py312/lib/python3.12/site-packa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: __ INFO 05-28 19:02:30 [__init__.py:248] Automatically detected platform cuda. '0.9.1.dev59+gb6a6e7a52' >>> >>> import torch; torch.__version__ '2.7.0+cu126' >>> import transformers; transformers.__version__ '4.52.2' ``...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] raise BackendCompilerFailed( (VllmWorker rank=1 pid=191128) ERROR 05-28 18:58:32 [multiproc_executor.py:522] File "/mnt/fs/venv_cu126_py312/lib/python3.12/s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
