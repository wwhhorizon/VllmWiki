# vllm-project/vllm#9367: [Bug]: --cpu-offload-gb flag not honored in vllm/vllm-openai container on amazon g5.2xlarge

| 字段 | 值 |
| --- | --- |
| Issue | [#9367](https://github.com/vllm-project/vllm/issues/9367) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --cpu-offload-gb flag not honored in vllm/vllm-openai container on amazon g5.2xlarge

### Issue 正文摘录

### Your current environment Collecting environment information... /opt/conda/lib/python3.12/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.16.3 Libc version: glibc-2.31 Python version: 3.12.6 | packaged by conda-forge | (main, Sep 22 2024, 14:16:49) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.0-1070-aws-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G Nvidia driver version: 550.90.07 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian Address sizes: 48 bits physical, 48 bits virtual CPU(s): 8 On-line CPU(s) list: 0-7 Thread(s) per core: 2 Core(s) p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._version' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: 2xlarge bug;stale ### Your current environment Collecting environment information... /opt/conda/lib/python3.12/site-packages/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm._vers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: flag not honored in vllm/vllm-openai container on amazon g5.2xlarge bug;stale ### Your current environment Collecting environment information... /opt/conda/lib/python3.12/site-packages/vllm/connections.py:8: RuntimeWarn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ion__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -trust-remote-code --max-model-len 30000 --gpu-memory-utilization 0.90 --dtype float16 --cpu-offload-gb 4 And the output: /usr/local/lib/python3.12/dist-packages/vllm/connections.py:8: RuntimeWarning: Failed to read com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
