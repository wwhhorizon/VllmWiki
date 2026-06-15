# vllm-project/vllm#6728: [Feature]: vllm support for Ascend NPU

| 字段 | 值 |
| --- | --- |
| Issue | [#6728](https://github.com/vllm-project/vllm/issues/6728) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm support for Ascend NPU

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Due to its powerful computing capabilities, Ascend NPU is currently used by many customers. We hope that vLLM can run smoothly on Ascend NPU, thereby serving more users. We have also completed the adaptation of vLLM's v0.4.2 version on Ascend NPU hardware. The adapted Ascend-vLLM demonstrates good performance in terms of ease of use and high performance. Now we plan to contribute the code to the vLLM project. Additionally, we welcome everyone to participate in the joint construction and collaboratively build the framework capabilities for large models on Ascend NPU. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rving more users. We have also completed the adaptation of vLLM's v0.4.2 version on Ascend NPU hardware. The adapted Ascend-vLLM demonstrates good performance in terms of ease of use and high performance. Now we plan to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: vllm support for Ascend NPU feature request;stale ### 🚀 The feature, motivation and pitch Due to its powerful computing capabilities, Ascend NPU is currently used by many customers. We hope that vLLM can run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: scend NPU is currently used by many customers. We hope that vLLM can run smoothly on Ascend NPU, thereby serving more users. We have also completed the adaptation of vLLM's v0.4.2 version on Ascend NPU hardware. The ada...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: struction and collaboratively build the framework capabilities for large models on Ascend NPU. ### Alternatives _No response_ ### Additional context _No response_

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
