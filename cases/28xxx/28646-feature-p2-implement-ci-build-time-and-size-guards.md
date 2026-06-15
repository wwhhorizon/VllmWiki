# vllm-project/vllm#28646: [Feature][P2]:  Implement CI Build Time and Size Guards

| 字段 | 值 |
| --- | --- |
| Issue | [#28646](https://github.com/vllm-project/vllm/issues/28646) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P2]:  Implement CI Build Time and Size Guards

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Once we optimize the Docker build, we need to prevent regressions. Create CI checks that fail if build time exceeds thresholds or if image size grows beyond acceptable limits. Also set up monitoring dashboards. ### What You'll Do 1. Create Python scripts to check image metrics: - `check-image-size.py` (extend existing wheel size checker) - `check-build-time.py` - `check-image-layers.py` 2. Add these checks to CI pipeline after image build 3. Set appropriate thresholds (configurable) 4. Create Buildkite annotations for warnings 5. Set up CloudWatch dashboard for metrics (optional) ### Deliverables - [ ] Python scripts for checking metrics - [ ] Integration into test-template-ci.j2 - [ ] Configurable thresholds via environment variables - [ ] Documentation on how to adjust thresholds - [ ] CloudWatch dashboard (optional) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freque...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature][P2]: Implement CI Build Time and Size Guards feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Once we optimize the Docker build, we need to prevent regressions. Create CI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][P2]: Implement CI Build Time and Size Guards feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Once we optimize the Docker build, we need to prevent regressions. Create CI...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: h ### Description Once we optimize the Docker build, we need to prevent regressions. Create CI checks that fail if build time exceeds thresholds or if image size grows beyond acceptable limits. Also set up monitoring da...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e checks to CI pipeline after image build 3. Set appropriate thresholds (configurable) 4. Create Buildkite annotations for warnings 5. Set up CloudWatch dashboard for metrics (optional) ### Deliverables - [ ] Python scr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
