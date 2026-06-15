# vllm-project/vllm#669: can't build in windows

| 字段 | 值 |
| --- | --- |
| Issue | [#669](https://github.com/vllm-project/vllm/issues/669) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> can't build in windows

### Issue 正文摘录

On win10 I have cuda 11.8 and pytorch using cuda 11.8. nvcc and python torch show the same version: ``` C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools>nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022 Cuda compilation tools, release 11.8, V11.8.89 Build cuda_11.8.r11.8/compiler.31833905_0 C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools>python Python 3.11.3 (tags/v3.11.3:f3909b8, Apr 4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32 Type "help", "copyright", "credits" or "license" for more information. >>> import torch >>> print(torch.__version__) 2.0.1+cu118 >>> print(torch.cuda.is_available()) True >>> torch.version.cuda '11.8' ``` using pip install vllm, and pip install . on the cloned source gets the same result: ``` _check_cuda_version(compiler_name, compiler_version) File "C:\Users\A\AppData\Local\Temp\pip-build-env-5lg7tzgg\overlay\Lib\site-packages\torch\utils\cpp_extension.py", line 383, in _check_cuda_version torch_cuda_version = packaging.version.parse(torch.version.cuda) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\A\App...

## 现有链接修复摘要

#14891 [Kernel] vLLM Windows CUDA support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: can't build in windows On win10 I have cuda 11.8 and pytorch using cuda 11.8. nvcc and python torch show the same version: ``` C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools>nvcc --version nvcc: NVIDIA (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: can't build in windows On win10 I have cuda 11.8 and pytorch using cuda 11.8. nvcc and python torch show the same version: ``` C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools>nvcc --version nvcc: NVIDIA (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 4)] on win32 Type "help", "copyright", "credits" or "license" for more information. >>> import torch >>> print(torch.__version__) 2.0.1+cu118 >>> print(torch.cuda.is_available()) True >>> torch.version.cuda '11.8' ``` u...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14891](https://github.com/vllm-project/vllm/pull/14891) | closes_keyword | 0.95 | [Kernel] vLLM Windows CUDA support | FIX #669 FIX #5086 FIX #5631 FIX #1685 FIX #179 FIX #2309 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
