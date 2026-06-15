# vllm-project/vllm#37852: [Bug]: Phi qk_layernorm appears to be unsupported in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#37852](https://github.com/vllm-project/vllm/issues/37852) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi qk_layernorm appears to be unsupported in vLLM

### Issue 正文摘录

### Your current environment This appears to be a model-implementation / config-compliance issue. ### 🐛 Describe the bug It looks like Phi's `qk_layernorm` behavior may be unsupported in vLLM. In the Transformers Phi implementation, when `config.qk_layernorm=True`, the model creates per-head `q_layernorm` / `k_layernorm` modules and applies them before rotary embedding: ```python self.qk_layernorm = config.qk_layernorm if self.qk_layernorm: self.q_layernorm = nn.LayerNorm(...) self.k_layernorm = nn.LayerNorm(...) if self.qk_layernorm: query_states = self.q_layernorm(query_states) key_states = self.k_layernorm(key_states) ``` However, in vllm/model_executor/models/phi.py, the current Phi attention path appears to be: ``` qkv, _ = self.qkv_proj(hidden_states) q, k, v = qkv.chunk(chunks=3, dim=-1) q, k = self.rotary_emb(position_ids, q, k) attn_output = self.attn(q, k, v) ``` There is no corresponding q_layernorm / k_layernorm branch. As a result, Phi configs/checkpoints with qk_layernorm=True may silently produce different attention behavior from Transformers. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pported in vLLM bug ### Your current environment This appears to be a model-implementation / config-compliance issue. ### 🐛 Describe the bug It looks like Phi's `qk_layernorm` behavior may be unsupported in vLLM. In the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
