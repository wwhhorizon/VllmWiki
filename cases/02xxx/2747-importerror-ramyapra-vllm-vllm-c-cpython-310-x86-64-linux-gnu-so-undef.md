# vllm-project/vllm#2747: ImportError: /ramyapra/vllm/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol:

| 字段 | 值 |
| --- | --- |
| Issue | [#2747](https://github.com/vllm-project/vllm/issues/2747) |
| 状态 | closed |
| 标签 |  |
| 评论 | 64; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ImportError: /ramyapra/vllm/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol:

### Issue 正文摘录

I'm trying to run vllm and lm-eval-harness. I'm using vllm 0.2.5. After I'm done installing both, if I try importing vllm I get the following error: ` File "/ramyapra/lm-evaluation-harness/lm_eval/models/__init__.py", line 7, in from . import vllm_causallms File "/ramyapra/lm-evaluation-harness/lm_eval/models/vllm_causallms.py", line 16, in from vllm import LLM, SamplingParams File "/ramyapra/vllm/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/ramyapra/vllm/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, File "/ramyapra/vllm/vllm/config.py", line 9, in from vllm.utils import get_cpu_memory, is_hip File "/ramyapra/vllm/vllm/utils.py", line 8, in from vllm._C import cuda_utils ImportError: /ramyapra/vllm/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops19empty_memory_format4callEN3c108ArrayRefINS2_6SymIntEEESt8optionalINS2_10ScalarTypeEES6_INS2_6LayoutEES6_INS2_6DeviceEES6_IbES6_INS2_12MemoryFormatEE ` I'm using the NGC docker container 23:10-py3.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ImportError: /ramyapra/vllm/vllm/_C.cpython-310-x86_64-linux-gnu.so: undefined symbol: I'm trying to run vllm and lm-eval-harness. I'm using vllm 0.2.5. After I'm done installing both, if I try importing vllm I get the f
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: et the following error: ` File "/ramyapra/lm-evaluation-harness/lm_eval/models/__init__.py", line 7, in from . import vllm_causallms File "/ramyapra/lm-evaluation-harness/lm_eval/models/vllm_causallms.py", line 16, in f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m/config.py", line 9, in from vllm.utils import get_cpu_memory, is_hip File "/ramyapra/vllm/vllm/utils.py", line 8, in from vllm._C import cuda_utils ImportError: /ramyapra/vllm/vllm/_C.cpython-310-x86_64-linux-gnu.so:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: callEN3c108ArrayRefINS2_6SymIntEEESt8optionalINS2_10ScalarTypeEES6_INS2_6LayoutEES6_INS2_6DeviceEES6_IbES6_INS2_12MemoryFormatEE ` I'm using the NGC docker container 23:10-py3.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 310-x86_64-linux-gnu.so: undefined symbol: I'm trying to run vllm and lm-eval-harness. I'm using vllm 0.2.5. After I'm done installing both, if I try importing vllm I get the following error: ` File "/ramyapra/lm-evalua...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
