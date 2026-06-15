# vllm-project/vllm#12321: [Usage]: The problems about the communication synchronization in disaggregated prefilling

| 字段 | 值 |
| --- | --- |
| Issue | [#12321](https://github.com/vllm-project/vllm/issues/12321) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: The problems about the communication synchronization in disaggregated prefilling

### Issue 正文摘录

### Your current environment Dear VLLM, I want to do some experiments in disaggregated prefilling. And I have the following code documents: ``` from vllm import LLM, LLMEngine from typing import (Any, ClassVar, Dict, List, Optional, Sequence, Tuple, Type, Union, cast, overload) import os os.environ["VLLM_TORCH_PROFILER_DIR"] = "./vllm_profile" os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"] = '1' import torch import time import argparse from vllm import SamplingParams parser = argparse.ArgumentParser() parser.add_argument('--device', type=int, default=0) parser.add_argument('--rank', type=int, default=0) parser.add_argument('--role', type=str, default='kv_producer') args = parser.parse_args() os.environ["CUDA_VISIBLE_DEVICES"] = f'{args.device}' prompts = """Help me summarize the introduction with one brief sentence. Harvard University, an iconic institution of higher education located in Cambridge, Massachusetts, stands as a beacon of academic excellence and innovation. Established in 1636........ (abbreviation for too long sentence) """ kv_transfer_config = '{"kv_connector":"PyNcclConnector", "kv_role":' + f'"{args.role}"' + ', "kv_rank":' + f'{args.rank}' + ', "kv_parallel_size":2}...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 38, 2.7500, 1.6797, ..., -1.9453, 2.7656, 1.8594], device='cuda:0', dtype=torch.bfloat16) ``` **hidden_states in Decode phase** ``` tensor([ 0.3066, 2.5625, 0.5039, ..., -2.3281, 0.3125, -0.0576], device='cuda:0', dtype...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _TORCH_PROFILER_DIR"] = "./vllm_profile" os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"] = '1' import torch import time import argparse from vllm import SamplingParams parser = argparse.ArgumentParser() parser.add_argument(...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ated prefilling. And I have the following code documents: ``` from vllm import LLM, LLMEngine from typing import (Any, ClassVar, Dict, List, Optional, Sequence, Tuple, Type, Union, cast, overload) import os os.environ["...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: type=str, default='kv_producer') args = parser.parse_args() os.environ["CUDA_VISIBLE_DEVICES"] = f'{args.device}' prompts = """Help me summarize the introduction with one brief sentence. Harvard University, an iconic in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: The problems about the communication synchronization in disaggregated prefilling usage ### Your current environment Dear VLLM, I want to do some experiments in disaggregated prefilling. And I have the following code...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
