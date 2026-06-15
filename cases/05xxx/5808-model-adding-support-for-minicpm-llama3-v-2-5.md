# vllm-project/vllm#5808: [Model]: Adding support for MiniCPM-Llama3-V-2_5

| 字段 | 值 |
| --- | --- |
| Issue | [#5808](https://github.com/vllm-project/vllm/issues/5808) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Model]: Adding support for MiniCPM-Llama3-V-2_5

### Issue 正文摘录

Please support for MiniCPM-Llama3-V-2_5. - HuggingFace Page: https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5 - Github : https://github.com/OpenBMB/MiniCPM-V Currently I am using vllm 0.5.0.post1 version.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Model]: Adding support for MiniCPM-Llama3-V-2_5 new-model Please support for MiniCPM-Llama3-V-2_5. - HuggingFace Page: https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5 - Github : https://github.com/OpenBMB/MiniCPM-V
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s://github.com/OpenBMB/MiniCPM-V Currently I am using vllm 0.5.0.post1 version.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
