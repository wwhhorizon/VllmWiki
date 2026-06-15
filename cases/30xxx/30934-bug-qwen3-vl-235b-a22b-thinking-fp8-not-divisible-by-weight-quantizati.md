# vllm-project/vllm#30934: [Bug]:  Qwen3-VL-235B-A22B-Thinking-FP8 not divisible by weight quantization block_n = 128.

| 字段 | 值 |
| --- | --- |
| Issue | [#30934](https://github.com/vllm-project/vllm/issues/30934) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Qwen3-VL-235B-A22B-Thinking-FP8 not divisible by weight quantization block_n = 128.

### Issue 正文摘录

### Your current environment I am trying to run FP8 version on 8*A100 GPUs but I encountered `ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128.` The backtrace is as follows, ``` (Worker_TP4 pid=2755748) INFO 12-18 14:30:15 [fp8.py:159] Using Marlin backend for FP8 MoE (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] WorkerProc failed to start. (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] Traceback (most recent call last): (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] File "/mnt/vlm/common/env/vllm/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 715, in worker_main (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] worker = WorkerProc(*args, **kwargs) (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] File "/mnt/vlm/common/env/vllm/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 555, in __init__ (Worker_TP1 pid=2755745) ERROR 12-18 14:30:1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Qwen3-VL-235B-A22B-Thinking-FP8 not divisible by weight quantization block_n = 128. bug ### Your current environment I am trying to run FP8 version on 8*A100 GPUs but I encountered `ValueError: The output_size of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: block_n = 128. bug ### Your current environment I am trying to run FP8 version on 8*A100 GPUs but I encountered `ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3-VL-235B-A22B-Thinking-FP8 not divisible by weight quantization block_n = 128. bug ### Your current environment I am trying to run FP8 version on 8*A100 GPUs but I encountered `ValueError: The output_size of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 8. bug ### Your current environment I am trying to run FP8 version on 8*A100 GPUs but I encountered `ValueError: The output_size of gate's and up's weight = 192 is not divisible by weight quantization block_n = 128.` Th...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: d=2755748) INFO 12-18 14:30:15 [fp8.py:159] Using Marlin backend for FP8 MoE (Worker_TP1 pid=2755745) ERROR 12-18 14:30:15 [multiproc_executor.py:743] WorkerProc failed to start. (Worker_TP1 pid=2755745) ERROR 12-18 14:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
