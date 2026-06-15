# vllm-project/vllm#8268: [Bug]: AssertionError when using automatic prefix caching and prompt_logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#8268](https://github.com/vllm-project/vllm/issues/8268) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError when using automatic prefix caching and prompt_logprobs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm having issues using automatic prefix caching with prompt_logprobs option. The first call to the `generate` method goes through, but the second call errors with an `AssertionError`. Reproduction code: ```py from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_path = "meta-llama/Meta-Llama-3.1-8B-Instruct" model = LLM(model_path, tensor_parallel_size=8, dtype="bfloat16", gpu_memory_utilization=0.8, enable_prefix_caching=True) sampling_params = SamplingParams(prompt_logprobs=1, max_tokens=1) tokenizer = AutoTokenizer.from_pretrained(model_path) chat_prompts = tokenizer.apply_chat_template([[{"role": "user", "content": "Test 1"}]], tokenize=False) output = model.generate(chat_prompts, sampling_params, use_tqdm=False) print("OK") chat_prompts = tokenizer.apply_chat_template([[{"role": "user", "content": "Test 2"}]], tokenize=False) output = model.generate(chat_prompts, sampling_params, use_tqdm=False) # ERROR! ``` Full stack trace: ```py --------------------------------------------------------------------------- AssertionError Traceback (most recent call last) Cell In[2], line 10 7 print("OK") 9 chat_p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ll errors with an `AssertionError`. Reproduction code: ```py from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_path = "meta-llama/Meta-Llama-3.1-8B-Instruct" model = LLM(model_path, tenso...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: sertionError when using automatic prefix caching and prompt_logprobs bug;stale ### Your current environment ### 🐛 Describe the bug I'm having issues using automatic prefix caching with prompt_logprobs option. The first...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: a-Llama-3.1-8B-Instruct" model = LLM(model_path, tensor_parallel_size=8, dtype="bfloat16", gpu_memory_utilization=0.8, enable_prefix_caching=True) sampling_params = SamplingParams(prompt_logprobs=1, max_tokens=1) tokeni...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm import LLM, SamplingParams from transformers import AutoTokenizer model_path = "meta-llama/Meta-Llama-3.1-8B-Instruct" model = LLM(model_path, tensor_parallel_size=8, dtype="bfloat16", gpu_memory_utilization=0.8, e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sampling_params.logprobs) 1077 use_beam_search = use_beam_search or sampling_params.use_beam_search -> 1079 assert len(next_token_ids) == len(query_indices) 1081 if len(query_indices) == 0: 1082 empty_sampled_logprob: S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
