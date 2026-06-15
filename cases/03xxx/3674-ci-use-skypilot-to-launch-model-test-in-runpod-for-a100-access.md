# vllm-project/vllm#3674: [CI] Use Skypilot to launch model test in runpod for A100 access

| 字段 | 值 |
| --- | --- |
| Issue | [#3674](https://github.com/vllm-project/vllm/issues/3674) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] Use Skypilot to launch model test in runpod for A100 access

### Issue 正文摘录

### Anything you want to discuss about vllm. Current we do not run model test on A100 machine because we can't get any capacity in GCP. https://skypilot.readthedocs.io/ supports runpod and we happen to have account there. This task requires some infra fiddling but to start, demonstrating a way to use skypilot to run the test container images (they are public) would be useful.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI] Use Skypilot to launch model test in runpod for A100 access stale ### Anything you want to discuss about vllm. Current we do not run model test on A100 machine because we can't get any capacity in GCP. https://skypi
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI] Use Skypilot to launch model test in runpod for A100 access stale ### Anything you want to discuss about vllm. Current we do not run model test on A100 machine because we can't get any capacity in GCP. https://skyp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [CI] Use Skypilot to launch model test in runpod for A100 access stale ### Anything you want to discuss about vllm. Current we do not run model test on A100 machine because we can't get any capacity in GCP. https://skyp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI] Use Skypilot to launch model test in runpod for A100 access stale ### Anything you want to discuss about vllm. Current we do not run model test on A100 machine because we can't get any capacity in GCP. https://skyp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI] Use Skypilot to launch model test in runpod for A100 access stale ### Anything you want to discuss about vllm. Current we do not run model test on A100 machine because we can't get any capacity in GCP. https://skyp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
