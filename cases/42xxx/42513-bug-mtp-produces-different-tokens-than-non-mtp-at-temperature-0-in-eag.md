# vllm-project/vllm#42513: [Bug]: MTP produces different tokens than non-MTP at temperature=0 in eager mode

| 字段 | 值 |
| --- | --- |
| Issue | [#42513](https://github.com/vllm-project/vllm/issues/42513) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;gemm_linear;hardware_porting;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cache;cuda;gemm;kernel;triton |
| 症状 | build_error;mismatch;nondeterministic |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: MTP produces different tokens than non-MTP at temperature=0 in eager mode

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.1 LTS (x86_64) GCC version : (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ============================== Python Environment ============================== Python version : 3.10.8 ============================== CUDA / GPU Info ============================== GPU models and configuration : NVIDIA GeForce RTX 3090 (24GB) Nvidia driver version : 580.76.05 CUDA Version : 13.0 ============================== Versions of relevant libraries ============================== flashinfer-python : 0.6.6 nvidia-cublas-cu12 : 12.8.4.1 nvidia-cuda-runtime-cu12 : 12.8.90 nvidia-cudnn-cu12 : 9.10.2.21 torch : 2.10.0 transformers : 4.57.6 triton : 3.6.0 ============================== vLLM Info ============================== vLLM Version : 0.19.1 CUDA Archs : Not Set; ROCm: Disabled Attention Backend : FLASH_ATTN (FlashAttention v2) ### 🐛 Describe the bug MTP n=1 produces different token sequences than non-...

## 现有链接修复摘要

#38938 Bug/test eagle dp v0

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 7: han non-MTP decoding at temperature=0 when enforce_eager=True. The first mismatch occurs at a consistent, reproducible position (e.g., pos 99 for "Hello, my name is"). With enforce_eager=False (CUDA graph enabled), outp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ========= OS : Ubuntu 22.04.1 LTS (x86_64) GCC version : (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version :
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ============================== Python Environment ============================== Python version : 3.10.8 ============================== CUD...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ========== Versions of relevant libraries ============================== flashinfer-python : 0.6.6 nvidia-cublas-cu12 : 12.8.4.1 nvidia-cuda-runtime-cu12 : 12.8.90 nvidia-cudnn-cu12 : 9.10.2.21 torch : 2.10.0 transforme...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: use chain: MTP verification forward uses batch_size=2 (original token + draft token), non-MTP decode uses batch_size=1 In eager mode, cuBLAS auto-tuner selects different GEMM algorithms for different batch sizes, with d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38938](https://github.com/vllm-project/vllm/pull/38938) | mentioned | 0.45 | Bug/test eagle dp v0 | ring identical kernel launch at every step. this is distinct from pr #38938 (which fixed batch invariance for lm_head and rmsnorm under eagle). the attention gemm itself is not co… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
