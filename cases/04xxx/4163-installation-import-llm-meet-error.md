# vllm-project/vllm#4163: [Installation]: import llm meet error

| 字段 | 值 |
| --- | --- |
| Issue | [#4163](https://github.com/vllm-project/vllm/issues/4163) |
| 状态 | closed |
| 标签 | installation;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: import llm meet error

### Issue 正文摘录

### Your current environment ```text Traceback (most recent call last): File "inference.py", line 355, in data_all_with_response = get_pred_func(data=data_all, task_prompt=task_prompt,\ File "inference.py", line 24, in get_pred_vllm from vllm import LLM, SamplingParams File "/usr/local/lib/python3.8/dist-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/usr/local/lib/python3.8/dist-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, File "/usr/local/lib/python3.8/dist-packages/vllm/config.py", line 9, in from vllm.utils import get_cpu_memory, is_hip File "/usr/local/lib/python3.8/dist-packages/vllm/utils.py", line 8, in from vllm._C import cuda_utils ImportError: /usr/local/lib/python3.8/dist-packages/vllm/_C.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE``` ### How you are installing vllm ```sh export VLLM_VERSION=0.2.4 export PYTHON_VERSION=38 pip install https://github.com/vllm-project/vllm/releases/down...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: import llm meet error installation;unstale ### Your current environment ```text Traceback (most recent call last): File "inference.py", line 355, in data_all_with_response = get_pred_func(data=dat
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n3.8/dist-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, ModelConfig, ParallelConfig, File "/usr/local/lib/python3.8/dist-packages/vllm/config.py", line 9, in from vllm.utils import...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: m/config.py", line 9, in from vllm.utils import get_cpu_memory, is_hip File "/usr/local/lib/python3.8/dist-packages/vllm/utils.py", line 8, in from vllm._C import cuda_utils ImportError: /usr/local/lib/python3.8/dist-pa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: llm/_C.cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE``` ###...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .cpython-38-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE``` ### How y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
