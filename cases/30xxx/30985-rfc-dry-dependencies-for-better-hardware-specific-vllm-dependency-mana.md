# vllm-project/vllm#30985: [RFC]: DRY Dependencies for Better Hardware-Specific vLLM Dependency Management

| 字段 | 值 |
| --- | --- |
| Issue | [#30985](https://github.com/vllm-project/vllm/issues/30985) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: DRY Dependencies for Better Hardware-Specific vLLM Dependency Management

### Issue 正文摘录

### Motivation. vLLM currently maintains **16 separate `requirements/*.txt` files** (cuda.txt, rocm.txt, tpu.txt, xpu.txt, cpu.txt, plus build/test variants) with **no centralized dependency specification for common dependencies**. This creates three critical issues: #### 1. No Single Source of Truth Creates CI Fragility - Each hardware target has **divergent torch versions**: - CUDA: `torch==2.9.0` - XPU: `torch==2.9.0+xpu` with custom index URLs - TPU: Completely different dependency set - **Non-CUDA builds discover breakages only after CUDA CI passes** → CI flakes and delayed feedback #### 2. Development vs CI Install Paths Have Diverged - Developers: `pip install -e .` → relies on `pyproject.toml` dynamic dependency resolution - CI: Explicitly installs from hardware-specific requirements files - **Result**: Changes that work locally fail in CI (or vice versa) - **Evidence**: pyproject.toml contains `# Should be mirrored in requirements/build.txt` admitting synchronization debt - **No guardrails** to detect drift until builds break #### 3. Lack of Automated Validation - When PyTorch or common dependencies are updated, manual effort required to validate across 16 files - High li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [RFC]: DRY Dependencies for Better Hardware-Specific vLLM Dependency Management RFC;stale ### Motivation. vLLM currently maintains **16 separate `requirements/*.txt` files** (cuda.txt, rocm.txt, tpu.txt, xpu.txt, cpu.tx...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: n. vLLM currently maintains **16 separate `requirements/*.txt` files** (cuda.txt, rocm.txt, tpu.txt, xpu.txt, cpu.txt, plus build/test variants) with **no centralized dependency specification for common dependencies**....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: /build.txt` admitting synchronization debt - **No guardrails** to detect drift until builds break #### 3. Lack of Automated Validation - When PyTorch or common dependencies are updated, manual effort required to validat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Dependencies for Better Hardware-Specific vLLM Dependency Management RFC;stale ### Motivation. vLLM currently maintains **16 separate `requirements/*.txt` files** (cuda.txt, rocm.txt, tpu.txt, xpu.txt, cpu.txt, plus bui...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: mprovements** ### Proposed Change. Implement a setuptools custom build backend that **uses `VLLM_TARGET_DEVICE` as the single source of truth**: ```toml [build-system] requires = ["setuptools"] build-backend = "backend"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
