# vllm-project/vllm#7863: [New Model]: Request to integrate Chexagent Multimodel in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#7863](https://github.com/vllm-project/vllm/issues/7863) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Request to integrate Chexagent Multimodel in vLLM

### Issue 正文摘录

### The model to consider. https://huggingface.co/StanfordAIMI/CheXagent-8b ### The closest model vllm already supports. https://huggingface.co/microsoft/llava-med-v1.5-mistral-7b ### What's your difficulty of supporting the model you want? when i tried to host chexagent it says, model architecture not supported by vllm.its has integrated qformer inside this.any help in integrating this will be helpful. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Request to integrate Chexagent Multimodel in vLLM new-model;stale ### The model to consider. https://huggingface.co/StanfordAIMI/CheXagent-8b ### The closest model vllm already supports. https://huggingface...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [New Model]: Request to integrate Chexagent Multimodel in vLLM new-model;stale ### The model to consider. https://huggingface.co/StanfordAIMI/CheXagent-8b ### The closest model vllm already supports. https://huggingface...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rting the model you want? when i tried to host chexagent it says, model architecture not supported by vllm.its has integrated qformer inside this.any help in integrating this will be helpful. ### Before submitting a new...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
