# vllm-project/vllm#31599: [Bug]: AssertionError in `per_token_quant_int8` for long input

| 字段 | 值 |
| --- | --- |
| Issue | [#31599](https://github.com/vllm-project/vllm/issues/31599) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in `per_token_quant_int8` for long input

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While trying the [W4A8 marlin kernel](https://github.com/vllm-project/vllm/pull/24722) with AWQ quantization checkpoint, I consistently get the following tensor contiguity error in `per_token_quant_int8` for long inputs: ```log ... (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] WorkerProc hit an exception. (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] Traceback (most recent call last): (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] File "/app/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] output = func(*args, **kwargs) (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] File "/app/.venv/lib/python3.12/site-packages/vllm/v1/worker/worker_base.py", line 369, in execute_model (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] ruturn self.worker.execute_model(scheduler_output, *args, **kwargs) (Worker_TP4 pid=74...

## 现有链接修复摘要

#31637 [Bugfix][Quantization] Ensure input contiguity in per_token_quant_int8

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: =743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] output = TorchCompileWithNoGuardsWrapper.__call__(self, *args, **kwargs) (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] ^^^^^^^^^^^^^^^^^^^^^...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: or.py:824] File "/app/.venv/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1044, in _fn (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] return fn(*args, **kwargs) (Worker_TP4 pid=7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: AssertionError in `per_token_quant_int8` for long input bug ### Your current environment ### 🐛 Describe the bug While trying the [W4A8 marlin kernel](https://github.com/vllm-project/vllm/pull/24722) with AWQ quan...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 3:32:52 [multiproc_executor.py:824] ruturn self.worker.execute_model(scheduler_output, *args, **kwargs) (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y:824] File "/app/.venv/lib/python3.12/site-packages/vllm/v1/attention/backends/mla/common.py", line 2021, in forward (Worker_TP4 pid=743) ERROR 12-30 23:32:52 [multiproc_executor.py:824] self._forward_prefill( (Worker_...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31637](https://github.com/vllm-project/vllm/pull/31637) | closes_keyword | 0.95 | [Bugfix][Quantization] Ensure input contiguity in per_token_quant_int8 | Fixes #31599. When using AWQ-Marlin quantization (specifically with VLLM_MARLIN_INPUT_DTYPE=int8) for models employing MLA (Multi-Head Latent Attention) like DeepSeek-V2/V3/R1, |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
