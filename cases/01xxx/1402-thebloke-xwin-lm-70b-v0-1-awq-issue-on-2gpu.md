# vllm-project/vllm#1402: TheBloke/Xwin-LM-70B-V0.1-AWQ issue on 2GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#1402](https://github.com/vllm-project/vllm/issues/1402) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization;sampling_logits |
| 子分类 | debug |
| Operator 关键词 | quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> TheBloke/Xwin-LM-70B-V0.1-AWQ issue on 2GPU

### Issue 正文摘录

I'm running on 2GPU A100 the following code: ``` sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model=MODEL_NAME, quantization="awq", dtype="half", tensor_parallel_size=2) ``` and getting the *incomplete* error as ``` AssertionError Traceback (most recent call last) File , line 1 ----> 1 outputs = benchmark_generation_speed(MODEL_NAME, PROMPTS) File , line 6, in benchmark_generation_speed(model_name, prompts) 4 print(f"Benchmarking time to first token for {model_name}") 5 start_time = time.time() ----> 6 _1 = llm.generate(prompts[0], sampling_params) # Generate the first token 7 print(_1) # Avoid spark lazy execution 8 time_to_first_token = time.time() - start_time File /local_disk0/.ephemeral_nfs/cluster_libraries/python/lib/python3.10/site-packages/vllm/entrypoints/llm.py:157, in LLM.generate(self, prompts, sampling_params, prompt_token_ids, use_tqdm) 155 token_ids = prompt_token_ids[i] 156 self._add_request(prompt, sampling_params, token_ids) --> 157 return self._run_engine(use_tqdm) File /local_disk0/.ephemeral_nfs/cluster_libraries/python/lib/python3.10/site-packages/vllm/entrypoints/llm.py:177, in LLM._run_engine(self, use_tqdm) 175 outputs: List[Req...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ertion Error so I have no idea what is the issue. Help is very much appreciated development model_support;quantization;sampling_logits quantization;sampling crash dtype;env_dependency I'm running on 2GPU A100 the follow...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model=MODEL_NAME, quantization="awq", dtype="half", tensor_parallel_size=2) ``` and getting the *incomplete* error as ``` AssertionError Traceback (most recent call...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: = self._run_workers( 563 "execute_model", 564 seq_group_metadata_list=seq_group_metadata_list, 565 blocks_to_swap_in=scheduler_outputs.blocks_to_swap_in, 566 blocks_to_swap_out=scheduler_outputs.blocks_to_swap_out, 567...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m) 155 token_ids = prompt_token_ids[i] 156 self._add_request(prompt, sampling_params, token_ids) --> 157 return self._run_engine(use_tqdm) File /local_disk0/.ephemeral_nfs/cluster_libraries/python/lib/python3.10/site-pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: TheBloke/Xwin-LM-70B-V0.1-AWQ issue on 2GPU I'm running on 2GPU A100 the following code: ``` sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model=MODEL_NAME, quantization="awq", dtype="half", te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
