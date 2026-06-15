# vllm-project/vllm#6271: [Bug]: Generate with Random Seed throws exception claiming the seed is a str

| 字段 | 值 |
| --- | --- |
| Issue | [#6271](https://github.com/vllm-project/vllm/issues/6271) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Generate with Random Seed throws exception claiming the seed is a str

### Issue 正文摘录

### Your current environment Python 3.9 vllm==0.5.1 vllm-flash-attn==2.5.9 ### 🐛 Describe the bug I'm trying to generate with a seed ```python sampling_params = SamplingParams(seed=seed, top_k=10, n=1, stop_token_ids=terminators, max_tokens=None, temperature=0.1,) print(sampling_params) gen_results = llm.generate(prompt_list, sampling_params=sampling_params) ``` However, it throws an exception claiming that the seed passed is a string, ```text SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.1, top_p=1.0, top_k=10, min_p=0.0, seed=9553, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[128001, 128009], include_stop_str_in_output=False, ignore_eos=False, max_tokens=None, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None) --------------------------------------------------------------------------- RuntimeError Traceback (most recent call last) Cell In[85], line 9 7 sampling_params = SamplingParams(seed=seed, top_k=10, n=1, stop_token_ids=terminators, max_tokens=None, temperature=0.1,) 8 prin...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: enerate(self, prompts, sampling_params, prompt_token_ids, use_tqdm, lora_request) 301 sampling_params = SamplingParams() 303 self._validate_and_add_requests( 304 inputs=inputs, 305 params=sampling_params, 306 lora_reque...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rature=0.1, top_p=1.0, top_k=10, min_p=0.0, seed=9553, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[128001, 128009], include_stop_str_in_output=False, ignore_eos=False, max_t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _tokens=None, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None) ---------------------------------------------------------------...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , temperature=0.1, top_p=1.0, top_k=10, min_p=0.0, seed=9553, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[128001, 128009], include_stop_str_in_output=False, ignore_eos=False...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ted_token_indices, 119 dtype=torch.long, 120 target_device=device, 121 pin_memory=pin_memory) 122 categorized_sample_indices = { 12

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
