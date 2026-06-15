# vllm-project/vllm#13028: [Usage]: Ultravox-like Usage

| 字段 | 值 |
| --- | --- |
| Issue | [#13028](https://github.com/vllm-project/vllm/issues/13028) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Ultravox-like Usage

### Issue 正文摘录

### Your current environment Hi everyone, I would like to use VLLM to serve Ultravox models. Using Ultravox, I have the following code: ``` inference = ultravox_infer.UltravoxInference( "fixie-ai/ultravox-v0_4_1-llama-3_1-8b", device=None, data_type=None, conversation_mode=True ) user_audio_prompt = datasets.datasets.VoiceSample.from_prompt_and_file(" ", "/content/meine_tel_nummer.mp3") gen = inference.infer_stream(user_audio_prompt) print(next(gen)) ``` Using "**conversation_mode=True**", the Ultravox model will "remember" the past conversation and **inference.infer_stream()** allows streaming the tokens. Now, I would like to implement the same using VLLM. Currently, using [audio_language.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/audio_language.py), I came up with this code: ``` model_name = "fixie-ai/ultravox-v0_4_1-llama-3_1-8b" tokenizer = AutoTokenizer.from_pretrained(model_name) messages = [{ 'role': 'user', 'content': " \n" }] prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True) llm = LLM(model=model_name, max_model_len=4096, max_num_seqs=5, trust_remote_code=True, limit_mm_per_prompt={"audio": audi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt environment Hi everyone, I would like to use VLLM to serve Ultravox models. Using Ultravox, I have the following code: ``` inference = ultravox_infer.UltravoxInference( "fixie-ai/ultravox-v0_4_1-llama-3_1-8b", device...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ly_chat_template(messages, tokenize=False, add_generation_prompt=True) llm = LLM(model=model_name, max_model_len=4096, max_num_seqs=5, trust_remote_code=True, limit_mm_per_prompt={"audio": audio_cou
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
