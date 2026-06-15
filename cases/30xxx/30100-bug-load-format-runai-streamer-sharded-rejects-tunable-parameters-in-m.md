# vllm-project/vllm#30100: [Bug]: Load format `runai_streamer_sharded` rejects tunable parameters in `model_loader_extra_config`

| 字段 | 值 |
| --- | --- |
| Issue | [#30100](https://github.com/vllm-project/vllm/issues/30100) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Load format `runai_streamer_sharded` rejects tunable parameters in `model_loader_extra_config`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Loading a pre-sharded model with the Run:ai Model Streamer (`load_format="runai_streamer_sharded"`) rejects tunable parameters passed in `model_loader_extra_config`. I'm using vLLM 0.12.0 (`vllm[runai]==0.12.0`). ``` (Worker_TP0_EP0 pid=50) INFO 12-05 00:02:27 [gpu_model_runner.py:3467] Starting to load model /root/.cache/huggingface/sharded/Qwen3-Next-80B-A3B-Thinking... (Worker_TP1_EP1 pid=51) ERROR 12-05 00:02:27 [multiproc_executor.py:750] WorkerProc failed to start. (Worker_TP1_EP1 pid=51) ERROR 12-05 00:02:27 [multiproc_executor.py:750] Traceback (most recent call last): (Worker_TP1_EP1 pid=51) ERROR 12-05 00:02:27 [multiproc_executor.py:750] File "/usr/local/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 722, in worker_main (Worker_TP1_EP1 pid=51) ERROR 12-05 00:02:27 [multiproc_executor.py:750] worker = WorkerProc(*args, **kwargs) (Worker_TP1_EP1 pid=51) ERROR 12-05 00:02:27 [multiproc_executor.py:750] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1_EP1 pid=51) ERROR 12-05 00:02:27 [multiproc_executor.py:750] File "/usr/local/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 56...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Load format `runai_streamer_sharded` rejects tunable parameters in `model_loader_extra_config` bug;stale ### Your current environment ### 🐛 Describe the bug Loading a pre-sharded model with the Run:ai Model Strea...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s invoked. ### Steps to reproduce ```python from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine engine_args = AsyncEngineArgs( # Use pre-sharded model for faster loa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: r_sharded` rejects tunable parameters in `model_loader_extra_config` bug;stale ### Your current environment ### 🐛 Describe the bug Loading a pre-sharded model with the Run:ai Model Streamer (`load_format="runai_streamer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: py:66: [RunAI Streamer] Overall time to stream 151.5 GiB of all files to cuda:1: 67.79s, 2.2 GiB/s (Worker_TP0_EP0 pid=50) [2025-12-04 20:35:00] INFO file_streamer.py:66: [RunAI Streamer] Overall time to stream 151.5 Gi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ble_custom_all_reduce=True, max_num_batched_tokens=65536, enable_expert_parallel=True, enable_chunked_prefill=False, enforce_eager=False, disable_log_stats=False, enable_log_requests=True, reasoning_parser="deepseek_r1"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
