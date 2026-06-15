# vllm-project/vllm#5206: [Bug]: Detokenize delay when update vllm from 0.3.0 to 0.4.2

| 字段 | 值 |
| --- | --- |
| Issue | [#5206](https://github.com/vllm-project/vllm/issues/5206) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Detokenize delay when update vllm from 0.3.0 to 0.4.2

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3.1-2) Clang version: 3.4.2 (tags/RELEASE_34/dot2-final) CMake version: version 3.29.3 Libc version: glibc-2.17 Python version: 3.10.12 (main, Jul 5 2023, 18:54:27) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.18.0-193.28.1.el8_2.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A800-SXM4-80GB GPU 1: NVIDIA A800-SXM4-80GB Nvidia driver version: 525.125.06 cuDNN version: Probably one of the following: /usr/lib64/libcudnn.so.8.0.5 /usr/lib64/libcudnn_adv_infer.so.8.0.5 /usr/lib64/libcudnn_adv_train.so.8.0.5 /usr/lib64/libcudnn_cnn_infer.so.8.0.5 /usr/lib64/libcudnn_cnn_train.so.8.0.5 /usr/lib64/libcudnn_ops_infer.so.8.0.5 /usr/lib64/libcudnn_ops_train.so.8.0.5 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn.so.8.9.5 /usr/local/cuda/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.5 /usr/local/c...

## 现有链接修复摘要

#5207 [BugFix] Apply get_cached_tokenizer to the tokenizer setter of LLM

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat 9.3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 0.4.2 bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: torch==2.3.0 [pip3] torchaudio==2.3.0 [pip3] torchvision==0.18.0 [pip3] triton==2.3.0 [pip3] vllm-nccl-cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 9.3.1 20200408 (Red Hat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5207](https://github.com/vllm-project/vllm/pull/5207) | closes_keyword | 0.95 | [BugFix] Apply get_cached_tokenizer to the tokenizer setter of LLM | FIX #5206 FIX #5240 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown r |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
