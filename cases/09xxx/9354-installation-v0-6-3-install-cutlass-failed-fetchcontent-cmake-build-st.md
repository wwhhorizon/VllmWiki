# vllm-project/vllm#9354: [Installation]: v0.6.3 install -cutlass failed (Fetchcontent.cmake build step)

| 字段 | 值 |
| --- | --- |
| Issue | [#9354](https://github.com/vllm-project/vllm/issues/9354) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: v0.6.3 install -cutlass failed (Fetchcontent.cmake build step)

### Issue 正文摘录

### Your current environment Collecting environment information... WARNING 10-16 03:35:02 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/work/.local/lib/python3.10/site-packages/_distutils_hack/__init__.py:54: UserWarning: Reliance on distutils from stdlib is deprecated. Users must rely on setuptools to provide the distutils module. Avoid importing distutils or import setuptools first, and avoid setting SETUPTOOLS_USE_DISTUTILS=stdlib. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml warnings.warn( PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.4 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.4.0-148-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.52 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: CUDA GPU GPU 1: CUDA G...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: v0.6.3 install -cutlass failed (Fetchcontent.cmake build step) installation;stale ### Your current environment Collecting environment information... WARNING 10-16 03:35:02 _custom_ops.py:19] Failed to imp
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: .yml warnings.warn( PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nstallation;stale ### Your current environment Collecting environment information... WARNING 10-16 03:35:02 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/wo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tion.yml warnings.warn( PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Installation]: v0.6.3 install -cutlass failed (Fetchcontent.cmake build step) installation;stale ### Your current environment Collecting environment information... WARNING 10-16 03:35:02 _custom_ops.py:19] Failed to im...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
