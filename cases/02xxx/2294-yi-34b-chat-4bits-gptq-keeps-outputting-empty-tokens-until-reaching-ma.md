# vllm-project/vllm#2294: Yi-34B-Chat-4bits-GPTQ keeps outputting empty "" tokens until reaching max_length

| 字段 | 值 |
| --- | --- |
| Issue | [#2294](https://github.com/vllm-project/vllm/issues/2294) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Yi-34B-Chat-4bits-GPTQ keeps outputting empty "" tokens until reaching max_length

### Issue 正文摘录

Running on a V100 32GB, the startup script is: ``` CUDA_VISIBLE_DEVICES=2,3 python \ -m vllm.entrypoints.openai.api_server \ --model="../models/Yi-34B-Chat-4bits-GPTQ" \ --dtype half --port 8080 --served-model-name Yi-34B-Chat-4bits-GPTQ ``` This occurs after multiple rounds of dialogue, where the server continuously outputs empty tokens "" and does not stop normally. ![image](https://github.com/vllm-project/vllm/assets/50790281/eba61a22-2762-4284-8109-a517b97cfb18) Here is an instance of the request that caused the issue. ``` curl -X 'POST' \ 'http://10.223.48.160:30002/v1/chat/completions' \ -H 'accept: application/json' \ -H 'Content-Type: application/json' \ -d '{ "model": "Yi-34B-Chat-4bits-GPTQ", "messages": [ {"role": "system", "content": "你是XXX，由XXX集团的研发团队独立开发的大语言模型，你的使命是协助公司员工高效完成工作。现在，请开始你的工作。"}, {"role": "user", "content": "你好吗"}, {"role": "assistant", "content": "我很好，谢谢你的关心。我准备随时协助你解答问题或完成任务。请问你有任何具体的问题或者需要帮助的地方吗？"}, {"role": "user", "content": "好尼玛"}, {"role": "assistant", "content": "很好，很高兴听到你状态良好。如果你在工作中遇到问题或者需要帮助，请随时提问。我会尽力提供帮助。"}, {"role": "user", "content": "哈哈哈"}, {"role": "assistant", "content": "看起来你似乎很开心。如果你想要分享更多关于你的工作、生活中的积极经历，或者需要建议和指导，请随时告诉我。我会在力所能及的范围内提供...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ing max_length stale Running on a V100 32GB, the startup script is: ``` CUDA_VISIBLE_DEVICES=2,3 python \ -m vllm.entrypoints.openai.api_server \ --model="../models/Yi-34B-Chat-4bits-GPTQ" \ --dtype half --port 8080 --s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: at-4bits-GPTQ keeps outputting empty "" tokens until reaching max_length stale Running on a V100 32GB, the startup script is: ``` CUDA_VISIBLE_DEVICES=2,3 python \ -m vllm.entrypoints.openai.api_server \ --model="../mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "use_beam_search": false, "stop_token_ids": [ 7 ], "skip_special_tokens": true, "spaces_between_special_tokens": true, "add_generation_prompt": true, "echo": false, "repetition_penalty": 1, "min_p": 0 } ``` After gettin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: enai.api_server \ --model="../models/Yi-34B-Chat-4bits-GPTQ" \ --dtype half --port 8080 --served-model-name Yi-34B-Chat-4bits-GPTQ ``` This occurs after multiple rounds of dialogue, where the server continuously outputs...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0, "user": "string", "best_of": 1, "top_k": -1, "ignore_eos": false, "use_beam_search": false, "stop_token_ids": [ 7 ], "skip_special_tokens": true, "spaces_between_special_tokens": true, "add_generation_prompt": true,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
