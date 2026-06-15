# vllm-project/vllm#7160: [Bug]: InternVL2 Mismatch in number of image tokens and image embedding size

| 字段 | 值 |
| --- | --- |
| Issue | [#7160](https://github.com/vllm-project/vllm/issues/7160) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL2 Mismatch in number of image tokens and image embedding size

### Issue 正文摘录

### Your current environment ```text Collecting environment information... /opt/aritra.c/worktree/vllm-main/vllm/connections.py:8: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 11 (bullseye) (x86_64) GCC version: (Debian 10.2.1-6) 10.2.1 20210110 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.31 Python version: 3.10.14 | packaged by conda-forge | (main, Mar 20 2024, 12:45:18) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-5.10.0-30-cloud-amd64-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 GPU 2: NVIDIA H100 80GB HBM3 GPU 3: NVIDIA H100 80GB HBM3 GPU 4: NVIDIA H100 80GB HBM3 GPU 5: NVIDIA H100 80GB HBM3 GPU 6: NVIDIA H100 80GB HBM3 GPU 7: NVIDIA H100 80GB HBM3 Nvidia driver version: 550.54.15 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime...

## 现有链接修复摘要

#7164 [Bugfix] Fix input processor for InternVL2 model

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build Py...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: InternVL2 Mismatch in number of image tokens and image embedding size bug ### Your current environment ```text Collecting environment information... /opt/aritra.c/worktree/vllm-main/vllm/connections.py:8: Runtime...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: InternVL2 Mismatch in number of image tokens and image embedding size bug ### Your current environment ```text Collecting environment information... /opt/aritra.c/worktree/vllm-main/vllm/connections.py:8: Runtime...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 arat avx512vbmi umip avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpop cntdq rdpid cldemote movdiri movdir64b fsrm md_cl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: .4.0.post0 [pip3] torchvision==0.19.0 [pip3] transformers==4.43.3 [pip3] triton==3.0.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] pytorch-lightning 2.3.3

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7164](https://github.com/vllm-project/vllm/pull/7164) | closes_keyword | 0.95 | [Bugfix] Fix input processor for InternVL2 model | FIX #7160 FIX #7272 - This PR also aims to make some small refactor to fix some hidden issues. ~~So I marked it as a draft.~~ - Since most of process args can be obtained from |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
