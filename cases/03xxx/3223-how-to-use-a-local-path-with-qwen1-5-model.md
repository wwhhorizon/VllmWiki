# vllm-project/vllm#3223: How to use a local path with Qwen1.5 model?

| 字段 | 值 |
| --- | --- |
| Issue | [#3223](https://github.com/vllm-project/vllm/issues/3223) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to use a local path with Qwen1.5 model?

### Issue 正文摘录

I meet a problem when I use the following code， ``` File "/opt/conda/lib/python3.10/site-packages/requests/models.py", line 1021, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://www.modelscope.cn/api/v1/models//app/local/Qwen1.5-0.5B-Chat/revisions ``` ``` python from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_path="/app/local/Qwen1.5-0.5B-Chat" # Initialize the tokenizer tokenizer = AutoTokenizer.from_pretrained(model_path) # Pass the default decoding hyperparameters of Qwen1.5-7B-Chat # max_tokens is for the maximum length for generation. sampling_params = SamplingParams(temperature=0.7, top_p=0.8, repetition_penalty=1.05, max_tokens=512) # Input the model name or path. Can be GPTQ or AWQ models. llm = LLM(model=model_path,dtype="float16",trust_remote_code=True) # Prepare your prompts prompt = "给我介绍一下大型语言模型。" messages = [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) ``` Anyone who can help me? However, the...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: odel name or path. Can be GPTQ or AWQ models. llm = LLM(model=model_path,dtype="float16",trust_remote_code=True) # Prepare your prompts prompt = "给我介绍一下大型语言模型。" messages = [ {"role": "system", "content": "You are a help...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: How to use a local path with Qwen1.5 model? I meet a problem when I use the following code， ``` File "/opt/conda/lib/python3.10/site-packages/requests/models.py", line 1021, in raise_for_status raise HTTPError(http_erro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /app/local/Qwen1.5-0.5B-Chat/revisions ``` ``` python from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_path="/app/local/Qwen1.5-0.5B-Chat" # Initialize the tokenizer tokenizer = AutoToke...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: pt} ] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) ``` Anyone who can help me? However, the following code is work. ```python model_path="Qwen/Qwen1.5-0.5B-Chat" ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the following code， ``` File "/opt/conda/lib/python3.10/site-packages/requests/models.py", line 1021, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 404 Client Error: N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
