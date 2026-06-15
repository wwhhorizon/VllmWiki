# vllm-project/vllm#9961: [help wanted]: fix broken xverse model 

| 字段 | 值 |
| --- | --- |
| Issue | [#9961](https://github.com/vllm-project/vllm/issues/9961) |
| 状态 | closed |
| 标签 | help wanted |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [help wanted]: fix broken xverse model 

### Issue 正文摘录

### Anything you want to discuss about vllm. Per the discussion in https://github.com/vllm-project/vllm/issues/9669 , this issue is to ask for help from model vendors or the community. For the xverse model added by https://github.com/vllm-project/vllm/pull/3610 , the tokenizer in the huggingface repo [huggingface.co/xverse/XVERSE-7B-Chat/tree/main](https://huggingface.co/xverse/XVERSE-7B-Chat/tree/main) is broken in recent transformers, leading to an error similar to https://github.com/huggingface/transformers/issues/31789 . For more information, I find that I have to use the tokenizer from meta-llama/Llama-2-7b-chat-hf in order to run the model. cc @hxer7963 who contributes this model. If the issue cannot be solved in 4 weeks ( 11.2 - 11.30, both inclusive) , we will delete the model from vllm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [help wanted]: fix broken xverse model help wanted ### Anything you want to discuss about vllm. Per the discussion in https://github.com/vllm-project/vllm/issues/9669 , this issue is to ask for help from model vendors o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
