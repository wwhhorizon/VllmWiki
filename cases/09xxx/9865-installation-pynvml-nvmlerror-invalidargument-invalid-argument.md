# vllm-project/vllm#9865: [Installation]: pynvml.NVMLError_InvalidArgument: Invalid Argument

| 字段 | 值 |
| --- | --- |
| Issue | [#9865](https://github.com/vllm-project/vllm/issues/9865) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: pynvml.NVMLError_InvalidArgument: Invalid Argument

### Issue 正文摘录

### Your current environment ```text [infxGPU Msg(52547:140064190512000:libvgpu.c:872)]: Initializing... Collecting environment information... [infxGPU Msg(52547:140064190512000:hook.c:400)]: loaded nvml libraries [infxGPU Msg(52547:140064190512000:hook.c:408)]: initial_virtual_map /root/miniconda3/envs/myenv/lib/python3.10/site-packages/_distutils_hack/__init__.py:54: UserWarning: Reliance on distutils from stdlib is deprecated. Users must rely on setuptools to provide the distutils module. Avoid importing distutils or import setuptools first, and avoid setting SETUPTOOLS_USE_DISTUTILS=stdlib. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.15 (main, Oct 3 2024, 07:27:34) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1067-kvm-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: pynvml.NVMLError_InvalidArgument: Invalid Argument installation ### Your current environment ```text [infxGPU Msg(52547:140064190512000:libvgpu.c:872)]: Initializing... Collecting environment information.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: .yml warnings.warn( PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 40064190512000:libvgpu.c:872)]: Initializing... Collecting environment information... [infxGPU Msg(52547:140064190512000:hook.c:400)]: loaded nvml libraries [infxGPU Msg(52547:140064190512000:hook.c:408)]: initial_virtu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation;...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.46.1 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
