# vllm-project/vllm#20685: [Usage]: Local model returns empty text with vLLM despite matching upstream HF files

| 字段 | 值 |
| --- | --- |
| Issue | [#20685](https://github.com/vllm-project/vllm/issues/20685) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Local model returns empty text with vLLM despite matching upstream HF files

### Issue 正文摘录

### Your current environment ```text INFO 07-09 20:53:46 [__init__.py:240] Automatically detected platform rocm. Collecting environment information... /usr/local/lib/python3.10/dist-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( PyTorch version: 2.4.1 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.25211 OS: Ubuntu 22.04.5 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 15.0.0 CMake version: version 3.29.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, May 27 2025, 17:12:29) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.18.0-348.el8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: K100_AI (gfx928:sramecc+:xnack-) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runtime version: 6.3.25211 MIOpen runti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 9: [Usage]: Local model returns empty text with vLLM despite matching upstream HF files usage ### Your current environment ```text INFO 07-09 20:53:46 [__init__.py:240] Automatically detected platform rocm. Collecting envi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: xt INFO 07-09 20:53:46 [__init__.py:240] Automatically detected platform rocm. Collecting environment information... /usr/local/lib/python3.10/dist-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is rep...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: down: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vuln...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: etion_tokens": 128, "prompt_tokens_details": null } } ``` Example test file: ```python from vllm import LLM, SamplingParams from vllm.assets.image import ImageAsset from transformers import AutoProcessor # Define model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
