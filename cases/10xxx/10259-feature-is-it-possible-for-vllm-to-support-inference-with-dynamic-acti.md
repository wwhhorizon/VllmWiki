# vllm-project/vllm#10259: [Feature]: Is it possible for VLLM to support inference with dynamic activation sparsity?

| 字段 | 值 |
| --- | --- |
| Issue | [#10259](https://github.com/vllm-project/vllm/issues/10259) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Is it possible for VLLM to support inference with dynamic activation sparsity?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We know that language models exhibit activation sparsity during inference, meaning that they can perform lossless inference even when only a portion of the activation values are activated. This activation sparsity is not limited to language models using the ReLU function; it is also observed in current large models that use the SiLU function. Additionally, recent studies have shown that language models can exhibit a "flocking" phenomenon during inference (see below), where different tokens in a sentence share relatively high activation values. By applying this process to inference, one can record the activated neurons during the prefill stage and then compute only the selected neurons during the decode stage, thereby accelerating inference. For more details, refer to the article https://arxiv.org/abs/2404.01365v3. ![image](https://github.com/user-attachments/assets/fe5290aa-4b9e-4dcb-9e6e-38e7706df8ac) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pa...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: for VLLM to support inference with dynamic activation sparsity? feature request;stale ### 🚀 The feature, motivation and pitch We know that language models exhibit activation sparsity during inference, meaning that they...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: est;stale ### 🚀 The feature, motivation and pitch We know that language models exhibit activation sparsity during inference, meaning that they can perform lossless inference even when only a portion of the activation va...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
