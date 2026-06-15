# vllm-project/vllm#3557: [Bug]: Using `pytest --forked` when CUDA is not generally fork-safe

| 字段 | 值 |
| --- | --- |
| Issue | [#3557](https://github.com/vllm-project/vllm/issues/3557) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using `pytest --forked` when CUDA is not generally fork-safe

### Issue 正文摘录

### Your current environment The environment vLLM uses to CI test a PR. ### 🐛 Describe the bug Multiple tests for [my pull request](https://github.com/vllm-project/vllm/pull/3476) are failing due to `pytest --forked` trying to fork new child processes during testing, trying to re-initialize the CUDA context. I'm not sure how other PRs are passing these tests, but I don't know why `pytest --forked` is explicitly being used when CUDA isn't fork-safe. This is fine as long as `conftest.py` doesn't ever initialize CUDA before forking, but this may be difficult to maintain and may be a cause of some sneaky bugs, like from #3487

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fork-safe bug ### Your current environment The environment vLLM uses to CI test a PR. ### 🐛 Describe the bug Multiple tests for [my pull request](https://github.com/vllm-project/vllm/pull/3476) are failing due to `pytes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: Using `pytest --forked` when CUDA is not generally fork-safe bug ### Your current environment The environment vLLM uses to CI test a PR. ### 🐛 Describe the bug Multiple tests for [my pull request](https://github....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: es to CI test a PR. ### 🐛 Describe the bug Multiple tests for [my pull request](https://github.com/vllm-project/vllm/pull/3476) are failing due to `pytest --forked` trying to fork new child processes during testing, try...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Using `pytest --forked` when CUDA is not generally fork-safe bug ### Your current environment The environment vLLM uses to CI test a PR. ### 🐛 Describe the bug Multiple tests for [my pull request](https://github....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
