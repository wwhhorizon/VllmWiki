# vllm-project/vllm#39613: [Doc]: Docs audit: CLI, plugins, features, env vars, and auth mismatches

| 字段 | 值 |
| --- | --- |
| Issue | [#39613](https://github.com/vllm-project/vllm/issues/39613) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Docs audit: CLI, plugins, features, env vars, and auth mismatches

### Issue 正文摘录

### 📚 The doc issue ## Summary An automated documentation audit found several places where the docs and current code appear to diverge, mostly around CLI behavior, plugin loading, feature compatibility, environment variables, pooling endpoints, and API-key auth. Some of these may be intentional, outdated docs, or false positives from the tool, so we wanted to share them for review. > **Note:** This issue was generated automatically by [LyingDocs](https://github.com/KMing-L/lying-docs), a documentation-code misalignment detection tool. The analysis may contain errors or misinterpretations — please feel free to close or correct this issue if any finding does not apply or if we have misunderstood the codebase. ## Finding Categories The findings below are classified into one or more of the following categories: | Category | Meaning | |----------|---------| | **LogicMismatch** | The code behaves differently from what the documentation describes | | **PhantomSpec** | The documentation describes a feature or behavior that does not appear to exist in the code | | **ShadowLogic** | The code contains significant behavior that is not documented at all | | **HardcodedDrift** | A value or para...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: erence**: `vllm/utils/argparse_utils.py:111` The CLI docs describe a special `--help=listgroup` mode for `vllm serve`, but it appears the parser only supports `--help= ` matching `all`, an exact group title, or a flag s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Doc]: Docs audit: CLI, plugins, features, env vars, and auth mismatches documentation ### 📚 The doc issue ## Summary An automated documentation audit found several places where the docs and current code appear to diver...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Doc]: Docs audit: CLI, plugins, features, env vars, and auth mismatches documentation ### 📚 The doc issue ## Summary An automated documentation audit found several places where the docs and current code appear to diver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mented at all | | **HardcodedDrift** | A value or parameter described as configurable in the docs is hardcoded in the implementation | ## Findings ### Documented `--help=listgroup` mode is not implemented - **Category**...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ds. ### Environment variable handling includes undocumented non-`VLLM_` fallbacks and compatibility vars - **Category**: ShadowLogic - **Documentation reference**: `configuration/env_vars.md:3-8` - **Code reference**: `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
