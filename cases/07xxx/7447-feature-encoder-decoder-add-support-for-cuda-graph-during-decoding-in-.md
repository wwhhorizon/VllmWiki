# vllm-project/vllm#7447: [Feature][Encoder-Decoder]: Add support for cuda graph during decoding in encoder-decoder models

| 字段 | 值 |
| --- | --- |
| Issue | [#7447](https://github.com/vllm-project/vllm/issues/7447) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][Encoder-Decoder]: Add support for cuda graph during decoding in encoder-decoder models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently for encoder-decoder models we don't support cuda graph during the decode phase. This fr tracks adding support for cuda graph during decode phase. Adding this support will help speed up the decode phase. #7366 cc: @afeldman-nm ### Alternatives _No response_ ### Additional context _No response_

## 现有链接修复摘要

#7631 [Encoder decoder] Add cuda graph support during decoding for encoder-decoder models

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature][Encoder-Decoder]: Add support for cuda graph during decoding in encoder-decoder models feature request;stale ### 🚀 The feature, motivation and pitch Currently for encoder-decoder models we don't support cuda g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature][Encoder-Decoder]: Add support for cuda graph during decoding in encoder-decoder models feature request;stale ### 🚀 The feature, motivation and pitch Currently for encoder-decoder models we don't support cuda g...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: -Decoder]: Add support for cuda graph during decoding in encoder-decoder models feature request;stale ### 🚀 The feature, motivation and pitch Currently for encoder-decoder models we don't support cuda graph during the d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7631](https://github.com/vllm-project/vllm/pull/7631) | mentioned | 0.6 | [Encoder decoder] Add cuda graph support during decoding for encoder-decoder models | e being padded appropriately during CUDA Graph capture and replay. #7447 Measurements based on e2e test For the test test_model_with_cuda_graph[DecoderPromptType.CUSTOM-5-20 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
