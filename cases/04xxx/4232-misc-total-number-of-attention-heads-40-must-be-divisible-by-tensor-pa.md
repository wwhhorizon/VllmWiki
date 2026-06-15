# vllm-project/vllm#4232: [Misc]: Total number of attention heads (40) must be divisible by tensor parallel size (6)

| 字段 | 值 |
| --- | --- |
| Issue | [#4232](https://github.com/vllm-project/vllm/issues/4232) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Total number of attention heads (40) must be divisible by tensor parallel size (6)

### Issue 正文摘录

### Anything you want to discuss about vllm. I want to deploy qwen-1.5-32B,but there is a problem:Total number of attention heads (40) must be divisible by tensor parallel size (6).how could I do to overcome this problem?my vllm version is 0.4.1+cu118,thanks a lot!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tensor parallel size (6).how could I do to overcome this problem?my vllm version is 0.4.1+cu118,thanks a lot!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: size (6) ### Anything you want to discuss about vllm. I want to deploy qwen-1.5-32B,but there is a problem:Total number of attention heads (40) must be divisible by tensor parallel size (6).how could I do to overcome th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
