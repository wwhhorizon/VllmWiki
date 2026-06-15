# vllm-project/vllm#12770: [Bug]: Deploy the qwen2.5-instruct-gptq-int4 model on NVIDIA A40 (48G) using the official vllm 0.6.4 image, enable the multi-step decoding feature with 8 decoding steps, and observe repeated content in the model output

| 字段 | 值 |
| --- | --- |
| Issue | [#12770](https://github.com/vllm-project/vllm/issues/12770) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deploy the qwen2.5-instruct-gptq-int4 model on NVIDIA A40 (48G) using the official vllm 0.6.4 image, enable the multi-step decoding feature with 8 decoding steps, and observe repeated content in the model output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use the following demand to deploy qwen2.5-instruct-gptq-int4 model on two NVIDIA A40s: ```bash python3 -m vllm.entrypoints.api_server --model /model --quantization gptq --max-seq-len-to-capture 32768 --num-scheduler-steps 8 --enable-prefix-caching --tensor-parallel-size 2 --host 0.0.0.0 --port 48000 --trust-remote-code --max-num-batched-tokens 32768 --max-model-len 32768 --max-num-seqs 6 --gpu-memory-utilization 0.9 ``` The inference parameters are as follows: ```bash SamplingParams(n=1, best_of=1, presence_penalty=1.2, frequency_ penalty=0.0, repetition_penalty=1.0, temperature=0.2, top_p=1, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], in clude_stop_str_in_output=False, ignore_eos=False, max_tokens=8192, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_ prompt_tokens=None) ``` Using the client script to access the exposed generate API after deployment, when the requests per minute (QPM) is 4, the average input and output are 6000 tokens and 500 tokens, respectively. The model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y the qwen2.5-instruct-gptq-int4 model on NVIDIA A40 (48G) using the official vllm 0.6.4 image, enable the multi-step decoding feature with 8 decoding steps, and observe repeated content in the model output bug;stale ##...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Deploy the qwen2.5-instruct-gptq-int4 model on NVIDIA A40 (48G) using the official vllm 0.6.4 image, enable the multi-step decoding feature with 8 decoding steps, and observe repeated content in the model output...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: h 8 decoding steps, and observe repeated content in the model output bug;stale ### Your current environment ### 🐛 Describe the bug I use the following demand to deploy qwen2.5-instruct-gptq-int4 model on two NVIDIA A40s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .0, temperature=0.2, top_p=1, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], in clude_stop_str_in_output=False, ignore_eos=False, max_tokens=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Deploy the qwen2.5-instruct-gptq-int4 model on NVIDIA A40 (48G) using the official vllm 0.6.4 image, enable the multi-step decoding feature with 8 decoding steps, and observe repeated content in the model output...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
