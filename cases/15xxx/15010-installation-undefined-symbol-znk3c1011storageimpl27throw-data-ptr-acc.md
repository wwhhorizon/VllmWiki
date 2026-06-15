# vllm-project/vllm#15010: [Installation]: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

| 字段 | 值 |
| --- | --- |
| Issue | [#15010](https://github.com/vllm-project/vllm/issues/15010) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

### Issue 正文摘录

### Your current environment python 3.10, H100 ```text python -c 'import vllm' INFO 03-18 16:16:30 __init__.py:183] Automatically detected platform cuda. Traceback (most recent call last): File " ", line 1, in File "/cpfs01/shared/vllm/vllm/__init__.py", line 6, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/cpfs01/shared/vllm/vllm/engine/arg_utils.py", line 18, in from vllm.executor.executor_base import ExecutorBase File "/cpfs01/shared/vllm/vllm/executor/executor_base.py", line 13, in from vllm.platforms import current_platform File "/cpfs01/shared/vllm/vllm/platforms/__init__.py", line 215, in __getattr__ _current_platform = resolve_obj_by_qualname( File "/cpfs01/shared/vllm/vllm/utils.py", line 1894, in resolve_obj_by_qualname module = importlib.import_module(module_name) File "/cpfs01/shared/env/miniconda/envs/vllm_gpu/lib/python3.10/importlib/__init__.py", line 126, in import_module return _bootstrap._gcd_import(name[level:], package, level) File "/cpfs01/shared/vllm/vllm/platforms/cuda.py", line 15, in import vllm._C # noqa ImportError: /cpfs01/shared/vllm/vllm/_C.abi3.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv ``` ##...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv installation;stale ### Your current environment python 3.10, H100 ```text python -c 'import vllm' INFO 03-18 16:16:30 __init__.py:183
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ss_errorEv installation;stale ### Your current environment python 3.10, H100 ```text python -c 'import vllm' INFO 03-18 16:16:30 __init__.py:183] Automatically detected platform cuda. Traceback (most recent call last):...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ymbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv installation;stale ### Your current environment python 3.10, H100 ```text python -c 'import vllm' INFO 03-18 16:16:30 __init__.py:183] Automatically detected p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda crash;import_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
