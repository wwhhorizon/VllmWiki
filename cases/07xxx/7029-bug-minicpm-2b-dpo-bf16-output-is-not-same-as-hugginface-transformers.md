# vllm-project/vllm#7029: [Bug]: MiniCPM-2B-dpo-bf16 output is not same as hugginface transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#7029](https://github.com/vllm-project/vllm/issues/7029) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniCPM-2B-dpo-bf16 output is not same as hugginface transformers

### Issue 正文摘录

### Your current environment vllm==0.5.0 transformers==4.42.4 ### 🐛 Describe the bug this is vllm: ``` llm = LLM(model=args.ckpt_dir, trust_remote_code=True, seed=42, tensor_parallel_size=torch.cuda.device_count()) sampling_params = SamplingParams( n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.3, top_p=0.7, top_k=20, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[' '], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2048, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None ) input_texts=" 了解罗马的可以解释一下什么是紫罗;绿罗;蓝罗;红罗;三罗;神罗分别是什么吗？ " outputs = llm.generate(input_texts, sampling_params, use_tqdm=False) ``` outputs is "抱歉，但您提供的信息似乎是关于古代罗马的服装" this is hugginface: ``` tokenizer = AutoTokenizer.from_pretrained(args.ckpt_dir, trust_remote_code=True) model = AutoModelForCausalLM.from_pretrained( args.ckpt_dir, trust_remote_code=True, torch_dtype=torch.bfloat16 ).cuda() generation_config = GenerationConfig.from_pretrained(args.ckpt_dir, trust_remote_code=True) ##GenerationCon...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: MiniCPM-2B-dpo-bf16 output is not same as hugginface transformers bug ### Your current environment vllm==0.5.0 transformers==4.42.4 ### 🐛 Describe the bug this is vllm: ``` llm = LLM(model=args.ckpt_dir, trust_re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gs.ckpt_dir, trust_remote_code=True, seed=42, tensor_parallel_size=torch.cuda.device_count()) sampling_params = SamplingParams( n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temper...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nsformers==4.42.4 ### 🐛 Describe the bug this is vllm: ``` llm = LLM(model=args.ckpt_dir, trust_remote_code=True, seed=42, tensor_parallel_size=torch.cuda.device_count()) sampling_params = SamplingParams( n=1, best_of=1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _tokens=2048, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None ) input_texts=" 了解罗马的可以解释一下什么是紫罗;绿罗;蓝罗;红罗;三罗;神罗分别是什么吗？ " outputs...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: rature=0.3, top_p=0.7, top_k=20, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[' '], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2048,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
