# vllm-project/vllm#3607: [Bug]: The fine-tuned qwen1.5 model uses transformers generate() to have a normal dialogue, but the dialogue output using vllm openai API has multiple line breaks.

| 字段 | 值 |
| --- | --- |
| Issue | [#3607](https://github.com/vllm-project/vllm/issues/3607) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The fine-tuned qwen1.5 model uses transformers generate() to have a normal dialogue, but the dialogue output using vllm openai API has multiple line breaks.

### Issue 正文摘录

### Your current environment ```text vllm==0.3.3+cu118 transformers==4.38.2 qwen1.5-14B-Chat A100 GPU ``` ### 🐛 Describe the bug # The fine-tuned qwen1.5 model uses transfoemers generate() to have a normal dialogue, but the dialogue output using vllm openai API has multiple line breaks. ## 1. transfoemers generate() dialog is normal **model_checkpoint** is my fine-tuned qwen1.5 model. ### 1.1 code as follows: ```python model = AutoModelForCausalLM.from_pretrained( model_checkpoint, torch_dtype="auto", device_map="auto" ) from transformers import TextStreamer tokenizer = AutoTokenizer.from_pretrained(model_checkpoint) streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True) messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "介绍一下武汉"} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) model_inputs = tokenizer([text], return_tensors="pt").to(device) generated_ids = model.generate( model_inputs.input_ids, max_new_tokens=1024, streamer=streamer, ) ``` ### 1.2 Output ``` 你好，我很乐意为你介绍武汉。 武汉，简称“汉”，是中国湖北省的省会，位于长江中游，素有“九省通衢”之称，是华中地区最大的城市和交通枢纽。武汉有着悠久的历史，被誉为“楚文化”的发源地之一，拥有丰富的历史...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: point, torch_dtype="auto", device_map="auto" ) from transformers import TextStreamer tokenizer = AutoTokenizer.from_pretrained(model_checkpoint) streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The fine-tuned qwen1.5 model uses transformers generate() to have a normal dialogue, but the dialogue output using vllm openai API has multiple line breaks. bug;stale ### Your current environment ```text vllm==0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the dialogue output using vllm openai API has multiple line breaks. bug;stale ### Your current environment ```text vllm==0.3.3+cu118 transformers==4.38.2 qwen1.5-14B-Chat A100 GPU ``` ### 🐛 Describe the bug # The fine-t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: = AutoModelForCausalLM.from_pretrained( model_checkpoint, torch_dtype="auto", device_map="auto" ) from transformers import TextStreamer tokenizer = AutoTokenizer.from_pretrained(model_checkpoint) streamer = TextStreamer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ronment ```text vllm==0.3.3+cu118 transformers==4.38.2 qwen1.5-14B-Chat A100 GPU ``` ### 🐛 Describe the bug # The fine-tuned qwen1.5 model uses transfoemers generate() to have a normal dialogue, but the dialogue output...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
