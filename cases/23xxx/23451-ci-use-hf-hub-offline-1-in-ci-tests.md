# vllm-project/vllm#23451: [CI]: Use `HF_HUB_OFFLINE=1` in CI tests

| 字段 | 值 |
| --- | --- |
| Issue | [#23451](https://github.com/vllm-project/vllm/issues/23451) |
| 状态 | closed |
| 标签 | ci/build |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Use `HF_HUB_OFFLINE=1` in CI tests

### Issue 正文摘录

CI tests frequently fail due to connection failures to HF hub. AFAIK we have a more local cache of the models, but these connections are still made by default to check for a newer revision. There's no reason to do this and it would be better anyhow for determinism to not update implicitly to newer revisions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Use `HF_HUB_OFFLINE=1` in CI tests ci/build CI tests frequently fail due to connection failures to HF hub. AFAIK we have a more local cache of the models, but these connections are still made by default to check fo
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI]: Use `HF_HUB_OFFLINE=1` in CI tests ci/build CI tests frequently fail due to connection failures to HF hub. AFAIK we have a more local cache of the models, but these connections are still made by default to check f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: There's no reason to do this and it would be better anyhow for determinism to not update implicitly to newer revisions.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Use `HF_HUB_OFFLINE=1` in CI tests ci/build CI tests frequently fail due to connection failures to HF hub. AFAIK we have a more local cache of the models, but these connections are still made by default to check f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
