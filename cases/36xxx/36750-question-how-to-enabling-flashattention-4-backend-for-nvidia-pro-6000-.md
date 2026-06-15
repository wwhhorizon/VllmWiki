# vllm-project/vllm#36750: [Question]HOW TO  Enabling FlashAttention- 4 backend for NVIDIA PRO 6000   (Blackwell) with MiniMax-2.5-230B

| 字段 | 值 |
| --- | --- |
| Issue | [#36750](https://github.com/vllm-project/vllm/issues/36750) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;hardware_porting;model_support;moe |
| 子分类 | throughput |
| Operator 关键词 | attention;moe |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Question]HOW TO  Enabling FlashAttention- 4 backend for NVIDIA PRO 6000   (Blackwell) with MiniMax-2.5-230B

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I am trying to deploy the MiniMax-M2.5-230B-MoE model using vLLM on a node with 4x NVIDIA PRO6000 (Blackwell architecture, 96GB each). Despite using the latest vllm==0.17.0, the system automatically falls back to the FlashAttention-2 (FA2) backend. Given our requirement for a long context window (196,608 tokens), we are looking to leverage FlashAttention-4 (or FA3) to optimize memory efficiency and throughput on this new hardware. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Question]HOW TO Enabling FlashAttention- 4 backend for NVIDIA PRO 6000 (Blackwell) with MiniMax-2.5-230B usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to us...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: are looking to leverage FlashAttention-4 (or FA3) to optimize memory efficiency and throughput on this new hardware. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: estion]HOW TO Enabling FlashAttention- 4 backend for NVIDIA PRO 6000 (Blackwell) with MiniMax-2.5-230B usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: NVIDIA PRO6000 (Blackwell architecture, 96GB each). Despite using the latest vllm==0.17.0, the system automatically falls back to the FlashAttention-2 (FA2) backend. Given our requirement for a long context window (196,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ld you like to use vllm I am trying to deploy the MiniMax-M2.5-230B-MoE model using vLLM on a node with 4x NVIDIA PRO6000 (Blackwell architecture, 96GB each). Despite using the latest vllm==0.17.0, the system automatica...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
