# vllm-project/vllm#4755: Regression in support of customized "role" in OpenAI compatible API (v.0.4.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#4755](https://github.com/vllm-project/vllm/issues/4755) |
| 状态 | closed |
| 标签 | good first issue |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Regression in support of customized "role" in OpenAI compatible API (v.0.4.2)

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/4745 Originally posted by **tanliboy** May 10, 2024 Hi vLLM team, We have been using vLLM for serving models, and it went really well. We have been using the OpenAI compatible API along with our customized "role" for different entities. However, when we upgraded the version to v0.4.2 recently, we realized that the customized "role" is not supported and the role is only limited to "system", "user", and "assistant". I understand that it is tightly aligned with OpenAI's chat completion role definition; however, it limits the customization of different roles along with fine-tuning. Moreover, we also saw a trend (including the recent Llama3 chat template) to support different roles for multi-agent interactions. Can you upgrade to bring back the previous support of customized roles in OpenAI chat completion APIs? Thanks, Li

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: liboy** May 10, 2024 Hi vLLM team, We have been using vLLM for serving models, and it went really well. We have been using the OpenAI compatible API along with our customized "role" for different entities. However, when...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: customized "role" for different entities. However, when we upgraded the version to v0.4.2 recently, we realized that the customized "role" is not supported and the role is only limited to "system", "user", and "assistan...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Regression in support of customized "role" in OpenAI compatible API (v.0.4.2) good first issue ### Discussed in https://github.com/vllm-project/vllm/discussions/4745 Originally posted by **tanliboy** May 10, 2024 H

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
