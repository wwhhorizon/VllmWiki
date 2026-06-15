# vllm-project/vllm#40620: [RFC]: Unified Device Capability Abstraction for Cross-Platform Feature Detection

| 字段 | 值 |
| --- | --- |
| Issue | [#40620](https://github.com/vllm-project/vllm/issues/40620) |
| 状态 | open |
| 标签 | rocm;RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Unified Device Capability Abstraction for Cross-Platform Feature Detection

### Issue 正文摘录

### Motivation. This is an AI-generated proposal, there may be some error. appreciate if you can point out. ## 1. Problem Summary As raised by @tjtanaa in [#39158](https://github.com/vllm-project/vllm/issues/39158), the current `has_device_capability(int)` / `is_device_capability_family(int)` API is **fundamentally CUDA-centric** and does **not** translate correctly to ROCm or XPU. ### 1.1 Problem A: `device_capability` is inherently a CUDA concept `torch.cuda.get_device_capability()` returns `(major, minor)` tied to NVIDIA's SM (Streaming Multiprocessor) versioning. **ROCm and XPU have completely different hardware models** — any mapping to CUDA-style numbers is artificial and lossy: | Platform | Capability Model | How it works | |----------|-----------------|--------------| | **CUDA** | SM version `(major, minor)` e.g. `(8,9)`, `(9,0)`, `(10,0)` | Native `torch.cuda.get_device_capability()` | | **ROCm** | GCN arch string (e.g. `gfx942`) → **artificially mapped** to `(major, minor)` | Semantic mismatch: `gfx90a` maps to `(9,0)` but has NO FP8, while CUDA's `(9,0)` = Hopper = has FP8 | | **XPU** | No capability model → always returns `None` → all checks = `False` | All feature gat...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 13: [RFC]: Unified Device Capability Abstraction for Cross-Platform Feature Detection rocm;RFC ### Motivation. This is an AI-generated proposal, there may be some error. appreciate if you can point out. ## 1. Problem Summar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: (major, minor)` | Semantic mismatch: `gfx90a` maps to `(9,0)` but has NO FP8, while CUDA's `(9,0)` = Hopper = has FP8 | | **XPU** | No capability model → always returns `None` → all checks = `False` | All feature gates...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: amily(100)` and `is_device_capability_family(120)` separately (e.g., in `cutlass_moe.py`), and this will only get worse. ### 1.3 Problem C: Cross-platform semantic mismatch The same numeric value means **completely diff...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vation. This is an AI-generated proposal, there may be some error. appreciate if you can point out. ## 1. Problem Summary As raised by @tjtanaa in [#39158](https://github.com/vllm-project/vllm/issues/39158), the current...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: (e.g. `gfx942`) → **artificially mapped** to `(major, minor)` | Semantic mismatch: `gfx90a` maps to `(9,0)` but has NO FP8, while CUDA's `(9,0)` = Hopper = has FP8 | | **XPU** | No capability model → always returns `Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
