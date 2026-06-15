# vllm-project/vllm#23427: [Bug]: Error infering Qwen3-MoE with compilation_config={"level": 0, "cudagraph_mode": "FULL_DECODE_ONLY"}

| 字段 | 值 |
| --- | --- |
| Issue | [#23427](https://github.com/vllm-project/vllm/issues/23427) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error infering Qwen3-MoE with compilation_config={"level": 0, "cudagraph_mode": "FULL_DECODE_ONLY"}

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While trying to deploy Qwen3-235B-A22B with vllm 0.10.1 while setting `compilation_config={"level": 0, "cudagraph_mode": "FULL_DECODE_ONLY"}`, the following exception occurs: ```Capturing CUDA graphs (decode, FULL): 0%| | 0/1 [00:00<?, ?it/s](VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] WorkerProc hit an exception. (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] Traceback (most recent call last): (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] File "/root/swift_50/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 591, in worker_busy_loop (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] output = func(*args, **kwargs) (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] File "/root/swift_50/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 315, in compile_or_warm_up_model (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] self.mode...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 315, in compile_or_warm_up_model (VllmWorker PP8 pid=235775) ERROR 08-22 20:11:45 [multiproc_executor.py:596] self.model_runner.capture_model() (VllmWorke...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error infering Qwen3-MoE with compilation_config={"level": 0, "cudagraph_mode": "FULL_DECODE_ONLY"} bug ### Your current environment ### 🐛 Describe the bug While trying to deploy Qwen3-235B-A22B with vllm 0.10.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Error infering Qwen3-MoE with compilation_config={"level": 0, "cudagraph_mode": "FULL_DECODE_ONLY"} bug ### Your current environment ### 🐛 Describe the bug While trying to deploy Qwen3-235B-A22B with vllm 0.10.1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g Qwen3-MoE with compilation_config={"level": 0, "cudagraph_mode": "FULL_DECODE_ONLY"} bug ### Your current environment ### 🐛 Describe the bug While trying to deploy Qwen3-235B-A22B with vllm 0.10.1 while setting `compi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: port;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
