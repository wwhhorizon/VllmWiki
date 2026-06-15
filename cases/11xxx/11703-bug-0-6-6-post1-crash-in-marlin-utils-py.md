# vllm-project/vllm#11703: [Bug]: 0.6.6.post1 crash in marlin_utils.py

| 字段 | 值 |
| --- | --- |
| Issue | [#11703](https://github.com/vllm-project/vllm/issues/11703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.6.6.post1 crash in marlin_utils.py

### Issue 正文摘录

### Your current environment ### Model Input Dumps the input file is empty ### 🐛 Describe the bug In the case of concurrent pressure testing interface v1/cat/completeness, a crash occurs： INFO 01-03 10:56:03 metrics.py:483] Prefix cache hit rate: GPU: 2.62%, CPU: 0.00% INFO: 192.168.152.11:53750 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 192.168.152.11:53758 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 192.168.152.11:53732 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 192.168.152.11:53744 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO 01-03 10:56:05 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250103-105605.pkl... WARNING 01-03 10:56:05 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered WARNING 01-03 10:56:05 model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. WARNING 01-03 10:56:05 model_runner_base.py:143] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 WARNING 01-03 10:56:05 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CUDA_LAUNCH_BLOCKING=1 WARNING 01-03 10:56:05 model_runner_base.py:143] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. WARNING 01-03 10:56:05 model_runner_base.py:143] ERROR 01-03 10:56:05 engine.py...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 5 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: an illegal memory access was encountered WARNING 01-03 10:56:05 model_runner_base.py:143] CUDA kernel errors might be asynchronously r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: y", line 196, in run_engine_loop ERROR 01-03 10:56:05 engine.py:135] request_outputs = self.engine_step() ERROR 01-03 10:56:05 engine.py:135] File "/usr/local/lib/python3.10/dist-packages/vllm/engine/multiprocessing/eng...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ompleteness, a crash occurs： INFO 01-03 10:56:03 metrics.py:483] Prefix cache hit rate: GPU: 2.62%, CPU: 0.00% INFO: 192.168.152.11:53750 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 192.168.152.11:53758 - "POST...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
