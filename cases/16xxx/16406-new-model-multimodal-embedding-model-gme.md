# vllm-project/vllm#16406: [New Model]: Multimodal Embedding Model GME.

| 字段 | 值 |
| --- | --- |
| Issue | [#16406](https://github.com/vllm-project/vllm/issues/16406) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 68; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Multimodal Embedding Model GME.

### Issue 正文摘录

### The model to consider. Multimodal Embedding Model GME. https://huggingface.co/collections/Alibaba-NLP/gme-models-67667e092da3491f630964d6 ### The closest model vllm already supports. Qwen2 VL、VLM2Vec ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: Multimodal Embedding Model GME. stale ### The model to consider. Multimodal Embedding Model GME. https://huggingface.co/collections/Alibaba-NLP/gme-models-67667e092da3491f630964d6 ### The closest model vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Multimodal Embedding Model GME. stale ### The model to consider. Multimodal Embedding Model GME. https://huggingface.co/collections/Alibaba-NLP/gme-models-67667e092da3491f630964d6 ### The closest model vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
