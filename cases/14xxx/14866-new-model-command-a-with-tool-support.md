# vllm-project/vllm#14866: [New Model]: Command A with tool support

| 字段 | 值 |
| --- | --- |
| Issue | [#14866](https://github.com/vllm-project/vllm/issues/14866) |
| 状态 | closed |
| 标签 | new-model;stale;tool-calling |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Command A with tool support

### Issue 正文摘录

### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-a-03-2025 ### The closest model vllm already supports. command r ### What's your difficulty of supporting the model you want? Properly support tokenizer and templates, as well as tool calling on the model ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [New Model]: Command A with tool support new-model;stale;tool-calling ### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-a-03-2025 ### The closest model vllm already supports. command r ### What's
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: del ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: Command A with tool support new-model;stale;tool-calling ### The model to consider. https://huggingface.co/CohereForAI/c4ai-command-a-03-2025 ### The closest model vllm already supports. command r ### What'...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
