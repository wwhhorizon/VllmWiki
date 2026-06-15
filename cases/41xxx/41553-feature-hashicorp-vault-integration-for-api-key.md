# vllm-project/vllm#41553: [Feature]: Hashicorp Vault Integration for API Key

| 字段 | 值 |
| --- | --- |
| Issue | [#41553](https://github.com/vllm-project/vllm/issues/41553) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Hashicorp Vault Integration for API Key

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Add option to use a Hashicorp KV V2 endpoint for API Key check. Update/end entrypoints/openai/server_utils.py to use an argument `use-vault` and then use environment variables `VAULT_ADDR`, `VAULT_TOKEN` and `VAULT_SECRET_PATH` to validate the api-token header on each request. Currently, to change the api-key, the vllm service needs to restart, by externalizing to Vault, the key can be changed independently without requiring the restart. ### Alternatives - static key and restart of the vllm server on key change - externalize endpoint protection to a proxy/sidecar ### Additional context None ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: one ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Hashicorp Vault Integration for API Key feature request ### 🚀 The feature, motivation and pitch Add option to use a Hashicorp KV V2 endpoint for API Key check. Update/end entrypoints/openai/server_utils.py to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
