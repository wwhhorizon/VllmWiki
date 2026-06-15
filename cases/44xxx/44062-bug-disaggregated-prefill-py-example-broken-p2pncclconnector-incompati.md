# vllm-project/vllm#44062: [Bug]: disaggregated_prefill.py example broken - P2pNcclConnector incompatible with offline mode

| 字段 | 值 |
| --- | --- |
| Issue | [#44062](https://github.com/vllm-project/vllm/issues/44062) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: disaggregated_prefill.py example broken - P2pNcclConnector incompatible with offline mode

### Issue 正文摘录

### Your current environment **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B **Description**: Running `examples/disaggregated/disaggregated_prefill.py` with P2pNcclConnector fails with: ValueError: Request id 0 does not contain hostname and port Root cause: `P2pNcclConnector.parse_request_id()` expects request_id to contain `___decode_addr_IP:PORT` or `___prefill_addr_IP:PORT___` patterns, which are injected by a proxy in online serving mode. In offline mode there is no proxy, so this information is never present in the request_id. The example script implies P2pNcclConnector works in offline mode, but it is fundamentally designed for proxy-based online serving only. The example is misleading or broken. Note: `VLLM_DISABLE_REQUEST_ID_RANDOMIZATION=1` workaround does not help. **Steps to reproduce**: 1. Run `python examples/disaggregated/disaggregated_prefill.py` 2. After fixing the port conflict issue (bug #1), script fails with ValueError on request_id **Related**: #38808 [...

## 现有链接修复摘要

#44179 fix offline disaggregated prefill request ids for P2P NCCL

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: disaggregated_prefill.py example broken - P2pNcclConnector incompatible with offline mode bug ### Your current environment **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: h offline mode bug ### Your current environment **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Environment**: - vLLM versio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA 13.0 - Model: Qwen/Qwen3-8B ### 🐛 Describe the bug **Environment**: - vLLM version: 0.22.0 - Hardware: 2x NVIDIA L40 46GB - OS: Ubuntu, CUDA...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ISABLE_REQUEST_ID_RANDOMIZATION=1` workaround does not help. **Steps to reproduce**: 1. Run `python examples/disaggregated/disaggregated_prefill.py` 2. After fixing the port conflict issue (bug #1), script fails with Va...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44179](https://github.com/vllm-project/vllm/pull/44179) | closes_keyword | 0.95 | fix offline disaggregated prefill request ids for P2P NCCL | Fixes #44062. - split the prefill and decode KV ports in `examples/disaggregated/disaggregated_prefill.py` - generate endpoint-encoded request IDs for the offline example so it |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
