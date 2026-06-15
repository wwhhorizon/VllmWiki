# vllm-project/vllm#5033: [Misc]: LLM is responding with advertisement

| 字段 | 值 |
| --- | --- |
| Issue | [#5033](https://github.com/vllm-project/vllm/issues/5033) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: LLM is responding with advertisement

### Issue 正文摘录

### Anything you want to discuss about vllm. Hello! I am a Chemical Engineer, so I am no up do date with all the progress in the LLM world. However, I found out something interesting and I did not found anything directly about it on internet. I am using LLM to parse some chemical synthesis paragraphs. In this specific case I want to give a synthesis paragraph and the LLM should return all samples inside it and some information about it as dictionary. It works pretty well with Mixtral-8x7B-v0.1 model, howvever more than half of the prompts are responded with a advertisement response: " Do you need a similar assignment done for you from scratch? We have qualified writers to help you. We assure you an A+ quality paper that is free from plagiarism. Order now for an Amazing Discount! Use Discount Code "Newclient" for a 15% Discount! NB: We do not resell papers. Upon ordering, we do an original paper exclusively for you." I tested with the Mixtral-7B-v0.1 and this don't happen. I am curious if this is something that the model was trained on, it is an automatic response from vLLM or there is other reason? The only thing that I changed between the two models is that the bigger model is ru...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sis paragraph and the LLM should return all samples inside it and some information about it as dictionary. It works pretty well with Mixtral-8x7B-v0.1 model, howvever more than half of the prompts are responded with a a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . I am using LLM to parse some chemical synthesis paragraphs. In this specific case I want to give a synthesis paragraph and the LLM should return all samples inside it and some information about it as dictionary. It wo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to help you. We assure you an A+ quality paper that is free from plagiarism. Order now for an Amazing Discount! Use Discount Code "Newclient" for a 15% Discount! NB: We do not resell papers. Upon ordering, we do an orig...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: l papers. Upon ordering, we do an original paper exclusively for you." I tested with the Mixtral-7B-v0.1 and this don't happen. I am curious if this is something that the model was trained on, it is an automatic respons...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
