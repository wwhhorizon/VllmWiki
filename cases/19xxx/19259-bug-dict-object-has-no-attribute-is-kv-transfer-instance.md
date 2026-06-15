# vllm-project/vllm#19259: [Bug]: 'dict' object has no attribute 'is_kv_transfer_instance'

| 字段 | 值 |
| --- | --- |
| Issue | [#19259](https://github.com/vllm-project/vllm/issues/19259) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;sampling |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'dict' object has no attribute 'is_kv_transfer_instance'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - run vllm container ``` docker run -d -it --rm --privileged --entrypoint /bin/bash --network host --name poolv1-mbl-test-2 --shm-size 512g --gpus all -v /:/disc vllm/vllm-openai:v0.9.0.1 docker exec -it poolv1-mbl-test-2 bash pip install lmcache ``` - start vllm by lmcache example. The following python script is copied from `examples/others/lmcache/cpu_offload_lmcache.py` and did some minor changes to run model locally. ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project """ This file demonstrates the example usage of cpu offloading with LMCache in vLLM v1 or v0. Usage: Specify vLLM version -v v0 : Use LMCacheConnector model = mistralai/Mistral-7B-Instruct-v0.2 (Includes enable_chunked_prefill = True) -v v1 : Use LMCacheConnectorV1 (default) model = meta-llama/Meta-Llama-3.1-8B-Instruct (Without enable_chunked_prefill) Note that `lmcache` is needed to run this example. Requirements: Linux, Python: 3.10 or higher, CUDA: 12.1 Learn more about LMCache environment setup, please refer to: https://docs.lmcache.ai/getting_started/installation.html """ import argparse impo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: current environment ### 🐛 Describe the bug - run vllm container ``` docker run -d -it --rm --privileged --entrypoint /bin/bash --network host --name poolv1-mbl-test-2 --shm-size 512g --gpus all -v /:/disc vllm/vllm-open...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: The following python script is copied from `examples/others/lmcache/cpu_offload_lmcache.py` and did some minor changes to run model locally. ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copy...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: others/lmcache/cpu_offload_lmcache.py` and did some minor changes to run model locally. ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project """ This file...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: needed to run this example. Requirements: Linux, Python: 3.10 or higher, CUDA: 12.1 Learn more about LMCache environment setup, please refer to: https://docs.lmcache.ai/getting_started/installation.html """ import argpa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mistralai/Mistral-7B-Instruct-v0.2 (Includes enable_chunked_prefill = True) -v v1 : Use LMCacheConnectorV1 (default) model = meta-llama/Meta-Llama-3.1-8B-Instruct (Without enable_chunked_prefill) Note that `lmcache` is...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
