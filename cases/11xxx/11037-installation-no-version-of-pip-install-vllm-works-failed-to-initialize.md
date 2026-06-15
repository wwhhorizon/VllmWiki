# vllm-project/vllm#11037: [Installation]: no version of pip install vllm works - Failed to initialize NumPy: No Module named 'numpy'

| 字段 | 值 |
| --- | --- |
| Issue | [#11037](https://github.com/vllm-project/vllm/issues/11037) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: no version of pip install vllm works - Failed to initialize NumPy: No Module named 'numpy'

### Issue 正文摘录

### Your current environment ```text Traceback (most recent call last): File "/mnt/MSAI/home/cephdon/sources/vllm/collect_env.py", line 15, in from vllm.envs import environment_variables File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/config.py", line 21, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/model_executor/__init__.py", line 1, in from vllm.model_executor.parameter import (BasevLLMParameter, File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/model_executor/parameter.py", line 7, in from vllm.distributed import get_tensor_model_parallel_rank File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/distributed/__init__.py", line 1, in from .communication_op import * File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/distributed/communication_op.py", line 6, in from .parallel_state import get_tp_group File "/mnt/MSAI/home/cephdon/sourc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: no version of pip install vllm works - Failed to initialize NumPy: No Module named 'numpy' installation;stale ### Your current environment ```text Traceback (most recent call last): File "/mnt/MSAI/home
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hdon/sources/vllm/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/config.py", line 21, in from vllm.model_exec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: phdon/sources/vllm/vllm/platforms/__init__.py", line 100, in from .cuda import CudaPlatform File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/platforms/cuda.py", line 14, in import vllm._C # noqa ModuleNotFoundError: No mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /vllm/vllm/config.py", line 21, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "/mnt/MSAI/home/cephdon/sources/vllm/vllm/model_executor/__init__.py", line 1, in from vllm.model_execut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: works - Failed to initialize NumPy: No Module named 'numpy' installation;stale ### Your current environment ```text Traceback (most recent call last): File "/mnt/MSAI/home/cephdon/sources/vllm/collect_env.py", line 15,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
