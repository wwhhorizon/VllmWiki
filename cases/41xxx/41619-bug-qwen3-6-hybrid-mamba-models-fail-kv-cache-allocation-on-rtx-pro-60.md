# vllm-project/vllm#41619: [Bug]: Qwen3.6 hybrid Mamba models fail KV cache allocation on RTX PRO 6000 Blackwell + WSL2 — 16 GiB invisible CUDA overhead

| 字段 | 值 |
| --- | --- |
| Issue | [#41619](https://github.com/vllm-project/vllm/issues/41619) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.6 hybrid Mamba models fail KV cache allocation on RTX PRO 6000 Blackwell + WSL2 — 16 GiB invisible CUDA overhead

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary vLLM (and SGLang) cannot load any Qwen3.6 / Qwen3.5 family models (Qwen3_5ForConditionalGeneration / Qwen3_5MoeForConditionalGeneration architecture) on RTX PRO 6000 Blackwell Workstation Edition (96 GB VRAM, sm_120) under WSL2 Ubuntu 22.04. The model loads to GPU successfully (~30 GB), but allocation of the Mamba state cache fails with `torch.OutOfMemoryError: CUDA out of memory. Tried to allocate X GiB. GPU has 95.59 GiB total of which 50+ GiB is free`. The "non-PyTorch memory in use" reported by torch is **16 GiB** on this WSL2 setup (vs ~1-2 GiB normal on native Linux). This abnormal CUDA driver overhead consumes memory invisibly and causes the contiguous Mamba state allocation to fail. ## Reproduction ### Hardware - GPU: NVIDIA RTX PRO 6000 Blackwell Workstation Edition (compute 12.0, sm_120, 97887 MiB VRAM) - CPU: Intel Core i5-13400F - RAM: 32 GB ### Software - Host: Windows 11 IoT Enterprise LTSC, build 26100 - NVIDIA driver: tested **596.36** AND **581.80 (RTX Enterprise)** — same result - WSL: WSL 2.6.3.0, kernel 6.6.87.2-microsoft-standard-WSL2 - Distro: Ubuntu 22.04.5 LTS - Python 3.10.12 - CUDA: tested cu1...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: |--------------|---------------------------|--------| | Qwen/Qwen3.6-27B-FP8 | Qwen3_5ForConditionalGeneration | 3.77 GB | OOM | | Qwen/Qwen3.6-35B-A3B-FP8 | Qwen3_5MoeForConditionalGeneration (MoE) | 4.99 GB | OOM | Al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Qwen3.6 hybrid Mamba models fail KV cache allocation on RTX PRO 6000 Blackwell + WSL2 — 16 GiB invisible CUDA overhead bug ### Your current environment ### 🐛 Describe the bug ## Summary vLLM (and SGLang) cannot l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3.6 hybrid Mamba models fail KV cache allocation on RTX PRO 6000 Blackwell + WSL2 — 16 GiB invisible CUDA overhead bug ### Your current environment ### 🐛 Describe the bug ## Summary vLLM (and SGLang) cannot l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 400F - RAM: 32 GB ### Software - Host: Windows 11 IoT Enterprise LTSC, build 26100 - NVIDIA driver: tested **596.36** AND **581.80 (RTX Enterprise)** — same result - WSL: WSL 2.6.3.0, kernel 6.6.87.2-microsoft-standard-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: Qwen3.6 hybrid Mamba models fail KV cache allocation on RTX PRO 6000 Blackwell + WSL2 — 16 GiB invisible CUDA overhead bug ### Your current environment ### 🐛 Describe the bug ## Summary vLLM (and SGLang) cannot l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
