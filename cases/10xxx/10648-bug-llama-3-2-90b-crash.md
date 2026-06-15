# vllm-project/vllm#10648: [Bug]: Llama 3.2 90b crash

| 字段 | 值 |
| --- | --- |
| Issue | [#10648](https://github.com/vllm-project/vllm/issues/10648) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Llama 3.2 90b crash

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running 90b LLama 3.2 vision model using vllm, see command below: python3 -m vllm.entrypoints.openai.api_server --served-model-name=meta-llama/Llama-3.2-90B-Vision-Instruct --model=/data/001 --tensor-parallel-size=4 --max-num-seqs=96 --max-log-len=0 --load-format=safetensors --host=0.0.0.0 --port=80 --max-num-seqs=64 --gpu-memory-utilization=0.95 --enforce-eager --max-model-len=32768 It occasionally crashes, see logs INFO 11-25 16:02:04 logger.py:37] Received request cmpl-6ccba6262268459ab8a7317db4e6a4dd-0: prompt: '', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=0.9, top_k=10, min_p=0.0, seed=3497136763981421277, stop=[' ', ' ', ' '], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: [], lora_request: None, prompt_adapter_request: None. INFO 11-25 16:02:04 logger.py:37] Received request...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: max_tokens=1, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: [], lora_request: None...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ' ', ' '], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=1, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=Tr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Llama 3.2 90b crash bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When running 90b LLama 3.2 vision model using vllm, see command below: python3 -m vllm.entrypoints.op
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Internal Server Error ERROR 11-25 16:02:05 engine.py:143] RuntimeError('CUDA error: invalid configuration argument\nCUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below mig...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: casionally crashes, see logs INFO 11-25 16:02:04 logger.py:37] Received request cmpl-6ccba6262268459ab8a7317db4e6a4dd-0: prompt: '', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_pe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
