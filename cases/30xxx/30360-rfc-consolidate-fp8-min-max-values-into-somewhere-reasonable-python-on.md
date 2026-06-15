# vllm-project/vllm#30360: [RFC]: Consolidate FP8 min/max values into somewhere reasonable (Python only)

| 字段 | 值 |
| --- | --- |
| Issue | [#30360](https://github.com/vllm-project/vllm/issues/30360) |
| 状态 | closed |
| 标签 | rocm;RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | hardware_porting;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8 |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Consolidate FP8 min/max values into somewhere reasonable (Python only)

### Issue 正文摘录

### Motivation. On platforms such as MI300 that have `torch.float8_e4m3fnuz` as their fp8 dtype, it is necessary to use `-224.0/224.0 ` for fp8 min/max values for better accuracy when making fp8 computations. There are two problems that exist: 1) There is code that uses the default min/max values that torch provides and not the recommended ones: * currently, this doesn't cause errors because the tests and implementations agree on these values 2) There are mismatches between the default and recommended values (+-224 vs +=240) * this causes test failures due to mismatches between test and implementation: * there are PRs to fix the mismatches that occur * https://github.com/vllm-project/vllm/pull/30292 * https://github.com/vllm-project/vllm/pull/30291 Of course there can be future reoccurrences of the mentioned problems. ### Proposed Change. I'm proposing to: 1. Consolidate the recommended fp8 min/max values into fp8_utils, 2. Update usage of fp8 min/max values to use the newly consolidated values, ### Feedback Period. 2 weeks ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, a...

## 现有链接修复摘要

#31106 [Bugfix][Hardware][AMD] Consolidate FP8 min/max values helper function

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: : Consolidate FP8 min/max values into somewhere reasonable (Python only) rocm;RFC ### Motivation. On platforms such as MI300 that have `torch.float8_e4m3fnuz` as their fp8 dtype, it is necessary to use `-224.0/224.0 ` f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [RFC]: Consolidate FP8 min/max values into somewhere reasonable (Python only) rocm;RFC ### Motivation. On platforms such as MI300 that have `torch.float8_e4m3fnuz` as their fp8 dtype, it is necessary to use `-224.0/224....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: it is necessary to use `-224.0/224.0 ` for fp8 min/max values for better accuracy when making fp8 computations. There are two problems that exist: 1) There is code that uses the default min/max values that torch provide...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: it is necessary to use `-224.0/224.0 ` for fp8 min/max values for better accuracy when making fp8 computations. There are two problems that exist: 1) There is code that uses the default min/max values that torch provide...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stions. correctness hardware_porting;quantization fp8 mismatch dtype;env_dependency #31106 [Bugfix][Hardware][AMD] Consolidate FP8 min/max values helper function Motivation.

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31106](https://github.com/vllm-project/vllm/pull/31106) | closes_keyword | 0.95 | [Bugfix][Hardware][AMD] Consolidate FP8 min/max values helper function | Fixes #30360 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
