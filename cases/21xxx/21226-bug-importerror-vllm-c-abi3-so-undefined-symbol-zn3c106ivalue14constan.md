# vllm-project/vllm#21226: [Bug]: ImportError: vllm/_C.abi3.so: undefined symbol _ZN3c106ivalue14ConstantString6createENSt7

| 字段 | 值 |
| --- | --- |
| Issue | [#21226](https://github.com/vllm-project/vllm/issues/21226) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ImportError: vllm/_C.abi3.so: undefined symbol _ZN3c106ivalue14ConstantString6createENSt7

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The detail of the error: INFO 07-19 13:20:10 [__init__.py:239] Automatically detected platform cuda. Traceback (most recent call last): File "/workspace/vllm/collect_env.py", line 17, in from vllm.envs import environment_variables File "/workspace/vllm/vllm/__init__.py", line 12, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/workspace/vllm/vllm/engine/arg_utils.py", line 15, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/workspace/vllm/vllm/config.py", line 29, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "/workspace/vllm/vllm/model_executor/__init__.py", line 3, in from vllm.model_executor.parameter import (BasevLLMParameter, File "/workspace/vllm/vllm/model_executor/parameter.py", line 9, in from vllm.distributed import get_tensor_model_parallel_rank File "/workspace/vllm/vllm/distributed/__init__.py", line 3, in from .communication_op import * File "/workspace/vllm/vllm/distributed/communication_op.py", line 8, in from .parallel_state import get_tp_group File "/workspace/vllm/vllm/distributed/parallel_state.py", line 122, in from...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: "/workspace/vllm/vllm/engine/arg_utils.py", line 15, in from vllm.config import (CacheConfig, CompilationConfig, ConfigFormat, File "/workspace/vllm/vllm/config.py", line 29, in from vllm.model_executor.layers.quantizat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: ImportError: vllm/_C.abi3.so: undefined symbol _ZN3c106ivalue14ConstantString6createENSt7 bug ### Your current environment ### 🐛 Describe the bug The detail of the error: INFO 07-19 13:20:10 [__init__.py:239] Aut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r: INFO 07-19 13:20:10 [__init__.py:239] Automatically detected platform cuda. Traceback (most recent call last): File "/workspace/vllm/collect_env.py", line 17, in from vllm.envs import environment_variables File "/wor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /vllm/vllm/config.py", line 29, in from vllm.model_executor.layers.quantization import (QUANTIZATION_METHODS, File "/workspace/vllm/vllm/model_executor/__init__.py", line 3, in from vllm.model_executor.parameter import...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel;quantization cuda;quantization crash;import_error Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
