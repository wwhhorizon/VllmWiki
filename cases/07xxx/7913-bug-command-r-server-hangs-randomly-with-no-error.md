# vllm-project/vllm#7913: [Bug]: command r server hangs randomly with no error

| 字段 | 值 |
| --- | --- |
| Issue | [#7913](https://github.com/vllm-project/vllm/issues/7913) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: command r server hangs randomly with no error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Server runs fine for the first 100 or so requests and then randomly hangs without any error message ``` INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-a9ac2e0376b44cda9aeb5f4635d2fa12. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-d13358ef80e04122a1171f9b7419dad4. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-fb808f8709124805ad06c470340557b1. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-30c54579ff5441ddb0a3b0166c19f828. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-43d885b1665d46e4a43c3d86b48cd737. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-4ab0462d1c4d41e7abab908eee2b2355. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-7951c7896aee40d3a1d4d97f8545d3a0. INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-29b49e4d8e0549d0acfb416b1f29873a. INFO 08-27 13:53:14 metrics.py:351] Avg prompt throughput: 9293.3 tokens/s, Avg generation throughput: 30.9 tokens/s, Running: 21 reqs, Swapped: 0 reqs, Pending: 11 reqs, GPU KV cache usage: 3.3%, CPU KV cache usage: 0.0%. INFO 08-27 13:53:14 metrics.py:367]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: . To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-08-27 13:53:17.646091: I tensorflow/core/platform/cpu_feature_guard.cc:210] This Tensor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ent ### 🐛 Describe the bug Server runs fine for the first 100 or so requests and then randomly hangs without any error message ``` INFO 08-27 13:53:13 async_llm_engine.py:208] Added request chat-a9ac2e0376b44cda9aeb5f46...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: :15 async_llm_engine.py:176] Finished request chat-a83ff738e3ac44a695b4fafa3226b0a8. INFO 08-27 13:53:15 async_llm_engine.py:176] Finished request chat-06cf60bd33d644ab82367c2e67c15709. INFO 08-27 13:53:15 async_llm_eng...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 30.9 tokens/s, Running: 21 reqs, Swapped: 0 reqs, Pending: 11 reqs, GPU KV cache usage: 3.3%, CPU KV cache usage: 0.0%. INFO 08-27 13:53:14 metrics.py:367] Prefix cache hit rate: GPU: 91.31%, CPU: 0.00% INFO 08-27 13:53...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
