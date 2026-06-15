# vllm-project/vllm#388: supporting superhot models?

| 字段 | 值 |
| --- | --- |
| Issue | [#388](https://github.com/vllm-project/vllm/issues/388) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> supporting superhot models?

### Issue 正文摘录

specifically: - https://huggingface.co/kaiokendev/superhot-30b-8k-no-rlhf-test i've confirmed that i can load the model in vllm and successfully generate completions but the context length is still only 2048.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: supporting superhot models? new-model specifically: - https://huggingface.co/kaiokendev/superhot-30b-8k-no-rlhf-test i've confirmed that i can load the model in vllm and successfully generate completions but the context...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: supporting superhot models? new-model specifically: - https://huggingface.co/kaiokendev/superhot-30b-8k-no-rlhf-test i've confirmed that i can load the model in vllm and successfully generate completions but the context...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ecifically: - https://huggingface.co/kaiokendev/superhot-30b-8k-no-rlhf-test i've confirmed that i can load the model in vllm and successfully generate completions but the context length is still only 2048.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
