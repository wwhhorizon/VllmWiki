# vllm-project/vllm#32862: [Bug]: llama4-fp8 tp=2 ep=2 doesn't work on b200

| 字段 | 值 |
| --- | --- |
| Issue | [#32862](https://github.com/vllm-project/vllm/issues/32862) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: llama4-fp8 tp=2 ep=2 doesn't work on b200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the following command: ``` vllm bench throughput --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 -tp=2 --enable-expert-parallel ``` Gets the following error: ``` (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] WorkerProc failed to start. (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] Traceback (most recent call last): (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] File "/home/ProExpertProg/git/vllm/vllm/v1/executor/multiproc_executor.py", line 737, in worker_main (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] worker = WorkerProc(*args, **kwargs) (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] File "/home/ProExpertProg/git/vllm/vllm/v1/executor/multiproc_executor.py", line 575, in __init__ (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] self.worker.load_model() (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] File "/home/Pro...

## 现有链接修复摘要

#32886 [Bugfix] Fix FP8 MoE EP Weight Loading for ModelOpt Llama4

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: llama4-fp8 tp=2 ep=2 doesn't work on b200 bug;stale ### Your current environment ### 🐛 Describe the bug Running the following command: ``` vllm bench throughput --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: llama4-fp8 tp=2 ep=2 doesn't work on b200 bug;stale ### Your current environment ### 🐛 Describe the bug Running the following command: ``` vllm bench throughput --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: llama4-fp8 tp=2 ep=2 doesn't work on b200 bug;stale ### Your current environment ### 🐛 Describe the bug Running the following command: ``` vllm bench throughput --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: oughput --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 -tp=2 --enable-expert-parallel ``` Gets the following error: ``` (Worker_TP1_EP1 pid=56590) ERROR 01-22 10:13:03 [multiproc_executor.py:766] WorkerProc failed to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32886](https://github.com/vllm-project/vllm/pull/32886) | closes_keyword | 0.95 | [Bugfix] Fix FP8 MoE EP Weight Loading for ModelOpt Llama4 | Fix FP8 MoE EP Weight Loading for ModelOpt Llama4 ## Purpose #32862 Add a version-guarded fallback in Llama4 MoE weight loading to avoid CPU FP8 indexing on older PyTorch releas |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
