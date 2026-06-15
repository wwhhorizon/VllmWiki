# vllm-project/vllm#415: I want use the function prefix_allowed_tokens_fn of huggingface model.generate(), where of vllm's source code shall I modify?

| 字段 | 值 |
| --- | --- |
| Issue | [#415](https://github.com/vllm-project/vllm/issues/415) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> I want use the function prefix_allowed_tokens_fn of huggingface model.generate(), where of vllm's source code shall I modify?

### Issue 正文摘录

Hello, we all know that in huggingface transformers' origin `model.generate()` method, we can set the function paremeter `prefix_allowed_tokens_fn` to restrict the generation rule. I want to use this function in vllm just like I used in origin `model.generate()` to control the generation process, could you please tell me where of the source code shall I modify to make the model generation obey my custom prefix_allowed_tokens_fn?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: I want use the function prefix_allowed_tokens_fn of huggingface model.generate(), where of vllm's source code shall I modify? good first issue;feature request Hello, we all know that in huggingface transformers' origin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: (), where of vllm's source code shall I modify? good first issue;feature request Hello, we all know that in huggingface transformers' origin `model.generate()` method, we can set the function paremeter `prefix_allowed_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
