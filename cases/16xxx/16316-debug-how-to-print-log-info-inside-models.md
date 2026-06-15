# vllm-project/vllm#16316: [Debug]: How to print/log info inside models

| 字段 | 值 |
| --- | --- |
| Issue | [#16316](https://github.com/vllm-project/vllm/issues/16316) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Debug]: How to print/log info inside models

### Issue 正文摘录

### Your current environment OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.13.0-40-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A5000 GPU 1: NVIDIA RTX A5000 GPU 2: NVIDIA RTX A5000 GPU 3: NVIDIA RTX A5000 Nvidia driver version: 530.30.02 vLLM Version: 0.8.3rc2.dev80+gcb84e45ac.d20250409 ### How would you like to use vllm Hi there, I try to debug the model by adding a line of code `logger.debug(f"hidden_states: {hidden_states.shape}")` in line 343, `vllm/vllm/model_executor/models/qwen2.py` file. But I get the error below: ``` ERROR 04-09 13:42:56 [core.py:386] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-09 13:42:56 [core.py:386] File "/storage_fast/ylqiu/programming/vllm/vllm/v1/engine/core.py", line 377, in run_engine_core ERROR 04-09 13:42:56 [core.py:386] engine_core = EngineCoreProc(*args, **kwargs)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: usage ### Your current environment OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python versio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Debug]: How to print/log info inside models usage ### Your current environment OS: Ubuntu 20.04.4 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ntime) Python platform: Linux-5.13.0-40-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A5000 GPU 1: N...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: vailable_memory ERROR 04-09 13:42:56 [core.py:386] self.model_runner.profile_run() ERROR 04-09 13:42:56 [core.py:386] File "/storage_fast/ylqiu/programming/vllm/vllm/v1/worker/gpu_model_runner.py", line 1592, in profile...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nvert.py", line 962, in step ERROR 04-09 13:42:56 [core.py:386] self.dispatch_table[inst.opcode](self, inst) ERROR 04-09 13:42:56 [core.py:386] File "/storage_fast/ylqiu/miniconda3/envs/embed/lib/python3.11/site-package...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
