# vllm-project/vllm#39108: [Bug]: Complex tool json schemas not dereferenced before passing to chat templates

| 字段 | 值 |
| --- | --- |
| Issue | [#39108](https://github.com/vllm-project/vllm/issues/39108) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Complex tool json schemas not dereferenced before passing to chat templates

### Issue 正文摘录

### Your current environment local testing from main ### 🐛 Describe the bug When users are using complex JSON schemas in their tool definitions with features like `anyOf`, `$ref`, `$def`, and so on we're not deferencing those `$ref` nor are we flattening any of the `anyOf` things into lists before passing to chat templates. The net result of this is most models do not actually see those referenced properties or anyOf types in their rendered chat templates, as the jinja templates can't easily dereference these things. See https://github.com/vllm-project/vllm/issues/39089#issuecomment-4194272963 for an example where I noticed this as part of a separate user-reported bug. Potential options here include using the `jsonref` library to flatten all function tool call properties before we pass them to tokenizers, such as within our `OpenAIServingRender` class and its `render_chat` method. Likewise, we should probably flatten `anyOf` types to type lists, and exclude `nullable` there as that's already handled via the `required` field on function definition. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s with features like `anyOf`, `$ref`, `$def`, and so on we're not deferencing those `$ref` nor are we flattening any of the `anyOf` things into lists before passing to chat templates. The net result of this is most mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o lists before passing to chat templates. The net result of this is most models do not actually see those referenced properties or anyOf types in their rendered chat templates, as the jinja templates can't easily derefe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: before passing to chat templates bug ### Your current environment local testing from main ### 🐛 Describe the bug When users are using complex JSON schemas in their tool definitions with features like `anyOf`, `$ref`, `$...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
