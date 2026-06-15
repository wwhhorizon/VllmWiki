# vllm-project/vllm#315: RunTime Error: Cannot find CUDA at CUDA_HOME

| 字段 | 值 |
| --- | --- |
| Issue | [#315](https://github.com/vllm-project/vllm/issues/315) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RunTime Error: Cannot find CUDA at CUDA_HOME

### Issue 正文摘录

running ```nvcc -V``` results ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022 Cuda compilation tools, release 11.8, V11.8.89 Build cuda_11.8.r11.8/compiler.31833905_0 ``` I am currently in a Conda environment. But I receive RunTime error when attempting to install vllm ``` No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8' Traceback (most recent call last): File "C:\Users\danng\anaconda3\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 351, in main() File "C:\Users\danng\anaconda3\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 333, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "C:\Users\danng\anaconda3\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "C:\Users\danng\AppData\Local\Temp\pip-build-env-c61dnyp7\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in get_requires_for_build_wheel return self._get_build_requires(config_settings, requirements=['wheel']) File "C:\Users...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: UDA at CUDA_HOME running ```nvcc -V``` results ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022 Cuda compilation tools, release...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: RunTime Error: Cannot find CUDA at CUDA_HOME running ```nvcc -V``` results ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022 Cud...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "C:\Users\danng\AppData\Local\Temp\pip-build-env-c61dnyp7\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in get_requires_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
