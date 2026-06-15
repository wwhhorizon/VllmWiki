# vllm-project/vllm#8477: [Bug]: : CPU silently doesn't support multi-step (--num-scheduler-steps)

| 字段 | 值 |
| --- | --- |
| Issue | [#8477](https://github.com/vllm-project/vllm/issues/8477) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: : CPU silently doesn't support multi-step (--num-scheduler-steps)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tested the following script running on a CPU backend which set num_scheduler_steps > 1 to force use mult-step: ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125M", gpu_memory_utilization=0.4, max_model_len=1024, num_scheduler_steps=8 ) params = SamplingParams(seed=123, prompt_logprobs=5, temperature=1) prompts = ["How to make pizza?"] outputs = llm.generate(prompts, sampling_params=params ) for o in outputs: print('_________') print('### Text') print('_________') for o2 in o.outputs: print(o2.text) ``` Got the following output: ``` INFO 09-13 19:33:10 importing.py:10] Triton not installed; certain GPU-related functions will not be available. WARNING 09-13 19:33:13 arg_utils.py:902] Enabled BlockSpaceManagerV2 because it is required for multi-step (--num-scheduler-steps > 1) WARNING 09-13 19:33:13 config.py:370] Async output processing is only supported for CUDA or TPU. Disabling it for other platforms. INFO 09-13 19:33:13 llm_engine.py:213] Initializing an LLM engine (v0.6.0) with config: model='facebook/opt-125M', speculative_config=None, tokenizer='facebook/op...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: set num_scheduler_steps > 1 to force use mult-step: ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125M", gpu_memory_utilization=0.4, max_model_len=1024, num_scheduler_steps=8 ) params = Sa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: p (--num-scheduler-steps) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tested the following script running on a CPU backend which set num_scheduler_steps > 1 to for...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ### 🐛 Describe the bug I tested the following script running on a CPU backend which set num_scheduler_steps > 1 to force use mult-step: ```python from vllm import LLM, SamplingParams llm = LLM(model="facebook/opt-125M",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: : CPU silently doesn't support multi-step (--num-scheduler-steps) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tested the following script running on a CPU b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
