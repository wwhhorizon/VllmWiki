# vllm-project/vllm#23594: [CI]: Host images used by multimodal tests locally

| 字段 | 值 |
| --- | --- |
| Issue | [#23594](https://github.com/vllm-project/vllm/issues/23594) |
| 状态 | closed |
| 标签 | good first issue;ci/build |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Host images used by multimodal tests locally

### Issue 正文摘录

The multimodal tests currently reference external image URLs (e.g. on wikipedia). This is the source of some failures where there is a problem connecting to the external URL, and also has the potential for future breakage if those URLs change or go away. Ideally we should host the images locally, we could even run a local http server as part of the test. We might not want to store the images in the GH repo though. Example failure: https://buildkite.com/vllm/ci/builds/28257#0198e22b-fa99-4342-a5e6-31d0b268e67a

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Host images used by multimodal tests locally good first issue;ci/build The multimodal tests currently reference external image URLs (e.g. on wikipedia). This is the source of some failures where there is a problem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [CI]: Host images used by multimodal tests locally good first issue;ci/build The multimodal tests currently reference external image URLs (e.g. on wikipedia). This is the source of some failures where there is a problem...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Host images used by multimodal tests locally good first issue;ci/build The multimodal tests currently reference external image URLs (e.g. on wikipedia). This is the source of some failures where there is a problem...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
