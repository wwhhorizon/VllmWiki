# vllm-project/vllm#20566: [Feature]: vLLM does not support torch 2.7.1

| 字段 | 值 |
| --- | --- |
| Issue | [#20566](https://github.com/vllm-project/vllm/issues/20566) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vLLM does not support torch 2.7.1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm currently using vLLM alongside torch==2.7.1 for inference workloads. However, I'm encountering compatibility issues between the latest version of vLLM and torch==2.7.1, particularly involving flash-attn dependencies. It would be helpful if the vLLM project could update or support compatibility with torch==2.7.1, or at least document known compatibility constraints for newer Torch versions. This would make it easier for users who need to use the latest PyTorch release due to other ecosystem or performance requirements. ![Image](https://github.com/user-attachments/assets/53f1da0c-bfa1-4311-9b36-a9c55471c3ae) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: loads. However, I'm encountering compatibility issues between the latest version of vLLM and torch==2.7.1, particularly involving flash-attn dependencies. It would be helpful if the vLLM project could update or support...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: vLLM does not support torch 2.7.1 feature request ### 🚀 The feature, motivation and pitch I'm currently using vLLM alongside torch==2.7.1 for inference workloads. However, I'm encountering compatibility issue...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: workloads. However, I'm encountering compatibility issues between the latest version of vLLM and torch==2.7.1, particularly involving flash-attn dependencies. It would be helpful if the vLLM project could update or supp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
