# vllm-project/vllm#23669: [CI]: Quantization tests cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#23669](https://github.com/vllm-project/vllm/issues/23669) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI]: Quantization tests cleanup

### Issue 正文摘录

Weight loading multiple gpus // quantization test // quantized Model Tests - Weight loading → convert this to nightly - Quantization/Quantized Models Test → consolidate + potentially reduce the number of parameters / remove some of the low priority integrations

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI]: Quantization tests cleanup ci/build;stale Weight loading multiple gpus // quantization test // quantized Model Tests - Weight loading → convert this to nightly - Quantization/Quantized Models Test → consolidate
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [CI]: Quantization tests cleanup ci/build;stale Weight loading multiple gpus // quantization test // quantized Model Tests - Weight loading → convert this to nightly - Quantization/Quantized Models Test → consolidate +...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ild;stale Weight loading multiple gpus // quantization test // quantized Model Tests - Weight loading → convert this to nightly - Quantization/Quantized Models Test → consolidate + potentially reduce the number of param...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Quantization tests cleanup ci/build;stale Weight loading multiple gpus // quantization test // quantized Model Tests - Weight loading → convert this to nightly - Quantization/Quantized Models Test → consolidate +...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI]: Quantization tests cleanup ci/build;stale Weight loading multiple gpus // quantization test // quantized Model Tests - Weight loading → convert this to nightly - Quantization/Quantized Models Test → consolidate +...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
