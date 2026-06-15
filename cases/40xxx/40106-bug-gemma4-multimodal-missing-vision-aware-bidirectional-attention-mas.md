# vllm-project/vllm#40106: [Bug]: Gemma4 multimodal: missing vision-aware bidirectional attention mask for use_bidirectional_attention="vision" models

| 字段 | 值 |
| --- | --- |
| Issue | [#40106](https://github.com/vllm-project/vllm/issues/40106) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 multimodal: missing vision-aware bidirectional attention mask for use_bidirectional_attention="vision" models

### Issue 正文摘录

### 🐛 Describe the bug For Gemma4 checkpoints whose text config has `use_bidirectional_attention="vision"` (e.g. `gemma-4-31B-it`, `gemma-4-26B-A4B-it`), vLLM's Gemma4 implementation silently ignores the flag and runs standard causal attention on vision tokens. HF transformers' `Gemma4Model.forward` calls `create_causal_mask_mapping`, which makes tokens inside the same vision group bidirectionally visible to each other. The vLLM forward diverges from HF on multimodal inputs as a result. This affects any multimodal use case (generation, logprobs) and causes significant numerical divergence compared to the HF reference, concentrated on image token positions. ### Reproduction Running a teacher-forcing forward pass on `gemma-4-31B-it` (dense, `use_bidirectional_attention="vision"`) and `gemma-4-26B-A4B-it` (MoE, same flag) with a multimodal prompt (a synthetic 224×224 image + text instruction), and comparing HF logprobs to vLLM logprobs on the generation tokens: | model | `KL(P_HF || P_vLLM)` on generation tokens | |---|---| | gemma-4-E4B-it (no bidir) | 0.0004 | | gemma-4-31B-it (bidir=vision) | ~0.03 | | gemma-4-26B-A4B-it (bidir=vision) | ~0.09 | ### Before submitting a new issue.....

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma4 multimodal: missing vision-aware bidirectional attention mask for use_bidirectional_attention="vision" models bug ### 🐛 Describe the bug For Gemma4 checkpoints whose text config has `use_bidirectional_atte...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ts any multimodal use case (generation, logprobs) and causes significant numerical divergence compared to the HF reference, concentrated on image token positions. ### Reproduction Running a teacher-forcing forward pass...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Gemma4 multimodal: missing vision-aware bidirectional attention mask for use_bidirectional_attention="vision" models bug ### 🐛 Describe the bug For Gemma4 checkpoints whose text config has `use_bidirectional_atte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: trated on image token positions. ### Reproduction Running a teacher-forcing forward pass on `gemma-4-31B-it` (dense, `use_bidirectional_attention="vision"`) and `gemma-4-26B-A4B-it` (MoE, same flag) with a multimodal pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 9 | ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
