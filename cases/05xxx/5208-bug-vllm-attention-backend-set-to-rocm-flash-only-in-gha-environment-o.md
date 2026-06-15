# vllm-project/vllm#5208: [Bug]: VLLM_ATTENTION_BACKEND set to ROCM_FLASH only in GHA environment, overriding automatic backend selection; this breaks other kernel unit tests.

| 字段 | 值 |
| --- | --- |
| Issue | [#5208](https://github.com/vllm-project/vllm/issues/5208) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM_ATTENTION_BACKEND set to ROCM_FLASH only in GHA environment, overriding automatic backend selection; this breaks other kernel unit tests.

### Issue 正文摘录

### Your current environment Note: I only observe this problem when the tests are automatically executed by GitHub actions (GHA); as I do not have access to the GHA compute, I cannot provide an environment variable dump. However, I *do not* observe this issue on my development machine. The environment dump *from my development machine which does not exhibit this issue* is provided below: ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.28.3 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-26-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.103 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA RTX A4000 GPU 1: NVIDIA RTX A4000 GPU 2: NVIDIA RTX A4000 GPU 3: NVIDIA RTX A4000 Nvidia driver version: 545.23.08 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.s...

## 现有链接修复摘要

#5210 [Bugfix]: During testing, use pytest monkeypatch for safely overriding the env var that indicates the vLLM backend

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: s provided below: ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: VLLM_ATTENTION_BACKEND set to ROCM_FLASH only in GHA environment, overriding automatic backend selection; this breaks other kernel unit tests. bug ### Your current environment Note: I only observe this problem wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: exhibit this issue* is provided below: ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: VLLM_ATTENTION_BACKEND set to ROCM_FLASH only in GHA environment, overriding automatic backend selection; this breaks other kernel unit tests. bug ### Your current environment Note: I only observe this problem wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: d_ppin arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip rdpid overflow_recov succor smca sev sev_es Virtualization: AMD-V...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5210](https://github.com/vllm-project/vllm/pull/5210) | closes_keyword | 0.95 | [Bugfix]: During testing, use pytest monkeypatch for safely overriding the env var that indicates the vLLM backend | FIX #5208 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
