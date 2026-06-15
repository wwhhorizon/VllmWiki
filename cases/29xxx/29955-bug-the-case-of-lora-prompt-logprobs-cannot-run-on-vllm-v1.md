# vllm-project/vllm#29955: [Bug]: The case of LORA + prompt_logprobs cannot run on vLLM v1

| 字段 | 值 |
| --- | --- |
| Issue | [#29955](https://github.com/vllm-project/vllm/issues/29955) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The case of LORA + prompt_logprobs cannot run on vLLM v1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Starting from version 0.8.3**, after vLLM switched to the v1 engine by default, the case combining LORA and prompt_logprobs can no longer run. For example, the https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/multilora_inference.py will throw an error. However, when using vLLM v1, removing `prompt_logprobs=1` from the example allows it to run normally. ```bash $ python3 examples/offline_inference/multilora_inference.py INFO 12-03 00:11:33 [model.py:631] Resolved architecture: LlamaForCausalLM INFO 12-03 00:11:33 [model.py:1745] Using max model len 4096 INFO 12-03 00:11:33 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 12-03 00:11:33 [interface.py:409] Using 'pin_memory=False' as WSL is detected. This may slow down the performance. (EngineCore_DP0 pid=168) INFO 12-03 00:11:33 [core.py:93] Initializing a V1 LLM engine (v0.11.2) with config: model='/models/Llama-2-7b-hf', speculative_config=None, tokenizer='/models/Llama-2-7b-hf', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 3 examples/offline_inference/multilora_inference.py INFO 12-03 00:11:33 [model.py:631] Resolved architecture: LlamaForCausalLM INFO 12-03 00:11:33 [model.py:1745] Using max model len 4096 INFO 12-03 00:11:33 [scheduler....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: 3 00:11:33 [model.py:1745] Using max model len 4096 INFO 12-03 00:11:33 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 12-03 00:11:33 [interface.py:409] Using 'pin_memory=False'...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Your current environment ### 🐛 Describe the bug **Starting from version 0.8.3**, after vLLM switched to the v1 engine by default, the case combining LORA and prompt_logprobs can no longer run. For example, the https...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
