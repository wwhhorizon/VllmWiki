# vllm-project/vllm#27858: [Bug]: potential inconsistencies in shared memory due to lack of memory ordering guarantees

| 字段 | 值 |
| --- | --- |
| Issue | [#27858](https://github.com/vllm-project/vllm/issues/27858) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: potential inconsistencies in shared memory due to lack of memory ordering guarantees

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While running different models (including Qwen3-32B and DeepSeek-R1, etc.), we encountered several errors about deserialization. These errors appeared in various forms, but most of them pointed to `pickle.loads(buf[1:])`: 1. `AttributeError: 'int' object has no attribute 'append'` ```text (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] EngineCore encountered a fatal error. (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] Traceback (most recent call last): (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] File "*****/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 711, in run_engine_core (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] engine_core.run_busy_loop() (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] File "*****/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 738, in run_busy_loop (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] self._process_engine_step() (EngineCore_DP0 pid=929792) ERROR 09-26 17:27:45 [core.py:720] File "*****/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 769, in _process_engine_step...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: tencies in shared memory due to lack of memory ordering guarantees bug;unstale ### Your current environment ### 🐛 Describe the bug While running different models (including Qwen3-32B and DeepSeek-R1, etc.), we encounter...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: potential inconsistencies in shared memory due to lack of memory ordering guarantees bug;unstale ### Your current environment ### 🐛 Describe the bug While running different models (including Qwen3-32B and DeepSee...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n_warning = 1 while True: with self.buffer.get_metadata(self.current_idx) as metadata_buffer: read_count = sum(metadata_buffer[1:]) written_flag = metadata_buffer[0] if written_flag and read_count != self.buffer.n_reade
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: current environment ### 🐛 Describe the bug While running different models (including Qwen3-32B and DeepSeek-R1, etc.), we encountered several errors about deserialization. These errors appeared in various forms, but mos...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is synchronized across processes (or say cpus). Otherwise, for some cpu architectures with weak memory ordering, `metadata_buffer[0] = 1` may be observed by readers **BUT** `buf` is not ready completely. Therefore, new...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
