# vllm-project/vllm#6616: [Feature]: Support DeepSeek-V2 - MI300x

| 字段 | 值 |
| --- | --- |
| Issue | [#6616](https://github.com/vllm-project/vllm/issues/6616) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support DeepSeek-V2 - MI300x

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Actually seems the last version of rocm-vllm doesn't support deepseek-ai/DeepSeek-V2-Chat-0628, vllm crash trying to load it. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Support DeepSeek-V2 - MI300x feature request;stale ### 🚀 The feature, motivation and pitch Actually seems the last version of rocm-vllm doesn't support deepseek-ai/DeepSeek-V2-Chat-0628, vllm crash trying to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support DeepSeek-V2 - MI300x feature request;stale ### 🚀 The feature, motivation and pitch Actually seems the last version of rocm-vllm doesn't support deepseek-ai/DeepSeek-V2-Chat-0628, vllm crash trying to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t;stale ### 🚀 The feature, motivation and pitch Actually seems the last version of rocm-vllm doesn't support deepseek-ai/DeepSeek-V2-Chat-0628, vllm crash trying to load it. ### Alternatives _No response_ ### Additional...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
