# vllm-project/vllm#24544: [Bug]: TensorSchema validation fails for allenai/Molmo-7B-D-0924

| 字段 | 值 |
| --- | --- |
| Issue | [#24544](https://github.com/vllm-project/vllm/issues/24544) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TensorSchema validation fails for allenai/Molmo-7B-D-0924

### Issue 正文摘录

### 🐛 Describe the bug When you run the model, the TensorSchema validation fails. Command: ``` python -m vllm.entrypoints.openai.api_server --model allenai/Molmo-7B-D-0924 --trust-remote-code ``` Error: ``` (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] EngineCore failed to start. (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] Traceback (most recent call last): (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] File "/root/dev/vllm/vllm/v1/engine/core.py", line 709, in run_engine_core (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] File "/root/dev/vllm/vllm/v1/engine/core.py", line 505, in __init__ (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] super().__init__(vllm_config, executor_class, log_stats, (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] File "/root/dev/vllm/vllm/v1/engine/core.py", line 91, in __init__ (EngineC...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: /github.com/vllm-project/vllm/pull/22022 cc @bbeckca ``` correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: for allenai/Molmo-7B-D-0924 bug ### 🐛 Describe the bug When you run the model, the TensorSchema validation fails. Command: ``` python -m vllm.entrypoints.openai.api_server --model allenai/Molmo-7B-D-0924 --trust-remote-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 6535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] self.model_runner.profile_run() (EngineCore_DP0 pid=16535) ERROR 09-09 22:57:37 [v1/engine/core.py:718] File "/root/dev/vllm/vllm/v1/worker/gpu_model_runner.py", line 2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape 🐛 Describe the bug
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape 🐛 Describe the bug

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
