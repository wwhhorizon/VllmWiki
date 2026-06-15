# vllm-project/vllm#43323: [Feature]: Performance Tiers: Apple-style hardware requirements for stable inference

| 字段 | 值 |
| --- | --- |
| Issue | [#43323](https://github.com/vllm-project/vllm/issues/43323) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;moe |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Performance Tiers: Apple-style hardware requirements for stable inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## The Problem (2.5 Years Unsolved) vLLM tries to support everything — CUDA, ROCm, CPU, Apple Silicon, TPU. The result? Hundreds of configuration flags, cryptic docs, and users spending hours tuning PagedAttention only to get `OutOfMemory` or suboptimal performance. "The project that tries to catch two hares catches neither." vLLM chases both universal compatibility and ease of use — and fails at both for the average user. ## The Solution: Performance Tiers Stop trying to run everywhere. Start running perfectly where it matters. Just as Apple doesn't support every hardware configuration — but delivers a flawless experience on supported devices — vLLM should define clear, enforceable system requirements. ### Three Tiers **Minimum** - Requirements: 16 GB VRAM, 32 GB RAM - Context Length: Up to 8K tokens - Use Case: Development, testing **Recommended** - Requirements: 24 GB VRAM, 64 GB RAM - Context Length: Up to 32K tokens - Use Case: Production, single-user **Optimal** - Requirements: 48+ GB VRAM, 128 GB RAM - Context Length: Up to 128K tokens - Use Case: Enterprise, multi-user ### How It Works 1. **Hardware Detection**: On startup, vLLM chec...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ## The Problem (2.5 Years Unsolved) vLLM tries to support everything — CUDA, ROCm, CPU, Apple Silicon, TPU. The result? Hundreds of configuration flags, cryptic docs, and users spending hours tuning PagedAttention only...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: verything — CUDA, ROCm, CPU, Apple Silicon, TPU. The result? Hundreds of configuration flags, cryptic docs, and users spending hours tuning PagedAttention only to get `OutOfMemory` or suboptimal performance. "The projec...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: eded. No rewrite. Tiers are opt-in for new projects. **Escape hatch for experts**: `tier="legacy"` preserves all existing flags. No hidden parameters. No `_override` hacks. Explicit and documented. License for this prop...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: AM, 32 GB RAM - Context Length: Up to 8K tokens - Use Case: Development, testing **Recommended** - Requirements: 24 GB VRAM, 64 GB RAM - Context Length: Up to 32K tokens - Use Case: Production, single-user **Optimal** -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for edge cases**: This is what created the current mess. **Hardware-specific forks** (e.g., tiny-vllm): Fragments the ecosystem, duplicates maintenance effort. **Status quo**: Continue supporting everything poorly vs. s...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
