# vllm-project/vllm#41376: [CI/Build] pre-commit pip-compile fails for ~half of recent PRs: PyPI quarantined the `lightning` project

| 字段 | 值 |
| --- | --- |
| Issue | [#41376](https://github.com/vllm-project/vllm/issues/41376) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [CI/Build] pre-commit pip-compile fails for ~half of recent PRs: PyPI quarantined the `lightning` project

### Issue 正文摘录

### Summary PyPI has flagged the [`lightning`](https://pypi.org/project/lightning/) project as `quarantined`. The simple index returns ` ` with **zero release files** exposed: ``` $ curl -s https://pypi.org/simple/lightning/ | head Links for lightning Links for lightning ``` Every published `terratorch` version transitively requires `lightning`, and `torchgeo==0.7.0` (in `requirements/test/rocm.in`) requires `lightning[pytorch-extra]`. As a result the `pip-compile` and `pip-compile-rocm` pre-commit hooks abort with `× No solution found ... Because there are no versions of lightning ...`. Pre-releases do not help (the quarantine hides everything). ### Affected `pre-commit` is failing on every PR that triggers re-resolution. Sampled 12 recent open PRs touched today: 6 fail, 2 pass (stale, ran before the quarantine), 3 skipped, 1 too new. Examples of failing PRs: #40808, #41255, #41318, #41366. Main commit `ff449b6426` shows `pre-commit: success` but only because that status was recorded before the quarantine; re-running `pre-commit` on `main` HEAD now reproduces the failure. ### Root cause confirmation Reproduces locally with `uv` 0.9.26: ``` $ echo 'terratorch>=1.2.2' > probe.in $...

## 现有链接修复摘要

#40808 [Bugfix] Disable FlashInfer CUTLASS MoE on SM110 (Jetson Thor AGX) | #41255 [Perf] Intergrate Tile Kernels `head_compute_mix_kernel` for Deepseek-V4 | #41318 [Feat] dnnl build for AVX2 W8A8 Int8 | #41377 [CI/Build] Skip terratorch + torchgeo while PyPI has lightning quarantined

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI/Build] pre-commit pip-compile fails for ~half of recent PRs: PyPI quarantined the `lightning` project ### Summary PyPI has flagged the [`lightning`](https://pypi.org/project/lightning/) project as `quarantined`. The
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ively requires `lightning`, and `torchgeo==0.7.0` (in `requirements/test/rocm.in`) requires `lightning[pytorch-extra]`. As a result the `pip-compile` and `pip-compile-rocm` pre-commit hooks abort with `× No solution fou...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pment ci_build;hardware_porting cuda build_error #40808 [Bugfix] Disable FlashInfer CUTLASS MoE on SM110 (Jetson Thor AGX) | #41255 [Perf] Intergrate Tile Kernels `head_compute_mix_kernel` for Deepseek-V4 | #41318 [Feat...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: corded before the quarantine; re-running `pre-commit` on `main` HEAD now reproduces the failure. ### Root cause confirmation Reproduces locally with `uv` 0.9.26: ``` $ echo 'terratorch>=1.2.2' > probe.in $ uv pip compil...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ware_porting cuda build_error #40808 [Bugfix] Disable FlashInfer CUTLASS MoE on SM110 (Jetson Thor AGX) | #41255 [Perf] Intergrate Tile Kernels `head_compute_mix_kernel` for Deepseek-V4 | #41318 [Feat] dnnl build for AV...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40808](https://github.com/vllm-project/vllm/pull/40808) | mentioned | 0.45 | [Bugfix] Disable FlashInfer CUTLASS MoE on SM110 (Jetson Thor AGX) | efore the quarantine), 3 skipped, 1 too new. examples of failing prs: #40808, #41255, #41318, #41366. main commit `ff449b6426` shows `pre-commit: success` but only because that st… |
| [#41255](https://github.com/vllm-project/vllm/pull/41255) | mentioned | 0.45 | [Perf] Intergrate Tile Kernels `head_compute_mix_kernel` for Deepseek-V4 | e quarantine), 3 skipped, 1 too new. examples of failing prs: #40808, #41255, #41318, #41366. main commit `ff449b6426` shows `pre-commit: success` but only because that status was… |
| [#41318](https://github.com/vllm-project/vllm/pull/41318) | mentioned | 0.45 | [Feat] dnnl build for AVX2 W8A8 Int8 | tine), 3 skipped, 1 too new. examples of failing prs: #40808, #41255, #41318, #41366. main commit `ff449b6426` shows `pre-commit: success` but only because that status was recorde… |
| [#41377](https://github.com/vllm-project/vllm/pull/41377) | closes_keyword | 0.95 | [CI/Build] Skip terratorch + torchgeo while PyPI has lightning quarantined | Fixes #41376. PyPI is currently serving the `lightning` project as **quarantined**: the simple index has `<meta name="pypi:project-status" content="quarantined">` with zero releas |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
