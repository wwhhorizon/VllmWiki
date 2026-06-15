# vllm-project/vllm#22372: [Bug]: vLLM crashes on B200 when attempting to load Qwen3 due to `AttributeError: module 'vllm.envs' has no attribute 'VLLM_USE_TRTLLM_ATTENTION'`

| 字段 | 值 |
| --- | --- |
| Issue | [#22372](https://github.com/vllm-project/vllm/issues/22372) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes on B200 when attempting to load Qwen3 due to `AttributeError: module 'vllm.envs' has no attribute 'VLLM_USE_TRTLLM_ATTENTION'`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Starting vllm on B200 against HEAD with: ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 --port 8000 --enforce-eager --disable-log-requests --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 2 --trust-remote-code ``` results in the following crash when attempting to serve a request. ``` (EngineCore_0 pid=6088) Traceback (most recent call last): (EngineCore_0 pid=6088) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_0 pid=6088) self.run() (EngineCore_0 pid=6088) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_0 pid=6088) self._target(*self._args, **self._kwargs) (EngineCore_0 pid=6088) File "/app/vllm/vllm/v1/engine/core.py", line 687, in run_engine_core (EngineCore_0 pid=6088) raise e (EngineCore_0 pid=6088) File "/app/vllm/vllm/v1/engine/core.py", line 676, in run_engine_core (EngineCore_0 pid=6088) engine_core.run_busy_loop() (EngineCore_0 pid=6088) File "/app/vllm/vllm/v1/engine/core.py", line 1017, in run_busy_loop (EngineCore_0 pid=6088) executed = self._process_engine_step() (EngineCore_0 pid=6088) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineC...

## 现有链接修复摘要

#22095 [NVIDIA] Support Flashinfer TRT-LLM Prefill Attention Kernel

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: m serve Qwen/Qwen3-30B-A3B-FP8 --port 8000 --enforce-eager --disable-log-requests --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 2 --trust-remote-code ``` results in the following crash when atte...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ^^^^^^^^^^^^ (EngineCore_0 pid=6088) File "/app/vllm/vllm/v1/attention/backends/flashinfer.py", line 529, in build (EngineCore_0 pid=6088) and use_trtllm_attention( (EngineCore_0 pid=6088) ^^^^^^^^^^^^^^^^^^^^^ (EngineC...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e 851, in _prepare_inputs (EngineCore_0 pid=6088) attn_metadata_i = (builder.build( (EngineCore_0 pid=6088) ^^^^^^^^^^^^^^ (EngineCore_0 pid=6088) File "/app/vllm/vllm/v1/attention/backends/flashinfer.py", line 529, in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ing vllm on B200 against HEAD with: ``` $ vllm serve Qwen/Qwen3-30B-A3B-FP8 --port 8000 --enforce-eager --disable-log-requests --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 2 --trust-remote-code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: vLLM crashes on B200 when attempting to load Qwen3 due to `AttributeError: module 'vllm.envs' has no attribute 'VLLM_USE_TRTLLM_ATTENTION'` bug ### Your current environment ### 🐛 Describe the bug Starting vllm on...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22095](https://github.com/vllm-project/vllm/pull/22095) | mentioned | 0.45 | [NVIDIA] Support Flashinfer TRT-LLM Prefill Attention Kernel | mean: 'vllm_use_trtllm_decode_attention'? ``` looking at the source, #22095 did not add it to vllm.envs. ### before submitting a new issue... - [x] make sure you already searched… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
