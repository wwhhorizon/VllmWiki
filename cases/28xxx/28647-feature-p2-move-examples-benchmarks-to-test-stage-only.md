# vllm-project/vllm#28647: [Feature][P2]:  Move Examples/Benchmarks to Test Stage Only

| 字段 | 值 |
| --- | --- |
| Issue | [#28647](https://github.com/vllm-project/vllm/issues/28647) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P2]:  Move Examples/Benchmarks to Test Stage Only

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description The `examples/` and `benchmarks/` directories (~300MB combined) are copied into all images, including production images where they're not needed. These should only be present in test images. ### What You'll Do 1. Analyze which stages actually need examples/benchmarks 2. Remove COPY commands from vllm-base stage 3. Add COPY commands only to test stage 4. Verify production images still work 5. Use `COPY --link` for better caching ### Deliverables - [ ] Modified Dockerfile with conditional examples copying - [ ] Examples only in test stage - [ ] Production image size reduced - [ ] All tests still pass ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ature][P2]: Move Examples/Benchmarks to Test Stage Only feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description The `examples/` and `benchmarks/` directories (~300MB combined) are copied i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][P2]: Move Examples/Benchmarks to Test Stage Only feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description The `examples/` and `benchmarks/` directories (~300MB combined) are copie...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature][P2]: Move Examples/Benchmarks to Test Stage Only feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description The `examples/` and `benchmarks/` directories (~300MB combined) are copie...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
