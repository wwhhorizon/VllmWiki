# vllm-project/vllm#35494: [Bug]: sparsemixer uses hard-coded jitter_eps instead of config

| 字段 | 值 |
| --- | --- |
| Issue | [#35494](https://github.com/vllm-project/vllm/issues/35494) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: sparsemixer uses hard-coded jitter_eps instead of config

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug In vllm/model_executor/models/phimoe.py, the sparsemixer function currently has a hard-coded default value for jitter_eps: ``` def sparsemixer(scores, jitter_eps=0.01): ... topk_weights, topk_ids = sparsemixer(gating_output) ``` However, in the HuggingFace transformers implementation (modeling_phimoe.py), this value is configurable via config.router_jitter_noise: ``` self.router_jitter_noise = config.router_jitter_noise routing_weights, selected_experts = sparsemixer( router_logits, jitter_eps=self.router_jitter_noise, ...) ``` This mismatch may lead to inconsistent behavior when reproducing models that rely on a specific router_jitter_noise setting. Expected behavior sparsemixer should use the value from config.router_jitter_noise by default, and set router_jitter_noise defaults to 0.01 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: ironment None ### 🐛 Describe the bug In vllm/model_executor/models/phimoe.py, the sparsemixer function currently has a hard-coded default value for jitter_eps: ``` def sparsemixer(scores, jitter_eps=0.01): ... topk_weig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: sparsemixer uses hard-coded jitter_eps instead of config bug;stale ### Your current environment None ### 🐛 Describe the bug In vllm/model_executor/models/phimoe.py, the sparsemixer function currently has a hard-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: router_logits, jitter_eps=self.router_jitter_noise, ...) ``` This mismatch may lead to inconsistent behavior when reproducing models that rely on a specific router_jitter_noise setting. Expected behavior sparsemixer sho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _jitter_noise: ``` self.router_jitter_noise = config.router_jitter_noise routing_weights, selected_experts = sparsemixer( router_logits, jitter_eps=self.router_jitter_noise, ...) ``` This mismatch may lead to inconsiste...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r( router_logits, jitter_eps=self.router_jitter_noise, ...) ``` This mismatch may lead to inconsistent behavior when reproducing models that rely on a specific router_jitter_noise setting. Expected behavior sparsemixer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
