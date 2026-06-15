# vllm-project/vllm#38375: [Bug]: IndexError when `--renderer-num-workers` + `--mm-processor-cache-type shm`

| 字段 | 值 |
| --- | --- |
| Issue | [#38375](https://github.com/vllm-project/vllm/issues/38375) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: IndexError when `--renderer-num-workers` + `--mm-processor-cache-type shm`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #34789 introduces renderer threadpool set by `--renderer-num-workers` CLI argument, but it seems this option is incompatible with `--mm-processor-cache-type shm`. If we set both options in a vision language model server, it crashes with the following index error under a high concurrency workload (e.g. running chartqa benchmark): ```log (APIServer pid=1) INFO 03-28 00:00:07 [async_llm.py:420] Added request chatcmpl-a0fe280d9f2887ae-b8cfa283. (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py:949] WorkerProc hit an exception. (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py:949] Traceback (most recent call last): (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py:949] File "/app/.venv/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 944, in worker_busy_loop (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py:949] output = func(*args, **kwargs) (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py:949] ^^^^^^^^^^^^^^^^^^^^^ (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py...

## 现有链接修复摘要

#34789 [Bugfix] Offload blocking tokenizer ops to shared thread pool to unblock event loop | #38418 [Bugfix] Disallow renderer_num_workers > 1 with mm processor cache

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: m-processor-cache-type shm`. If we set both options in a vision language model server, it crashes with the following index error under a high concurrency workload (e.g. running chartqa benchmark): ```log (APIServer pid=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : ```log (APIServer pid=1) INFO 03-28 00:00:07 [async_llm.py:420] Added request chatcmpl-a0fe280d9f2887ae-b8cfa283. (Worker_TP7_DCP1_EP7 pid=641) ERROR 03-28 00:00:07 [multiproc_executor.py:949] WorkerProc hit an except...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding cuda...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: index out of range ... ``` ## example deployment spec ```shell # On a H100 x 8 worker node vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct \ --port 8080 \ --gpu-memory-utilization 0.91 \ --tensor-parallel-size 8 \ --enable-...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --gpu-memory-utilization 0.91 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --max-num-seqs 32 \ --renderer-num-workers 4 \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm ``` ### Before submitting a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34789](https://github.com/vllm-project/vllm/pull/34789) | mentioned | 0.45 | [Bugfix] Offload blocking tokenizer ops to shared thread pool to unblock event loop | rker_multiproc_method=spawn ``` </details> ### 🐛 describe the bug #34789 introduces renderer threadpool set by `--renderer-num-workers` cli argument, but it seems this option is i… |
| [#38418](https://github.com/vllm-project/vllm/pull/38418) | closes_keyword | 0.95 | [Bugfix] Disallow renderer_num_workers > 1 with mm processor cache | Closes #38375 ## Test Plan ```bash python -m pytest tests/test_config.py::test_renderer_num_workers_with_mm_cache -v ``` ## Test Result Test covers four cases: - `renderer_num_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
