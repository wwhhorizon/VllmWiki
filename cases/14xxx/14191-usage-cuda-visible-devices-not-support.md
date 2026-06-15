# vllm-project/vllm#14191: [Usage]: CUDA_VISIBLE_DEVICES not support

| 字段 | 值 |
| --- | --- |
| Issue | [#14191](https://github.com/vllm-project/vllm/issues/14191) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: CUDA_VISIBLE_DEVICES not support

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` `Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8 (x86_64) GCC version: (GCC) 8.5.0 20210514 (Red Hat 8.5.0-4) Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.28 Python version: 3.12.9 | packaged by conda-forge | (main, Feb 14 2025, 08:00:06) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-4.18.0-348.7.1.el8_5.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3060 GPU 1: NVIDIA GeForce RTX 3060 GPU 2: NVIDIA GeForce RTX 3060 GPU 3: NVIDIA GeForce RTX 3060 GPU 4: NVIDIA GeForce RTX 3060 GPU 5: NVIDIA GeForce RTX 3060 GPU 6: NVIDIA GeForce RTX 3060 GPU 7: NVIDIA GeForce RTX 3060 Nvidia driver version: 550.142 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True` ### How would you like to use vllm I want to run inference of a [specific model](put link...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ython collect_env.py` ``` `Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 8 (x86_64) GCC versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: CUDA_VISIBLE_DEVICES not support usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` `Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: Fa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: text The output of `python collect_env.py` ``` `Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: --served-model-name DeepSeekR1 \ > --host 0.0.0.0 \ > --port 8086 \ > --dtype float16 \ > --gpu_memory_utilization 0.7 \ > --max-model-len 2048` ERROR 03-04 16:45:10 engine.py:400] torch.OutOfMemoryError: CUDA out of me...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: CUDA_VISIBLE_DEVICES not support usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` `Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: Fa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
