# vllm-project/vllm#1376: Telemetry Support

| 字段 | 值 |
| --- | --- |
| Issue | [#1376](https://github.com/vllm-project/vllm/issues/1376) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Telemetry Support

### Issue 正文摘录

We should add telemetry for collecting anonymized information to inform project roadmap. Currently, we are unsure about the following: - The types of hardware, specifically GPU types. - The relevant performance counters (latency, memory usage) and effectiveness of PagedAttention Kernel. - The cloud providers vLLM is running on. - The type of architecture and models users are using. The lack of such visibility and signals harms our prioritization. We are a small team with very little resource; therefore, we want whatever we focus on to be most impactful. The telemetry would be on by default for CLI and Docker usage. It can be opt-out easily using environment variable/config switches. For library usage (`import vllm`), I think it would be trickier but we can experiment with turning it on. Whatever data we collect and the resulting dashboard will be publicly visible.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: urrently, we are unsure about the following: - The types of hardware, specifically GPU types. - The relevant performance counters (latency, memory usage) and effectiveness of PagedAttention Kernel. - The cloud providers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Telemetry Support We should add telemetry for collecting anonymized information to inform project roadmap. Currently, we are unsure about the following: - The types of hardware, specifically GPU types. - The relevant pe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ention Kernel. - The cloud providers vLLM is running on. - The type of architecture and models users are using. The lack of such visibility and signals harms our prioritization. We are a small team with very little reso...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: f hardware, specifically GPU types. - The relevant performance counters (latency, memory usage) and effectiveness of PagedAttention Kernel. - The cloud providers vLLM is running on. - The type of architecture and models...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
