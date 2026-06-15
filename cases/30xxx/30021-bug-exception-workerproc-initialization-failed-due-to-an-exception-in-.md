# vllm-project/vllm#30021: [Bug]: Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.

| 字段 | 值 |
| --- | --- |
| Issue | [#30021](https://github.com/vllm-project/vllm/issues/30021) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Exception: WorkerProc initialization failed due to an exception in a background process. See stack trace for root cause.

### Issue 正文摘录

### Your current environment INFO:swift] Successfully registered `/home/dugis/shihaofeng/llm/ms-swift/swift/llm/dataset/data/dataset_info.json`. [INFO:swift] Successfully registered `/home/dugis/shihaofeng/llm/ms-swift/swift/llm/dataset/data/dataset_info.json`. [INFO:swift] Successfully registered `/home/dugis/shihaofeng/llm/ms-swift/swift/llm/dataset/data/dataset_info.json`. [INFO:swift] Successfully registered `/home/dugis/shihaofeng/llm/ms-swift/swift/llm/dataset/data/dataset_info.json`. INFO 12-04 11:31:13 [parallel_state.py:1200] world_size=4 rank=1 local_rank=1 distributed_init_method=tcp://127.0.0.1:41725 backend=nccl INFO 12-04 11:31:13 [parallel_state.py:1200] world_size=4 rank=3 local_rank=3 distributed_init_method=tcp://127.0.0.1:41725 backend=nccl INFO 12-04 11:31:14 [parallel_state.py:1200] world_size=4 rank=0 local_rank=0 distributed_init_method=tcp://127.0.0.1:41725 backend=nccl INFO 12-04 11:31:14 [parallel_state.py:1200] world_size=4 rank=2 local_rank=2 distributed_init_method=tcp://127.0.0.1:41725 backend=nccl INFO 12-04 11:31:14 [pynccl.py:111] vLLM is using nccl==2.27.5 (EngineCore_DP0 pid=16064) ERROR 12-04 11:31:15 [core.py:843] EngineCore failed to start. (E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _ (EngineCore_DP0 pid=16064) ERROR 12-04 11:31:15 [core.py:843] self.model_executor = executor_class(vllm_config) (EngineCore_DP0 pid=16064) ERROR 12-04 11:31:15 [core.py:843] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: size=4 rank=1 local_rank=1 distributed_init_method=tcp://127.0.0.1:41725 backend=nccl INFO 12-04 11:31:13 [parallel_state.py:1200] world_size=4 rank=3 local_rank=3 distributed_init_method=tcp://127.0.0.1:41725 backend=n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n exception in a background process. See stack trace for root cause. bug;stale ### Your current environment INFO:swift] Successfully registered `/home/dugis/shihaofeng/llm/ms-swift/swift/llm/dataset/data/dataset_info.js...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
