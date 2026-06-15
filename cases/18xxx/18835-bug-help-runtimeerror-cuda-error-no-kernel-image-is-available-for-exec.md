# vllm-project/vllm#18835: [Bug]: Help, RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#18835](https://github.com/vllm-project/vllm/issues/18835) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Help, RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ERROR 05-28 19:38:44 [dump_input.py:68] Dumping input data --- Logging error --- Traceback (most recent call last): File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 207, in execute_model return self.model_executor.execute_model(scheduler_output) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/v1/executor/abstract.py", line 86, in execute_model output = self.collective_rpc("execute_model", ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc answer = run_method(self.driver_worker, method, args, kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/utils.py", line 2605, in run_method return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vll...

## 现有链接修复摘要

#20050 [Core][Bugfix] new way for full cudagraph, add support for FA2 and FlashInfer; Two minor bugs fixed | #20219 [CI/Build][Bugfix]Fix marlin kernel no built on 4090

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ### run: CUDA_VISIBLE_DEVICES=0 vllm serve qwen3-4B/ --served-model-name Qwen3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Help, RuntimeError: CUDA error: no kernel image is available for execution on the device bug ### Your current environment ERROR 05-28 19:38:44 [dump_input.py:68] Dumping input data --- Logging error --- Traceback...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: -- Traceback (most recent call last): File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 207, in execute_model return self.model_executor.execute_model(scheduler_output) ^^...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: line 207, in execute_model return self.model_executor.execute_model(scheduler_output) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/v1/execu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: iniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/v1/attention/backends/flash_attn.py", line 622, in forward flash_attn_varlen_func( File "/root/miniconda3/envs/vllm-qwen3/lib/python3.12/site-packages/vllm/vll...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20050](https://github.com/vllm-project/vllm/pull/20050) | closes_keyword | 0.95 | [Core][Bugfix] new way for full cudagraph, add support for FA2 and FlashInfer; Two minor bugs fixed | fixed this problem. Similar issues see #18835 ## Test Plan benchmark serving, lm_eval performance of FA2 and FlashInfer I have no plan to test FlashMLA and FA3 as no hopper g |
| [#20219](https://github.com/vllm-project/vllm/pull/20219) | closes_keyword | 0.95 | [CI/Build][Bugfix]Fix marlin kernel no built on 4090 | fixed this problem. Similar problems see Issue #18835 ## Test Plan Now it works on 4090 device. No further test plan as this is simple. <!--- pyml disable-next-line no-emphasis- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
