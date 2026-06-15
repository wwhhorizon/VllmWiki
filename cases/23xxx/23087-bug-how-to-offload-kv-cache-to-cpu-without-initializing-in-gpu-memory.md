# vllm-project/vllm#23087: [Bug]: How to Offload KV Cache to CPU without initializing in GPU Memory ?

| 字段 | 值 |
| --- | --- |
| Issue | [#23087](https://github.com/vllm-project/vllm/issues/23087) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: How to Offload KV Cache to CPU without initializing in GPU Memory ?

### Issue 正文摘录

### Your current environment It is possible to offload KV cache to CPU using LM Cache but VLLM throws OOM error if KV Cache size is more than GPU Memory. If we use cpu-offload-gb to load, VLLM loads the model inside CPU memory first and then fills GPU memory with KV Cache. How to ensure that only KV Cache is offloaded to CPU using LM Cache and not the model ? ### 🐛 Describe the bug It is possible to offload KV cache to CPU using LM Cache but VLLM throws OOM error if KV Cache size is more than GPU Memory. If we use cpu-offload-gb to load, VLLM loads the model inside CPU memory first and then fills GPU memory with KV Cache. How to ensure that only KV Cache is offloaded to CPU using LM Cache and not the model ? ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project import os from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig # Set token chunk size to 256 os.environ["LMCACHE_CHUNK_SIZE"] = "256" # Enable CPU memory backend os.environ["LMCACHE_LOCAL_CPU"] = "True" # Set CPU memory limit to 5GB os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0" # Configure KV cache transfer to use LMCache ktc = KVTran...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: [Bug]: How to Offload KV Cache to CPU without initializing in GPU Memory ? bug;stale ### Your current environment It is possible to offload KV cache to CPU using LM Cache but VLLM throws OOM error if KV Cache size is mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s more than GPU Memory. If we use cpu-offload-gb to load, VLLM loads the model inside CPU memory first and then fills GPU memory with KV Cache. How to ensure that only KV Cache is offloaded to CPU using LM Cache and not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: How to Offload KV Cache to CPU without initializing in GPU Memory ? bug;stale ### Your current environment It is possible to offload KV cache to CPU using LM Cache but VLLM throws OOM error if KV Cache size is more than...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: size to 256 os.environ["LMCACHE_CHUNK_SIZE"] = "256" # Enable CPU memory backend os.environ["LMCACHE_LOCAL_CPU"] = "True" # Set CPU memory limit to 5GB os.environ["LMCACHE_MAX_LOCAL_CPU_SIZE"] = "5.0" # Configure KV cac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project import os from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig # Set token chunk size to 256 os.environ["LMCACHE_CHUNK_SI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
