# vllm-project/vllm#24107: [Bug]: CUDA illegal memory access during structured output (xgrammar) crashes vLLM workers and API returns 500

| 字段 | 值 |
| --- | --- |
| Issue | [#24107](https://github.com/vllm-project/vllm/issues/24107) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access during structured output (xgrammar) crashes vLLM workers and API returns 500

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When doing structured output (GuidedDecoding with a JSON schema; backend=xgrammar) on vLLM (Kwaipilot/KAT-V1-40B, TP=2, bf16), both GPU workers hit RuntimeError: CUDA error: an illegal memory access was encountered at gpu_model_runner.py:1733 (sampled_token_ids.tolist()), leading to EngineDeadError and /v1/chat/completions responding 500. Logs also show CUDA errors from custom_all_reduce.cuh:594 and nanobind leaks for xgrammar types (CompiledGrammar, GrammarMatcher). ```python 2025-09-02T08:04:02.874454226-07:00 [1;36m(VllmWorker TP0 pid=442)[0;0m ERROR 09-02 08:04:02 [multiproc_executor.py:596] WorkerProc hit an exception. 2025-09-02T08:04:02.874480216-07:00 [1;36m(VllmWorker TP0 pid=442)[0;0m ERROR 09-02 08:04:02 [multiproc_executor.py:596] Traceback (most recent call last): 2025-09-02T08:04:02.874484356-07:00 [1;36m(VllmWorker TP0 pid=442)[0;0m ERROR 09-02 08:04:02 [multiproc_executor.py:596] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loop 2025-09-02T08:04:02.874488526-07:00 [1;36m(VllmWorker TP0 pid=442)[0;0m ERROR 09-02 08:04:02 [multiproc_executor....

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: tructured output (xgrammar) crashes vLLM workers and API returns 500 bug;stale ### Your current environment ### 🐛 Describe the bug When doing structured output (GuidedDecoding with a JSON schema; backend=xgrammar) on vL...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rs from custom_all_reduce.cuh:594 and nanobind leaks for xgrammar types (CompiledGrammar, GrammarMatcher). ```python 2025-09-02T08:04:02.874454226-07:00 [1;36m(VllmWorker TP0 pid=442)[0;0m ERROR 09-02 08:04:02 [multip...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: th a JSON schema; backend=xgrammar) on vLLM (Kwaipilot/KAT-V1-40B, TP=2, bf16), both GPU workers hit RuntimeError: CUDA error: an illegal memory access was encountered at gpu_model_runner.py:1733 (sampled_token_ids.toli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access during structured output (xgrammar) crashes vLLM workers and API returns 500 bug;stale ### Your current environment ### 🐛 Describe the bug When doing structured output (GuidedDecoding w...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: 2 [multiproc_executor.py:596] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 2025-09-02T08:04:02.874564897-07:00 [1;36m(VllmWorker TP0 pid=442)[0;0m ERROR 09-02 08:04:02 [multiproc_executor.py:596] Compile with...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
