# vllm-project/vllm#8204: [Bug]: [Errno 98] error while attempting to bind on address ('0.0.0.0', 8000): address already in use

| 字段 | 值 |
| --- | --- |
| Issue | [#8204](https://github.com/vllm-project/vllm/issues/8204) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [Errno 98] error while attempting to bind on address ('0.0.0.0', 8000): address already in use

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a bug we encounter a lot in our ci, e.g. https://buildkite.com/vllm/ci-aws/builds/8098#0191bf43-446d-411d-80c7-3ba10bc392e8/192-1557 I have been tracking this for months, and try to add more logging information to help debugging. from the logging information: > [2024-09-05T00:38:34Z] INFO: Started server process [60858] > -- > | [2024-09-05T00:38:34Z] INFO: Waiting for application startup. > | [2024-09-05T00:38:34Z] INFO: Application startup complete. > | [2024-09-05T00:38:34Z] ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 44319): [errno 98] address already in use > | [2024-09-05T00:38:34Z] INFO: Waiting for application shutdown. > | [2024-09-05T00:38:34Z] INFO: Application shutdown complete. > | [2024-09-05T00:38:34Z] DEBUG 09-04 17:38:34 launcher.py:64] port 44319 is used by process psutil.Process(pid=60914, name='pt_main_thread', status='sleeping', started='17:37:05') launched with command: > | [2024-09-05T00:38:34Z] DEBUG 09-04 17:38:34 launcher.py:64] /usr/bin/python3 -c from multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=16, pipe_handle=18) --multiprocessing-fork > > we can...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ment ### 🐛 Describe the bug This is a bug we encounter a lot in our ci, e.g. https://buildkite.com/vllm/ci-aws/builds/8098#0191bf43-446d-411d-80c7-3ba10bc392e8/192-1557 I have been tracking this for months, and try to a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: arted server process [60858] > -- > | [2024-09-05T00:38:34Z] INFO: Waiting for application startup. > | [2024-09-05T00:38:34Z] INFO: Application startup complete. > | [2024-09-05T00:38:34Z] ERROR: [Errno 98] error while...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ay. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 557 I have been tracking this for months, and try to add more logging information to help debugging. from the logging information: > [2024-09-05T00:38:34Z] INFO: Started server process [60858] > -- > | [2024-09-05T00:38...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
