# vllm-project/vllm#17276: [Bug]: nightly version:  EngineCore encountered a fatal error.

| 字段 | 值 |
| --- | --- |
| Issue | [#17276](https://github.com/vllm-project/vllm/issues/17276) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: nightly version:  EngineCore encountered a fatal error.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-VL-3B-Instruct ``` INFO 04-28 02:37:03 [async_llm.py:252] Added request 13_chatcmpl-c78d39a6d1d8469f90f3bda9bd41ca6a. INFO 04-28 02:37:03 [async_llm.py:252] Added request 14_chatcmpl-c78d39a6d1d8469f90f3bda9bd41ca6a. INFO 04-28 02:37:03 [async_llm.py:252] Added request 15_chatcmpl-c78d39a6d1d8469f90f3bda9bd41ca6a. ERROR 04-28 02:37:03 [core.py:398] EngineCore encountered a fatal error. ERROR 04-28 02:37:03 [core.py:398] Traceback (most recent call last): ERROR 04-28 02:37:03 [core.py:398] File "/home/zhiyuan/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 389, in run_engine_core ERROR 04-28 02:37:03 [core.py:398] engine_core.run_busy_loop() ERROR 04-28 02:37:03 [core.py:398] File "/home/zhiyuan/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 413, in run_busy_loop ERROR 04-28 02:37:03 [core.py:398] self._process_engine_step() ERROR 04-28 02:37:03 [core.py:398] File "/home/zhiyuan/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 438, in _process_engine_step ERROR 04-28 02:37:03 [core.py:398] outputs = self.step_fn() E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug ### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-VL-3B-Instruct ``` INFO 04-28 02:37:03 [async_llm.py:252] Added request 13_chatcmpl-c78d39a6d1d8469f90f3bda9bd41ca6a.
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: iyuan/anaconda3/envs/vllm/lib/python3.12/site-packages/vllm/v1/attention/backends/flash_attn.py", line 598, in forward ERROR 04-28 02:37:03 [core.py:398] cascade_attention( ERROR 04-28 02:37:03 [core.py:398] File "/home...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e_attention ERROR 04-28 02:37:03 [core.py:398] prefix_output, prefix_lse = flash_attn_varlen_func( ERROR 04-28 02:37:03 [core.py:398] ^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-28 02:37:03 [core.py:398] File "/home/zhiyuan/anacon...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: /Qwen2.5-VL-3B-Instruct ``` INFO 04-28 02:37:03 [async_llm.py:252] Added request 13_chatcmpl-c78d39a6d1d8469f90f3bda9bd41ca6a. INFO 04-28 02:37:03 [async_
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e/zhiyuan/anaconda3/envs/vllm/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 745, in _fn ERROR 04-28 02:37:03 [core.py:398] return fn(*args, **kwargs) ERROR 04-28 02:37:03 [core.py:398] ^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
