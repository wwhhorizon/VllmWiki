# vllm-project/vllm#6429: [Bug]: illegal memory access when increase max_model_length on FP8 models

| 字段 | 值 |
| --- | --- |
| Issue | [#6429](https://github.com/vllm-project/vllm/issues/6429) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: illegal memory access when increase max_model_length on FP8 models

### Issue 正文摘录

### Your current environment ```text # Using pip install vllm vllm==v0.5.1 ``` ### 🐛 Describe the bug ```text # My python script to test long text def run_Mixtral(): tokenizer = AutoTokenizer.from_pretrained("/mnt/beegfs2/maojunxiong/Mixtral-8x7B-Instruct-v0.1-FP8-KV2", trust_remote_code=True) sampling_params = SamplingParams(max_tokens=100, temperature=1, top_p=0.01, top_k=1) llm = LLM(model="/mnt/beegfs2/maojunxiong/Mixtral-8x7B-Instruct-v0.1-FP8-KV2", tensor_parallel_size=4, disable_custom_all_reduce=True, max_num_seqs=1, enforce_eager=False, kv_cache_dtype='fp8) with open('/mnt/beegfs2/maojunxiong/long_code_test1.txt', 'r', encoding='utf-8') as file: lines = file.readlines() third_line = lines[30].strip() prompts = third_line.split(' ')[0].strip().replace(" ", "\n") prompt_ids = tokenizer.encode(prompts, return_tensors="pt") num_tokens = len(prompt_ids[0]) print("prompt_tokens:", num_tokens) outputs = [] start_time = time.time() outputs = llm.generate(prompts, sampling_params) end_time = time.time() total_tokens = 0 for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text token = len(tokenizer.encode(generated_text)) total_tokens += token print(f"G...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: illegal memory access when increase max_model_length on FP8 models bug;stale ### Your current environment ```text # Using pip install vllm vllm==v0.5.1 ``` ### 🐛 Describe the bug ```text # My python script to tes...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: _size=4, disable_custom_all_reduce=True, max_num_seqs=1, enforce_eager=False, kv_cache_dtype='fp8) with open('/mnt/beegfs2/maojunxiong/long_code_test1.txt', 'r', encoding='utf-8') as file: lines = file.readlines() third...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vllm==v0.5.1 ``` ### 🐛 Describe the bug ```text # My python script to test long text def run_Mixtral(): tokenizer = AutoTokenizer.from_pretrained("/mnt/beegfs2/maojunxiong/Mixtral-8x7B-Instruct-v0.1-FP8-KV2", trust_remo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 43) ERROR 07-15 09:41:46 multiproc_worker_utils.py:226] output = ops.cutlass_scaled_mm( (VllmWorkerProcess pid=29143) ERROR 07-15 09:41:46 multiproc_worker_utils.py:226] File "/home/vllm/vllm/_custom_ops.py", line 34, i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n FP8 models bug;stale ### Your current environment ```text # Using pip install vllm vllm==v0.5.1 ``` ### 🐛 Describe the bug ```text # My python script to test long text def run_Mixtral(): tokenizer = AutoTokenizer.from...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
