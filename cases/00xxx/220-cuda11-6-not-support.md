# vllm-project/vllm#220: CUDA11.6 not support?

| 字段 | 值 |
| --- | --- |
| Issue | [#220](https://github.com/vllm-project/vllm/issues/220) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA11.6 not support?

### Issue 正文摘录

(base) C:\Users\a>pip install vllm Collecting vllm Using cached vllm-0.1.1.tar.gz (83 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exited-with-error × Getting requirements to build wheel did not run successfully. │ exit code: 1 ╰─> [16 lines of output] No CUDA runtime is found, using CUDA_HOME='C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6' Traceback (most recent call last): File "D:\software_loc\anaconda\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 363, in main() File "D:\software_loc\anaconda\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 345, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "D:\software_loc\anaconda\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 130, in get_requires_for_build_wheel return hook(config_settings) File "C:\Users\hzy\AppData\Local\Temp\pip-build-env-67chdc7b\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in get_requires_for_build_wheel return self._get_build_requires(config_settings, requirements=['wheel']) File "C:\Users\hzy\AppData\Local\Temp\pip-build-env-67chdc7b\overlay...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CUDA11.6 not support? (base) C:\Users\a>pip install vllm Collecting vllm Using cached vllm-0.1.1.tar.gz (83 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subprocess-exit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: CUDA11.6 not support? (base) C:\Users\a>pip install vllm Collecting vllm Using cached vllm-0.1.1.tar.gz (83 kB) Installing build dependencies ... done Getting requirements to build wheel ... error error: subproce
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 130, in get_requires_for_build_wheel return hook(config_settings) File "C:\Users\hzy\AppData\Local\Temp\pip-build-env-67chdc7b\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in get_requires...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
