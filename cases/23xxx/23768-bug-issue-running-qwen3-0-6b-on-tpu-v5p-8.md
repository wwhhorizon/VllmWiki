# vllm-project/vllm#23768: [Bug]: Issue running Qwen3-0.6B on TPU-v5p-8

| 字段 | 值 |
| --- | --- |
| Issue | [#23768](https://github.com/vllm-project/vllm/issues/23768) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue running Qwen3-0.6B on TPU-v5p-8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tried running `vllm serve Qwen/Qwen3-0.6B` on a v5p-8 but it didn't work for me. After loading the model weights and while doing the first AoT compilation, I get this core dump error. Ran on `vllm/vllm-tpu:3c545c0c3b98ee642373a308197d750d0e449403` ``` Debug this vLLM issue on TPU when I run vllm serve Qwen/Qwen3-0.6B: Error: INFO 08-27 17:25:21 [weight_utils.py:308] Time spent downloading weights for Qwen/Qwen3-0.6B: 2.675431 seconds INFO 08-27 17:25:21 [weight_utils.py:345] No model.safetensors.index.json found in remote. Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:02<00:00, 2.21s/it] Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:02<00:00, 2.21s/it] INFO 08-27 17:25:23 [default_loader.py:272] Loading weights took 2.24 seconds INFO 08-27 17:25:46 [tpu_model_runner.py:1592] Clear dynamo cache and cached dynamo bytecode. INFO 08-27 17:25:46 [kv_cache_utils.py:716] GPU KV cache size: 795,392 tokens INFO 08-27 17:25:46 [kv_cache_utils.py:720] Maximum concurrency for 40,960 tokens per request: 19.42x INFO 08-27 17:25:59 [tp...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;speculative_decoding cache;cuda;operator;triton build_error env_dependency #23942 [CI] Add `a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ;hardware_porting;model_support;speculative_decoding cache;cuda;operator;triton build_error env_dependency #23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Issue running Qwen3-0.6B on TPU-v5p-8 bug ### Your current environment ### 🐛 Describe the bug Tried running `vllm serve Qwen/Qwen3-0.6B` on a v5p-8 but it didn't work for me. After loading the model weights and w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: :25:46 [kv_cache_utils.py:720] Maximum concurrency for 40,960 tokens per request: 19.42x INFO 08-27 17:25:59 [tpu_model_runner.py:1294] Compiling the model with different input shapes. INFO 08-27 17:25:59 [tpu_model_run...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23773: Should have ROCm label: NO (0 matches) #23768: Should have ROCm label: NO (0 matches) #23767: Should have ROCm label: NO (0 matches) #23761: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
