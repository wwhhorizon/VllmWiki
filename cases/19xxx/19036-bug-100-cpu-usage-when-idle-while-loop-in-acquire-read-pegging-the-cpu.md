# vllm-project/vllm#19036: [Bug]: 100% CPU usage when idle. While loop in `acquire_read` pegging the CPU.

| 字段 | 值 |
| --- | --- |
| Issue | [#19036](https://github.com/vllm-project/vllm/issues/19036) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 100% CPU usage when idle. While loop in `acquire_read` pegging the CPU.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running `vllm serve "deepseek-ai/DeepSeek-R1-0528-Qwen3-8B" --tensor-parallel-size 2` results in 2 python processes taking up 100% each of a CPU while vllm is idle. `py-spy top` output of one of the offending processes ``` GIL: 49.00%, Active: 100.00%, Threads: 5 %Own %Total OwnTime TotalTime Function (filename) 54.00% 54.00% 5.03s 5.03s sched_yield (vllm/distributed/utils.py) 14.00% 100.00% 1.09s 8.95s acquire_read (vllm/distributed/device_communicators/shm_broadcast.py) 12.00% 13.00% 1.04s 1.09s get_metadata (vllm/distributed/device_communicators/shm_broadcast.py) 5.00% 5.00% 0.590s 0.670s __init__ (contextlib.py) 6.00% 100.00% 0.410s 8.95s __enter__ (contextlib.py) 3.00% 4.00% 0.380s 0.400s __exit__ (contextlib.py) 5.00% 10.00% 0.360s 1.03s helper (contextlib.py) 1.00% 1.00% 0.050s 0.050s buf (multiprocessing/shared_memory.py) 0.00% 100.00% 0.000s 8.95s dequeue (vllm/distributed/device_communicators/shm_broadcast.py) 0.00% 100.00% 0.000s 8.95s worker_main (vllm/v1/executor/multiproc_executor.py) 0.00% 100.00% 0.000s 8.95s worker_busy_loop (vllm/v1/executor/multiproc_executor.py) 0.00% 100.00% 0.000s 8.95s ( ) 0.00% 100.00% 0.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ad` runs again and `sched_yield` is called again, pegging the CPU. Replacing the implementation of `sched_yield` with just a `time.sleep(0.0001)` call decreases the CPU usage to something like 2% on my system, but that...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ve? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## 🐛 Describe the bug Running `vllm serve "deepseek-ai/DeepSeek-R1-0528-Qwen3-8B" --tensor-parallel-size 2` results in 2 python processes taking up 100% each of a CPU while vllm is idle. `py-spy top` output of one of th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: multiprocessing/shared_memory.py) 0.00% 100.00% 0.000s 8.95s dequeue (vllm/distributed/device_communicators/shm_broadcast.py) 0.00% 100.00% 0.000s 8.95s worker_main (vllm/v1/executor/multiproc_executor.py) 0.00% 100.00%...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
