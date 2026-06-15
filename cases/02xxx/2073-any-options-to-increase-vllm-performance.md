# vllm-project/vllm#2073: Any options to increase vLLM performance?

| 字段 | 值 |
| --- | --- |
| Issue | [#2073](https://github.com/vllm-project/vllm/issues/2073) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | attention;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Any options to increase vLLM performance?

### Issue 正文摘录

I am testing on A100 and H100, but the performance is significantly lower compared to TGI. TGI and vLLM have many similar features such as paged attention and continuous batch. I tested both serving solutions with the latest version using the LLaMA 2 70B model. I ran it with the default options, are there any options that need to be added or changed in order to improve vLLM performance? vLLM Setting Client Settings sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=500, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), Server Settings args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='/mnt/models/Llama-2-70b', tokenizer=None, revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pip...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Any options to increase vLLM performance? I am testing on A100 and H100, but the performance is significantly lower compared to TGI. TGI and vLLM have many similar features such as paged attention and continuous batch....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: batch. I tested both serving solutions with the latest version using the LLaMA 2 70B model. I ran it with the default options, are there any options that need to be added or changed in order to improve vLLM performance?...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: on and continuous batch. I tested both serving solutions with the latest version using the LLaMA 2 70B model. I ran it with the default options, are there any options that need to be added or changed in order to improve...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, block_size=16, seed=0, swap_space=4, gpu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: =1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=500, logprobs=None, prompt_logprobs=None, skip_special_tokens=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
