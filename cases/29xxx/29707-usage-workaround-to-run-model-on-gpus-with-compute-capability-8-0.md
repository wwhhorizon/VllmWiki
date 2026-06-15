# vllm-project/vllm#29707: [Usage]: Workaround to run model on GPUs with Compute Capability < 8.0?

| 字段 | 值 |
| --- | --- |
| Issue | [#29707](https://github.com/vllm-project/vllm/issues/29707) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Workaround to run model on GPUs with Compute Capability < 8.0?

### Issue 正文摘录

### Your current environment Problem: I am unable to run the Qwen3-VL-32B-Instruct-AWQ-4bit model due to a CUDA compute capability requirement. My hardware consists of two NVIDIA QUADRO RTX 5000 cards (16GB each, 32GB total) with a compute capability of 7.5. The software framework (likely a recent version of PyTorch or a specific library) raises an error: "GPUs with compute capability = 8 ERROR 11-29 20:52:08 [fa_utils.py:57] Cannot use FA version 2 is not supported due to FA2 is only supported on devices with compute capability >= 8 INFO 11-29 20:52:11 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_bffa6a1b'), local_subscribe_addr='ipc:///tmp/6257d372-f203-4a0e-94d8-8c768328eb43', remote_subscribe_addr=None, remote_addr_ipv6=False) INFO 11-29 20:52:11 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_d3ed3511'), local_subscribe_addr='ipc:///tmp/01782614-de40-4a90-a115-8461024c4cb4', remote_subscribe_addr=None, remote_addr_ipv6=False) [Gloo] Rank 1 is connected to 1 peer ranks. Expected number of connected peer ranks...

## 现有链接修复摘要

#29732 [Quantization] Enable compressed-tensors AWQ for Turing GPU

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ith a compute capability of 7.5. The software framework (likely a recent version of PyTorch or a specific library) raises an error: "GPUs with compute capability = 8 ERROR 11-29 20:52:08 [fa_utils.py:57] Cannot use FA v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Workaround to run model on GPUs with Compute Capability < 8.0? usage ### Your current environment Problem: I am unable to run the Qwen3-VL-32B-Instruct-AWQ-4bit model due to a CUDA compute capability requiremen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Usage]: Workaround to run model on GPUs with Compute Capability < 8.0? usage ### Your current environment Problem: I am unable to run the Qwen3-VL-32B-Instruct-AWQ-4bit model due to a CUDA compute capability requiremen...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ed as DP rank 0, PP rank 0, TP rank 1, EP rank 1 WARNING 11-29 20:52:14 [topk_topp_sampler.py:66] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: capability >= 8 INFO 11-29 20:52:11 [shm_broadcast.py:289] vLLM message queue communication handle: Handle(local_reader_ranks=[0], buffer_handle=(1, 10485760, 10, 'psm_bffa6a1b'), local_subscribe_addr='ipc:///tmp/6257d3...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29732](https://github.com/vllm-project/vllm/pull/29732) | closes_keyword | 0.95 | [Quantization] Enable compressed-tensors AWQ for Turing GPU | Fix #29707 - Compressed-tensors AWQ quantization should be able to run on Turing GPU, verified on Tesla T4 GPU ## Test Plan Tested with `cpatonn/Qwen3-VL-32B-Instruct-AWQ-4bit` on |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
