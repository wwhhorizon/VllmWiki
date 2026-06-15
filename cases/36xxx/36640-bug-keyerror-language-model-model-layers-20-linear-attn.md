# vllm-project/vllm#36640: [Bug]: KeyError: 'language_model.model.layers.20.linear_attn'

| 字段 | 值 |
| --- | --- |
| Issue | [#36640](https://github.com/vllm-project/vllm/issues/36640) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'language_model.model.layers.20.linear_attn'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving `Qwen-3.5-397B-A17B` with `--max-model-len 65536`, it works well. But when serving with `--max-model-len 262144`, I get a key error `KeyError: 'language_model.model.layers.20.linear_attn'`. Interestingly, `--max-model-len 65536` no longer functions after running the 262144 len version. I have to reboot my entire cluster to get it to work again. I am running on 3x DGX Spark with GB10 (total VRAM 360GB). vLLM is run via a modified `spark-vllm-docker` image [here is the image I am using](https://github.com/itfwonjulee/fullmesh-spark-vllm-docker). I am running with TP=1 and PP=3. I can believe that all the dumb mods I made to make NCCL / that docker image / vLLM's Distributed Executor Backend (see [Issue #35848](https://github.com/vllm-project/vllm/issues/35848)) is causing something to mess up, but I find it strange that it works at first but then breaks. I believe its not a memory issue, since vLLM notes that the max concurrency for 262,144 tokens p/r is around 19. The error message is pasted below: ``` (EngineCore_DP0 pid=1346) INFO 03-10 10:41:15 [kv_cache_utils.py:1319] Maximum concurrency for 262,144 tokens per req...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: `--max-model-len 65536` no longer functions after running the 262144 len version. I have to reboot my entire cluster to get it to work again. I am running on 3x DGX Spark with GB10 (total VRAM 360GB). vLLM is run via a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: KeyError: 'language_model.model.layers.20.linear_attn' bug ### Your current environment ### 🐛 Describe the bug When serving `Qwen-3.5-397B-A17B` with `--max-model-len 65536`, it works well. But when serving with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ds I made to make NCCL / that docker image / vLLM's Distributed Executor Backend (see [Issue #35848](https://github.com/vllm-project/vllm/issues/35848)) is causing something to mess up, but I find it strange that it wor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: EngineCore_DP0 pid=1346) ERROR 03-10 10:41:15 [core.py:1111] num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( (EngineCore_DP0 pid=1346) ERROR 03-10 10:41:15 [core.py:1111] ^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
