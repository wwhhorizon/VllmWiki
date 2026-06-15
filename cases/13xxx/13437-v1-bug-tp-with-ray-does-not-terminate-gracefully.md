# vllm-project/vllm#13437: [V1][Bug]: TP with Ray does not terminate gracefully

| 字段 | 值 |
| --- | --- |
| Issue | [#13437](https://github.com/vllm-project/vllm/issues/13437) |
| 状态 | closed |
| 标签 | bug;ray;v1 |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [V1][Bug]: TP with Ray does not terminate gracefully

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using Ray as the distributed executor backend and using the `LLM` Python API , the main process does not terminate gracefully: ``` *** SIGTERM received at time=1739834838 on cpu 88 *** PC: @ 0x7fe108d1f117 (unknown) (unknown) @ 0x7fe108cd0520 (unknown) (unknown) [2025-02-17 15:27:18,341 E 2669821 2669821] logging.cc:460: *** SIGTERM received at time=1739834838 on cpu 88 *** [2025-02-17 15:27:18,341 E 2669821 2669821] logging.cc:460: PC: @ 0x7fe108d1f117 (unknown) (unknown) [2025-02-17 15:27:18,341 E 2669821 2669821] logging.cc:460: @ 0x7fe108cd0520 (unknown) (unknown) 2025-02-17 15:27:18,342 INFO compiled_dag_node.py:1867 -- Tearing down compiled DAG 2025-02-17 15:27:18,342 INFO compiled_dag_node.py:1872 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, a1dcab214fac9e464505ef2701000000) 2025-02-17 15:27:18,342 INFO compiled_dag_node.py:1872 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, fad8cccd5652d08fb1c696bb01000000) 2025-02-17 15:27:18,342 INFO compiled_dag_node.py:1872 -- Cancelling compiled worker on actor: Actor(RayWorkerWrapper, 37fc4010a9fc8557c83a042201000000) 2025-02-17 15:27:18,342...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t ### 🐛 Describe the bug When using Ray as the distributed executor backend and using the `LLM` Python API , the main process does not terminate gracefully: ``` *** SIGTERM received at time=1739834838 on cpu 88 *** PC:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: @ 0x7fe108cd0520 (unknown) (unknown) 2025-02-17 15:27:18,342 INFO compiled_dag_node.py:1867 -- Tearing down compiled DAG 2025-02-17 15:27:18,342 INFO compiled_dag_node.py:1872 -- Cancelling compiled worker on actor: Act...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 5ef2701000000) 2025-02-17 15:27:19,080 INFO compiled_dag_node.py:1892 -- Waiting for worker tasks to exit 2025-02-17 15:27:19,080 INFO compiled_dag_node.py:1894 -- Teardown complete ``` ### Before submitting a new issue...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
