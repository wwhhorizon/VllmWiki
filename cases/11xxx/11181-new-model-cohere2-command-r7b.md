# vllm-project/vllm#11181: [New Model]: Cohere2 (Command R7B)

| 字段 | 值 |
| --- | --- |
| Issue | [#11181](https://github.com/vllm-project/vllm/issues/11181) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Cohere2 (Command R7B)

### Issue 正文摘录

### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-r7b-12-2024 ### The closest model vllm already supports. Likely either the original Cohere (for. obvious reasons) or Gemma2 (as it also has a funky SWA architecture) ### What's your difficulty of supporting the model you want? It uses SWA, but this can likely be ditched to get MVP inference working ala how gemma 2 was done For some reason every 4th layer uses global attention _without_ positional embeddings? Not sure how or why that one works tbh ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Cohere2 (Command R7B) new-model ### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-r7b-12-2024 ### The closest model vllm already supports. Likely either the original Cohere (for. ob...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: inal Cohere (for. obvious reasons) or Gemma2 (as it also has a funky SWA architecture) ### What's your difficulty of supporting the model you want? It uses SWA, but this can likely be ditched to get MVP inference workin...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: y supports. Likely either the original Cohere (for. obvious reasons) or Gemma2 (as it also has a funky SWA architecture) ### What's your difficulty of supporting the model you want? It uses SWA, but this can likely be d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
