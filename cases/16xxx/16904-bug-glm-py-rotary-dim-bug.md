# vllm-project/vllm#16904: [Bug]: glm.py rotary_dim bug

| 字段 | 值 |
| --- | --- |
| Issue | [#16904](https://github.com/vllm-project/vllm/issues/16904) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: glm.py rotary_dim bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug class GlmForCausalLM(LlamaForCausalLM, SupportsV0Only): def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""): super().__init__(vllm_config=vllm_config, prefix=prefix) # Hack Llama model to fit HF format GLM implementation # Attention difference between GLM and Llama: # 1. Half partial rotary_dim and no Neox style. # 2. There is no bias for o_proj in attention for layer in self.model.layers: if not isinstance(layer, PPMissingLayer): print(layer.self_attn.rotary_emb.rotary_dim) layer.self_attn.rotary_emb.rotary_dim //= 2 layer.self_attn.rotary_emb.is_neox_style = False layer.self_attn.o_proj.bias = None layer.self_attn.o_proj.skip_bias_add = True layer.self_attn.rotary_emb.rotary_dim is divided in every layer: ![Image](https://github.com/user-attachments/assets/d3862aff-ca7c-4ca5-8bde-b03fd2ab3d44) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: our current environment ### 🐛 Describe the bug class GlmForCausalLM(LlamaForCausalLM, SupportsV0Only): def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""): super().__init__(vllm_config=vllm_config, prefix=p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 44) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y_dim //= 2 layer.self_attn.rotary_emb.is_neox_style = False layer.self_attn.o_proj.bias = None layer.self_attn.o_proj.skip_bias_add = True layer.self_attn.rotary_emb.rotary_dim is divided in every layer: ![Image](https...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
