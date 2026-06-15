# vllm-project/vllm#7390: [Bug]: guided regex (using outlines and lm format enforcer) return bad error description on invalid regex

| 字段 | 值 |
| --- | --- |
| Issue | [#7390](https://github.com/vllm-project/vllm/issues/7390) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: guided regex (using outlines and lm format enforcer) return bad error description on invalid regex

### Issue 正文摘录

### 🐛 Describe the bug Rather I am using outlines as guidance engine or lm-format-enforcer and when i pass an invalid regex, there is log on that bad bad error over api (500 internal server error). I thing it should be 400 (because this is bad input, and a better description

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: guided regex (using outlines and lm format enforcer) return bad error description on invalid regex bug;stale ### 🐛 Describe the bug Rather I am using outlines as guidance engine or lm-format-enforcer and when i p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nd lm format enforcer) return bad error description on invalid regex bug;stale ### 🐛 Describe the bug Rather I am using outlines as guidance engine or lm-format-enforcer and when i pass an invalid regex, there is log on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
