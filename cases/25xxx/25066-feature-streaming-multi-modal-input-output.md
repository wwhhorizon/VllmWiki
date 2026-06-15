# vllm-project/vllm#25066: [Feature]: Streaming multi-modal input/output

| 字段 | 值 |
| --- | --- |
| Issue | [#25066](https://github.com/vllm-project/vllm/issues/25066) |
| 状态 | closed |
| 标签 | feature request;multi-modality |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Streaming multi-modal input/output

### Issue 正文摘录

This is a tracking issue for enabling streaming MM I/O. ## Outline Streaming input: - Support streaming multi-modal inputs at API level. - Handle streaming inputs in the multi-modal processor. - Define an interface for models to indicate support for streaming inputs. - Update V1 model runner and scheduler to handle partial MM encoding requests (this is the hardest part IMO) Streaming output: - Implement `RequestOutputKind.DELTA` for multi-modal outputs in V1 output processor. - Support streaming multi-modal outputs at API level. ## Notes - Currently we are waiting for AWS's proposal - Take inspiration from https://github.com/vllm-project/vllm/pull/16347? - See also [#22695](https://github.com/vllm-project/vllm/issues/22695)

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Streaming multi-modal input/output feature request;multi-modality This is a tracking issue for enabling streaming MM I/O. ## Outline Streaming input: - Support streaming multi-modal inputs at API level. - Han...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: streaming inputs in the multi-modal processor. - Define an interface for models to indicate support for streaming inputs. - Update V1 model runner and scheduler to handle partial MM encoding requests (this is the hardes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
