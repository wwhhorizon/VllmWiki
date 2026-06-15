# vllm-project/vllm#739: 使用 api_server.py运行QWen-7b 后，推理时错误

| 字段 | 值 |
| --- | --- |
| Issue | [#739](https://github.com/vllm-project/vllm/issues/739) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 使用 api_server.py运行QWen-7b 后，推理时错误

### Issue 正文摘录

当发送http请求时，日志打印以下错误信息： .......... “api_server”,line 56, in generate ......... AttributeError: 'QWenTokenizer' object has no attribute 'byte_decoder'

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 使用 api_server.py运行QWen-7b 后，推理时错误 当发送http请求时，日志打印以下错误信息： .......... “api_server”,line 56, in generate ......... AttributeError: 'QWenTokenizer' object has no attribute 'byte_decoder'
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ......... AttributeError: 'QWenTokenizer' object has no attribute 'byte_decoder'

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
