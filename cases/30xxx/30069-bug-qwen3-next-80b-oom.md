# vllm-project/vllm#30069: [Bug]: Qwen3-Next-80B OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#30069](https://github.com/vllm-project/vllm/issues/30069) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug code below cause OOM on 4xH100, which is unexpected, as the model is around 40GB per GPU and the input is only 2k. ```python sampling_params = SamplingParams( max_tokens=3, ) llm = LLM( model=model_name, # qwen3-next trust_remote_code=True, tensor_parallel_size=4, load_format="dummy", enforce_eager=eager, max_num_seqs=4, enable_prefix_caching=False, enable_chunked_prefill=False, ) import random tokenizer = llm.get_tokenizer() seqlen = 2048 vocab_size = len(tokenizer) prompt_token_ids = [random.randint(100, vocab_size - 1) for _ in range(seqlen)] prompt = tokenizer.decode(prompt_token_ids, skip_special_tokens=True) prompt_len = len(tokenizer(prompt).input_ids) request = [ { "prompt": prompt, "prompt_token_ids": prompt_token_ids, "prompt_len": prompt_len, } ] print(f"length of prompt token: {len(prompt_token_ids)}") llm.generate(request, sampling_params) ``` ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e_prefix_caching=False, enable_chunked_prefill=False, ) import random tokenizer = llm.get_tokenizer() seqlen = 2048 vocab_size = len(tokenizer) prompt_token_ids = [random.randint(100, vocab_size - 1) for _ in range(seql...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: _num_seqs=4, enable_prefix_caching=False, enable_chunked_prefill=False, ) import random tokenizer = llm.get_tokenizer() seqlen = 2048 vocab_size = len(tokenizer) prompt_token_ids = [random.randint(100, vocab_size - 1) f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: urrent environment ### 🐛 Describe the bug code below cause OOM on 4xH100, which is unexpected, as the model is around 40GB per GPU and the input is only 2k. ```python sampling_params = SamplingParams( max_tokens=3, ) ll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next-80B OOM bug ### Your current environment ### 🐛 Describe the bug code below cause OOM on 4xH100, which is unexpected, as the model is around 40GB per GPU and the input is only 2k. ```python sampling_p
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: linear;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;oom env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
