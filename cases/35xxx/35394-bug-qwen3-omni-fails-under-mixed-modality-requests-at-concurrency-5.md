# vllm-project/vllm#35394: [Bug]: Qwen3-Omni Fails Under Mixed-Modality Requests at Concurrency 5

| 字段 | 值 |
| --- | --- |
| Issue | [#35394](https://github.com/vllm-project/vllm/issues/35394) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Omni Fails Under Mixed-Modality Requests at Concurrency 5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug version: vllm 0.16.0 use vllm/examples/offline_inference/qwen3_omni/only_thinker.py , set use_audio_in_video = False and duplicate the same mixed-modality request five times to form a batch. Error: ``` (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] File "/home/cwj/vllm/vllm/v1/engine/core.py", line 999, in run_engine_core^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] engine_core.run_busy_loop()^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] return self.__get_result()^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] ^^^^^^^^^^^^^^^^^^^^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] File "/usr/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] raise self._exception^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] File "/home/cwj/vllm/vllm/v1/executor/uniproc_executor.py", line 79, in collective_rpc^M (EngineCore_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] result = run_method(self.driver_worker, method, args, kwargs)^M (EngineCore_DP0 pid=31...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] RuntimeError: shape mismatch: value tensor of shape [7368, 2048] cannot be broadcast to indexing result of shape [9216, 2048] ``` ### Before submitting a new issue... -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-Omni Fails Under Mixed-Modality Requests at Concurrency 5 bug ### Your current environment ### 🐛 Describe the bug version: vllm 0.16.0 use vllm/examples/offline_inference/qwen3_omni/only_thinker.py , set us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3-Omni Fails Under Mixed-Modality Requests at Concurrency 5 bug ### Your current environment ### 🐛 Describe the bug version: vllm 0.16.0 use vllm/examples/offline_inference/qwen3_omni/only_thinker.py , set us...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e_DP0 pid=31755) ERROR 02-26 05:13:00 [core.py:1008] RuntimeError: shape mismatch: value tensor of shape [7368, 2048] cannot be broadcast to indexing result of shape [9216, 2048] ``` ### Before submitting a new issue......
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ncurrency 5 bug ### Your current environment ### 🐛 Describe the bug version: vllm 0.16.0 use vllm/examples/offline_inference/qwen3_omni/only_thinker.py , set use_audio_in_video = False and duplicate the same mixed-modal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
