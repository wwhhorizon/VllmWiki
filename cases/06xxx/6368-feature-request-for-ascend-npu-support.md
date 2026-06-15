# vllm-project/vllm#6368: [Feature]: Request for Ascend NPU support

| 字段 | 值 |
| --- | --- |
| Issue | [#6368](https://github.com/vllm-project/vllm/issues/6368) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Request for Ascend NPU support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Please visit: https://github.com/vllm-project/vllm-ascend Thanks again for your trial and feedback that made the first step for vLLM Ascend support. --- 请访问vllm-ascend官方仓库: https://github.com/vllm-project/vllm-ascend 再次感谢大家的试用，是您的及时反馈，让vLLM的昇腾支持迈出了第一步。 # Background Currently, the project supports various hardware accelerators such as GPUs, but there is no support for NPUs. Adding NPU support could significationly benefit users who have access to these devices, enabling faster and more efficient computations. # Reference Materials Ascend is a full-stack AI computing infrastructure for industry applications and services based on Huawei Ascend processors and software. For more information about Ascend, see [Ascend Community](https://www.hiascend.com/en/). [CANN](https://www.hiascend.com/en/software/cann) (Compute Architecture of Neural Networks), developped by Huawei, is a heterogeneous computing architecture for AI. Pytorch has officially announced [support for Ascend NPU](https://pytorch.org/blog/pytorch-2-1/) (through key PrivateUse1), please see the PrivateUse1 tutorial [here](https://pytorch.org/tutorials/advanced/privateuseone.html). # Sp...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Request for Ascend NPU support feature request;stale ### 🚀 The feature, motivation and pitch Please visit: https://github.com/vllm-project/vllm-ascend Thanks again for your trial and feedback that made the fi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fit users who have access to these devices, enabling faster and more efficient computations. # Reference Materials Ascend is a full-stack AI computing infrastructure for industry applications and services based on Huawe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nd.com/en/). [CANN](https://www.hiascend.com/en/software/cann) (Compute Architecture of Neural Networks), developped by Huawei, is a heterogeneous computing architecture for AI. Pytorch has officially announced [support...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: and services based on Huawei Ascend processors and software. For more information about Ascend, see [Ascend Community](https://www.hiascend.com/en/). [CANN](https://www.hiascend.com/en/software/cann) (Compute Architectu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
