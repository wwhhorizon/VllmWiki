# vllm-project/vllm#9040: [New Model]: NVLM 1.0

| 字段 | 值 |
| --- | --- |
| Issue | [#9040](https://github.com/vllm-project/vllm/issues/9040) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: NVLM 1.0

### Issue 正文摘录

### The model to consider. **Collection**: https://huggingface.co/collections/nvidia/nvlm-10-66e9f407c764a0ee6e37b7f4 **NVLM-D 1.0 72B**: https://huggingface.co/nvidia/NVLM-D-72B ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/internvl.py The Huggingface inference code was reportedly adapted from the InternVL codebase. ![Screenshot from 2024-10-03 07-17-00](https://github.com/user-attachments/assets/495130c6-2cb3-42c2-bdfc-90ec974391e8) ### What's your difficulty of supporting the model you want? NVLM 1.0 has a new architecture that may take some time to support in vLLM. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: NVLM 1.0 new-model ### The model to consider. **Collection**: https://huggingface.co/collections/nvidia/nvlm-10-66e9f407c764a0ee6e37b7f4 **NVLM-D 1.0 72B**: https://huggingface.co/nvidia/NVLM-D-72B ### The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 's your difficulty of supporting the model you want? NVLM 1.0 has a new architecture that may take some time to support in vLLM. ### Before submitting a new issue... - [X] Make sure you already searched for relevant iss...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
