# vllm-project/vllm#17969: [Bug]: slot_mapping of schedulined_tokens in tpu_model_runner should be an array (not tensor).

| 字段 | 值 |
| --- | --- |
| Issue | [#17969](https://github.com/vllm-project/vllm/issues/17969) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: slot_mapping of schedulined_tokens in tpu_model_runner should be an array (not tensor).

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running `examples/offline_inference/tpu.py`, came up with the following issue: ``` Traceback (most recent call last): File "/home/jcgu_google_com/anaconda3/envs/nixl/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/xxx/anaconda3/envs/nixl/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/xxx/vllm/vllm/v1/engine/core.py", line 425, in run_engine_core raise e File "/home/xxx/vllm/vllm/v1/engine/core.py", line 414, in run_engine_core engine_core.run_busy_loop() File "/home/xxx/vllm/vllm/v1/engine/core.py", line 438, in run_busy_loop self._process_engine_step() File "/home/xxx/vllm/vllm/v1/engine/core.py", line 463, in _process_engine_step outputs = self.step_fn() File "/home/xxx/vllm/vllm/v1/engine/core.py", line 226, in step model_output = self.execute_model(scheduler_output) File "/home/xxx/vllm/vllm/v1/engine/core.py", line 213, in execute_model raise err File "/home/xxx/vllm/vllm/v1/engine/core.py", line 207, in execute_model return self.model_executor.execute_model(scheduler_output) File "/home/xxx/vllm/vllm/v1/execut...

## 现有链接修复摘要

#17483 [v1] Pass BlockTable and KVCacheSpec to AttentionMetadataBuilders

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: [Bug]: slot_mapping of schedulined_tokens in tpu_model_runner should be an array (not tensor). bug ### Your current environment ### 🐛 Describe the bug When running `examples/offline_inference/tpu.py`, came up with the f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependenc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 83. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine/core.py", line 226, in step model_output = self.execute_model(scheduler_output) File "/home/xxx/vllm/vllm/v1/engine/core.py", line 213, in execute_model raise err File "/home/xxx/vllm/vllm/v1/engine/core.py", lin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #17483 [v1] Pass BlockTable and KVCacheSpec to AttentionMetadataBuilders Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17483](https://github.com/vllm-project/vllm/pull/17483) | mentioned | 0.45 | [v1] Pass BlockTable and KVCacheSpec to AttentionMetadataBuilders | duled_tokens should be converted to an array. the issue was caused by #17483. ### before submitting a new issue... - [x] make sure you already searched for relevant issues, and as… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
