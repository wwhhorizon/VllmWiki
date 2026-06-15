# vllm-project/vllm#17517: [Bug]: vllm-v0 engine Qwen2.5 Model run eagle algo, KeyError: 'norm.weight' bugfix

| 字段 | 值 |
| --- | --- |
| Issue | [#17517](https://github.com/vllm-project/vllm/issues/17517) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm-v0 engine Qwen2.5 Model run eagle algo, KeyError: 'norm.weight' bugfix

### Issue 正文摘录

### Your current environment INFO 05-01 12:26:10 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /mnt/bn/pan-personal-bytenas-lf/software/conda/anaconda3/envs/ycp_py39_vllm/lib/python3.9/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: version 3.30.3 Libc version: glibc-2.36 Python version: 3.9.21 (main, Dec 11 2024, 16:24:11) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.143.bsk.8-amd64-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L20 GPU 1: NVIDIA L20 GPU 2: NVIDIA L20 GPU 3: NVIDIA L20 Nvidia driver version:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: t INFO 05-01 12:26:10 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /mnt/bn/pan-personal-bytenas-lf/software/conda/anaconda3/envs/ycp_py39_vllm/lib/python3.9/site-packages...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm-v0 engine Qwen2.5 Model run eagle algo, KeyError: 'norm.weight' bugfix bug;stale ### Your current environment INFO 05-01 12:26:10 [__init__.py:239] Automatically detected platform cuda. Collecting environmen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine Qwen2.5 Model run eagle algo, KeyError: 'norm.weight' bugfix bug;stale ### Your current environment INFO 05-01 12:26:10 [__init__.py:239] Automatically detected platform cuda. Collecting environment information.....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.51.3 [pip3] triton==3.2.0 [conda] numpy 2.0.2 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
