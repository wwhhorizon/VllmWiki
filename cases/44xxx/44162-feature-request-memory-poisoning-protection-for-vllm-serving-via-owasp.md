# vllm-project/vllm#44162: [Feature Request] Memory Poisoning Protection for vLLM Serving via OWASP Agent Memory Guard

| 字段 | 值 |
| --- | --- |
| Issue | [#44162](https://github.com/vllm-project/vllm/issues/44162) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Memory Poisoning Protection for vLLM Serving via OWASP Agent Memory Guard

### Issue 正文摘录

## Problem vLLM-served models used in agentic pipelines with persistent memory are vulnerable to **memory poisoning attacks**. Adversarial inputs stored in conversation history or context windows can cause served models to leak system prompts, ignore safety instructions, or produce corrupted outputs. ## Proposed Solution **OWASP Agent Memory Guard (AMG)** is an open-source Python library that wraps any memory store as a transparent security layer: - `pip install agent-memory-guard` - Scans every memory write for prompt injection, PII leakage, and tampering - 92.5% detection rate on AgentThreatBench - Works with vLLM + LangChain, LlamaIndex, or any custom pipeline - <5ms latency per scan ## Links - GitHub: https://github.com/OWASP/www-project-agent-memory-guard - PyPI: https://pypi.org/project/agent-memory-guard/ - Benchmark: https://pypi.org/project/agent-threat-bench/

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ary that wraps any memory store as a transparent security layer: - `pip install agent-memory-guard` - Scans every memory write for prompt injection, PII leakage, and tampering - 92.5% detection rate on AgentThreatBench...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on for vLLM Serving via OWASP Agent Memory Guard ## Problem vLLM-served models used in agentic pipelines with persistent memory are vulnerable to **memory poisoning attacks**. Adversarial inputs stored in conversation h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: - Works with vLLM + LangChain, LlamaIndex, or any custom pipeline - <5ms latency per scan ## Links - GitHub: https://github.com/OWASP/www-project-agent-memory-guard - PyPI: https://pypi.org/project/agent-memory-guard/ -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature Request] Memory Poisoning Protection for vLLM Serving via OWASP Agent Memory Guard ## Problem vLLM-served models used in agentic pipelines with persistent memory are vulnerable to **memory poisoning attacks**....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
