# vllm-project/vllm#34865: [Bug]: Prefix caching failing for Nemotron models

| 字段 | 值 |
| --- | --- |
| Issue | [#34865](https://github.com/vllm-project/vllm/issues/34865) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache |
| 子分类 | debug |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix caching failing for Nemotron models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have noticed failures on latest main for 'all' mode prefix caching (default for Nemotron currently), documented with a reproducer here: https://github.com/NVIDIA-NeMo/RL/pull/1987 I am able to easily reproduce the issue using [this file](https://github.com/NVIDIA-NeMo/RL/pull/1987/changes#diff-40feff91d5c12968cf45122eb98b89fd9c36ef72226d104a7ac0e329fbd2d6ee) from that PR. Using 'align' mode prefix caching, it works properly and I do see some cache hits in the log and much faster prefill for the second step. A discussion in slack independently found this problem, and mentioned that disabling the block table update resolved the issue somewhat. I have not tested this. The issue seems to go back a couple versions at least (note, I did not run this bisect and have not confirmed which env/setup was used for this test): ``` RESULT: PASS — no issues detected in vLLM 0.11.2 RESULT: PASS — no issues detected in vLLM 0.13.0 RESULT: FAIL — prefix caching appears broken in vLLM 0.14.0 RESULT: FAIL — prefix caching appears broken in vLLM 0.15.0 RESULT: FAIL — prefix caching appears broken in vLLM 0.15.1 ``` ### Before submitting a new issue...

## 现有链接修复摘要

#34874 [Bugfix] Fix prefix caching for Mamba 'all' mode (Nemotron models)

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: mode prefix caching (default for Nemotron currently), documented with a reproducer here: https://github.com/NVIDIA-NeMo/RL/pull/1987 I am able to easily reproduce the issue using [this file](https://github.com/NVIDIA-Ne...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e somewhat. I have not tested this. The issue seems to go back a couple versions at least (note, I did not run this bisect and have not confirmed which env/setup was used for this test): ``` RESULT: PASS — no issues det...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: slack independently found this problem, and mentioned that disabling the block table update resolved the issue somewhat. I have not tested this. The issue seems to go back a couple versions at least (note, I did not run...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: slack independently found this problem, and mentioned that disabling the block table update resolved the issue somewhat. I have not tested this. The issue seems to go back a couple versions at least (note, I did not run...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34874](https://github.com/vllm-project/vllm/pull/34874) | closes_keyword | 0.95 | [Bugfix] Fix prefix caching for Mamba 'all' mode (Nemotron models) | Fixes #34865 Fix prefix caching producing NaN logprobs and garbage tokens for Nemotron hybrid models (`mamba_cache_mode="all"`) when prefix caching is enabled. ### Root Cause Ne |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
