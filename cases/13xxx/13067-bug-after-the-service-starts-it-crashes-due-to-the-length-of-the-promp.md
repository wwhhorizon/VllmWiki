# vllm-project/vllm#13067: [Bug]: After the service starts, it crashes due to the length of the prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#13067](https://github.com/vllm-project/vllm/issues/13067) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After the service starts, it crashes due to the length of the prompt

### Issue 正文摘录

### Your current environment docker pull vllm/vllm-openai:latest. 4 days ago ### 🐛 Describe the bug GPU: 8*A800 ``` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --max-model-len 16384 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.9 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model cognitivecomputations/DeepSeek-R1-AWQ ``` ``` INFO 02-10 18:06:30 engine.py:275] Added request cmpl-30aaf466904d4d148c2e17a584f448e0-0. CRITICAL 02-10 18:06:30 launcher.py:101] MQLLMEngine is already dead, terminating server process INFO: 10.25.164.34:57224 - "POST /v1/completions HTTP/1.1" 500 Internal Server Error ERROR 02-10 18:06:30 engine.py:139] OutOfMemoryError('CUDA out of memory. Tried to allocate 1.27 GiB. GPU 0 has a total capacity of 79.33 GiB of which 109.81 MiB is free. Process 2377657 has 79.19 GiB memory in use. Of the allocated memory 67.68 GiB is allocated by PyTorch, with 76.00 MiB allocated in private pools (e.g., CUDA Gra phs), and 1.47 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expan...

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 000 --max-model-len 16384 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.9 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rashes due to the length of the prompt bug ### Your current environment docker pull vllm/vllm-openai:latest. 4 days ago ### 🐛 Describe the bug GPU: 8*A800 ``` python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ernal Server Error ERROR 02-10 18:06:30 engine.py:139] OutOfMemoryError('CUDA out of memory. Tried to allocate 1.27 GiB. GPU 0 has a total capacity of 79.33 GiB of which 109.81 MiB is free. Process 2377657 has 79.19 GiB...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: -parallel-size 8 --quantization moe_wna16 --gpu-memory-utilization 0.9 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-reasoner --model cognitivecomputations/DeepSeek-R1-AWQ ``` ``` INFO 02-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ations/DeepSeek-R1-AWQ ``` ``` INFO 02-10 18:06:30 engine.py:275] Added request cmpl-30aaf466904d4d148c2e17a584f448e0-0. CRITICAL 02-10 18:06:30 launcher.py:101] MQLLMEngine is already dead, terminating server process I...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 140 updates | Fix Pydantic release workflow (<a href="https://redirect.github.com/pydantic/pydantic/issues/13067">#13067</a>)</li> <li><a href="https://github.com/pydantic/pydantic/commit/1b359e |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | closes_keyword | 0.95 | Bump the minor-update group across 1 directory with 141 updates | Fix Pydantic release workflow (<a href="https://redirect.github.com/pydantic/pydantic/issues/13067">#13067</a>)</li> <li><a href="https://github.com/pydantic/pydantic/commit/1b359e |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
