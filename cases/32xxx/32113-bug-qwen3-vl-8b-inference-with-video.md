# vllm-project/vllm#32113: [Bug]: Qwen3-VL-8B inference with video

| 字段 | 值 |
| --- | --- |
| Issue | [#32113](https://github.com/vllm-project/vllm/issues/32113) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-8B inference with video

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Which parameter can affect the number of control tokens when using vllm for reasoning? When I run the following command, I keep getting an error at 256 frames： [1;36m(Worker_TP3 pid=255093)[0;0m ERROR 01-11 09:43:23 [v1/executor/multiproc_executor.py:671] WorkerProc hit an exception. [1;36m(Worker_TP3 pid=255093)[0;0m ERROR 01-11 09:43:23 [v1/executor/multiproc_executor.py:671] Traceback (most recent call last): [1;36m(Worker_TP3 pid=255093)[0;0m ERROR 01-11 09:43:23 [v1/executor/multiproc_executor.py:671] File "/remote-home/zhangkc/lmms-eval/.venv/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop [1;36m(Worker_TP3 pid=255093)[0;0m ERROR 01-11 09:43:23 [v1/executor/multiproc_executor.py:671] output = func(*args, **kwargs) [1;36m(Worker_TP3 pid=255093)[0;0m ERROR 01-11 09:43:23 [v1/executor/multiproc_executor.py:671] File "/remote-home/zhangkc/lmms-eval/.venv/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context [1;36m(Worker_TP3 pid=255093)[0;0m ERROR 01-11 09:43:23 [v1/executor/multiproc_executor.py:671] return func(*args, **kwargs) ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL-8B inference with video bug;stale ### Your current environment ### 🐛 Describe the bug Which parameter can affect the number of control tokens when using vllm for reasoning? When I run the following comma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen3-VL-8B inference with video bug;stale ### Your current environment ### 🐛 Describe the bug Which parameter can affect the number of control tokens when using vllm for reasoning? When I run the following comma...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: v1/executor/multiproc_executor.py:671] File "/remote-home/zhangkc/lmms-eval/.venv/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop [1;36m(Worker_TP3 pid=255093)[0;0m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: " ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
