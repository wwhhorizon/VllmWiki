# vllm-project/vllm#35005: Data Governance & Compliance Guide for vLLM Deployments (EU AI Act Article 6)

| 字段 | 值 |
| --- | --- |
| Issue | [#35005](https://github.com/vllm-project/vllm/issues/35005) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Data Governance & Compliance Guide for vLLM Deployments (EU AI Act Article 6)

### Issue 正文摘录

## Context vLLM powers high-throughput LLM inference for many production systems. Many deployments handle sensitive data and may fall under EU AI Act Article 6+ (High-Risk AI Systems). ## Problem Users deploying vLLM lack guidance on: 1. **Data Governance** - What data is retained (prompts, completions, logs)? - How long is data persisted? - GDPR deletion/retention compliance? 2. **Article 6 Risk Classification** - Is my vLLM deployment high-risk? - What additional safeguards are needed? 3. **Monitoring & Transparency** - How to audit LLM outputs for bias, safety issues? - Logging requirements for compliance? ## Proposal Add a **Compliance & Data Governance Guide**: - : - Data flow diagram: prompts → inference → outputs → storage - Configuration guide: privacy-first defaults - GDPR/EU AI Act checklist - Logging best practices (audit trail without storing sensitive data) - Integration with compliance scanners ## Call to Action 1. **Feedback**: What data governance questions do users ask? 2. **Discussion**: Should vLLM have privacy-by-default settings? 3. **Contribution**: Compliance documentation or config examples --- *Opened by ArkForge (EU AI Act compliance automation). https://...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: - : - Data flow diagram: prompts → inference → outputs → storage - Configuration guide: privacy-first defaults - GDPR/EU AI Act checklist - Logging best practices (audit trail without storing sensitive data) - Integrati...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: for vLLM Deployments (EU AI Act Article 6) ## Context vLLM powers high-throughput LLM inference for many production systems. Many deployments handle sensitive data and may fall under EU AI Act Article 6+ (High-Risk AI S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
