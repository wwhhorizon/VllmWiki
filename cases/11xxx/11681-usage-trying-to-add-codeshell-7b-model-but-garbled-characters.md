# vllm-project/vllm#11681: [Usage]: Trying to add codeshell 7b model, but garbled characters

| 字段 | 值 |
| --- | --- |
| Issue | [#11681](https://github.com/vllm-project/vllm/issues/11681) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Trying to add codeshell 7b model, but garbled characters

### Issue 正文摘录

### Your current environment ``` from typing import List, Optional, Tuple, Union, Iterable, Set import torch from torch import nn from transformers.configuration_utils import PretrainedConfig from transformers.utils import logging from vllm.attention import Attention, AttentionMetadata from vllm.config import CacheConfig from vllm.distributed.parallel_state import ( get_pp_group, get_tensor_model_parallel_world_size) from vllm.model_executor.layers.activation import get_act_fn from vllm.model_executor.layers.linear import (ColumnParallelLinear, QKVParallelLinear, RowParallelLinear) from vllm.model_executor.layers.logits_processor import LogitsProcessor from vllm.model_executor.layers.quantization.base_config import ( QuantizationConfig) from vllm.model_executor.layers.sampler import Sampler,SamplerOutput from vllm.model_executor.layers.vocab_parallel_embedding import ( VocabParallelEmbedding) from vllm.model_executor.model_loader.weight_utils import default_weight_loader from vllm.model_executor.sampling_metadata import SamplingMetadata # from vllm.sequence import IntermediateTensors, SamplerOutput from vllm.sequence import IntermediateTensors from .utils import is_pp_missing_para...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: led characters usage;stale ### Your current environment ``` from typing import List, Optional, Tuple, Union, Iterable, Set import torch from torch import nn from transformers.configuration_utils import PretrainedConfig...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .logits_processor import LogitsProcessor from vllm.model_executor.layers.quantization.base_config import ( QuantizationConfig) from vllm.model_executor.layers.sampler import Sampler,SamplerOutput from vllm.model_executo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ers.utils import logging from vllm.attention import Attention, AttentionMetadata from vllm.config import CacheConfig from vllm.distributed.parallel_state import ( get_pp_group, get_tensor_model_parallel_world_size) from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Trying to add codeshell 7b model, but garbled characters usage;stale ### Your current environment ``` from typing import List, Optional, Tuple, Union, Iterable, Set import torch from torch import nn from transf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
