# vllm-project/vllm#6503: [New Model]: Support for Telechat

| 字段 | 值 |
| --- | --- |
| Issue | [#6503](https://github.com/vllm-project/vllm/issues/6503) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support for Telechat

### Issue 正文摘录

### The model to consider. https://huggingface.co/Tele-AI/TeleChat-12B ### The closest model vllm already supports. qwen2 ### What's your difficulty of supporting the model you want? I have successfully loaded the model in vllm, but there is a problem with the model's inference and I have no idea how to debug it. Could someone help review it? ``` from typing import Iterable, List, Optional, Tuple import torch from torch import nn from transformers import PretrainedConfig from vllm.attention import Attention, AttentionMetadata from vllm.config import CacheConfig, LoRAConfig from vllm.distributed import get_tensor_model_parallel_world_size from vllm.model_executor.layers.activation import SiluAndMul from vllm.model_executor.layers.layernorm import RMSNorm from vllm.model_executor.layers.linear import (MergedColumnParallelLinear, QKVParallelLinear, RowParallelLinear) from vllm.model_executor.layers.logits_processor import LogitsProcessor from vllm.model_executor.layers.quantization.base_config import ( QuantizationConfig) from vllm.model_executor.layers.rotary_embedding import get_rope from vllm.model_executor.layers.sampler import Sampler from vllm.model_executor.layers.vocab_parall...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: import PretrainedConfig from vllm.attention import Attention, AttentionMetadata from vllm.config import CacheConfig, LoRAConfig from vllm.distributed import get_tensor_model_parallel_world_size from vllm.model_executor....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Support for Telechat new-model;stale ### The model to consider. https://huggingface.co/Tele-AI/TeleChat-12B ### The closest model vllm already supports. qwen2 ### What's your difficulty of supporting the mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .logits_processor import LogitsProcessor from vllm.model_executor.layers.quantization.base_config import ( QuantizationConfig) from vllm.model_executor.layers.rotary_embedding import get_rope from vllm.model_executor.la...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e no idea how to debug it. Could someone help review it? ``` from typing import Iterable, List, Optional, Tuple import torch from torch import nn from transformers import PretrainedConfig from vllm.attention import Atte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Support for Telechat new-model;stale ### The model to consider. https://huggingface.co/Tele-AI/TeleChat-12B ### The closest model vllm already supports. qwen2 ### What's your difficulty of supporting the mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
