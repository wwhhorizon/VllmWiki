# vllm-project/vllm#38754: [Bug]: GPT OSS Router GEMM Causing NaNs

| 字段 | 值 |
| --- | --- |
| Issue | [#38754](https://github.com/vllm-project/vllm/issues/38754) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | gemm_linear;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;kernel |
| 症状 | nan_inf |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT OSS Router GEMM Causing NaNs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The custom router GEMM kernel is causing infrequent NaNs in an internal test that poisons the correctness of the EAGLE draft model. It seems to only occur in very specific scenarios involving cuda graphs, prefix caching, and chunked prefills. Identified root-cause by manual bisection: https://github.com/vllm-project/vllm/pull/37205, originally manifested as acceptance rates of EAGLE3 going to zero. No special flags needed to reproduce, just running gpt-oss-120b on 1xB200 with EAGLE3 enabled. Unfortunately I cannot share the script to reproduce the failure, it is an internal script for multi-turn chat replay. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: draft model. It seems to only occur in very specific scenarios involving cuda graphs, prefix caching, and chunked prefills. Identified root-cause by manual bisection: https://github.com/vllm-project/vllm/pull/37205, ori...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: quent NaNs in an internal test that poisons the correctness of the EAGLE draft model. It seems to only occur in very specific scenarios involving cuda graphs, prefix caching, and chunked prefills. Identified root-cause...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: NaNs in an internal test that poisons the correctness of the EAGLE draft model. It seems to only occur in very specific scenarios involving cuda graphs, prefix caching, and chunked prefills. Identified root-cause by man...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: GPT OSS Router GEMM Causing NaNs bug ### Your current environment ### 🐛 Describe the bug The custom router GEMM kernel is causing infrequent NaNs in an internal test that poisons the correctness of the EAGLE draf...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: as acceptance rates of EAGLE3 going to zero. No special flags needed to reproduce, just running gpt-oss-120b on 1xB200 with EAGLE3 enabled. Unfortunately I cannot share the script to reproduce the failure, it is an inte...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
