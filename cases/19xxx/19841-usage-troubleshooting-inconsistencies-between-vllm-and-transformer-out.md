# vllm-project/vllm#19841: [Usage]: Troubleshooting Inconsistencies Between VLLM and Transformer Outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#19841](https://github.com/vllm-project/vllm/issues/19841) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Troubleshooting Inconsistencies Between VLLM and Transformer Outputs

### Issue 正文摘录

I encountered inconsistencies in the outputs between transformer and vllm. Is there a script available to compare the outputs of each layer of the transformer and vllm models?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: Troubleshooting Inconsistencies Between VLLM and Transformer Outputs usage;stale I encountered inconsistencies in the outputs between transformer and vllm. Is there a script available to compare the outputs of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ailable to compare the outputs of each layer of the transformer and vllm models?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oubleshooting Inconsistencies Between VLLM and Transformer Outputs usage;stale I encountered inconsistencies in the outputs between transformer and vllm. Is there a script available to compare the outputs of each layer...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
