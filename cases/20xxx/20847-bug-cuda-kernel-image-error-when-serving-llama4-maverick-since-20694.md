# vllm-project/vllm#20847: [Bug]: CUDA kernel image error when serving Llama4 Maverick since #20694

| 字段 | 值 |
| --- | --- |
| Issue | [#20847](https://github.com/vllm-project/vllm/issues/20847) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA kernel image error when serving Llama4 Maverick since #20694

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following maverick serving is failing due to kernel image issue. This starts with #20694 @mgoin ```bash CUDA_LAUNCH_BLOCKING=1 vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --max_model_len 8192 --kv_cache_dtype fp8 --enable-expert-parallel --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.9 --disable-log-requests --enforce_eager 2>&1 ``` There is a relevant issue with different exception stack - #20832 cc @luccafong @yeqcharlotte @houseroad ``` (VllmWorker rank=3 pid=1043748) ERROR 07-11 15:51:29 [multiproc_executor.py:522] WorkerProc hit an exception. (VllmWorker rank=3 pid=1043748) ERROR 07-11 15:51:29 [multiproc_executor.py:522] Traceback (most recent call last): (VllmWorker rank=3 pid=1043748) ERROR 07-11 15:51:29 [multiproc_executor.py:522] File "/data/users/yming/gitrepos/vllm/vllm/v1/executor/multiproc_executor.py", line 517, in worker_busy_loop (VllmWorker rank=3 pid=1043748) ERROR 07-11 15:51:29 [multiproc_executor.py:522] output = func(*args, **kwargs) (VllmWorker rank=3 pid=1043748) ERROR 07-11 15:51:29 [multiproc_executor.py:522] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=3 pid=104...

## 现有链接修复摘要

#20694 Use NVCC `--compress-mode` to reduce binary size by 30%

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ker rank=3 pid=1043748) ERROR 07-11 15:51:29 [multiproc_executor.py:522] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` ### Before submitting a new issue... - [x] Make sure you already searched...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: UNCH_BLOCKING=1 vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 --max_model_len 8192 --kv_cache_dtype fp8 --enable-expert-parallel --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.9 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA kernel image error when serving Llama4 Maverick since #20694 bug ### Your current environment ### 🐛 Describe the bug The following maverick serving is failing due to kernel image issue. This starts with #206...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: CUDA kernel image error when serving Llama4 Maverick since #20694 bug ### Your current environment ### 🐛 Describe the bug The following maverick serving is failing due to kernel image issue. This starts with #206...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 17B-128E-Instruct-FP8 --max_model_len 8192 --kv_cache_dtype fp8 --enable-expert-parallel --tensor-parallel-size 8 --trust-remote-code --gpu-memory-utilization 0.9 --disable-log-requests --enforce_eager 2>&1 ``` There is...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20694](https://github.com/vllm-project/vllm/pull/20694) | mentioned | 0.45 | Use NVCC `--compress-mode` to reduce binary size by 30% | verick serving is failing due to kernel image issue. this starts with #20694 @mgoin ```bash cuda_launch_blocking=1 vllm serve meta-llama/llama-4-maverick-17b-128e-instruct-fp8 --m… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
