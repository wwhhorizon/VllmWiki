# vllm-project/vllm#20956: [Usage]: How to feed multiple local images to llama4

| 字段 | 值 |
| --- | --- |
| Issue | [#20956](https://github.com/vllm-project/vllm/issues/20956) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to feed multiple local images to llama4

### Issue 正文摘录

### Your current environment ```text INFO 07-14 18:39:23 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /data/miniconda3/envs/lm_fact/lib/python3.11/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( ============================== System Info ============================== OS : Ubuntu 22.04.4 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.13 (main, Jun 5 2025, 13:12:00) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-4.18.0-513.5.1.el8_9.x86_64-x86_64-with-glibc2.35 =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: How to feed multiple local images to llama4 usage;stale ### Your current environment ```text INFO 07-14 18:39:23 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /da...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: xt INFO 07-14 18:39:23 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /data/miniconda3/envs/lm_fact/lib/python3.11/site-packages/_distutils_hack/__init__.py:30: UserWarning...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: How to feed multiple local images to llama4 usage;stale ### Your current environment ```text INFO 07-14 18:39:23 [__init__.py:239] Automatically detected platform cuda. Collecting environment information... /da...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dio==2.6.0 [pip3] torchvision==0.21.0 [pip3] transformers==4.52.4 [pip3] triton==3.2.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.4.5.8 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.4.127

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
