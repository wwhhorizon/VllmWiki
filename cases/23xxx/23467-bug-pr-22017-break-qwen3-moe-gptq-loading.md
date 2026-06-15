# vllm-project/vllm#23467: [Bug]: PR #22017 break Qwen3 MoE GPTQ loading

| 字段 | 值 |
| --- | --- |
| Issue | [#23467](https://github.com/vllm-project/vllm/issues/23467) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PR #22017 break Qwen3 MoE GPTQ loading

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/issues/23165, which is partially fixed in https://github.com/vllm-project/vllm/pull/23188/ by @Isotr0py This bug not only breaks Qwen3 MoE GGUF models, but also affects GPTQ model released by the Qwen team: https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4 Click the "File Info" button on the right-hand side of the above model link and check `layers.0.mlp.gate.weight`, it can be seen that this tensor is unquantized too. It's worth noting that I encountered this issue in a downstream branch I maintain, not in the official vLLM, but I believe this bug is also present in upstream. If I'm mistaken, please correct me. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: PR #22017 break Qwen3 MoE GPTQ loading bug ### Your current environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/issues/23165, which is partially fixed in https://github.com/vllm-project/vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Click the "File Info" button on the right-hand side of the above model link and check `layers.0.mlp.gate.weight`, it can be seen that this tensor is unquantized too. It's worth noting that I encountered this issue in a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: leased by the Qwen team: https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4 Click the "File Info" button on the right-hand side of the above model link and check `layers.0.mlp.gate.weight`, it can be seen that this ten...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: me. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: PR #22017 break Qwen3 MoE GPTQ loading bug ### Your current environment ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/issues/23165, which is partially fixed in https://github.com/vllm-project/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
