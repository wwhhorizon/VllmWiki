# vllm-project/vllm#19368: [Bug]: Incorrect "text_offset" when "--return_tokens_as_token_ids" is enabled

| 字段 | 值 |
| --- | --- |
| Issue | [#19368](https://github.com/vllm-project/vllm/issues/19368) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect "text_offset" when "--return_tokens_as_token_ids" is enabled

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `--return_tokens_as_token_ids` is enabled, the `response.choices[0].logprobs.text_offset` is calculated by accumating the length of f"token_id:{token_id}", but not the actual token length. It makes the returned text_offset even longer than `response.choices[0].text` Start the server as: ```bash vllm serve "facebook/opt-125m" --port 8000 --return_tokens_as_token_ids ``` Example to reproduce the issue: ```python from transformers import AutoTokenizer from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key='vllm') model = "facebook/opt-125m" prompt = "Hello, my name is" response = client.completions.create(model=model, prompt=prompt, temperature=0.8, top_p=0.95, logprobs=0) print('Returned offset:\n', response.choices[0].logprobs.text_offset) # Returned offset: # [0, 13, 23, 35, 48, 59, 71, 84, 94, 105, 116, 127, 138, 151, 161, 172] print('Returned text:\n', response.choices[0].text) # Returned text: # Joel, my dad is my friend and we are in a relationship. I am tokenizer = AutoTokenizer.from_pretrained(model) token_ids = tokenizer.encode(response.choices[0].text, add_special_tokens=False) expecte...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ken_ids ``` Example to reproduce the issue: ```python from transformers import AutoTokenizer from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key='vllm') model = "facebook/opt-125m" pro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: correct "text_offset" when "--return_tokens_as_token_ids" is enabled bug;stale ### Your current environment ### 🐛 Describe the bug When `--return_tokens_as_token_ids` is enabled, the `response.choices[0].logprobs.text_o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: t) # Returned text: # Joel, my dad is my friend and we are in a relationship. I am tokenizer = AutoTokenizer.from_pretrained(model) token_ids = tokenizer.encode(response.choices[0].text, add_special_tokens=False) expect...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
