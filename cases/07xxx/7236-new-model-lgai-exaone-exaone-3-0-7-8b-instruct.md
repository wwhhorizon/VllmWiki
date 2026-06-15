# vllm-project/vllm#7236: [New Model]: LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#7236](https://github.com/vllm-project/vllm/issues/7236) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct

### Issue 正文摘录

### The model to consider. A new model to consider for support. This is a recently developed model by LG. We kindly request that you consider adding support for it. ### The closest model vllm already supports. . ### What's your difficulty of supporting the model you want? new architecture We would greatly appreciate if you could add support for this model. It would be a valuable addition to the supported models list. Thank you for your consideration.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: supporting the model you want? new architecture We would greatly appreciate if you could add support for this model. It would be a valuable addition to the supported models list. Thank you for your consideration.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s. . ### What's your difficulty of supporting the model you want? new architecture We would greatly appreciate if you could add support for this model. It would be a valuable addition to the supported models list. Thank...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct new-model ### The model to consider. A new model to consider for support. This is a recently developed model by LG. We kindly request that you consider adding support fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nsider for support. This is a recently developed model by LG. We kindly request that you consider adding support for it. ### The closest model vllm already supports. . ### What's your difficulty of supporting the model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
