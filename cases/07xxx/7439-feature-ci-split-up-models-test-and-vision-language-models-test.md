# vllm-project/vllm#7439: [Feature]: CI - Split up "Models Test" and "Vision Language Models Test"

| 字段 | 值 |
| --- | --- |
| Issue | [#7439](https://github.com/vllm-project/vllm/issues/7439) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: CI - Split up "Models Test" and "Vision Language Models Test"

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Takes 1 hour+ on CI compared to others, which take <~30 min. Thus, ends up being a bottleneck So, should be split up similar to kernels CC: @khluu

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: CI - Split up "Models Test" and "Vision Language Models Test" feature request ### 🚀 The feature, motivation and pitch Takes 1 hour+ on CI compared to others, which take <~30 min. Thus, ends up being a bottlen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: CI - Split up "Models Test" and "Vision Language Models Test" feature request ### 🚀 The feature, motivation and pitch Takes 1 hour+ on CI compared to others, which take <~30 min. Thus, ends up being a bottlen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: CI - Split up "Models Test" and "Vision Language Models Test" feature request ### 🚀 The feature, motivation and pitch Takes 1 hour+ on CI compared to others, which take <~30 min. Thus, ends up being a bottleneck So,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: CI - Split up "Models Test" and "Vision Language Models Test" feature request ### 🚀 The feature, motivation and pitch Takes 1 hour+ on CI compared to others, which take <~30 min. Thus, ends up being a bottlen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
