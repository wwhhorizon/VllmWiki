# vllm-project/vllm#33428: [Bug]: GLM 4.6v startup failed

| 字段 | 值 |
| --- | --- |
| Issue | [#33428](https://github.com/vllm-project/vllm/issues/33428) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM 4.6v startup failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug GLM 4.6v startup failed with error: ``` (EngineCore_DP0 pid=809) INFO 01-30 07:54:57 [cuda.py:351] Using FLASHINFER attention backend out of potential backends: ('FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION') (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] EngineCore failed to start. (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] Traceback (most recent call last): (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 927, in run_engine_core (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 692, in __init__ (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] super().__init__( (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: t__ (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] self.model_executor = executor_class(vllm_config) (EngineCore_DP0 pid=809) ERROR 01-30 07:54:57 [core.py:936] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: r: ``` (EngineCore_DP0 pid=809) INFO 01-30 07:54:57 [cuda.py:351] Using FLASHINFER attention backend out of potential backends: ('FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION') (EngineCore_DP0 pid=809) ERROR 01-30 07:54:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding attentio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: up failed with error: ``` (EngineCore_DP0 pid=809) INFO 01-30 07:54:57 [cuda.py:351] Using FLASHINFER attention backend out of potential backends: ('FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION') (EngineCore_DP0 pid=809)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GLM 4.6v startup failed bug;stale ### Your current environment ### 🐛 Describe the bug GLM 4.6v startup failed with error: ``` (EngineCore_DP0 pid=809) INFO 01-30 07:54:57 [cuda.py:351] Using FLASHINFER attention...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
