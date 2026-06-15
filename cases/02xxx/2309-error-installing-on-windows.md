# vllm-project/vllm#2309: Error installing on windows

| 字段 | 值 |
| --- | --- |
| Issue | [#2309](https://github.com/vllm-project/vllm/issues/2309) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
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

> Error installing on windows

### Issue 正文摘录

NameError: name 'nvcc_cuda_version' is not defined. Did you mean: 'cuda_version'? This was a simple fix I defined the cuda version in line 268 of setup .py and installed with 'pip install .' so change line 268 from: cuda_version = str(nvcc_cuda_version) to: cuda_version = str(12.1) If this problem is common amongst windows users you could add a precheck for os version, and if windows, allow user to set cuda version via prompt. Although i still have a error building the wheels further down the line: copying vllm\transformers_utils\tokenizers\__init__.py -> build\lib.win-amd64-cpython-311\vllm\transformers_utils\tokenizers copying vllm\py.typed -> build\lib.win-amd64-cpython-311\vllm running build_ext C:\Users\PC\AppData\Local\Temp\pip-build-env-8j8g0uyh\overlay\Lib\site-packages\torch\utils\cpp_extension.py:383: UserWarning: Error checking compiler version for cl: [WinError 2] The system cannot find the file specified warnings.warn(f'Error checking compiler version for {compiler}: {error}') Traceback (most recent call last): File "C:\Python311\Lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 353, in main() File "C:\Python311\Lib\site-packages\pip\_ven...

## 现有链接修复摘要

#14891 [Kernel] vLLM Windows CUDA support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Error installing on windows NameError: name 'nvcc_cuda_version' is not defined. Did you mean: 'cuda_version'? This was a simple fix I defined the cuda version in line 268 of setup .py and installed with 'pip install .'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Error installing on windows NameError: name 'nvcc_cuda_version' is not defined. Did you mean: 'cuda_version'? This was a simple fix I defined the cuda version in line 268 of setup .py and installed with 'pip install .'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rocess\_in_process.py", line 251, in build_wheel return _build_backend().build_wheel(wheel_directory, config_settings, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\PC\AppData\Local\Temp\...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: m with pip. ERROR: Failed building wheel for vllm Building wheel for quantile-python (setup.py) ... done Created wheel for quantile-python: filename=quantile_python-1.1-py3-none-any.whl size=3452 sha256=14bb55c2f1ae4594...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ild_wheel return _build_backend().build_wheel(wheel_directory, config_settings, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "C:\Users\PC\AppData\Local\Temp\pip-build-env-8j8g0uyh\overlay\Lib\site...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#14891](https://github.com/vllm-project/vllm/pull/14891) | closes_keyword | 0.95 | [Kernel] vLLM Windows CUDA support | FIX #2309 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
