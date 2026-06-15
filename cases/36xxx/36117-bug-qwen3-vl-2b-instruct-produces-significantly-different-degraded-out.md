# vllm-project/vllm#36117: [Bug]: Qwen3-VL-2B-Instruct produces significantly different (degraded) outputs on v0.12.0 compared to v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#36117](https://github.com/vllm-project/vllm/issues/36117) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;gemm;sampling |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-2B-Instruct produces significantly different (degraded) outputs on v0.12.0 compared to v0.11.0

### Issue 正文摘录

### Your current environment ``` - vLLM v0.11.0 (baseline) and v0.12.0 (regression) - Model: Qwen/Qwen3-VL-2B-Instruct - GPU: 4x A100, tensor-parallel-size=4 - Evaluation: PointBench (982 samples, point-in-mask coordinate localization) - Parameters: temperature=0.0, top_p=0.9, max_tokens=1024 ``` ### 🐛 Describe the bug When serving **Qwen3-VL-2B-Instruct** with vLLM, upgrading from **v0.11.0 to v0.12.0** causes a severe degradation in coordinate localization outputs. The model produces systematically biased coordinates, resulting in accuracy dropping from **~60% to ~13%** on PointBench. This is **not** a scoring/evaluation issue — the raw model outputs are fundamentally different between versions for identical inputs and parameters. ### Observed behavior The model's predicted coordinates shift dramatically between versions: | Metric | v0.11.0 | v0.12.0 | |--------|---------|---------| | **PointBench accuracy** | **57.6%** | **~13%** | | X coordinate mean | 509 | 285 | | Y coordinate mean | 573 | 1074 | | Coordinates exceeding 0-1000 range | 0% | 10% | On v0.12.0, coordinates are **systematically biased** — X values skew low (toward left edge) and Y values skew high (often exceedin...

## 现有链接修复摘要

#27418 [MM][Bugfix] Replace `PatchEmbed`'s conv3d to linear layer | #28455 [Model][MM] Extract conv layer as CustomOp

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: uation issue — the raw model outputs are fundamentally different between versions for identical inputs and parameters. ### Observed behavior The model's predicted coordinates shift dramatically between versions: | Metri...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: puts. The model produces systematically biased coordinates, resulting in accuracy dropping from **~60% to ~13%** on PointBench. This is **not** a scoring/evaluation issue — the raw model outputs are fundamentally differ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: e) and v0.12.0 (regression) - Model: Qwen/Qwen3-VL-2B-Instruct - GPU: 4x A100, tensor-parallel-size=4 - Evaluation: PointBench (982 samples, point-in-mask coordinate localization) - Parameters: temperature=0.0, top_p=0....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-2B-Instruct produces significantly different (degraded) outputs on v0.12.0 compared to v0.11.0 ### Your current environment ``` - vLLM v0.11.0 (baseline) and v0.12.0 (regression) - Model: Qwen/Qwen3-VL-2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: ### Your current environment ``` - vLLM v0.11.0 (baseline) and v0.12.0 (regression) - Model: Qwen/Qwen3-VL-2B-Instruct - GPU: 4x A100, tensor-parallel-size=4 - Evaluation: PointBench (982 samples, point-in-mask coordina...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27418](https://github.com/vllm-project/vllm/pull/27418) | mentioned | 0.45 | [MM][Bugfix] Replace `PatchEmbed`'s conv3d to linear layer | ues - #27406 — mm performance regression from pytorch 2.9 (conv3d) - #27418 — replace patchembed's conv3d to linear layer (workaround) - #28455 — extract conv layer as customop (i… |
| [#28455](https://github.com/vllm-project/vllm/pull/28455) | mentioned | 0.45 | [Model][MM] Extract conv layer as CustomOp | - #27418 — replace patchembed's conv3d to linear layer (workaround) - #28455 — extract conv layer as customop (introduced conv3dlayer) - #33204 — qwen3-vl-embedding produces diffe… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
