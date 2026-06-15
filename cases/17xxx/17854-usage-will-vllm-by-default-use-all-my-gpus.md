# vllm-project/vllm#17854: [Usage]: Will vllm by default use all my gpus?

| 字段 | 值 |
| --- | --- |
| Issue | [#17854](https://github.com/vllm-project/vllm/issues/17854) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Will vllm by default use all my gpus?

### Issue 正文摘录

### Your current environment 2x3090s ### How would you like to use vllm I have below code: ```Python def zero_eval_vllm(df, model_name="facebook/opt-125m", batch_size=5, agieval=False): full_prompts = [] for _, row in df.iterrows(): question = row["question"] if agieval: choices_str = row["answer"] else: choices = eval(row["options"]) choices_str = "\n".join([f"({chr(65+i)}) {c}" for i, c in enumerate(choices)]) user_prompt = f"---\nQ: {question}\nChoices:\n{choices_str}\nA:" full_prompts.append(user_prompt) sampling_params = SamplingParams(max_tokens=2035) llm = LLM(model=model_name, dtype="float16") outputs = [] for i in tqdm(range(0, len(full_prompts), batch_size)): batch_prompts = full_prompts[i:i+batch_size] batch_outputs = llm.generate(batch_prompts, use_tqdm=True, sampling_params) outputs.extend([out.outputs[0].text.strip() for out in batch_outputs]) df["full_prompt"] = full_prompts df["model_output"] = outputs model_name_clean = model_name.split("/")[-1].replace(":", "_") timestamp = datetime.now().strftime("%H-%M_%Y-%m-%d") folder_name = model_name_clean os.makedirs(folder_name, exist_ok=True) file_name = f"{model_name_clean}_{timestamp}.csv" file_path = os.path.join(fold...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: params = SamplingParams(max_tokens=2035) llm = LLM(model=model_name, dtype="float16") outputs = [] for i in tqdm(range(0, len(full_prompts), batch_size)): batch_prompts = full_prompts[i:i+batch_size] batch_outputs = llm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: v(file_path, index=False) ``` I am confused whether vllm will use all 8xA100s that I have available or not ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the cha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: # How would you like to use vllm I have below code: ```Python def zero_eval_vllm(df, model_name="facebook/opt-125m", batch_size=5, agieval=False): full_prompts = [] for _, row in df.iterrows(): question = row["question"...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ro_eval_vllm(df, model_name="facebook/opt-125m", batch_size=5, agieval=False): full_prompts = [] for _, row in df.iterrows(): question = row["question"] if agieval: choices_str = row["answer"] else: choices = eval(row["...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: u like to use vllm I have below code: ```Python def zero_eval_vllm(df, model_name="facebook/opt-125m", batch_size=5, agieval=False): full_prompts = [] for _, row in df.iterrows(): question = row["question"] if agieval:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
