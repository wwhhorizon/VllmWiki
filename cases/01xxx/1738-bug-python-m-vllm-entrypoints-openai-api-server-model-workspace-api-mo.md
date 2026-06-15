# vllm-project/vllm#1738: BUG python -m vllm.entrypoints.openai.api_server --model /workspace/api/models/Qwen/Qwen-7B-Chat/ --trust-remote-code  vllm==0.2.2 torch2.1.0+cuda118

| 字段 | 值 |
| --- | --- |
| Issue | [#1738](https://github.com/vllm-project/vllm/issues/1738) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BUG python -m vllm.entrypoints.openai.api_server --model /workspace/api/models/Qwen/Qwen-7B-Chat/ --trust-remote-code  vllm==0.2.2 torch2.1.0+cuda118

### Issue 正文摘录

Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 185, in _run_module_as_main mod_name, mod_spec, code = _get_module_details(mod_name, _Error) File "/usr/lib/python3.8/runpy.py", line 111, in _get_module_details __import__(pkg_name) File "/usr/local/lib/python3.8/dist-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/usr/local/lib/python3.8/dist-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, File "/usr/local/lib/python3.8/dist-packages/vllm/config.py", line 9, in from vllm.utils import get_cpu_memory File "/usr/local/lib/python3.8/dist-packages/vllm/utils.py", line 8, in from vllm import cuda_utils ImportError: libcudart.so.12: cannot open shared object file: No such file or directory Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 646, in engine = AsyncLLMEngine.fro...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: BUG python -m vllm.entrypoints.openai.api_server --model /workspace/api/models/Qwen/Qwen-7B-Chat/ --trust-remote-code vllm==0.2.2 torch2.1.0+cuda118 Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py",...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: le "/usr/lib/python3.8/runpy.py", line 111, in _get_module_details __import__(pkg_name) File "/usr/local/lib/python3.8/dist-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, Engin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pi/models/Qwen/Qwen-7B-Chat/ --trust-remote-code vllm==0.2.2 torch2.1.0+cuda118 Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 185, in _run_module_as_main mod_name, mod_spec, code = _get_mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r.py", line 10, in from vllm.model_executor import get_model, InputMetadata, set_random_seed File "/usr/local/lib/python3.8/dist-packages/vllm/model_executor/__init__.py", line 2, in from vllm.model_executor.model_loade...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
