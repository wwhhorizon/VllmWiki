# vllm-project/vllm#8721: [Bug]: torch.OutOfMemoryError: CUDA out of memory.

| 字段 | 值 |
| --- | --- |
| Issue | [#8721](https://github.com/vllm-project/vllm/issues/8721) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch.OutOfMemoryError: CUDA out of memory.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run `python3 -m vllm.entrypoints.openai.api_server --model shuttleai/shuttle-3-GPTQ-Int4 --dtype bfloat16 --api-key 123456 --tensor-parallel-size 1 --gpu-memory-utilization 0.90 --served-model-name shuttle-2.5`, I get an OOM error. ``` shuttle@ShuttleAI:~$ python3 -m vllm.entrypoints.openai.api_server --model shuttleai/shuttle-3-GPTQ-Int4 --dtype bfloat16 --api-key Shuttle1010AI --tensor-parallel-size 1 --gpu-memory-utilization 0.90 --served-model-name shuttle-2.5 --max-num-seqs 32 --max-model-len 4096 INFO 09-23 00:28:06 api_server.py:495] vLLM API server version 0.6.1.post2 INFO 09-23 00:28:06 api_server.py:496] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key='Shuttle1010AI', lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, middleware=[], return_tokens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_auto_tool_choice=False, to...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_quantization=None, num_specu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 3 -m vllm.entrypoints.openai.api_server --model shuttleai/shuttle-3-GPTQ-Int4 --dtype bfloat16 --api-key 123456 --tensor-parallel-size 1 --gpu-memory-utilization 0.90 --served-model-name shuttle-2.5`, I get an OOM error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ax-model-len 4096 INFO 09-23 00:28:06 api_server.py:495] vLLM API server version 0.6.1.post2 INFO 09-23 00:28:06 api_server.py:496] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: emoryError: CUDA out of memory. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run `python3 -m vllm.entrypoints.openai.api_server --model shuttleai/shuttle-3-GPTQ-Int4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: torch.OutOfMemoryError: CUDA out of memory. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I run `python3 -m vllm.entrypoints.openai.api_server --model shuttleai/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
