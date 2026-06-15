# vllm-project/vllm#27855: [Bug]: Cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#27855](https://github.com/vllm-project/vllm/issues/27855) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes, I'm not sure whether it's a bug from ray or any other part in vllm. The single node works well for other models. the image I use is: rocm/vllm-dev:nightly_main_20251029, which is vllm v0.11.1rc5. I've noticed there are some similar issues, but none of them work for me. Here is my command: ```python VLLM_WORKER_MULTIPROC_METHOD=spawn vllm serve Qwen3-235B-A22B-Instruct-2507/ \ --block-size 16 \ --max-num-seqs 8 \ --max-model-len 1024 \ --trust-remote-code \ -tp 8 -pp 2 ``` Here is error: ``` ERROR 10-31 02:34:59 [multiproc_executor.py:631] WorkerProc failed to start. ERROR 10-31 02:34:59 [multiproc_executor.py:631] Traceback (most recent call last): ERROR 10-31 02:34:59 [multiproc_executor.py:631] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 605, in worker_main ERROR 10-31 02:34:59 [multiproc_executor.py:631] worker = WorkerProc(*args, **kwargs) ERROR 10-31 02:34:59 [multiproc_executor.py:631] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 10-31 02:34:59 [multiproc_executor.py:631] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes bug;rocm ### Your current environment ### 🐛 Describe the bug I cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes, I'm not sure whether it's a bug from ray or...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: AMD_SERIALIZE_KERNEL=3 ERROR 10-31 02:34:59 [multiproc_executor.py:631] Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions. ``` ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: R_MULTIPROC_METHOD=spawn vllm serve Qwen3-235B-A22B-Instruct-2507/ \ --block-size 16 \ --max-num-seqs 8 \ --max-model-len 1024 \ --trust-remote-code \ -tp 8 -pp 2 ``` Here is error: ``` ERROR 10-31 02:34:59 [multiproc_e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes bug;rocm ### Your current environment ### 🐛 Describe the bug I cannot run Qwen3-235B-A22B-Instruct-2507 on 2 nodes, I'm not sure whether it's a bug from ray or...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;mismatch;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
