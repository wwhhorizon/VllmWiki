# vllm-project/vllm#4171: [Bug]: Server crash for bloom-3b while use prefix_caching, `AssertionError assert Lk in {16, 32, 64, 128}`

| 字段 | 值 |
| --- | --- |
| Issue | [#4171](https://github.com/vllm-project/vllm/issues/4171) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Server crash for bloom-3b while use prefix_caching, `AssertionError assert Lk in {16, 32, 64, 128}`

### Issue 正文摘录

### Your current environment ```text vllm v0.4.0.post1 CUDA 12.2 ``` ### 🐛 Describe the bug ```text [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> File "/usr/local/lib/python3.10/dist-packages/vllm/attention/ops/paged_attn.py", line 178, in forward_prefix [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> context_attention_fwd( [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> return func(*args, **kwargs) [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> File "/usr/local/lib/python3.10/dist-packages/vllm/attention/ops/prefix_prefill.py", line 639, in context_attention_fwd [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> assert Lk in {16, 32, 64, 128} [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> AssertionError [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> [2024-04-17 20:07:13 ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ibe the bug ```text [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> File "/usr/local/lib/python3.10/dist-packages/vllm/attention/ops/paged_attn.py", line 178, in forward_prefix [2024-04-17 20:07:13,727] [ER...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2, 64, 128}` bug ### Your current environment ```text vllm v0.4.0.post1 CUDA 12.2 ``` ### 🐛 Describe the bug ```text [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> File "/usr/local/lib/python3.10/dist-pack...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Server crash for bloom-3b while use prefix_caching, `AssertionError assert Lk in {16, 32, 64, 128}` bug ### Your current environment ```text vllm v0.4.0.post1 CUDA 12.2 ``` ### 🐛 Describe the bug ```text [2024-04...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: File "/usr/local/lib/python3.10/dist-packages/vllm/attention/ops/prefix_prefill.py", line 639, in context_attention_fwd [2024-04-17 20:07:13,727] [ERROR] [MainThread] [asyncio] >>> assert Lk in {16, 32, 64, 128} [2024-0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
