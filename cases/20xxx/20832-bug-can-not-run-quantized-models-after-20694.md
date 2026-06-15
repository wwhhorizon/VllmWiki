# vllm-project/vllm#20832: [Bug]: Can not run quantized models after #20694

| 字段 | 值 |
| --- | --- |
| Issue | [#20832](https://github.com/vllm-project/vllm/issues/20832) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Can not run quantized models after #20694

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Cannot run quantized models(Qwen3-32B-AWQ) on my 3090 after pr #20694 @mgoin ``` Process EngineCore_0: Traceback (most recent call last): File "/home/mosh/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/mosh/.local/share/uv/python/cpython-3.12.9-linux-x86_64-gnu/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/data/lijinghui/uv_projects/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 590, in run_engine_core raise e File "/data/lijinghui/uv_projects/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 577, in run_engine_core engine_core = EngineCoreProc(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/data/lijinghui/uv_projects/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 404, in __init__ super().__init__(vllm_config, executor_class, log_stats, File "/data/lijinghui/uv_projects/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 75, in __init__ self.model_executor = executor_class(vllm_config) ^^^^^^^^^^^^^...

## 现有链接修复摘要

#20694 Use NVCC `--compress-mode` to reduce binary size by 30%

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. [rank0]:[W712 01:41:12.596494424 ProcessGroupNCCL.cpp:1476] Warning: WARNING:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^ RuntimeError: CUDA error: invalid resource handle CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Can not run quantized models after #20694 bug ### Your current environment ### 🐛 Describe the bug Cannot run quantized models(Qwen3-32B-AWQ) on my 3090 after pr #20694 @mgoin ``` Process EngineCore_0: Traceback (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Can not run quantized models after #20694 bug ### Your current environment ### 🐛 Describe the bug Cannot run quantized models(Qwen3-32B-AWQ) on my 3090 after pr #20694 @mgoin ``` Process EngineCore_0: Traceback (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;quantization;speculative_decoding cuda;kernel;operator;quantization;triton build_error;crash;mismatch env_dependency #20694 Use NVCC `--compress-mode` to reduce binary size by 30% Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20694](https://github.com/vllm-project/vllm/pull/20694) | mentioned | 0.45 | Use NVCC `--compress-mode` to reduce binary size by 30% | e bug cannot run quantized models(qwen3-32b-awq) on my 3090 after pr #20694 @mgoin ``` process enginecore_0: traceback (most recent call last): file "/home/mosh/.local/share/uv/py… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
