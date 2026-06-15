# vllm-project/vllm#28655: [Feature][P2]: Investigate Lazy Image Pull with Stargz/Nydus Snapshotters

| 字段 | 值 |
| --- | --- |
| Issue | [#28655](https://github.com/vllm-project/vllm/issues/28655) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P2]: Investigate Lazy Image Pull with Stargz/Nydus Snapshotters

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Docker pulls entire images before starting containers, which can take several minutes for large images (30GB). Lazy pulling technologies like stargz-snapshotter and nydus-snapshotter allow containers to start immediately by pulling only the layers needed for startup, fetching remaining layers on-demand in the background. This could significantly reduce the time between "docker run" and container actually starting, especially beneficial for test containers. ### What You'll Do 1. **Research Phase**: - Deep dive into stargz-snapshotter and nydus-snapshotter architectures - Compare performance characteristics, maturity, and maintenance status - Analyze compatibility with current setup (Docker/containerd, BuildKit) - Document security implications and production readiness - Check if vLLM's workload patterns benefit from lazy pull 2. **POC Phase** : - Set up test environment with containerd + snapshotter - Convert vLLM test image to stargz/nydus format - Benchmark startup times: traditional pull vs lazy pull - Measure actual layer access patterns during test runs - Evaluate complexity vs benefit tradeoff 3. **Decision & Documentati...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vestigate Lazy Image Pull with Stargz/Nydus Snapshotters feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Docker pulls entire images before starting containers, which can take sever...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: "docker run" and container actually starting, especially beneficial for test containers. ### What You'll Do 1. **Research Phase**: - Deep dive into stargz-snapshotter and nydus-snapshotter architectures - Compare perfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: especially beneficial for test containers. ### What You'll Do 1. **Research Phase**: - Deep dive into stargz-snapshotter and nydus-snapshotter architectures - Compare performance characteristics, maturity, and maintenan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [P2]: Investigate Lazy Image Pull with Stargz/Nydus Snapshotters feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Docker pulls entire images before starting containers, which can ta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: th containerd + snapshotter - Convert vLLM test image to stargz/nydus format - Benchmark startup times: traditional pull vs lazy pull - Measure actual layer access patterns during test runs - Evaluate complexity vs bene...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
