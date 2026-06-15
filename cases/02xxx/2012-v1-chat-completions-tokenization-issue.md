# vllm-project/vllm#2012: "/v1/chat/completions" tokenization issue

| 字段 | 值 |
| --- | --- |
| Issue | [#2012](https://github.com/vllm-project/vllm/issues/2012) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> "/v1/chat/completions" tokenization issue

### Issue 正文摘录

# Context The "/v1/chat/completions" endpoint uses the `apply_chat_template` method of the HF tokenizers. It seems to us that these templates take care of adding special tokens (cf. [this line from Llama's default template]( https://github.com/huggingface/transformers/blob/5e620a92cf7e6c312435db86ec55e13b75dece75/src/transformers/models/llama/tokenization_llama.py#L460)). However, tokenization in vLLM also seems to add special token(s) if this is the tokenizer's default behavior - in particular, the Llama tokenizer adds a BOS token at the start of its tokenization. There are therefore configurations in which the final tokenization will contain more special tokens than necessary. # Repro In a terminal, launch a vLLM server. For example: ```python python -m vllm.entrypoints.openai.api_server --model TheBloke/Llama-2-7B-Chat-AWQ ``` In another terminal, request this server: ``` from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "None" openai_api_base = f"http://{FILL_ME}/v1" client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) chat_response = client.chat.completions.create( model="TheBloke/Llama-2-7B-Chat-AWQ", mes...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: /chat/completions" endpoint uses the `apply_chat_template` method of the HF tokenizers. It seems to us that these templates take care of adding special tokens (cf. [this line from Llama's default template]( https://gith...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: F tokenizers. It seems to us that these templates take care of adding special tokens (cf. [this line from Llama's default template]( https://github.com/huggingface/transformers/blob/5e620a92cf7e6c312435db86ec55e13b75dec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: storians play cricket?\n\nBecause they prefer to leave their past in the archives!\n\nAnd now, if you'll excuse me, I must return to my scholarly pursuits. Although, I must admit, it is rather refreshing to engage in su...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: =1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], ignore_eos=False, max_tokens=3959, logprobs=None, prompt_logprobs=None,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pi_server --model TheBloke/Llama-2-7B-Chat-AWQ ``` In another terminal, request this server: ``` from openai import OpenAI # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "None" openai_api...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
