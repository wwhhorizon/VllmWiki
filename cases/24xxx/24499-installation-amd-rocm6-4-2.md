# vllm-project/vllm#24499: [Installation]: 在amd rocm6.4.2设备上安装报错

| 字段 | 值 |
| --- | --- |
| Issue | [#24499](https://github.com/vllm-project/vllm/issues/24499) |
| 状态 | closed |
| 标签 | installation;rocm;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: 在amd rocm6.4.2设备上安装报错

### Issue 正文摘录

### Your current environment ```text $ python collect_env.py WARNING 09-09 18:29:42 [__init__.py:25] The vLLM package was not found, so its version could not be inspected. This may cause platform detection to fail. INFO 09-09 18:29:42 [__init__.py:243] No platform detected, vLLM is running on UnspecifiedPlatform Collecting environment information... /home/modelscope/anaconda3/lib/python3.11/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils. warnings.warn("Setuptools is replacing distutils.") PyTorch version: 2.8.0+rocm6.4 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.4.43482-0f2d60242 OS: Ubuntu 24.04.2 LTS (x86_64) GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.39 Python version: 3.11.7 (main, Dec 15 2023, 18:12:31) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.14.0-29-generic-x86_64-with-glibc2.39 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Radeon Graphics (gfx1151) Nvidia driver version: Could not collect cuDNN ve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: 在amd rocm6.4.2设备上安装报错 installation;rocm;unstale ### Your current environment ```text $ python collect_env.py WARNING 09-09 18:29:42 [__init__.py:25] The vLLM package was not found, so its version could no
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: 在amd rocm6.4.2设备上安装报错 installation;rocm;unstale ### Your current environment ```text $ python collect_env.py WARNING 09-09 18:29:42 [__init__.py:25] The vLLM package was not found, so its version could n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: etected, vLLM is running on UnspecifiedPlatform Collecting environment information... /home/modelscope/anaconda3/lib/python3.11/site-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Installation]: 在amd rocm6.4.2设备上安装报错 installation;rocm;unstale ### Your current environment ```text $ python collect_env.py WARNING 09-09 18:29:42 [__init__.py:25] The vLLM package was not found, so its version could n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -nvjitlink-cu12==12.6.85 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pytorch-triton-rocm==3.4.0+gitf7888497 [pip3] pyzmq==25.1.2 [pip3] torch==2.8.0+rocm6.4 [pip3] torchaudio==2.8.0+rocm6.4 [pip3] torchvision==0.23.0+rocm6....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
