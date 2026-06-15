# vllm-project/vllm#12649: [Installation]: how to create envs.py file for build on CPU machine?

| 字段 | 值 |
| --- | --- |
| Issue | [#12649](https://github.com/vllm-project/vllm/issues/12649) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: how to create envs.py file for build on CPU machine?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Here's the output of collect_env.py file: WARNING 02-01 09:54:47 _custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.39 Python version: 3.12.3 (main, Jan 17 2025, 18:03:48) [GCC 13.3.0] (64-bit runtime) Python platform: Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.39 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 20 On-line CPU(s) list: 0-19 Ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: how to create envs.py file for build on CPU machine? installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Here's the output of collect_env.py file: WARNING 02
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 47 _custom_ops.py:20] Failed to import from vllm._C with ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') Collecting environment information... PyTorch version: 2.5.1+cpu Is debu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: shared object file: No such file or directory') Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.1.6+cu124torch2.4 [pip3] numpy==1.26.4 [pip3] nvidia-cublas-cu12==12.1.3.1 [pip3] nvidia-cuda-cupti-cu12==12.1.105 [pip3] nvidia-cuda-nvrtc-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tion]: how to create envs.py file for build on CPU machine? installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Here's the output of collect_env.py file: WARNING 02-01 09:54...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
