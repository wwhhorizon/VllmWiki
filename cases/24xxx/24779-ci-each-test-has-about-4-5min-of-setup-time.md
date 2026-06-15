# vllm-project/vllm#24779: [CI]: Each test has about 4-5min of setup time

| 字段 | 值 |
| --- | --- |
| Issue | [#24779](https://github.com/vllm-project/vllm/issues/24779) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Each test has about 4-5min of setup time

### Issue 正文摘录

As an example, consider the **Basic Models Test (Initialization)** unit test here https://buildkite.com/vllm/fastcheck/builds/41354/steps/canvas?jid=01993996-f4ae-4b6f-8629-c1c70d2283c8 - There are a number of test setup tasks which take only seconds, or even <1sec - However, it takes 3min 14sec to pull the docker container (public.ecr.aws/q9t5s3a7/vllm-ci-test-repo:e3e0bf20b2c0706495a266e1130cd5825fd43253) - The docker container runs for about 7min - The docker container starts at 17:12:05 - The first regression test starts at 17:13:27, 1min 22 sec after the container started So there is about 4.5min from when the CI activates **Basic Models Test (Initialization)**, to when the first pytest regression test actually runs. Besides being a waste of compute resources, this setup time also sets a 4.5min minimum duration for each test. This in turn complicates the task of lowering regression test runtime: the reduction in pytest execution time gained through sharding must be weighed against the cost of the unproductive test setup time, which will be multiplied by the `parallelism` factor (A similar tradeoff will apply to any strategy based on breaking up one test category into N test c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI]: Each test has about 4-5min of setup time feature request;stale As an example, consider the **Basic Models Test (Initialization)** unit test here https://buildkite.com/vllm/fastcheck/builds/41354/steps/canvas?jid=01
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI]: Each test has about 4-5min of setup time feature request;stale As an example, consider the **Basic Models Test (Initialization)** unit test here https://buildkite.com/vllm/fastcheck/builds/41354/steps/canvas?jid=0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI]: Each test has about 4-5min of setup time feature request;stale As an example, consider the **Basic Models Test (Initialization)** unit test here https://buildkite.com/vllm/fastcheck/builds/41354/steps/canvas?jid=0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: unproductive test setup time, which will be multiplied by the `parallelism` factor (A similar tradeoff will apply to any strategy based on breaking up one test category into N test categories.) While I am doubtful that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: of setup time feature request;stale As an example, consider the **Basic Models Test (Initialization)** unit test here https://buildkite.com/vllm/fastcheck/builds/41354/steps/canvas?jid=01993996-f4ae-4b6f-8629-c1c70d2283...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
