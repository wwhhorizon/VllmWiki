# vllm-project/vllm#3228: When running pytest tests/, undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

| 字段 | 值 |
| --- | --- |
| Issue | [#3228](https://github.com/vllm-project/vllm/issues/3228) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> When running pytest tests/, undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv

### Issue 正文摘录

Running command:`~# pytest tests/` Error Msg: ``` ======================= test session starts ============================== platform linux -- Python 3.9.12, pytest-7.1.1, pluggy-1.0.0 rootdir: /root/vllm plugins: anyio-3.5.0, forked-1.6.0, asyncio-0.23.5 asyncio: mode=strict collected 0 items / 1 error ============================= ERRORS============================== ___________________ ERROR collecting test session _______________________ ../anaconda3/lib/python3.9/importlib/__init__.py:127: in import_module return _bootstrap._gcd_import(name[level:], package, level) :1030: in _gcd_import ??? :1007: in _find_and_load ??? :986: in _find_and_load_unlocked ??? :680: in _load_unlocked ??? ../anaconda3/lib/python3.9/site-packages/_pytest/assertion/rewrite.py:168: in exec_module exec(co, module.__dict__) tests/lora/conftest.py:15: in from vllm.model_executor.layers.sampler import Sampler vllm/model_executor/__init__.py:2: in from vllm.model_executor.model_loader import get_model vllm/model_executor/model_loader.py:10: in from vllm.model_executor.weight_utils import (get_quant_config, vllm/model_executor/weight_utils.py:18: in from vllm.model_executor.layers.quantization import (get_q...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: When running pytest tests/, undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv Running command:`~# pytest tests/` Error Msg: ``` ======================= test session starts =============================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: exec(co, module.__dict__) tests/lora/conftest.py:15: in from vllm.model_executor.layers.sampler import Sampler vllm/model_executor/__init__.py:2: in from vllm.model_executor.model_loader import get_model vllm/model_exec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: loader.py:10: in from vllm.model_executor.weight_utils import (get_quant_config, vllm/model_executor/weight_utils.py:18: in from vllm.model_executor.layers.quantization import (get_quantization_config, vllm/model_execut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: When running pytest tests/, undefined symbol: _ZNSt15__exception_ptr13exception_ptr9_M_addrefEv Running command:`~# pytest tests/` Error Msg: ``` ======================= test session starts =============================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
