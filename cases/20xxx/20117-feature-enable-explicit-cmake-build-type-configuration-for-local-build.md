# vllm-project/vllm#20117: [Feature]: Enable explicit CMAKE_BUILD_TYPE configuration for local builds

| 字段 | 值 |
| --- | --- |
| Issue | [#20117](https://github.com/vllm-project/vllm/issues/20117) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Enable explicit CMAKE_BUILD_TYPE configuration for local builds

### Issue 正文摘录

### 🚀 The feature, motivation and pitch To improve the developer experience, it would be beneficial to have a more straightforward way to create a `Release` build locally. This would allow contributors to easily check the final wheel artifact size without the dependency on a properly configured SCCACHE. This need was discovered while working on PR #19794. I encountered SCCACHE authentication errors and, not immediately knowing the correct configuration flags (`SCCACHE_S3_NO_CREDENTIALS=1`), was unable to produce a `Release` build. This led to the realization that my local builds were not `Release` by default, explaining the unexpectedly large wheel sizes. This experience highlights how the current build process can be confusing for new contributors. When adding new features, it's crucial to verify that changes don't cause the wheel size to exceed PyPI's limitations *before* opening a pull request. Decoupling the build type from SCCACHE would solve this. A proposed implementation is as follows: ```diff diff --git a/docker/Dockerfile b/docker/Dockerfile index 8d4375470..ae866edd0 100644 --- a/docker/Dockerfile +++ b/docker/Dockerfile @@ -112,6 +112,7 @@ ENV MAX_JOBS=${max_jobs} ARG...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Feature]: Enable explicit CMAKE_BUILD_TYPE configuration for local builds feature request;stale ### 🚀 The feature, motivation and pitch To improve the developer experience, it would be beneficial to have a more straigh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: edentials and unnecessarily couples the build type to the caching mechanism, which can be a point of friction for contributors. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Enable explicit CMAKE_BUILD_TYPE configuration for local builds feature request;stale ### 🚀 The feature, motivation and pitch To improve the developer experience, it would be beneficial to have a more straightforward wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Enable explicit CMAKE_BUILD_TYPE configuration for local builds feature request;stale ### 🚀 The feature, motivation and pitch To improve the developer experience, it would be beneficial to have a more straigh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
