# vllm-project/vllm#1678: Can vllm support quantized INT4 and INT8 models? Whether there is a supporting plan for the future

| 字段 | 值 |
| --- | --- |
| Issue | [#1678](https://github.com/vllm-project/vllm/issues/1678) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can vllm support quantized INT4 and INT8 models? Whether there is a supporting plan for the future

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/150330243/76ee34a3-7f13-4475-ae16-4d13846810d5)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Can vllm support quantized INT4 and INT8 models? Whether there is a supporting plan for the future ![image](https://github.com/vllm-project/vllm/assets/150330243/76ee34a3-7f13-4475-ae16-4d13846810d5)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Can vllm support quantized INT4 and INT8 models? Whether there is a supporting plan for the future ![image](https://github.com/vllm-project/vllm/assets/150330243/76ee34a3-7f13-4475-ae16-4d13846810d5)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
