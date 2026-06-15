# vllm-project/vllm#38511: feat: DNS-AID SVCB endpoint capability advertisement

| 字段 | 值 |
| --- | --- |
| Issue | [#38511](https://github.com/vllm-project/vllm/issues/38511) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> feat: DNS-AID SVCB endpoint capability advertisement

### Issue 正文摘录

## Motivation When deploying multiple vLLM instances (different models, quantizations, context windows), consuming AI agents currently need to know each endpoint URL in advance and call `/v1/models` to discover capabilities. This adds a bootstrap dependency and doesn't scale well with dynamic infrastructure. ## Proposal Add opt-in [DNS-AID](https://dns-aid.org) ([RFC 9460](https://www.rfc-editor.org/rfc/rfc9460) SVCB profile) support: when `--dns-aid-enabled` is set, vLLM publishes a DNS SVCB record on startup encoding model name, context window, quantization, max batch size, and transport. AI agents can then discover vLLM endpoints via a single DNS lookup. **Key properties:** - Opt-in: disabled by default, zero behavior change for existing deployments - Optional dependency: `pip install vllm[dns-aid]` - Only global rank 0 registers in TP/PP configurations - Graceful deregistration on SIGTERM and ASGI shutdown ## Example ```bash vllm serve meta-llama/Llama-3-70b-instruct \ --dns-aid-enabled \ --dns-aid-zone agents.example.internal ``` Publishes: ``` _meta-llama-llama-3-70b-instruct._agents.agents.example.internal SVCB 1 serve.example.internal ( alpn="h2" port=8000 model="meta-llam...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ## Motivation When deploying multiple vLLM instances (different models, quantizations, context windows), consuming AI agents currently need to know each endpoint URL in advance and call `/v1/models` to discover capabili...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: isement ## Motivation When deploying multiple vLLM instances (different models, quantizations, context windows), consuming AI agents currently need to know each endpoint URL in advance and call `/v1/models` to discover...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ce and call `/v1/models` to discover capabilities. This adds a bootstrap dependency and doesn't scale well with dynamic infrastructure. ## Proposal Add opt-in [DNS-AID](https://dns-aid.org) ([RFC 9460](https://www.rfc-e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ://dns-aid.org) ([RFC 9460](https://www.rfc-editor.org/rfc/rfc9460) SVCB profile) support: when `--dns-aid-enabled` is set, vLLM publishes a DNS SVCB record on startup encoding model name, context window, quantization,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: feat: DNS-AID SVCB endpoint capability advertisement ## Motivation When deploying multiple vLLM instances (different models, quantizations, context windows), consuming AI agents currently need to know each endpoint URL...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
