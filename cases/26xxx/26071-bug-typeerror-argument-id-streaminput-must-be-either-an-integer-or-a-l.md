# vllm-project/vllm#26071: [Bug]: TypeError: argument 'id': StreamInput must be either an integer or a list of integers

| 字段 | 值 |
| --- | --- |
| Issue | [#26071](https://github.com/vllm-project/vllm/issues/26071) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: argument 'id': StreamInput must be either an integer or a list of integers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For the current main(`0.11.0rc2.dev120+da554f932`), the following error is raised often for DeepSeek V3 AWQ checkpoint. We haven't yet faced the same error for other flagship models (like llama 4, Qwen 3) or original DeepSeek V3 FP8 checkpoint. It tends to happen for long input, but not always. (Error happens continuously on live server, works normal for 120k input size in isolated test environment) ## Server launch script ```bash vllm serve /mnt/models --served-model-name deepseek-v3-awq \ --gpu-memory-utilization 0.94 \ --tensor-parallel-size 8 \ --max-model-len 128K \ --max-num-batched-tokens 16K \ --reasoning-parser deepseek_r1 \ --enable-auto-tool-choice \ --tool-call-parser deepseek_v3 ``` ## Error log ```log (APIServer pid=250) INFO: 172.16.33.39:42656 - "GET /metrics HTTP/1.1" 200 OK (APIServer pid=250) INFO 10-02 09:43:39 [logger.py:40] Received request chatcmpl-af0ffe2c-c802-4f47-be54-44f2fd2f37a7: prompt: ' \n ...LONG USER INPUT TEXT... ', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.3, top_p=0.95, top_k=0, min_p=0.0, seed=None, stop=[], stop_token_ids=[...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: " 200 OK (APIServer pid=250) INFO 10-02 09:43:39 [logger.py:40] Received request chatcmpl-af0ffe2c-c802-4f47-be54-44f2fd2f37a7: prompt: ' \n ...LONG USER INPUT TEXT... ', params: SamplingParams(n=1, presence_penalty=0.0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=4096, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None), prompt_token_ids: No...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: for other flagship models (like llama 4, Qwen 3) or original DeepSeek V3 FP8 checkpoint. It tends to happen for long input, but not always. (Error happens continuously on live server, works normal for 120k input size in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ek V3 AWQ checkpoint. We haven't yet faced the same error for other flagship models (like llama 4, Qwen 3) or original DeepSeek V3 FP8 checkpoint. It tends to happen for long input, but not always. (Error happens contin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 3 AWQ checkpoint. We haven't yet faced the same error for other flagship models (like llama 4, Qwen 3) or original DeepSeek V3 FP8 checkpoint. It tends to happen for long input, but not always. (Error happens continuous...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
