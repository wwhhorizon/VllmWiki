# vllm-project/vllm#4946: [Bug]: Error executing method load_model. This might cause deadlock in distributed execution.

| 字段 | 值 |
| --- | --- |
| Issue | [#4946](https://github.com/vllm-project/vllm/issues/4946) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error executing method load_model. This might cause deadlock in distributed execution.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: version 3.29.3 Libc version: glibc-2.27 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.15.0-213-generic-x86_64-with-glibc2.27 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla T4 GPU 1: Tesla T4 GPU 2: Tesla T4 GPU 3: Tesla T4 GPU 4: Tesla T4 GPU 5: Tesla T4 GPU 6: Tesla T4 GPU 7: Tesla T4 Nvidia driver version: 530.30.02 ### 🐛 Describe the bug I changed "torch_dtype" to "float16" in the model configuration file 'config.json' CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --model /data/deepseek/deepseek-coder-6.7b-base --served-model-name deepseek --tensor-parallel-size 4 --port 1101 (RayWorkerWrapper pid=28810) ERROR 05-21 12:53:01 worker_base.py:145] Error executing method load_model. This might...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC ver...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: idia driver version: 530.30.02 ### 🐛 Describe the bug I changed "torch_dtype" to "float16" in the model configuration file 'config.json' CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Error executing method load_model. This might cause deadlock in distributed execution. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Error executing method load_model. This might cause deadlock in distributed execution. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` PyTorch version: 2.3.0+cu121 Is debu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
