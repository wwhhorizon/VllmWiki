# vllm-project/vllm#34947: Feature: Audit-grade request logging for EU AI Act compliance (Article 12)

| 字段 | 值 |
| --- | --- |
| Issue | [#34947](https://github.com/vllm-project/vllm/issues/34947) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature: Audit-grade request logging for EU AI Act compliance (Article 12)

### Issue 正文摘录

## Context The EU AI Act (Regulation 2024/1689) requires high-risk AI systems to have **automatic logging capabilities** (Article 12) that record events throughout the system's operation for traceability purposes. For LLM serving infrastructure like vLLM, this translates to structured, audit-grade request logging. ## Current State vLLM provides excellent performance metrics and basic request logging via its OpenAI-compatible API server. However, the current logging is focused on **operational monitoring** (latency, throughput, errors) rather than **regulatory compliance**. Gaps include: - No structured per-request audit log with deterministic identifiers - No standardized capture of model version, quantization config, and serving parameters alongside each request - No built-in mechanism for log integrity verification (e.g., hash chaining) - Request/response content logging exists but isn't designed for compliance retention policies ## Proposal An optional `--audit-log` mode that emits structured JSON records per request: ```json { "request_id": "uuid-...", "timestamp": "2026-02-20T10:30:00Z", "model_id": "meta-llama/Llama-3-70B-Instruct", "model_hash": "sha256:abc...", "quantizati...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: st audit log with deterministic identifiers - No standardized capture of model version, quantization config, and serving parameters alongside each request - No built-in mechanism for log integrity verification (e.g., ha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: . However, the current logging is focused on **operational monitoring** (latency, throughput, errors) rather than **regulatory compliance**. Gaps include: - No structured per-request audit log with deterministic identif...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: it log with deterministic identifiers - No standardized capture of model version, quantization config, and serving parameters alongside each request - No built-in mechanism for log integrity verification (e.g., hash cha...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: compliance**. Gaps include: - No structured per-request audit log with deterministic identifiers - No standardized capture of model version, quantization config, and serving parameters alongside each request - No built-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: th deterministic identifiers - No standardized capture of model version, quantization config, and serving parameters alongside each request - No built-in mechanism for log integrity verification (e.g., hash chaining) -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
