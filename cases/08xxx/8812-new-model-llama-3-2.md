# vllm-project/vllm#8812: [New Model]: Llama 3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#8812](https://github.com/vllm-project/vllm/issues/8812) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Llama 3.2

### Issue 正文摘录

### The model to consider. - **Huggingface collection:** https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf Highlighted model weights: - **1B Instruct Model:** https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct - **3B Instruct Model:** https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct - **11B Instruct Model:** https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct - **90B Instruct Model:** https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct ### The closest model vllm already supports. https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llama.py https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/llava_onevision.py ### What's your difficulty of supporting the model you want? Yes, Llama 3.2 is multimodal with a different architecture than previous multimodal Llama models. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: Llama 3.2 new-model ### The model to consider. - **Huggingface collection:** https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf Highlighted model weights: - **1B Instruct Model:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rting the model you want? Yes, Llama 3.2 is multimodal with a different architecture than previous multimodal Llama models. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
