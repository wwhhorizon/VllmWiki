# vllm-project/vllm#7882: [Bug]: Intermitted model load failure with error `Got async event : local catastrophic error` on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#7882](https://github.com/vllm-project/vllm/issues/7882) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Intermitted model load failure with error `Got async event : local catastrophic error` on A100

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: NVIDIA DGX Server (x86_64) GCC version: (GCC) 11.4.1 20230605 (Red Hat 11.4.1-2) Clang version: Could not collect CMake version: version 3.30.2 Libc version: glibc-2.34 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.14.0-362.24.1.el9_3.x86_64-x86_64-with-glibc2.34 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB GPU 2: NVIDIA A100-SXM4-40GB GPU 3: NVIDIA A100-SXM4-40GB GPU 4: NVIDIA A100-SXM4-40GB GPU 5: NVIDIA A100-SXM4-40GB GPU 6: NVIDIA A100-SXM4-40GB GPU 7: NVIDIA A100-SXM4-40GB Nvidia driver version: 550.54.15 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.9.1.1 /usr/lib64/libcudnn_adv.so.9.1.1 /usr/lib64/libcudnn_cnn.so.9.1.1 /usr/lib64/libcudnn_engines_precompiled.so.9.1.1 /usr/lib64/libcudnn_engines_runtime_compiled.so.9.1.1 /usr/lib64/libcudnn_graph.so.9.1.1 /usr/lib64/libcudnn_heur...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: NVIDIA DGX Server (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: load failure with error `Got async event : local catastrophic error` on A100 bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Intermitted model load failure with error `Got async event : local catastrophic error` on A100 bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug bu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: lure with error `Got async event : local catastrophic error` on A100 bug;stale ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rch==2.4.0 [pip3] torchvision==0.19.0 [pip3] transformers==4.44.0 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.1.3.1 pypi_0 pypi [conda] nvidia-cuda-cupti-cu12 12.1.105

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | a-env/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0xa0 (0x1471338b5600 in /home/openinference_svc/envs/vll… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | a-env/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x1471338be6fc in /home/openinference_svc/envs/vllmv0.… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | a-env/lib/python3.11/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdbbf4 (0x147181074bf4 in /home/openinference_svc/envs/vllmv0.5.4-sophia-env/bin/../… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
