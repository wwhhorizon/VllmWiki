# vllm-project/vllm#13788: [Bug]: ValueError: Unsupported FA version: None on V100 and V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#13788](https://github.com/vllm-project/vllm/issues/13788) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Unsupported FA version: None on V100 and V1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Got crash after try to inferecne: ``` Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`. INFO 02-24 22:11:39 async_llm.py:164] Added request chatcmpl-75e19da5f42d4a30aba05a7e9dbb29e6. INFO 02-24 22:11:39 loggers.py:78] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% ERROR 02-24 22:11:40 core.py:294] EngineCore hit an exception: Traceback (most recent call last): ERROR 02-24 22:11:40 core.py:294] File "/root/vllm-0.7.3/vllm-0.7.3/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 287, in run_engine_core ERROR 02-24 22:11:40 core.py:294] engine_core.run_busy_loop() ERROR 02-24 22:11:40 core.py:294] File "/root/vllm-0.7.3/vllm-0.7.3/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 330, in run_busy_loop ERROR 02-24 22:11:40 core.py:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: Bug]: ValueError: Unsupported FA version: None on V100 and V1 engine bug;stale ### Your current environment ### 🐛 Describe the bug Got crash after try to inferecne: ``` Using a slow image processor as `use_fast` is unse...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: ValueError: Unsupported FA version: None on V100 and V1 engine bug;stale ### Your current environment ### 🐛 Describe the bug Got crash after try to inferecne: ``` Using a slow image processor as `use_fast` is uns...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rocessor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.48, even if the model was saved with a slow processor. This will result in minor differe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0% ERROR 02-24 22:11:40 core.py:294] EngineCore hit an exception: Traceback (most recent call last)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
