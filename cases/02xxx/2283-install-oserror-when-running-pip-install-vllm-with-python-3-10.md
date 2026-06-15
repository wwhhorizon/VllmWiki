# vllm-project/vllm#2283: Install OSError when running pip install vllm with python 3.10

| 字段 | 值 |
| --- | --- |
| Issue | [#2283](https://github.com/vllm-project/vllm/issues/2283) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Install OSError when running pip install vllm with python 3.10

### Issue 正文摘录

C:\Users\botao\AppData\Local\Temp\pip-build-env-d2ffimq3\overlay\Lib\site-packages\torch\nn\modules\transformer.py:20: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at ..\torch\csrc\utils\tensor_numpy.cpp:84.) device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'), Traceback (most recent call last): File "C:\Users\botao\anaconda3\envs\vllm\lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 353, in main() File "C:\Users\botao\anaconda3\envs\vllm\lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 335, in main json_out['return_val'] = hook(**hook_input['kwargs']) File "C:\Users\botao\anaconda3\envs\vllm\lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "C:\Users\botao\AppData\Local\Temp\pip-build-env-d2ffimq3\overlay\Lib\site-packages\setuptools\build_meta.py", line 325, in get_requires_for_build_wheel return self._get_build_requires(config_settings, requirements=['wheel']) File "C:\Users\botao\AppData\Local\Temp\pip-build-env-d2ffimq3\overlay\Lib\site...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Install OSError when running pip install vllm with python 3.10 C:\Users\botao\AppData\Local\Temp\pip-build-env-d2ffimq3\overlay\Lib\site-packages\torch\nn\modules\transformer.py:20: UserWarning: Failed to initialize NumP
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 3\overlay\Lib\site-packages\torch\utils\cpp_extension.py", line 1076, in CUDAExtension library_dirs += library_paths(cuda=True) File "C:\Users\botao\AppData\Local\Temp\pip-build-env-d2ffimq3\overlay\Lib\site-packages\to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ess.py", line 118, in get_requires_for_build_wheel return hook(config_settings) File "C:\Users\botao\AppData\Local\Temp\pip-build-env-d2ffimq3\overlay\Lib\site-packages\setuptools\build_meta.py", line 325, in get_requir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
