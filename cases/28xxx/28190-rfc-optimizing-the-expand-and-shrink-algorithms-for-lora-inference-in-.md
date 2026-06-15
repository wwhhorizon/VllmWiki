# vllm-project/vllm#28190: [RFC]: Optimizing the Expand and Shrink Algorithms for LoRA Inference in Dense Models

| 字段 | 值 |
| --- | --- |
| Issue | [#28190](https://github.com/vllm-project/vllm/issues/28190) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | operator |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Optimizing the Expand and Shrink Algorithms for LoRA Inference in Dense Models

### Issue 正文摘录

### Motivation. During multi-LoRA performance testing on NVIDIA H800 GPUs, we identified performance bottlenecks in the original LoRA expand and shrink operators during dense model inference. ### Proposed Change. By optimizing the execution branches of the relevant algorithms, we aim to enhance the overall GPU execution concurrency and improve operational efficiency.We have identified an optimization strategy and plan to implement it within one week. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nhance the overall GPU execution concurrency and improve operational efficiency.We have identified an optimization strategy and plan to implement it within one week. ### Feedback Period. _No response_ ### CC List. _No r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Optimizing the Expand and Shrink Algorithms for LoRA Inference in Dense Models RFC ### Motivation. During multi-LoRA performance testing on NVIDIA H800 GPUs, we identified performance bottlenecks in the original LoRA ex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rence in Dense Models RFC ### Motivation. During multi-LoRA performance testing on NVIDIA H800 GPUs, we identified performance bottlenecks in the original LoRA expand and shrink operators during dense model inference. #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
