# vllm-project/vllm#9294: [New Model]: meta-llama/Llama-Guard-3-1B

| 字段 | 值 |
| --- | --- |
| Issue | [#9294](https://github.com/vllm-project/vllm/issues/9294) |
| 状态 | closed |
| 标签 | help wanted;new-model |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: meta-llama/Llama-Guard-3-1B

### Issue 正文摘录

### The model to consider. meta-llama/Llama-Guard-3-1B ### The closest model vllm already supports. meta-llama/Llama-Guard-3-8B ### What's your difficulty of supporting the model you want? Currently the model runs, but its outputs are completely random, so the same prompt can be safe or unsafe at any point. Setting the temperature to 0.0 makes EVERY prompt return safe. My hunch is the issue comes from the model pruning: Output Layer Pruning The Llama Guard model is trained to generate 128k output tokens out of which only 20 tokens (e.g. safe, unsafe, S, 1,...) are used. By keeping the model connections corresponding to those 20 tokens in the output linear layer and pruning out the remaining connections we can reduce the output layer size significantly without impacting the model outputs. Using output layer pruning, we reduced the output layer size from 262.6M parameters (2048x128k) to 40.96k parameters (2048x20), giving us a total savings of 131.3MB with 4-bit quantized weights. Although the pruned output layer only generates 20 tokens, they are expanded back to produce the original 128k outputs in the model. ### Before submitting a new issue... - [X] Make sure you already searche...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: meta-llama/Llama-Guard-3-1B help wanted;new-model ### The model to consider. meta-llama/Llama-Guard-3-1B ### The closest model vllm already supports. meta-llama/Llama-Guard-3-8B ### What's your difficulty of
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 6k parameters (2048x20), giving us a total savings of 131.3MB with 4-bit quantized weights. Although the pruned output layer only generates 20 tokens, they are expanded back to produce the original 128k outputs in the m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
