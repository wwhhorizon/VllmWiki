# vllm-project/vllm#35021: [Bug]: GLM-5（Sparse MLA / DSA 模型）无法在 sm80 GPU（A100/A800）上运行 — DeepGemm 硬依赖无 fallback

| 字段 | 值 |
| --- | --- |
| Issue | [#35021](https://github.com/vllm-project/vllm/issues/35021) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;moe;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-5（Sparse MLA / DSA 模型）无法在 sm80 GPU（A100/A800）上运行 — DeepGemm 硬依赖无 fallback

### Issue 正文摘录

### Current environment ``` vLLM version: latest main (commit 1391378) PyTorch version: 2.7.0+cu126 GPU: 8x NVIDIA A800-SXM4-80GB (sm80, Ampere) OS: Ubuntu 22.04, Linux 5.15.0 ``` ### Model [ZhipuAI/GLM-5-FP8](https://huggingface.co/ZhipuAI/GLM-5-FP8) (744B total / 40B active, 256 experts, 78 layers, `GlmMoeDsaForCausalLM`) ### 🐛 Describe the bug GLM-5 and other models using **DeepSeek Sparse Attention (DSA)** cannot run on **sm80 GPUs** (A100/A800). There are **multiple layers** of sm80 incompatibility, not just a single missing fallback. ### How to reproduce ```bash python -m vllm.entrypoints.openai.api_server \ --model ZhipuAI/GLM-5-FP8 \ --tensor-parallel-size 8 \ --max-model-len 8192 \ --cpu-offload-gb 20 \ --gpu-memory-utilization 0.95 \ --trust-remote-code \ --enforce-eager \ --port 8000 ``` ### Root cause analysis (updated) > **Correction:** The original description oversimplified the problem as only a missing DeepGemm fallback in `sparse_attn_indexer.py`. After thorough testing, we found there are **at least 3 layers** of sm80 incompatibility: | Layer | Problem | Details | |-------|---------|--------| | **1. C++ compilation** | `dsv3_fused_a_gemm` in `csrc/ops.h` / `csrc/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: /A800）上运行 — DeepGemm 硬依赖无 fallback bug ### Current environment ``` vLLM version: latest main (commit 1391378) PyTorch version: 2.7.0+cu126 GPU: 8x NVIDIA A800-SXM4-80GB (sm80, Ampere) OS: Ubuntu 22.04, Linux 5.15.0 ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: GLM-5（Sparse MLA / DSA 模型）无法在 sm80 GPU（A100/A800）上运行 — DeepGemm 硬依赖无 fallback bug ### Current environment ``` vLLM version: latest main (commit 1391378) PyTorch version: 2.7.0+cu126 GPU: 8x NVIDIA A800-SXM4-80GB...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: g]: GLM-5（Sparse MLA / DSA 模型）无法在 sm80 GPU（A100/A800）上运行 — DeepGemm 硬依赖无 fallback bug ### Current environment ``` vLLM version: latest main (commit 1391378) PyTorch version: 2.7.0+cu126 GPU: 8x NVIDIA A800-SXM4-80GB (sm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 0, Ampere) OS: Ubuntu 22.04, Linux 5.15.0 ``` ### Model [ZhipuAI/GLM-5-FP8](https://huggingface.co/ZhipuAI/GLM-5-FP8) (744B total / 40B active, 256 experts, 78 layers, `GlmMoeDsaForCausalLM`) ### 🐛 Describe the bug GLM-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: IA A800-SXM4-80GB (sm80, Ampere) OS: Ubuntu 22.04, Linux 5.15.0 ``` ### Model [ZhipuAI/GLM-5-FP8](https://huggingface.co/ZhipuAI/GLM-5-FP8) (744B total / 40B active, 256 experts, 78 layers, `GlmMoeDsaForCausalLM`) ### 🐛...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
