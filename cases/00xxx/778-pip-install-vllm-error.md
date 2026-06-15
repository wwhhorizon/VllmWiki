# vllm-project/vllm#778: pip install vllm error!!!

| 字段 | 值 |
| --- | --- |
| Issue | [#778](https://github.com/vllm-project/vllm/issues/778) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | activation;attention;cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install vllm error!!!

### Issue 正文摘录

Building wheels for collected packages: vllm Building wheel for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building wheel for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [138 lines of output] running bdist_wheel running build running build_py creating build creating build\lib.win-amd64-cpython-38 creating build\lib.win-amd64-cpython-38\vllm copying vllm\block.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\config.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\logger.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\outputs.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\sampling_params.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\sequence.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\utils.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\__init__.py -> build\lib.win-amd64-cpython-38\vllm creating build\lib.win-amd64-cpython-38\vllm\core copying vllm\core\block_manager.py -> build\lib.win-amd64-cpython-38\vllm\core copying vllm\core\policy.py -> build\lib.win-amd64-cpython-38\vllm\core copying vllm\core\scheduler.py -> build\lib.win-amd64-cpython-38\vllm\core copying vllm\core\__in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: pip install vllm error!!! Building wheels for collected packages: vllm Building wheel for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building wheel for vllm (pyproject.toml) did not run succ
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: 38 creating build\lib.win-amd64-cpython-38\vllm copying vllm\block.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\config.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\logger.py -> build\lib.win-amd64-cp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm\block.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\config.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\logger.py -> build\lib.win-amd64-cpython-38\vllm copying vllm\outputs.py -> build\lib.win-a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: thon-38\vllm\transformers_utils\configs running build_ext No CUDA runtime is found, using CUDA_HOME='D:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.8' C:\Users\XXX\AppData\Local\Temp\pip-build-env-wwc5e373\overl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rocess\_in_process.py", line 251, in build_wheel return _build_backend().build_wheel(wheel_directory, config_settings, File "C:\Users\XXX\AppData\Local\Temp\pip-build-env-wwc5e373\overlay\Lib\site-packages\setuptools\bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
