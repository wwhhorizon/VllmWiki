# vllm-project/vllm#316: support for quantized models?

| 字段 | 值 |
| --- | --- |
| Issue | [#316](https://github.com/vllm-project/vllm/issues/316) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> support for quantized models?

### Issue 正文摘录

for those with limited VRAM, any plans to support quantized versions of models?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ture request for those with limited VRAM, any plans to support quantized versions of models?
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: support for quantized models? feature request for those with limited VRAM, any plans to support quantized versions of models?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: support for quantized models? feature request for those with limited VRAM, any plans to support quantized versions of models?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: support for quantized models? feature request for those with limited VRAM, any plans to support quantized versions of models?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
