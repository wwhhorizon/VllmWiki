# vllm-project/vllm#11451: [Usage]: Trying to add codeshell 7b model, but got an error

| 字段 | 值 |
| --- | --- |
| Issue | [#11451](https://github.com/vllm-project/vllm/issues/11451) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Trying to add codeshell 7b model, but got an error

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ####codeshell.py ``` from typing import List, Optional, Tuple, Union, Iterable, Set import torch from torch import nn from transformers.configuration_utils import PretrainedConfig from transformers.utils import logging from vllm.attention import Attention, AttentionMetadata from vllm.config import CacheConfig from vllm.distributed.parallel_state import ( get_pp_group, get_tensor_model_parallel_world_size) from vllm.model_executor.layers.activation import get_act_fn from vllm.model_executor.layers.linear import (ColumnParallelLinear, QKVParallelLinear, RowParallelLinear) from vllm.model_executor.layers.logits_processor import LogitsProcessor from vllm.model_executor.layers.quantization.base_config import ( QuantizationConfig) from vllm.model_executor.layers.sampler import Sampler from vllm.model_executor.layers.vocab_parallel_embedding import ( VocabParallelEmbedding) from vllm.model_executor.model_loader.weight_utils import default_weight_loader from vllm.model_executor.sampling_metadata import SamplingMetadata from vllm.sequence import IntermediateTensors, SamplerOutput from .utils import is_p...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: .logits_processor import LogitsProcessor from vllm.model_executor.layers.quantization.base_config import ( QuantizationConfig) from vllm.model_executor.layers.sampler import Sampler from vllm.model_executor.layers.vocab...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ers.utils import logging from vllm.attention import Attention, AttentionMetadata from vllm.config import CacheConfig from vllm.distributed.parallel_state import ( get_pp_group, get_tensor_model_parallel_world_size) from...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _No response_ ### 🐛 Describe the bug ####codeshell.py ``` from typing import List, Optional, Tuple, Union, Iterable, Set import torch from torch import nn from transformers.configuration_utils import PretrainedConfig fr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Trying to add codeshell 7b model, but got an error usage ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ####codeshell.py ``` from typing import List, Optional, Tuple, Un...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ne.py:57] File "/usr/local/lib/python3.10/site-packages/vllm/attention/backends/flash_attn.py", line 494, in forward ERROR 12-24 05:55:33 async_llm_engine.py:57] ops.reshape_and_cache_flash( ERROR 12-24 05:55:33 async_l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
