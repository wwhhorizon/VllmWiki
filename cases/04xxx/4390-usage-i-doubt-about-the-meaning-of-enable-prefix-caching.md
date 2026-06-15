# vllm-project/vllm#4390: [Usage]: I doubt about the meaning of --enable-prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#4390](https://github.com/vllm-project/vllm/issues/4390) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I doubt about the meaning of --enable-prefix-caching

### Issue 正文摘录

### Your current environment 1. I doubt which version that starting support feat `--enable-prefix-caching`. (seems v0.3.0 still not support yet, and v0.4.0 has supported it already) 2. does `--enable-prefix-caching` mean to prefix system prompt only? or is it an implementation of RadixAttention (https://arxiv.org/abs/2312.07104)? what is the difference between prefix-caching and prefix-sharing (the following implementation)? ``` if prefix_len != None: # start inference if prompt_token_ids != None: outputs = llm.generate(prompt_token_ids=prompt_token_ids, sampling_params=sampling_params, prefix_pos=prefix_len * (len(prompts) // len(prefix_len))) else: outputs = llm.generate(prompts=prompts, sampling_params=sampling_params, prefix_pos=prefix_len * (len(prompts) // len(prefix_len))) else: outputs = llm.generate(prompts, sampling_params=sampling_params) ``` ### How would you like to use vllm I want to know more details about `--enable-prefix-caching` and the releated paper.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: able-prefix-caching usage ### Your current environment 1. I doubt which version that starting support feat `--enable-prefix-caching`. (seems v0.3.0 still not support yet, and v0.4.0 has supported it already) 2. does `--...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: prefix_pos=prefix_len * (len(prompts) // len(prefix_len))) else: outputs = llm.generate(prompts=prompts, sampling_params=sampling_params, prefix_pos=prefix_len * (len(prompts) // len(prefix_len))) else:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
