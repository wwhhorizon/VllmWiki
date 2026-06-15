# vllm-project/vllm#42761: [Bug]: kv_cache_offloadig crashes on 0.21.0 - KeyError in self._block_id_to_pending_jobs[bid]

| 字段 | 值 |
| --- | --- |
| Issue | [#42761](https://github.com/vllm-project/vllm/issues/42761) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kv_cache_offloadig crashes on 0.21.0 - KeyError in self._block_id_to_pending_jobs[bid]

### Issue 正文摘录

### Your current environment I did set "--kv-offloading-size" "300" with the versio 0.21.0. It was running for a few requests but at some point crashed. ### 🐛 Describe the bug ``` (APIServer pid=1) INFO: 10.1.11.186:35998 - "POST /v1/chat/completions HTTP/1.1" 200 OK (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] EngineCore encountered a fatal error. (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] Traceback (most recent call last): (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1133, in run_engine_core (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] engine_core.run_busy_loop() (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1174, in run_busy_loop (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] self._process_engine_step() (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1213, in _process_engine_step (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] outputs, model_executed = self.step_fn()...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: -offloading-size" "300" with the versio 0.21.0. It was running for a few requests but at some point crashed. ### 🐛 Describe the bug ``` (APIServer pid=1) INFO: 10.1.11.186:35998 - "POST /v1/chat/completions HTTP/1.1" 20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ep (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] outputs, model_executed = self.step_fn() (EngineCore pid=993) ERROR 05-15 16:52:39 [core.py:1142] ^^^^^^^^^^^^^^ (EngineCore pid=993) ERROR 05-15 16:52:39 [cor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: kv_cache_offloadig crashes on 0.21.0 - KeyError in self._block_id_to_pending_jobs[bid] bug ### Your current environment I did set "--kv-offloading-size" "300" with the versio 0.21.0. It was running for a few requ...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: kv_cache_offloadig crashes on 0.21.0 - KeyError in self._block_id_to_pending_jobs[bid] bug ### Your current environment I did set "--kv-offloading-size" "300" with the versio 0.21.0. It was running for a few requ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
