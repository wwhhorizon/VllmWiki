# vllm-project/vllm#16826: [Bug]: The Transformers implementation of My Model is not compatible with vLLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#16826](https://github.com/vllm-project/vllm/issues/16826) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The Transformers implementation of My Model is not compatible with vLLM.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi there, I saw the post from X (https://x.com/vllm_project/status/1912958639633277218) that the vllm library currently supports self-implemented transformers models. This is an amazing progress and I think it is pretty important. However, when I try to use this function with the latest vllm library and refer to the https://github.com/huggingface/transformers/pull/36934 to update my model accordingly, it seems that my model is still not compatible with vllm. My model is provided as follows: ```python import os import re import torch import torch.nn as nn from torch.nn import CrossEntropyLoss from typing import Optional, List, Tuple, Union from transformers import Qwen2ForCausalLM, PretrainedConfig from transformers.modeling_outputs import CausalLMOutputWithPast HIDDEN_SIZE = 1536 MULT_K = 4 class Qwen2ForCausalPersonalLM(Qwen2ForCausalLM): _supports_attention_backend = True def __init__(self, config, **kwargs): super().__init__(config, **kwargs) device = torch.device("cuda" if torch.cuda.is_available() else "cpu") self.align_mlp_his = nn.Sequential(nn.Linear(HIDDEN_SIZE, config.hidden_size * MULT_K), nn.GELU(), nn.Linear(config.h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ransformers models. This is an amazing progress and I think it is pretty important. However, when I try to use this function with the latest vllm library and refer to the https://github.com/huggingface/transformers/pull...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: The Transformers implementation of My Model is not compatible with vLLM. bug ### Your current environment ### 🐛 Describe the bug Hi there, I saw the post from X (https://x.com/vllm_project/status/1912958639633277...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: super().__init__(config, **kwargs) device = torch.device("cuda" if torch.cuda.is_available() else "cpu") self.align_mlp_his = nn.Sequential(nn.Linear(HIDDEN_SIZE, config.hidden_size * MULT_K), nn.GELU(),
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: args) device = torch.device("cuda" if torch.cuda.is_available() else "cpu") self.align_mlp_his = nn.Sequential(nn.Linear(HIDDEN_SIZE, config.hidden_size * MULT_K), nn.GELU(), nn.Linear(config.hid
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lass Qwen2ForCausalPersonalLM(Qwen2ForCausalLM): _supports_attention_backend = True def __init__(self, config, **kwargs): super().__init__(config, **kwargs) device = torch.device("cuda" if torch.cuda.is_available() else...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
