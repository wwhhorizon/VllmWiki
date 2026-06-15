# vllm-project/vllm#15263: [Bug]: oracle for device checking raise exception unexpectly

| 字段 | 值 |
| --- | --- |
| Issue | [#15263](https://github.com/vllm-project/vllm/issues/15263) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: oracle for device checking raise exception unexpectly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Oracle check does no work as expected. Suggested to revert. The support for v1 should be determined by the pluggable platform, not the current status of in-tree project. This type of forced error seems problematic and redundant with "cuda check" at the last of function. (https://github.com/vllm-project/vllm/pull/15104) ``` python # https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py#L1601 if not (current_platform.is_cuda_alike() or current_platform.is_tpu()): _raise_or_fallback( feature_name=f"device type={current_platform.device_type}", recommend_to_remove=False) return False ``` It will forcely raise for any other platform, even V1 supported. Further, redundant with https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py#L1626 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: project. This type of forced error seems problematic and redundant with "cuda check" at the last of function. (https://github.com/vllm-project/vllm/pull/15104) ``` python # https://github.com/vllm-project/vllm/blob/main...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nt_platform.is_cuda_alike() or current_platform.is_tpu()): _raise_or_fallback( feature_name=f"device type={current_platform.device_type}", recommend_to_remove=False) return False ``` It will forcely raise for any other...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hich can answer lots of frequently asked questions. development cuda env_dependency #41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: vice type={current_platform.device_type}", recommend_to_remove=False) return False ``` It will forcely raise for any other platform, even V1 supported. Further, redundant with https://github.com/vllm-project/vllm/blob/m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development cuda env_dependency #41606 Bump the minor-update group across 1 directory...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15263">#15263</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15263">#15263</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15263">#15263</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15263">#15263</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15263">#15263</a> by <a href="https://github.com/apps/dependabot"><code>@​dependabot[bot]</code></a>.</li> <li>⬆ Bum… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
