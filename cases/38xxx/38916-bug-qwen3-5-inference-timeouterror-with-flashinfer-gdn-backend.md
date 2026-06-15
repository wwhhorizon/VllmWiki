# vllm-project/vllm#38916: [Bug]: Qwen3.5 Inference TimeoutError with flashinfer gdn backend

| 字段 | 值 |
| --- | --- |
| Issue | [#38916](https://github.com/vllm-project/vllm/issues/38916) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 Inference TimeoutError with flashinfer gdn backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We got TimeoutError when running Qwen3.5 model. See the error log below. We found this could be resolved by setting `--gdn-prefill-backend triton`. However, since flashinfer is supposed to be faster, it would be great if this can be fixed. ``` (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py:1101] Traceback (most recent call last): (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py:1101] File "/usr/local/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 376, in get_response (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py:1101] status, result = mq.dequeue(timeout=dequeue_timeout) (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py:1101] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py:1101] File "/usr/local/lib/python3.12/site-packages/vllm/distributed/device_communicators/shm_broadcast.py", line 755, in dequeue (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py:1101] with self.acquire_read(timeout, indefinite) as buf: (EngineCore pid=2906234) ERROR 04-01 22:27:40 [v1/engine/core.py...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Qwen3.5 Inference TimeoutError with flashinfer gdn backend bug ### Your current environment ### 🐛 Describe the bug We got TimeoutError when running Qwen3.5 model. See the error log below. We found this could be r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5 Inference TimeoutError with flashinfer gdn backend bug ### Your current environment ### 🐛 Describe the bug We got TimeoutError when running Qwen3.5 model. See the error log below. We found this could be r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the error log below. We found this could be resolved by setting `--gdn-prefill-backend triton`. However, since flashinfer is supposed to be faster, it would be great if this can be fixed. ``` (EngineCore pid=2906234) ER...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
