# vllm-project/vllm#44305: [Bug]: FlashInfer sampler JIT fails on Blackwell SM120f with CUDA 13.3: CUDA compiler and toolkit headers are incompatible

| 字段 | 值 |
| --- | --- |
| Issue | [#44305](https://github.com/vllm-project/vllm/issues/44305) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer sampler JIT fails on Blackwell SM120f with CUDA 13.3: CUDA compiler and toolkit headers are incompatible

### Issue 正文摘录

### Your current environment --2026-06-02 17:33:54-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.108.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected. HTTP request sent, awaiting response... ### 🐛 Describe the bug ## Description I hit a FlashInfer sampler JIT compilation failure when launching vLLM with a Qwen3.5 model on NVIDIA RTX PRO 6000 Blackwell GPUs. The model can be loaded by Transformers and vLLM can create the engine config successfully. vLLM also starts and responds correctly if I disable FlashInfer sampler with: ```bash VLLM_USE_FLASHINFER_SAMPLER=0 ``` However, when FlashInfer sampler is enabled, vLLM fails during startup while running the dummy sampler/profile stage. The failure happens in FlashInfer JIT compilation for cached_ops/sampling. ## Environment ``` GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition Architecture: SM120f / compute_120f Python: 3.12.13 PyTorch: 2.11.0+cu130 torch.version.cuda: 13.0 vLLM: 0.22.1rc1.dev58+g68dafcca7 Transformers: 5.9.0 FlashInfe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ]: FlashInfer sampler JIT fails on Blackwell SM120f with CUDA 13.3: CUDA compiler and toolkit headers are incompatible bug ### Your current environment --2026-06-02 17:33:54-- https://raw.githubusercontent.com/vllm-proj...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: FlashInfer sampler JIT fails on Blackwell SM120f with CUDA 13.3: CUDA compiler and toolkit headers are incompatible bug ### Your current environment --2026-06-02 17:33:54-- https://raw.githubusercontent.com/vllm-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: a FlashInfer sampler JIT compilation failure when launching vLLM with a Qwen3.5 model on NVIDIA RTX PRO 6000 Blackwell GPUs. The model can be loaded by Transformers and vLLM can create the engine config successfully. vL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .com (raw.githubusercontent.com)|185.199.110.133|:443... connected. HTTP request sent, awaiting response... ### 🐛 Describe the bug ## Description I hit a FlashInfer sampler JIT compilation failure when launching vLLM wi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: er is enabled, vLLM fails during startup while running the dummy sampler/profile stage. The failure happens in FlashInfer JIT compilation for cached_ops/sampling. ## Environment ``` GPU: NVIDIA RTX PRO 6000 Blackwell Se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
