# vllm-project/vllm#13200: [Bug]: multi-node serving occurs nccl error when using vllm installation from source code

| 字段 | 值 |
| --- | --- |
| Issue | [#13200](https://github.com/vllm-project/vllm/issues/13200) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: multi-node serving occurs nccl error when using vllm installation from source code

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Is there any difference between `cd vllm && pip install -v .`(buildint from source code) and `pip install vllm==v0.7.2`(installing from PyPI) Building vLLM from source code results in an NCCL error in my multi-node serving experiment, while installing the pre-built version (vllm==0.7.2) works without any issues. The NCCL error occurs at the line `_PP = init_model_parallel_group()` when attempting to initialize cross-node communication. (The parallel strategy is TP8PP2.) The error log is as follows: ``` (RayWorkerWrapper pid=9128) ERROR 02-12 19:57:26 worker_base.py:572] File "/root/miniconda3/envs/inference/lib/python3.10/site-packages/vllm/worker/worker_base.py", line 564, in execute_method (RayWorkerWrapper pid=9128) ERROR 02-12 19:57:26 worker_base.py:572] return run_method(target, method, args, kwargs) (RayWorkerWrapper pid=9128) ERROR 02-12 19:57:26 worker_base.py:572] File "/root/miniconda3/envs/inference/lib/python3.10/site-packages/vllm/utils.py", line 2208, in run_method (RayWorkerWrapper pid=9128) ERROR 02-12 19:57:26 worker_base.py:572] return func(*args, **kwargs) (RayWorkerWrapper pid=9128) ERROR 02-12 19:57:26 worke...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: multi-node serving occurs nccl error when using vllm installation from source code bug;stale ### Your current environment ### 🐛 Describe the bug Is there any difference between `cd vllm && pip install -v .`(build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cl-net.so NCCL INFO NET/Plugin: Using internal network plugin. NCCL INFO cudaDriverVersion 12040 NCCL version 2.21.5+cuda12.4 TUNER/Plugin: Plugin load returned 2 : libnccl-net.so: cannot open shared object file: No suc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: orks without any issues. The NCCL error occurs at the line `_PP = init_model_parallel_group()` when attempting to initialize cross-node communication. (The parallel strategy is TP8PP2.) The error log is as follows: ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ving occurs nccl error when using vllm installation from source code bug;stale ### Your current environment ### 🐛 Describe the bug Is there any difference between `cd vllm && pip install -v .`(buildint from source code)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
