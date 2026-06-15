# vllm-project/vllm#13392: [Bug]: Benchmark v1 on multi-gpu crashes with ValueError: Pointer argument (at 0) cannot be accessed from Triton

| 字段 | 值 |
| --- | --- |
| Issue | [#13392](https://github.com/vllm-project/vllm/issues/13392) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Benchmark v1 on multi-gpu crashes with ValueError: Pointer argument (at 0) cannot be accessed from Triton

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Benchmarking v1 on multi-gpu with `ENGINE_VERSION=v1 .buildkite/nightly-benchmarks/scripts/run-performance-benchmarks.sh` crashes with the following error: ``` (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] WorkerProc hit an exception: %s (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] Traceback (most recent call last): (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] File "/home/huydo/github/pytorch-integration-testing/vllm-benchmarks/vllm/vllm/v1/executor/multiproc_executor.py", line 370, in worker_busy_loop (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] output = func(*args, **kwargs) (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] File "/home/huydo/miniconda3/envs/py3.12/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] return func(*args, **kwargs) (Vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: nt ### 🐛 Describe the bug Benchmarking v1 on multi-gpu with `ENGINE_VERSION=v1 .buildkite/nightly-benchmarks/scripts/run-performance-benchmarks.sh` crashes with the following error: ``` (VllmWorker rank=2 pid=3748461) E...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Benchmark v1 on multi-gpu crashes with ValueError: Pointer argument (at 0) cannot be accessed from Triton bug ### Your current environment ### 🐛 Describe the bug Benchmarking v1 on multi-gpu with `ENGINE_VERSION=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: =2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] self.model_runner.profile_run() (VllmWorker rank=2 pid=3748461) ERROR 02-17 00:02:01 multiproc_executor.py:374] File "/home/huydo/github/pytorch-integratio...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: crashes with ValueError: Pointer argument (at 0) cannot be accessed from Triton bug ### Your current environment ### 🐛 Describe the bug Benchmarking v1 on multi-gpu with `ENGINE_VERSION=v1 .buildkite/nightly-benchmarks/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
