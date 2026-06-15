# vllm-project/vllm#10068: [Misc]: w8a8 model inference

| 字段 | 值 |
| --- | --- |
| Issue | [#10068](https://github.com/vllm-project/vllm/issues/10068) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: w8a8 model inference

### Issue 正文摘录

When vllm performs inference using a w8a8 quantized model, does it retain matrix operations on int8? If so, could you tell me where the specific implementation logic code is located

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: retain matrix operations on int8? If so, could you tell me where the specific implementation logic code is located
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: c]: w8a8 model inference stale When vllm performs inference using a w8a8 quantized model, does it retain matrix operations on int8? If so, could you tell me where the specific implementation logic code is located
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: w8a8 model inference stale When vllm performs inference using a w8a8 quantized model, does it retain matrix operations on int8? If so, could you tell me where the specific implementation logic code is located
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: w8a8 model inference stale When vllm performs inference using a w8a8 quantized model, does it retain matrix operations on int8? If so, could you tell me where the specific implementation logic code is located

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
