# vllm-project/vllm#39158: [RFC][Test]: Unified Platform-Aware Test Skip Mechanism

| 字段 | 值 |
| --- | --- |
| Issue | [#39158](https://github.com/vllm-project/vllm/issues/39158) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC][Test]: Unified Platform-Aware Test Skip Mechanism

### Issue 正文摘录

### Motivation. vLLM currently supports **multiple platform targets** (CUDA, ROCm, TPU, XPU, CPU, OOT) and a growing matrix of device capabilities (SM75–SM120+). The test suite has accumulated **at least 22 distinct patterns** for platform-based skipping, totaling **~600+ scattered skip sites** across `tests/`: | Pattern | Approx. Count | |---------|--------------| | `@pytest.mark.skipif(not current_platform.is_cuda(), ...)` | ~75 | | Module-level `pytest.skip(..., allow_module_level=True)` | ~24 | | In-body `if not current_platform.is_cuda(): pytest.skip(...)` | ~362 | | `torch.cuda.is_available()` (violates platform abstraction) | ~47 | | `envs.VLLM_TARGET_DEVICE` checks | ~15 | | `has_device_capability(N)` / `is_device_capability_family(N)` | ~63 | Problems: 1. **No single source of truth** — each test author picks a different pattern. 2. **Hard to query** — CI cannot answer "which tests run on CUDA/ROCm?" without parsing arbitrary Python. 3. **Verbose and error-prone** — repetitive boilerplate in every test file. ## Goal Provide a **single, declarative, composable** way to express "this test requires platform X (and optionally capability Y)" that: - Composes with existing mark...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [RFC][Test]: Unified Platform-Aware Test Skip Mechanism RFC ### Motivation. vLLM currently supports **multiple platform targets** (CUDA, ROCm, TPU, XPU, CPU, OOT) and a growing matrix of device capabilities (SM75–SM120+...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: h** — each test author picks a different pattern. 2. **Hard to query** — CI cannot answer "which tests run on CUDA/ROCm?" without parsing arbitrary Python. 3. **Verbose and error-prone** — repetitive boilerplate in ever...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: atform, requires_capability @requires_platform("cuda") def test_cutlass_scaled_mm(): ... @requires_platform("cuda", "rocm") @requires_capability(90) def test_fp8_marlin(): ... # Module-level pytestmark = requires_platfo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: uires_platform, requires_capability @requires_platform("cuda") def test_cutlass_scaled_mm(): ... @requires_platform("cuda", "rocm") @requires_capability(90) def test_fp8_marlin(): ... # Module-level pytestmark = require...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rm: platforms = [platform] if isinstance(platform, str) else platform if not _matches_any(platforms): item.add_marker(pytest.mark.skip(...)) if exclude: excludes = [exclude] if isinstance(exclude, str) else exclud

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
