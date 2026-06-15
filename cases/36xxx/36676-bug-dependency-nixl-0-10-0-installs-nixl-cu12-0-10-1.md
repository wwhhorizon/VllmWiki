# vllm-project/vllm#36676: [Bug]: dependency `nixl<0.10.0` installs `nixl-cu12==0.10.1`

| 字段 | 值 |
| --- | --- |
| Issue | [#36676](https://github.com/vllm-project/vllm/issues/36676) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: dependency `nixl<0.10.0` installs `nixl-cu12==0.10.1`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm uses nixl as the primary kv connector for PDD, and as such `vllm/vllm-openai` docker image [includes `nixl` as kv connector dependencies](https://github.com/vllm-project/vllm/blob/main/requirements/kv_connectors.txt). Since #35495 we pinned the nixl version as `nixl >= 0.7.1, =@VERSION@`, not `nixl-cu1{2,3}==@VERSION@`. One can check the package dependency like the following: ```shell # Inside vllm/vllm-openai:v0.17.0 container $ cat /usr/local/lib/python3.12/dist-packages/nixl-0.9.0-dist-info/METADATA | grep Requires-Dist # Requires-Dist: nixl-cu12>=0.9.0 # Requires-Dist: nixl-cu12>=0.9.0; extra == "cu12" # Requires-Dist: nixl-cu13>=0.9.0; extra == "cu13" $ uv pip show nixl-cu12 # Using Python 3.12.13 environment at: /usr # Name: nixl-cu12 # Version: 0.10.1 # Location: /usr/local/lib/python3.12/dist-packages # Requires: numpy, torch # Required-by: nixl ``` I haven't yet faced a bug from `nixl-cu12==0.10.1`, but it is worth fixing in CI build pipeline I think. The pain point for the fix is that we now need to manually edit CUDA runtime version to the `kv_connectors.txt`, some sort of `sed` is needed. cc. @NickLucche ### Befo...

## 现有链接修复摘要

#36735 [Docker] Resolve NIXL runtime wheel for kv connectors

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: dependency `nixl<0.10.0` installs `nixl-cu12==0.10.1` bug ### Your current environment ### 🐛 Describe the bug vllm uses nixl as the primary kv connector for PDD, and as such `vllm/vllm-openai` docker image [inclu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I think. The pain point for the fix is that we now need to manually edit CUDA runtime version to the `kv_connectors.txt`, some sort of `sed` is needed. cc. @NickLucche ### Before submitting a new issue... - [x] Make sur...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: iner $ cat /usr/local/lib/python3.12/dist-packages/nixl-0.9.0-dist-info/METADATA | grep Requires-Dist # Requires-Dist: nixl-cu12>=0.9.0 # Requires-Dist: nixl-cu12>=0.9.0; extra == "cu12" # Requires-Dist: nixl-cu13>=0.9....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel cuda build_error env_dependency #36735 [Doc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36735](https://github.com/vllm-project/vllm/pull/36735) | closes_keyword | 0.95 | [Docker] Resolve NIXL runtime wheel for kv connectors | Fixes #36676 by resolving `requirements/kv_connectors.txt` to the CUDA-runtime-specific NIXL wheel during Docker builds instead of relying on the `nixl` meta package. This keeps t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
