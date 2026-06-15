# vllm-project/vllm#26756: [Bug]: ModuleNotFoundError: No module named 'vllm.core'

| 字段 | 值 |
| --- | --- |
| Issue | [#26756](https://github.com/vllm-project/vllm/issues/26756) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'vllm.core'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It looks like an issue with `importlib` not being able to look up `vllm.core` when I'm creating an `AsyncLLM` from the default args of `SchedulerConfig`. ```python vllm_config = VllmConfig( model_config=ModelConfig( dtype='bfloat16', model=model_dir, seed=0, max_model_len=8_192, ), scheduler_config=SchedulerConfig( enable_chunked_prefill=True, max_num_batched_tokens=4_096, max_num_seqs=64, ), cache_config=CacheConfig( gpu_memory_utilization=0.9, ), observability_config=ObservabilityConfig(), ) async_llm = AsyncLLM( vllm_config=self.vllm_config, executor_class=Executor.get_class(self.vllm_config), log_stats=True, log_requests=True, ) ``` I'm then getting the following error: ``` (EngineCore_DP0 pid=545048) Process EngineCore_DP0: (EngineCore_DP0 pid=545048) Traceback (most recent call last): (EngineCore_DP0 pid=545048) File "/home/ryan/.cache/bazel/_bazel_ryan/aa8d1830602cc5ed03705f52effcdfcf/external/rules_python++python+python_3_12_x86_64-unknown-linux-gnu/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=545048) self.run() (EngineCore_DP0 pid=545048) File "/home/ryan/.cache/bazel/_bazel_rya...

## 现有链接修复摘要

#26758 scheduler.py: Update the name of the default scheduler.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ent environment ### 🐛 Describe the bug It looks like an issue with `importlib` not being able to look up `vllm.core` when I'm creating an `AsyncLLM` from the default args of `SchedulerConfig`. ```python vllm_config = Vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: up `vllm.core` when I'm creating an `AsyncLLM` from the default args of `SchedulerConfig`. ```python vllm_config = VllmConfig( model_config=ModelConfig( dtype='bfloat16', model=model_dir, seed=0, max_model_len=8_192, ),...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g`. ```python vllm_config = VllmConfig( model_config=ModelConfig( dtype='bfloat16', model=model_dir, seed=0, max_model_len=8_192, ), scheduler_config=SchedulerConfig( enable_chunked_prefill=True, max_num_batched_tokens=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: core` when I'm creating an `AsyncLLM` from the default args of `SchedulerConfig`. ```python vllm_config = VllmConfig( model_config=ModelConfig( dtype='bfloat16', model=model_dir, seed=0, max_model_len=8_192, ), schedule...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26758](https://github.com/vllm-project/vllm/pull/26758) | mentioned | 0.6 | scheduler.py: Update the name of the default scheduler. | ectify the name of the default scheduler which has been moved, fixing #26756. ## Test Plan To build an application directly using AsyncLLM using this updated build with default `S… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
