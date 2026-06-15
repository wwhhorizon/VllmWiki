# vllm-project/vllm#43755: [Bug]: `_check_enough_kv_cache_memory` does not account for TP/PP sharding,  making KV offloading impossible in multi-GPU distributed deployments

| 字段 | 值 |
| --- | --- |
| Issue | [#43755](https://github.com/vllm-project/vllm/issues/43755) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cache |
| 症状 | mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `_check_enough_kv_cache_memory` does not account for TP/PP sharding,  making KV offloading impossible in multi-GPU distributed deployments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Steps to Reproduce Launch vLLM with KV offloading enabled on a multi-node, multi-GPU setup: ```bash # Node 0 docker run --rm --gpus all --network host \ vllm/vllm-openai:v0.21.0 /model/DeepSeek-V4-Pro \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --nnodes 2 \ --node-rank 0 \ --master-addr "192.168.180.132" \ --max-model-len 1000000 \ --gpu-memory-utilization 0.95 \ --kv_offloading_backend native \ --kv_offloading_size 200 \ --disable-hybrid-kv-cache-manager \ ... # Node 1 docker run --rm --gpus all --network host \ vllm/vllm-openai:v0.21.0 /model/DeepSeek-V4-Pro \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --nnodes 2 \ --node-rank 1 \ --master-addr "192.168.180.132" \ --headless \ --max-model-len 1000000 \ --gpu-memory-utilization 0.95 \ --kv_offloading_backend native \ --kv_offloading_size 200 \ --disable-hybrid-kv-cache-manager \ ... ``` --- ### Actual Behavior The engine fails immediately at startup with: (EngineCore pid=401) ERROR [core.py:1140] ValueError: To serve at least one request with the models's max seq len (1000000), (223.68 GiB KV cache is needed, which is larger than the available KV c...

## 现有链接修复摘要

#43796 Fix KV cache memory check overcounting with pipeline parallelism

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: V offloading enabled on a multi-node, multi-GPU setup: ```bash # Node 0 docker run --rm --gpus all --network host \ vllm/vllm-openai:v0.21.0 /model/DeepSeek-V4-Pro \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: _enough_kv_cache_memory` does not account for TP/PP sharding, making KV offloading impossible in multi-GPU distributed deployments bug ### Your current environment ### 🐛 Describe the bug ### Steps to Reproduce Launch vL...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ug ### Your current environment ### 🐛 Describe the bug ### Steps to Reproduce Launch vLLM with KV offloading enabled on a multi-node, multi-GPU setup: ```bash # Node 0 docker run --rm --gpus all --network host \ vllm/vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GiB ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: gineCore pid=401) ERROR [core.py:1140] ValueError: To serve at least one request with the models's max seq len (1000000), (223.68 GiB KV cache is needed, which is larger than the available KV cache memory (15.57 GiB). B...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43796](https://github.com/vllm-project/vllm/pull/43796) | closes_keyword | 0.95 | Fix KV cache memory check overcounting with pipeline parallelism | Fixes #43755 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
