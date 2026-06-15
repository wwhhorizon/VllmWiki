# vllm-project/vllm#19206: [Bug]: Inference with the Moonlight model, the output becomes corrupted when n exceeds 1

| 字段 | 值 |
| --- | --- |
| Issue | [#19206](https://github.com/vllm-project/vllm/issues/19206) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference with the Moonlight model, the output becomes corrupted when n exceeds 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams model_path = '/sllmworkspace/share/sllmworks/model/moonlight-ckpts/Moonlight-16B-A3B-Instruct' llm = LLM( model=model_path, enable_sleep_mode=True, tensor_parallel_size=4, # distributed_executor_backend="external_launcher", dtype='bfloat16', enforce_eager=True, gpu_memory_utilization=0.5, disable_custom_all_reduce=True, disable_mm_preprocessor_cache=True, # limit_mm_per_prompt=limit_mm_per_prompt, skip_tokenizer_init=False, max_model_len=3074, # load_format=load_format, disable_log_stats=True, max_num_batched_tokens=8192, enable_chunked_prefill=False, enable_prefix_caching=True, trust_remote_code=True, seed=42, # **engine_kwargs, ) sampling_params = SamplingParams( logprobs=0, temperature=1, top_k=-1, top_p=1, n=2, max_tokens=2048 ) from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained(model_path,trust_remote_code=True) question = ( "Janet’s ducks lay 16 eggs per day. She eats three for breakfast every morning " "and bakes muffins for her friends every day with four. She sells the remainder " "at the farmers' market daily for $2 per fresh duck egg. How much...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams model_path = '/sllmworkspace/share/sllmworks/model/moonlight-ckpts/Moonlight-16B-A3B-Instruct' llm = LLM( model=model_path,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llel_size=4, # distributed_executor_backend="external_launcher", dtype='bfloat16', enforce_eager=True, gpu_memory_utilization=0.5, disable_custom_all_reduce=True, disable_mm_preprocessor_cache=True, # limit_mm_per_promp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: h the Moonlight model, the output becomes corrupted when n exceeds 1 bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams model_path = '/sllmworkspace/share/sllmwo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: _sleep_mode=True, tensor_parallel_size=4, # distributed_executor_backend="external_launcher", dtype='bfloat16', enforce_eager=True, gpu_memory_utilization=0.5, disable_custom_all_reduce=True, disable_mm_preprocessor_cac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 10) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
