# vllm-project/vllm#4017: [Installation]: Any plans on providing vLLM pre-compiled for ROCm?

| 字段 | 值 |
| --- | --- |
| Issue | [#4017](https://github.com/vllm-project/vllm/issues/4017) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Any plans on providing vLLM pre-compiled for ROCm?

### Issue 正文摘录

Hi, are there any plans to provide vLLM releases that are pre-compiled for AMD GPUs? ### How you are installing vllm https://docs.vllm.ai/en/latest/getting_started/amd-installation.html

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: Any plans on providing vLLM pre-compiled for ROCm? installation;stale Hi, are there any plans to provide vLLM releases that are pre-compiled for AMD GPUs? ### How you are installing vllm https://docs.vll
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: Any plans on providing vLLM pre-compiled for ROCm? installation;stale Hi, are there any plans to provide vLLM releases that are pre-compiled for AMD GPUs? ### How you are installing vllm https://docs.vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lation]: Any plans on providing vLLM pre-compiled for ROCm? installation;stale Hi, are there any plans to provide vLLM releases that are pre-compiled for AMD GPUs? ### How you are installing vllm https://docs.vllm.ai/en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: or AMD GPUs? ### How you are installing vllm https://docs.vllm.ai/en/latest/getting_started/amd-installation.html

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
