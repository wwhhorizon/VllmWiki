# vllm-project/vllm#12742: [Usage]: Empty mm_placeholders when running Qwen2-VL-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#12742](https://github.com/vllm-project/vllm/issues/12742) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Empty mm_placeholders when running Qwen2-VL-7B

### Issue 正文摘录

### Your current environment I am using vllm v0.7.1. My script looks like below. ```python model_directory=“xxx/Qwen-XL-7B” LLM(model=model_directory, tensor_parallel_size=np, max_num_seqs=batch_size, max_seq_len_to_capture=prompt_token_count+output_token_count+1, max_model_len=163840, max_num_batched_tokens=163840, limit_mm_per_prompt={"image": 2}) image_lion = "002_The_lion_king_Snyggve_in_the_Serengeti_National_Park_Photo_by_Giles_Laurent.jpg" question = "What is the content of each image? " def multi_modal_prompts(model, model_directory, batch_size, prompt_token_count, question, image_lion): image = Image.open(image_lion) prompt = { "prompt": question, "multi_modal_data": {"image": image} } prompts = [] for _ in range(batch_size): prompts.append(prompt) return prompts sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=output_token_count, ignore_eos=True) multi_modal_inputs = multi_modal_prompts(model, model_directory, batch_size, prompt_token_count, question, image_lion) generated_ids = model.generate(multi_modal_inputs, sampling_params=sampling_params) ``` The error is ```bash [rank0]: File "/scratch/kdur_root/kdur/yufenggu/miniforge3/envs/vllm/lib/pytho...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Empty mm_placeholders when running Qwen2-VL-7B usage ### Your current environment I am using vllm v0.7.1. My script looks like below. ```python model_directory=“xxx/Qwen-XL-7B” LLM(model=model_directory, tensor...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: _tokens(tokenizer, prompt_ids) mm_placeholders = hf_mm_placeholders else: ( prompt_ids, prompt, missing_mm_placeholders, ) = self._apply_prompt_replacements( prompt_ids, mm_missing_repls, mm_missing_repl_counts, ) print...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: _repls.values()): tokenizer = self.info.get_tokenizer() prompt = decode_tokens(tokenizer, prompt_ids) mm_placeholders = hf_mm_placeholders else: ( prompt_ids, prompt, missing_mm_placeholders, ) = self._apply_prompt_repl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ay. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
