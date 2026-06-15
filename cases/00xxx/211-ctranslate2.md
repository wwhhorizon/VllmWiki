# vllm-project/vllm#211: CTranslate2

| 字段 | 值 |
| --- | --- |
| Issue | [#211](https://github.com/vllm-project/vllm/issues/211) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> CTranslate2

### Issue 正文摘录

Hello, Thanks for the great framework for deploying LLM. Would it be possible to use a LLM model compiled with the CTranslate2 library?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: at framework for deploying LLM. Would it be possible to use a LLM model compiled with the CTranslate2 library?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he great framework for deploying LLM. Would it be possible to use a LLM model compiled with the CTranslate2 library?
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: CTranslate2 feature request Hello, Thanks for the great framework for deploying LLM. Would it be possible to use a LLM model compiled with the CTranslate2 library?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
