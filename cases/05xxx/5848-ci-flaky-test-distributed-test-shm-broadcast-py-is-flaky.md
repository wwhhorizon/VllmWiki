# vllm-project/vllm#5848: [CI] [Flaky test] distributed/test_shm_broadcast.py is flaky

| 字段 | 值 |
| --- | --- |
| Issue | [#5848](https://github.com/vllm-project/vllm/issues/5848) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] [Flaky test] distributed/test_shm_broadcast.py is flaky

### Issue 正文摘录

### Anything you want to discuss about vllm. Distributed comm ops test failed with below stacktrace. [Buildkite](https://buildkite.com/vllm/ci-aws/builds/2539#01904f5d-0bfd-4a7a-96b2-cdc7f8b60b09) ``` [2024-06-25T12:58:33Z] distributed/test_shm_broadcast.py:72: -- | [2024-06-25T12:58:33Z] _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ | [2024-06-25T12:58:33Z] | [2024-06-25T12:58:33Z] fn = .wrapped_fn at 0x7f8cc92afa30> | [2024-06-25T12:58:33Z] world_size = 4 | [2024-06-25T12:58:33Z] | [2024-06-25T12:58:33Z] def distributed_run(fn, world_size): | [2024-06-25T12:58:33Z] number_of_processes = world_size | [2024-06-25T12:58:33Z] processes = [] | [2024-06-25T12:58:33Z] for i in range(number_of_processes): | [2024-06-25T12:58:33Z] env = {} | [2024-06-25T12:58:33Z] env['RANK'] = str(i) | [2024-06-25T12:58:33Z] env['LOCAL_RANK'] = str(i) | [2024-06-25T12:58:33Z] env['WORLD_SIZE'] = str(number_of_processes) | [2024-06-25T12:58:33Z] env['LOCAL_WORLD_SIZE'] = str(number_of_processes) | [2024-06-25T12:58:33Z] env['MASTER_ADDR'] = 'localhost' | [2024-06-25T12:58:33Z] env['MASTER_PORT'] = '12345' | [2024-06-25T12:58:33Z] p = multiprocessing.Process(target=fn, ar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] [Flaky test] distributed/test_shm_broadcast.py is flaky ### Anything you want to discuss about vllm. Distributed comm ops test failed with below stacktrace. [Buildkite](https://buildkite.com/vllm/ci-aws/builds/2539#
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -25T12:58:33Z] | [2024-06-25T12:58:33Z] fn = .wrapped_fn at 0x7f8cc92afa30> | [2024-06-25T12:58:33Z] world_size = 4 | [2024-06-25T12:58:33Z] | [2024-06-25T12:58:33Z] def distributed_run(fn, world_size): | [2024-06-25T12...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI] [Flaky test] distributed/test_shm_broadcast.py is flaky ### Anything you want to discuss about vllm. Distributed comm ops test failed with below stacktrace. [Buildkite](https://buildkite.com/vllm/ci-aws/builds/2539...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
