# vllm-project/vllm#15470: [Bug]: Qwen2 MoE inference is super slow

| 字段 | 值 |
| --- | --- |
| Issue | [#15470](https://github.com/vllm-project/vllm/issues/15470) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2 MoE inference is super slow

### Issue 正文摘录

### Your current environment vllm version 0.8.1 ray version 2.44.0 protobuf version 6.30.1 ### 🐛 Describe the bug When running Qwen 2 MoE on vllm using tp 8 pp 2 and AsyncLLM, this inference speed is super slow, more than 20h on 10k data (<8k seq len). When switching on VLLM_USE_V1, there is an error: ``` Exception in thread ray_print_logs: Traceback (most recent call last): File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner self.run() File "/usr/lib/python3.10/threading.py", line 953, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.10/dist-packages/ray/_private/worker.py", line 967, in print_logs data = subscriber.poll() File "python/ray/_raylet.pyx", line 2914, in ray._raylet.GcsLogSubscriber.poll File "python/ray/includes/common.pxi", line 108, in ray._raylet.check_status ray.exceptions.RaySystemError: System error: Missing :authority header Exception in thread ray_listen_error_messages: Traceback (most recent call last): File "/usr/lib/python3.10/threading.py", line 1016, in _bootstrap_inner self.run() File "/usr/lib/python3.10/threading.py", line 953, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/pytho...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: inference is super slow bug;ray;stale ### Your current environment vllm version 0.8.1 ray version 2.44.0 protobuf version 6.30.1 ### 🐛 Describe the bug When running Qwen 2 MoE on vllm using tp 8 pp 2 and AsyncLLM, this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen2 MoE inference is super slow bug;ray;stale ### Your current environment vllm version 0.8.1 ray version 2.44.0 protobuf version 6.30.1 ### 🐛 Describe the bug When running Qwen 2 MoE on vllm using tp 8 pp 2 an...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Qwen2 MoE inference is super slow bug;ray;stale ### Your current environment vllm version 0.8.1 ray version 2.44.0 protobuf version 6.30.1 ### 🐛 Describe the bug When running Qwen 2 MoE on vllm using tp 8 pp 2 an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen2 MoE inference is super slow bug;ray;stale ### Your current environment vllm version 0.8.1 ray version 2.44.0 protobuf version 6.30.1 ### 🐛 Describe the bug When running Qwen 2 MoE on vllm using tp 8 pp 2 an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
