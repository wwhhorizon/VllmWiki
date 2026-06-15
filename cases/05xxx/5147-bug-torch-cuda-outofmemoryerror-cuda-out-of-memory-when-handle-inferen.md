# vllm-project/vllm#5147: [Bug]: torch.cuda.OutOfMemoryError: CUDA out of memory when Handle inference requests

| 字段 | 值 |
| --- | --- |
| Issue | [#5147](https://github.com/vllm-project/vllm/issues/5147) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.cuda.OutOfMemoryError: CUDA out of memory when Handle inference requests

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.31 Python version: 3.8.10 (default, Nov 22 2023, 10:22:35) [GCC 9.4.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.29 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.104.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.7.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.7.0 HIP runtime version: N/...

## 现有链接修复摘要

#5355 [Bugfix] Take the VRAM usage of prompt_logprobs into account

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: of `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: torch.cuda.OutOfMemoryError: CUDA out of memory when Handle inference requests bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch ve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nvironment information... PyTorch version: 2.2.1+cu118 Is debug build: False CUDA used to build PyTorch: 11.8 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.5 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.1)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: torch.cuda.OutOfMemoryError: CUDA out of memory when Handle inference requests bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch versio...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5355](https://github.com/vllm-project/vllm/pull/5355) | closes_keyword | 0.95 | [Bugfix] Take the VRAM usage of prompt_logprobs into account | FIX #5147 FIX #5274 FIX #5550 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist ( |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
