# vllm-project/vllm#1000: Inference server not working with models tuned on <|system|>,<|prompter|>,<|assistant|> or <|im_start|>,<|im_end|> format

| 字段 | 值 |
| --- | --- |
| Issue | [#1000](https://github.com/vllm-project/vllm/issues/1000) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Inference server not working with models tuned on <\|system\|>,<\|prompter\|>,<\|assistant\|> or <\|im_start\|>,<\|im_end\|> format

### Issue 正文摘录

Trying to run the vLLM server with https://huggingface.co/Open-Orca/LlongOrca-13B-16k but it returns just white space. It uses messages formatted as: ``` system You are LlongOrca, a large language model trained by Alignment Lab AI. Write out your reasoning step-by-step to be sure you get the right answers! ``` Also tried https://huggingface.co/OpenAssistant/llama2-13b-orca-8k-3319 but it returns empty. Message format: ``` system message user prompt ``` Is it possible to use models that require such different formatting? The vLLM request is abstracted away and only sends messages list. I tried wrapping the content with the special tokens. The only prompt format that works for me on vLLM server is ``` ### Instruction: ### Response: ``` from Open-Orca/OpenOrca-Platypus2-13B Maybe I am missing an argument when running the server?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Inference server not working with models tuned on <|system|>,<|prompter|>,<|assistant|> or <|im_start|>,<|im_end|> format Trying to run the vLLM server with https://huggingface.co/Open-Orca/LlongOrca-13B-16k but it retu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y and only sends messages list. I tried wrapping the content with the special tokens. The only prompt format that works for me on vLLM server is ``` ### Instruction: ### Response: ``` from Open-Orca/OpenOrca-Platypus2-1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: possible to use models that require such different formatting? The vLLM request is abstracted away and only sends messages list. I tried wrapping the content with the special tokens. The only prompt format that works fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
