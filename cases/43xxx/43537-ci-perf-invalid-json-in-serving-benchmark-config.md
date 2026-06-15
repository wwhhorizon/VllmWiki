# vllm-project/vllm#43537: [CI/Perf] Invalid JSON in serving benchmark config

| 字段 | 值 |
| --- | --- |
| Issue | [#43537](https://github.com/vllm-project/vllm/issues/43537) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI/Perf] Invalid JSON in serving benchmark config

### Issue 正文摘录

## Summary `.buildkite/performance-benchmarks/tests/serving-tests.json` is currently invalid JSON on `main`. The file contains a stray duplicate object after `serving_llama8B_tp1_sharegpt`, so JSON parsers fail before the serving benchmark suite can read the default config. ## Repro ```bash jq . .buildkite/performance-benchmarks/tests/serving-tests.json ``` Current result: ```text parse error: Objects must consist of key:value pairs at line 35, column 5 ``` I also verified the same failure with Python `json.load`. ## Why this matters `run-performance-benchmarks.sh` defaults to `serving-tests$ARCH.json`, and the non-arch-specific default points at `tests/serving-tests.json`. That means the default serving benchmark config is broken on the current `main` branch. ## Likely regression source `git blame` points the malformed block to `5d041cc1fe5181daabf39943efc7b678380d57bd` from PR #43262. ## Expected fix Remove the stray duplicate object and add a small validation guard so future benchmark config edits fail fast if one of these JSON files becomes unparsable again.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI/Perf] Invalid JSON in serving benchmark config ## Summary `.buildkite/performance-benchmarks/tests/serving-tests.json` is currently invalid JSON on `main`. The file contains a stray duplicate object after `serving_l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI/Perf] Invalid JSON in serving benchmark config ## Summary `.buildkite/performance-benchmarks/tests/serving-tests.json` is currently invalid JSON on `main`. The file contains a stray duplicate object after `serving_l
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: this matters `run-performance-benchmarks.sh` defaults to `serving-tests$ARCH.json`, and the non-arch-specific default points at `tests/serving-tests.json`. That means the default serving benchmark config is broken on th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI/Perf] Invalid JSON in serving benchmark config ## Summary `.buildkite/performance-benchmarks/tests/serving-tests.json` is currently invalid JSON on `main`. The file contains a stray duplicate object after `serving_l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ` branch. ## Likely regression source `git blame` points the malformed block to `5d041cc1fe5181daabf39943efc7b678380d57bd` from PR #43262. ## Expected fix Remove the stray duplicate object and add a small validation gua...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
