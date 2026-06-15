# vllm-project/vllm#210: What is the correct way to use quantized versions of vicuna or guanco?

| 字段 | 值 |
| --- | --- |
| Issue | [#210](https://github.com/vllm-project/vllm/issues/210) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What is the correct way to use quantized versions of vicuna or guanco?

### Issue 正文摘录

I have been trying to use quantized versions of models to use my GPU whose VRAM is 6GB max. However nothing seems to work. How would I go about using 5bit versions that use under 6GB in memory?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: What is the correct way to use quantized versions of vicuna or guanco? feature request I have been trying to use quantized versions of models to use my GPU whose VRAM is 6GB max. However nothing seems to work. How would...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: What is the correct way to use quantized versions of vicuna or guanco? feature request I have been trying to use quantized versions of models to use my GPU whose VRAM is 6GB max. However nothing seems to work. How would...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: guanco? feature request I have been trying to use quantized versions of models to use my GPU whose VRAM is 6GB max. However nothing seems to work. How would I go about using 5bit versions that use under 6GB in memory?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s the correct way to use quantized versions of vicuna or guanco? feature request I have been trying to use quantized versions of models to use my GPU whose VRAM is 6GB max. However nothing seems to work. How would I go...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
