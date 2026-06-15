# vllm-project/vllm#25991: [Bug]: VLLM V1 Engine crashes with KeyError when processing concurrent embedding requests

| 字段 | 值 |
| --- | --- |
| Issue | [#25991](https://github.com/vllm-project/vllm/issues/25991) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache;cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM V1 Engine crashes with KeyError when processing concurrent embedding requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # VLLM V1 Engine crashes with KeyError when processing concurrent embedding requests ## Environment - **VLLM Version**: 0.10.1.1 - **Model**: Qwen/Qwen3-Embedding-0.6B - **Python Version**: 3.12 - **CUDA/GPU**: CUDA environment (WSL detected) - **Deployment**: Docker container - **Engine**: V1 Engine with prefix caching and chunked prefill enabled ## Issue Description The VLLM embedding service crashes with a KeyError when processing multiple concurrent embedding requests. The EngineCore encounters a fatal error and the service needs to restart, causing all subsequent requests to fail during the restart period (~15-20 seconds). ## Error Stack Trace ```python (EngineCore_0 pid=142) ERROR 09-30 14:04:50 [core.py:702] Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 712, in _prepare_inputs tokens = [scheduler_output.num_scheduled_tokens[i] for i in req_ids] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^ KeyError: None ``` Full error path: ``` vllm/v1/engine/core.py:693 -> run_busy_loop() vllm/v1/engine/core.py:745 -> _process_engine_step() vllm/v1/engine/core.py:288...

## 现有链接修复摘要

#42158 [Bugfix][V1] Defensive guard for stale req_id in `_update_after_schedule`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r when processing concurrent embedding requests ## Environment - **VLLM Version**: 0.10.1.1 - **Model**: Qwen/Qwen3-Embedding-0.6B - **Python Version**: 3.12 - **CUDA/GPU**: CUDA environment (WSL detected) - **Deploymen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rent embedding requests ## Environment - **VLLM Version**: 0.10.1.1 - **Model**: Qwen/Qwen3-Embedding-0.6B - **Python Version**: 3.12 - **CUDA/GPU**: CUDA environment (WSL detected) - **Deployment**: Docker container -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LLM V1 Engine crashes with KeyError when processing concurrent embedding requests bug;unstale ### Your current environment ### 🐛 Describe the bug # VLLM V1 Engine crashes with KeyError when processing concurrent embeddi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 632 tokens Maximum concurrency for 4,096 tokens per request: 5.28x Using Flash Attention backend on V1 engine Compilation config: level=3, use_cudagraph=true ``` --- **Labels to add**: `bug`, `v1-engine`, `embeddings`,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .1 - **Model**: Qwen/Qwen3-Embedding-0.6B - **Python Version**: 3.12 - **CUDA/GPU**: CUDA environment (WSL detected) - **Deployment**: Docker container - **Engine**: V1 Engine with prefix caching and chunked prefill ena...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42158](https://github.com/vllm-project/vllm/pull/42158) | closes_keyword | 0.95 | [Bugfix][V1] Defensive guard for stale req_id in `_update_after_schedule` | Closes #42157 Related: #26400 (different layer), #25991 (different surface, same broader pattern). |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
