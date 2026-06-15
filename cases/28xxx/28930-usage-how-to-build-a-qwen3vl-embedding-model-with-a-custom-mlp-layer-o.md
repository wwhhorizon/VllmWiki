# vllm-project/vllm#28930: [Usage]: How to build a qwen3vl embedding model with a custom mlp layer on the top use vllm?

| 字段 | 值 |
| --- | --- |
| Issue | [#28930](https://github.com/vllm-project/vllm/issues/28930) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to build a qwen3vl embedding model with a custom mlp layer on the top use vllm?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Hi friends! I train a sft model built upon qwen3vl 2b model, we put a mlp layer on it to compress the embedding size of the backbone model. Now I want to use vllm 0.11.0 to serve it but I meet some confuse. Here is my custom class code ``` from argparse import Namespace from dataclasses import asdict from typing import Literal, NamedTuple, Optional, TypedDict, Union, get_args import torch import torch.nn as nn from vllm.model_executor.models.qwen3_vl import Qwen3VLForConditionalGeneration from vllm.v1.pool.metadata import PoolingMetadata from vllm.v1.sample.metadata import SamplingMetadata from vllm.config import VllmConfig from vllm.multimodal import MULTIMODAL_REGISTRY class CustomQwenVL3BPool(nn.Module): def __init__( self ): super().__init__() self.out = torch.nn.Sequential( torch.nn.Linear(2048, 512), torch.nn.SiLU(), torch.nn.Linear(512, 128) ) def get_prompt_lens(self, hidden_states: Union[torch.Tensor, list[torch.Tensor]], pooling_metadata: PoolingMetadata, ) -> torch.Tensor: return pooling_metadata.prompt_lens def forward( self, hidden_states: torch.Tensor, pooling_metadata: PoolingMetadata, )...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: How to build a qwen3vl embedding model with a custom mlp layer on the top use vllm? usage ### Your current environment ```text The output of `python collect_env.py` ``` Hi friends! I train a sft model built upo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: How to build a qwen3vl embedding model with a custom mlp layer on the top use vllm? usage ### Your current environment ```text The output of `python collect_env.py` ``` Hi friends! I train a sft model built upo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: odels.qwen3_vl import Qwen3VLForConditionalGeneration from vllm.v1.pool.metadata import PoolingMetadata from vllm.v1.sample.metadata import SamplingMetadata from vllm.config import VllmConfig from vllm.multimodal import...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
