# vllm-project/vllm#655: My summarization output is being cutoff

| 字段 | 值 |
| --- | --- |
| Issue | [#655](https://github.com/vllm-project/vllm/issues/655) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> My summarization output is being cutoff

### Issue 正文摘录

I am trying to generate a summary from my prompt, but the output is being cutoff and I am seeing this in my output finish_reason=length I tried to set max_length and num_tokens but seems like vllm doesnt accept those args: ``` prompts = [""" Your task is to generate a short summary in bullet points of a message from a patient. 'Client requested message be sent to banker, declined in office appointment. Client believes they were overcharged, wants to cancel account.' BULLET POINT SUMMARY: """] vllm_llama = LLM( model="meta-llama/Llama-2-7b-chat-hf", tokenizer='meta-llama/Llama-2-7b-chat-hf', dtype="float16", ) sampling_params = SamplingParams(temperature=0.8, top_p=0.05) outputs = vllm_llama.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") Prompt: '\n Your task is to generate a short summary in bullet points of a message from a patient.\n\n ```Client requested message be sent to banker, declined in office appointment. Client believes they were overcharged, wants to cancel account.```\n\n BULLET POINT SUMMARY:\n ', Generated te...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ged, wants to cancel account.' BULLET POINT SUMMARY: """] vllm_llama = LLM( model="meta-llama/Llama-2-7b-chat-hf", tokenizer='meta-llama/Llama-2-7b-chat-hf', dtype="float16", ) sampling_params = SamplingParams(temperatu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Llama-2-7b-chat-hf", tokenizer='meta-llama/Llama-2-7b-chat-hf', dtype="float16", ) sampling_params = SamplingParams(temperature=0.8, top_p=0.05) outputs = vllm_llama.generate(prompts, sampling_params) # Print the output...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: short summary in bullet points of a message from a patient. 'Client requested message be sent to banker, declined in office appointment. Client believes they were overcharged, wants to cancel account.' BULLET POINT SUMM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
