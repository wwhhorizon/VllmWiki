# vllm-project/vllm#13196: [Bug]: Speculative Decoding Output with Pytorch Rejection Sampling does not change when changing seed

| 字段 | 值 |
| --- | --- |
| Issue | [#13196](https://github.com/vllm-project/vllm/issues/13196) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding Output with Pytorch Rejection Sampling does not change when changing seed

### Issue 正文摘录

### Your current environment ## 🐛 Describe the bug When trying to run speculative decoding with rejection sampling, I noticed that changing the seed in the SamplingParams or globally does not change the output of the run. Here is the code I run: ``` llm = LLM( model=target_model_id, speculative_model=draft_model_id, tensor_parallel_size=1, num_speculative_tokens=5, max_num_batched_tokens=4096, max_model_len=4096, skip_tokenizer_init=True, disable_log_stats=True, ) for prompt in input_prompts: prompt_tokens = tokenizer( prompt, return_tensors="pt", padding=True ).input_ids.tolist() ip = [ TokensPrompt(prompt_token_ids=prompts) for prompts in prompt_tokens ] for r in range(10): sampling_params = SamplingParams( temperature=0.0, min_tokens=256, max_tokens=256, ignore_eos=True, seed=r * 10, ) set_random_seed(r * 10) outputs = llm.generate(ip, sampling_params) print(f"\\n#############################################\n") print(outputs) print("\n--------------------------------------------\n") print("==========================\n") ``` After a lot of digging, I noticed that the `capped_ratio` in `_create_uniform_samples` in the RejectionSampler class would just be 0s and 1s: Not sure why...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Speculative Decoding Output with Pytorch Rejection Sampling does not change when changing seed bug;stale ### Your current environment ## 🐛 Describe the bug When trying to run speculative decoding with rejection s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e output of the run. Here is the code I run: ``` llm = LLM( model=target_model_id, speculative_model=draft_model_id, tensor_parallel_size=1, num_speculative_tokens=5, max_num_batched_tokens=4096, max_model_len=4096, ski...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
