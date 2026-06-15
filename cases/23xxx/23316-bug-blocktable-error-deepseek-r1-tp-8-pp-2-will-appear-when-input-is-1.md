# vllm-project/vllm#23316: [Bug]: [BlockTable error] DeepSeek R1 (TP=8, PP=2) will appear when input is 16k and concurrent 128

| 字段 | 值 |
| --- | --- |
| Issue | [#23316](https://github.com/vllm-project/vllm/issues/23316) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [BlockTable error] DeepSeek R1 (TP=8, PP=2) will appear when input is 16k and concurrent 128

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```txt ERROR 08-21 03:43:01 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=65, num_waiting_reqs=35, kv_cache_usage=0.9860497558707277, prefix_cache_stats=PrefixCacheStats(reset=False, requests=0, queries=0, hits=0), spec_decoding_stats=None, num_corrupted_reqs=0) ERROR 08-21 03:43:01 [core.py:634] EngineCore encountered a fatal error. ERROR 08-21 03:43:01 [core.py:634] Traceback (most recent call last): ERROR 08-21 03:43:01 [core.py:634] File "/home/oppoer/.local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 625, in run_engine_core ERROR 08-21 03:43:01 [core.py:634] engine_core.run_busy_loop() ERROR 08-21 03:43:01 [core.py:634] File "/home/oppoer/.local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 652, in run_busy_loop ERROR 08-21 03:43:01 [core.py:634] self._process_engine_step() ERROR 08-21 03:43:01 [core.py:634] File "/home/oppoer/.local/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 677, in _process_engine_step ERROR 08-21 03:43:01 [core.py:634] outputs, model_executed = self.step_fn() ERROR 08-21 03:43:01 [core.py:634] File "/home/oppoer/.local/lib/python3.1...

## 现有链接修复摘要

#26661 [Bugfix][Core]Fix block table out-of-range issue in priority scheduling

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: File "/home/oppoer/.local/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 150, in get ERROR 08-21 03:43:01 [core.py:634] return _process_return_vals(return_vals, True) ERROR 08-21 03:43:01 [core...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Describe the bug ```txt ERROR 08-21 03:43:01 [dump_input.py:79] Dumping scheduler stats: SchedulerStats(num_running_reqs=65, num_waiting_reqs=35, kv_cache_usage=0.9860497558707277, prefix_cache_stats=PrefixCacheStats(re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: [BlockTable error] DeepSeek R1 (TP=8, PP=2) will appear when input is 16k and concurrent 128 bug ### Your current environment ### 🐛 Describe the bug ```txt ERROR 08-21 03:43:01 [dump_input.py:79] Dumping schedule...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_parallel;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error;crash env_dependency;shape #26661 [Bugfix][Core]Fix block table out-of-range issue in priority scheduling Your current environm...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26661](https://github.com/vllm-project/vllm/pull/26661) | closes_keyword | 0.95 | [Bugfix][Core]Fix block table out-of-range issue in priority scheduling | Fixes [#23316](https://github.com/vllm-project/vllm/issues/23316) --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The purpose |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
