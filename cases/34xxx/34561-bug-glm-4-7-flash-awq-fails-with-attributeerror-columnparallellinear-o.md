# vllm-project/vllm#34561: [Bug]: GLM-4.7-Flash-AWQ fails with AttributeError: 'ColumnParallelLinear' object has no attribute 'weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#34561](https://github.com/vllm-project/vllm/issues/34561) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.7-Flash-AWQ fails with AttributeError: 'ColumnParallelLinear' object has no attribute 'weight'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Sometime after commit 13397841ab469cecf1ed425c3f52a9ffc38139b5, cyankiwi/GLM-4.7-Flash-AWQ-4bit stopped working on DGX Spark. It now fails with the following error during inference (startup is normal): ``` (EngineCore_DP0 pid=240) Traceback (most recent call last): (EngineCore_DP0 pid=240) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=240) self.run() (EngineCore_DP0 pid=240) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=240) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=240) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1033, in run_engine_core (EngineCore_DP0 pid=240) raise e (EngineCore_DP0 pid=240) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1022, in run_engine_core (EngineCore_DP0 pid=240) engine_core.run_busy_loop() (EngineCore_DP0 pid=240) File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1049, in run_busy_loop (EngineCore_DP0 pid=240) self._process_engine_step() (EngineCore_DP0 pid=240) File "/usr/local/lib/python3.12/dist-...

## 现有链接修复摘要

#34695 [Bugfix] Fix MLA attention crash with AWQ/GPTQ quantized models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tors.py", line 471, in __call__ (EngineCore_DP0 pid=240) return TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) # type: ignore[arg-type] (EngineCore_DP0 pid=240) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 3.12/dist-packages/vllm/v1/engine/core.py", line 497, in step_with_batch_queue (EngineCore_DP0 pid=240) exec_model_fut.result() (EngineCore_DP0 pid=240) File "/usr/lib/python3.12/concurrent/futures/_base.py", line 449,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: te_prefill_context (EngineCore_DP0 pid=240) or self.kv_b_proj.weight.dtype != current_platform.fp8_dtype() (EngineCore_DP0 pid=240) ^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=240) File "/usr/local/lib/python3.12/dist-pac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: id=240) File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/cuda_graph.py", line 222, in __call__ (EngineCore_DP0 pid=240) return self.runnable(*args, **kwargs) (EngineCore_DP0 pid=240) ^^^^^^^^^^^^^^^^^^^^^^...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/glm4_moe_lite.py", line 604, in forward (EngineCore_DP0 pid=240) hidden_states = self.model( (EngineCore_DP0 pid=240) ^^^^^^^^^^^ (EngineCore_DP0 pid=2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34695](https://github.com/vllm-project/vllm/pull/34695) | closes_keyword | 0.95 | [Bugfix] Fix MLA attention crash with AWQ/GPTQ quantized models | Closes #34561. **Root cause**: MLA attention code accesses `self.kv_b_proj.weight.dtype` in 3 places, but AWQ/GPTQ-quantized `ColumnParallelLinear` layers store weights as `qweigh |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
