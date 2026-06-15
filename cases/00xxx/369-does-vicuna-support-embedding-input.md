# vllm-project/vllm#369: does vicuna support embedding input?

| 字段 | 值 |
| --- | --- |
| Issue | [#369](https://github.com/vllm-project/vllm/issues/369) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> does vicuna support embedding input?

### Issue 正文摘录

Does vllm support embedding input in vicuna model, in official version support embedding input like llm_model.generate(inputs_embeds=inputs_embeds)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ature request Does vllm support embedding input in vicuna model, in official version support embedding input like llm_model.generate(inputs_embeds=inputs_embeds)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dding input? feature request Does vllm support embedding input in vicuna model, in official version support embedding input like llm_model.generate(inputs_embeds=inputs_embeds)
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: does vicuna support embedding input? feature request Does vllm support embedding input in vicuna model, in official version support embedding input like llm_model.generate(inputs_embeds=inputs_embeds)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
