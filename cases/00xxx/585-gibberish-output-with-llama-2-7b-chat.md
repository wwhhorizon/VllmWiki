# vllm-project/vllm#585: Gibberish output with llama-2-7b-chat

| 字段 | 值 |
| --- | --- |
| Issue | [#585](https://github.com/vllm-project/vllm/issues/585) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Gibberish output with llama-2-7b-chat

### Issue 正文摘录

I'm using llama-2-7b-chat through vLLM. I have tried redownloading the model 2 times and I'm facing the same issue. I've also tried using different tokenizers. When I query "What is the capital of Germany?" It responds with: iskaὶід}$.)}{nex програ FoiProgramкли Referencias nov laugh maven нап "," I am unsure on what to do next. I'm trying to redownload the model once again, but if that also does not work, I don't know how to resolve this. I've attached a screenshot of my notebook below.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Gibberish output with llama-2-7b-chat I'm using llama-2-7b-chat through vLLM. I have tried redownloading the model 2 times and I'm facing the same issue. I've also tried using different tokenizers. When I query "What is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hat through vLLM. I have tried redownloading the model 2 times and I'm facing the same issue. I've also tried using different tokenizers. When I query "What is the capital of Germany?" It responds with: iskaὶід}$.)}{nex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
