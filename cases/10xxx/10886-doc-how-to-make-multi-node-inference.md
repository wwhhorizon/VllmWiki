# vllm-project/vllm#10886: [Doc]: How to make Multi-Node Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#10886](https://github.com/vllm-project/vllm/issues/10886) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: How to make Multi-Node Inference

### Issue 正文摘录

### 📚 The doc issue I need to use 72B model for inference about 10W cases, and have learn about Distributed Inference and Serving. I have 4 machines, each with 2 A10 GPUs. I think vLLM can split this model across 8 GPUs using tensor parallelism and pipeline parallelism. (Ray can start on these machines) However, I haven't found how to do multi-node inference. The documentation seems to only cover single-node inference & serving, as well as multi-node serving, which might not be what I need. ### Suggest a potential alternative/fix If can rewrite to add how to make multi-node inference ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s. I think vLLM can split this model across 8 GPUs using tensor parallelism and pipeline parallelism. (Ray can start on these machines) However, I haven't found how to do multi-node inference. The documentation seems to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ulti-Node Inference documentation ### 📚 The doc issue I need to use 72B model for inference about 10W cases, and have learn about Distributed Inference and Serving. I have 4 machines, each with 2 A10 GPUs. I think vLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
