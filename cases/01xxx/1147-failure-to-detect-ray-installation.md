# vllm-project/vllm#1147: Failure to detect Ray installation

| 字段 | 值 |
| --- | --- |
| Issue | [#1147](https://github.com/vllm-project/vllm/issues/1147) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failure to detect Ray installation

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/116034543/fc48e90b-0135-4926-a85f-8ccdf4462200) I've tried with different models, and there are 4 GPUs being made available. Regardless of the model selected, it gives the same error claiming Ray is not installed, despite it clearly being installed/running

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Failure to detect Ray installation ![image](https://github.com/vllm-project/vllm/assets/116034543/fc48e90b-0135-4926-a85f-8ccdf4462200) I've tried with different models, and there are 4 GPUs being made available. Regard...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 16034543/fc48e90b-0135-4926-a85f-8ccdf4462200) I've tried with different models, and there are 4 GPUs being made available. Regardless of the model selected, it gives the same error claiming Ray is not installed, despit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
