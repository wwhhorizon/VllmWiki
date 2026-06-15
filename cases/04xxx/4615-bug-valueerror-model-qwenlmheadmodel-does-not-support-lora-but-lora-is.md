# vllm-project/vllm#4615: [Bug]: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

| 字段 | 值 |
| --- | --- |
| Issue | [#4615](https://github.com/vllm-project/vllm/issues/4615) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. bug;stale ### Your cur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 D...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: future. If this is important to you, please open an issue on github. bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ValueError: Model QWenLMHeadModel does...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
