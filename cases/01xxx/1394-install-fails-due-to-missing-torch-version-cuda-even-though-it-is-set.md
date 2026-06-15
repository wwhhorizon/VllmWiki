# vllm-project/vllm#1394: Install fails due to missing torch.version.cuda, even though it is set

| 字段 | 值 |
| --- | --- |
| Issue | [#1394](https://github.com/vllm-project/vllm/issues/1394) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> Install fails due to missing torch.version.cuda, even though it is set

### Issue 正文摘录

During vllm install I get the following error: ``` File "C:\Users\tomas\AppData\Local\Temp\pip-build-env-dl9xeg5d\overlay\Lib\site-packages\torch\utils\cpp_extension.py", line 383, in _check_cuda_version torch_cuda_version = packaging.version.parse(torch.version.cuda) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\tomas\AppData\Local\Temp\pip-build-env-dl9xeg5d\overlay\Lib\site-packages\pkg_resources\_vendor\packaging\version.py", line 52, in parse return Version(version) ^^^^^^^^^^^^^^^^ File "C:\Users\tomas\AppData\Local\Temp\pip-build-env-dl9xeg5d\overlay\Lib\site-packages\pkg_resources\_vendor\packaging\version.py", line 196, in __init__ match = self._regex.search(version) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ TypeError: expected string or bytes-like object, got 'NoneType' [end of output] note: This error originates from a subprocess, and is likely not a problem with pip. ERROR: Failed building wheel for vllm Failed to build vllm ERROR: Could not build wheels for vllm, which is required to install pyproject.toml-based projects ``` However, I already re-installed and configured torch, and it looks as expected in the same terminal: ``` >>> import torch >>> >>> print(torch.vers...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Install fails due to missing torch.version.cuda, even though it is set During vllm install I get the following error: ``` File "C:\Users\tomas\AppData\Local\Temp\pip-build-env-dl9xeg5d\overlay\Lib\site-packages\t
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Install fails due to missing torch.version.cuda, even though it is set During vllm install I get the following error: ``` File "C:\Users\tomas\AppData\Local\Temp\pip-build-env-dl9xeg5d\overlay\Lib\site-packages\torch\ut...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l pyproject.toml-based projects ``` However, I already re-installed and configured torch, and it looks as expected in the same terminal: ``` >>> import torch >>> >>> print(torch.version.cuda) 11.8 >>> >>> print(torch.cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
