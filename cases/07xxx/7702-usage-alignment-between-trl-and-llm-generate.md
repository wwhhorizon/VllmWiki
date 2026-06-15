# vllm-project/vllm#7702: [Usage]: alignment between trl and llm.generate

| 字段 | 值 |
| --- | --- |
| Issue | [#7702](https://github.com/vllm-project/vllm/issues/7702) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: alignment between trl and llm.generate

### Issue 正文摘录

### Your current environment vllm 0.5.4 ### How would you like to use vllm hi authors, I sft the llms using trl Supervised Fine-tuning Trainer. As you can see here https://huggingface.co/docs/trl/en/sft_trainer#dataset-format-support, it supports `instruction format`. So i use it for my sft, and samples are like this: ``` {"prompt": "question1", "completion": "generation1"} {"prompt": "question2", "completion": "generation2"} {"prompt": "question3", "completion": "generation3"} ``` (as you may know, this is a common and practical template for many tasks.) SFT goes fine, then I try to launch the lora parameters from trl sft, via vllm. which is ok. like this : ``` responses = llm.generate(prompts, sampling_params, lora_request=LoRARequest("llama31_adapter_583", 3, args.ft) ) ``` my question is, assuming my inference dataset samples are like this: ``` {"prompt": "question4", "completion": "generation4"} {"prompt": "question5", "completion": "generation5"} {"prompt": "question6", "completion": "generation6"} ``` then `prompts` will be [question4, question5, question6 ...] should I make some changes on `prompts` ? I mean should I add some special token on each sample of `prompts` ? the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s using trl Supervised Fine-tuning Trainer. As you can see here https://huggingface.co/docs/trl/en/sft_trainer#dataset-format-support, it supports `instruction format`. So i use it for my sft, and samples are like this:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: alignment between trl and llm.generate usage;stale ### Your current environment vllm 0.5.4 ### How would you like to use vllm hi authors, I sft the llms using trl Supervised Fine-tuning Trainer. As you can see...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ] should I make some changes on `prompts` ? I mean should I add some special token on each sample of `prompts` ? the reason why I ask is because I see on your vllm document that when doing inference, `tokenizer.apply_ch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: okenizer.apply_chat_template(msg, add_generation_prompt=True, tokenize=False)` is needed, which will format the original msg, or maybe question in my case, into llm-specific format, with added generation token. the same...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
