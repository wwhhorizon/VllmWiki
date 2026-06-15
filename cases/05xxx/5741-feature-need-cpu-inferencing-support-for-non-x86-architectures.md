# vllm-project/vllm#5741: [Feature]: Need CPU inferencing support for non-x86 architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#5741](https://github.com/vllm-project/vllm/issues/5741) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Need CPU inferencing support for non-x86 architectures

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have a need for vLLM to support CPU inferencing for the PowerPC architecture. This project should start thinking about non-x86 platforms. [Initial PowerPC CPU support](https://github.com/vllm-project/vllm/pull/5652) ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Need CPU inferencing support for non-x86 architectures feature request;stale ### 🚀 The feature, motivation and pitch We have a need for vLLM to support CPU inferencing for the PowerPC architecture. This projec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Need CPU inferencing support for non-x86 architectures feature request;stale ### 🚀 The feature, motivation and pitch We have a need for vLLM to support CPU inferencing for the PowerPC architecture. This proje...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Need CPU inferencing support for non-x86 architectures feature request;stale ### 🚀 The feature, motivation and pitch We have a need for vLLM to support CPU inferencing for the PowerPC architecture. This proje...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
