# vllm-project/vllm#28703: [Bug]: run_batch hang on fresh start

| 字段 | 值 |
| --- | --- |
| Issue | [#28703](https://github.com/vllm-project/vllm/issues/28703) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: run_batch hang on fresh start

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug the CLI command `run_batch` hangs until I press ctrl+c. Here's the log before sigterm: ```log (EngineCore_DP0 pid=109) INFO 11-14 13:17:38 [default_loader.py:314] Loading weights took 1.27 seconds (EngineCore_DP0 pid=109) INFO 11-14 13:17:39 [gpu_model_runner.py:3126] Model loading took 7.6065 GiB memory and 24.608049 seconds (EngineCore_DP0 pid=109) INFO 11-14 13:17:45 [backends.py:618] Using cache directory: /root/.cache/vllm/torch_compile_cache/a713495fcb/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=109) INFO 11-14 13:17:45 [backends.py:634] Dynamo bytecode transform time: 5.61 s (EngineCore_DP0 pid=109) [rank0]:W1114 13:17:46.038000 109 torch/_inductor/utils.py:1558] [0/0] Not enough SMs to use max_autotune_gemm mode (EngineCore_DP0 pid=109) INFO 11-14 13:17:55 [backends.py:250] Cache the graph for dynamic shape for later use (EngineCore_DP0 pid=109) INFO 11-14 13:18:04 [backends.py:281] Compiling a graph for dynamic shape takes 19.27 s (EngineCore_DP0 pid=109) INFO 11-14 13:18:06 [monitor.py:34] torch.compile takes 24.88 s in total (EngineCore_DP0 pid=109) INFO 11-14 13:18:08 [gpu_worker.py:353] Available K...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: 3:17:45 [backends.py:618] Using cache directory: /root/.cache/vllm/torch_compile_cache/a713495fcb/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=109) INFO 11-14 13:17:45 [backends.py:634] Dynamo bytecode...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: run_batch hang on fresh start bug;stale ### Your current environment ### 🐛 Describe the bug the CLI command `run_batch` hangs until I press ctrl+c. Here's the log before sigterm: ```log (EngineCore_DP0 pid=109) I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: mory and 24.608049 seconds (EngineCore_DP0 pid=109) INFO 11-14 13:17:45 [backends.py:618] Using cache directory: /root/.cache/vllm/torch_compile_cache/a713495fcb/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 1114 13:17:46.038000 109 torch/_inductor/utils.py:1558] [0/0] Not enough SMs to use max_autotune_gemm mode (EngineCore_DP0 pid=109) INFO 11-14 13:17:55 [backends.py:250] Cache the graph for dynamic shape for later use (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ghts took 1.27 seconds (EngineCore_DP0 pid=109) INFO 11-14 13:17:39 [gpu_model_runner.py:3126] Model loading took 7.6065 GiB memory and 24.608049 seconds (EngineCore_DP0 pid=109) INFO 11-14 13:17:45 [backends.py:618] Us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
