# vllm-project/vllm#29259: [Bug]: `simple_profiling.py` fails on CPU target

| 字段 | 值 |
| --- | --- |
| Issue | [#29259](https://github.com/vllm-project/vllm/issues/29259) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `simple_profiling.py` fails on CPU target

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description When executing the `examples\offline_inference\simple_profiling.py` script on a CPU, an error occurs. ```bash (EngineCore_DP0 pid=367027) ERROR 11-23 14:03:28 [v1/engine/core.py:844] File "/home/____/vllm_cpu/.venv/lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 520, in annotate_profile (EngineCore_DP0 pid=367027) ERROR 11-23 14:03:28 [v1/engine/core.py:844] return self.profiler.annotate_context_manager( (EngineCore_DP0 pid=367027) ERROR 11-23 14:03:28 [v1/engine/core.py:844] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=367027) ERROR 11-23 14:03:28 [v1/engine/core.py:844] AttributeError: 'profile' object has no attribute 'annotate_context_manager' ``` full log: [full_log.txt](https://github.com/user-attachments/files/23693710/full_log.txt) ## Environment - Target Device: CPU (x86) - Build from source ## Details The root cause appears to be incomplete application of changes introduced by Pull Request #28987 . This conclusion was drawn by bisecting the commits: | Commit | SHA | Status | |---|---|---| | Previous Commit | 3168285fcaaee09bc93dce7bc9ae6ee823c71652 | No Error | | Failing Com...

## 现有链接修复摘要

#28987 [Feat] Iteration-level profiling for Torch and CUDA profiler

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: iles/23693710/full_log.txt) ## Environment - Target Device: CPU (x86) - Build from source ## Details The root cause appears to be incomplete application of changes introduced by Pull Request #28987 . This conclusion was...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: `simple_profiling.py` fails on CPU target bug ### Your current environment ### 🐛 Describe the bug ## Description When executing the `examples\offline_inference\simple_profiling.py` script on a CPU, an error occur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cause appears to be incomplete application of changes introduced by Pull Request #28987 . This conclusion was drawn by bisecting the commits: | Commit | SHA | Status | |---|---|---| | Previous Commit | 3168285fcaaee09bc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #28987 [Feat] Iteration-level profiling for Torch and CUDA profiler Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28987](https://github.com/vllm-project/vllm/pull/28987) | mentioned | 0.45 | [Feat] Iteration-level profiling for Torch and CUDA profiler | rs to be incomplete application of changes introduced by pull request #28987 . this conclusion was drawn by bisecting the commits: \| commit \| sha \| status \| \|---\|---\|---\| \| previo… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
