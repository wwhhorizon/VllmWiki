# vllm-project/vllm#22071: [Usage]: Kubernetes Offline Model Usage

| 字段 | 值 |
| --- | --- |
| Issue | [#22071](https://github.com/vllm-project/vllm/issues/22071) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Kubernetes Offline Model Usage

### Issue 正文摘录

### Your current environment Chart version: 0.1.6 ### How would you like to use vllm Hello, I have installed vLLM in a Rancher Kubernetes environment using a Helm chart. The Rancher environment does not have internet access, so I have to manually download the models from Hugging Face and use them. I am using Longhorn as the storage class. How can I pull the model files into the PVCs from local S3 storage or another location? Thanks four your support in advance. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: etes Offline Model Usage usage;stale ### Your current environment Chart version: 0.1.6 ### How would you like to use vllm Hello, I have installed vLLM in a Rancher Kubernetes environment using a Helm chart. The Rancher...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Kubernetes Offline Model Usage usage;stale ### Your current environment Chart version: 0.1.6 ### How would you like to use vllm Hello, I have installed vLLM in a Rancher Kubernetes environment using a Helm char...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Kubernetes Offline Model Usage usage;stale ### Your current environment Chart version: 0.1.6 ### How would you like to use vllm Hello, I have installed vLLM in a Rancher Kubernetes environment using a Helm char...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
