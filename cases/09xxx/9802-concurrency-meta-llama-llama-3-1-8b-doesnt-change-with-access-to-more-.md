# vllm-project/vllm#9802: Concurrency meta-llama/Llama-3.1-8B doesnt change with access to more GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#9802](https://github.com/vllm-project/vllm/issues/9802) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Concurrency meta-llama/Llama-3.1-8B doesnt change with access to more GPUs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running Llama 3.1 8b and try to optimize the throughput. I have been testing it both on a single A100 and on a setup with 4xA100 (where I used `tensor_parallel_size=4`. I see the following but want to understand better whats going on: When initialising the model I see the following log line: ``` Maximum concurrency for 40000 tokens per request: 52.89x ``` However, when sending f.e. 100 requests, the number of jobs running at the same never never goes beyond 3. And the number of pending jobs is much larger. I run the model using the following arguments and sampling params: ``` args = AsyncEngineArgs( model=local_model_folder, # This has the HF version of meta-llama/Llama-3.1-8B max_model_len=40000, max_num_seqs=512, tensor_parallel_size=4, enable_chunked_prefill=True, multi_step_stream_outputs=False, ) SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=16, min_tokens=0, logprobs=None, prompt_logprobs=None...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: AsyncEngineArgs( model=local_model_folder, # This has the HF version of meta-llama/Llama-3.1-8B max_model_len=40000, max_num_seqs=512, tensor_parallel_size=4, enable_chunked_prefill=True, multi_step_stream_outputs=False,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: try to optimize the throughput. I have been testing it both on a single A100 and on a setup with 4xA100 (where I used `tensor_parallel_size=4`. I see the following but want to understand better whats going on: When init...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Concurrency meta-llama/Llama-3.1-8B doesnt change with access to more GPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running Llama 3.1 8b and try to optimize...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rency meta-llama/Llama-3.1-8B doesnt change with access to more GPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am running Llama 3.1 8b and try to optimize the th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ## 🐛 Describe the bug I am running Llama 3.1 8b and try to optimize the throughput. I have been testing it both on a single A100 and on a setup with 4xA100 (where I used `tensor_parallel_size=4`. I see the following but...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
