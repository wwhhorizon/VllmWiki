# vllm-project/vllm#668: T5 like encoder-decoder model support

| 字段 | 值 |
| --- | --- |
| Issue | [#668](https://github.com/vllm-project/vllm/issues/668) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> T5 like encoder-decoder model support

### Issue 正文摘录

vllm is a great open source project and we are looking forward to running the T5 model with vllm.I know there is a plan for T5 in the roadmap, but I still want to know, is there an approximate time for this? Or can there be a specific encoder-decoder code structure, and then everyone will work together to contribute

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: T5 like encoder-decoder model support feature request vllm is a great open source project and we are looking forward to running the T5 model with vllm.I know there is a plan for T5 in the roadmap, but I still want to kn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ant to know, is there an approximate time for this? Or can there be a specific encoder-decoder code structure, and then everyone will work together to contribute
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: T5 like encoder-decoder model support feature request vllm is a great open source project and we are looking forward to running the T5 model with vllm.I know there is a plan for T5 in the roadmap, but I still want to kn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
