# vllm-project/vllm#38982: [Bug]: Enabling cudagraph_mm_encoder results in ModuleNotFoundError

| 字段 | 值 |
| --- | --- |
| Issue | [#38982](https://github.com/vllm-project/vllm/issues/38982) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enabling cudagraph_mm_encoder results in ModuleNotFoundError

### Issue 正文摘录

### Your current environment vllm/vllm-openai:latest-cu130 ### 🐛 Describe the bug Trying to serve a model such as Qwen3.5 with `--compilation-config '{"cudagraph_mm_encoder": true}'` results in the following error: ``` (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] EngineCore failed to start. (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] Traceback (most recent call last): (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1082, in run_engine_core (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] return func(*args, **kwargs) (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] ^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] File "/usr/local/lib/python3.12/dist-package...

## 现有链接修复摘要

#38997 [Bug] Fix Import paths for `encoder_cudagraph` modules | #39028 [Bugfix] Fix broken imports for encoder_cudagraph after partial revert

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 6 [core.py:1108] File "/usr/local/lib/python3.12/dist-packages/vllm/tracing/otel.py", line 178, in sync_wrapper (EngineCore pid=45) ERROR 04-04 12:15:46 [core.py:1108] return func(*args, **kwargs) (EngineCore pid=45) ER...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: m/vllm-openai:latest-cu130 ### 🐛 Describe the bug Trying to serve a model such as Qwen3.5 with `--compilation-config '{"cudagraph_mm_encoder": true}'` results in the following error: ``` (EngineCore pid=45) ERROR 04-04...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Enabling cudagraph_mm_encoder results in ModuleNotFoundError bug ### Your current environment vllm/vllm-openai:latest-cu130 ### 🐛 Describe the bug Trying to serve a model such as Qwen3.5 with `--compilation-confi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;crash;import_error;nan_inf env_dependency #38997 [Bug] Fix Import paths for `encoder_cudagraph` modules | #39028 [Bugfix] Fix b...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;crash;import_error;n...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38997](https://github.com/vllm-project/vllm/pull/38997) | closes_keyword | 0.95 | [Bug] Fix Import paths for `encoder_cudagraph` modules | Fixes: #38982 ## Test Plan - [x] Verified imports resolve: `from vllm.v1.worker.encoder_cudagraph import EncoderCudaGraphManager` ✓ - [x] Ran `pytest tests/v1/cudagraph/t |
| [#39028](https://github.com/vllm-project/vllm/pull/39028) | closes_keyword | 0.95 | [Bugfix] Fix broken imports for encoder_cudagraph after partial revert | Fixes #38982 PR #38116 relocated `encoder_cudagraph.py` and `encoder_cudagraph_defs.py` into `vllm/v1/worker/gpu/mm/`. PR #38556 then moved them back to `vllm/v1/worker/`, but **9 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
