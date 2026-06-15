# vllm-project/vllm#2198: Mixtral GPTQ Long Prompts exceed capacity of block_manager

| 字段 | 值 |
| --- | --- |
| Issue | [#2198](https://github.com/vllm-project/vllm/issues/2198) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Mixtral GPTQ Long Prompts exceed capacity of block_manager

### Issue 正文摘录

I loaded Mixtral TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ in VLLM successfully. Everything works for short prompts. However, longer prompts lead to the error: ``` WARNING 12-19 10:21:05 scheduler.py:161] Input prompt (1217 tokens) is too long and exceeds the capacity of block_manager INFO 12-19 10:21:05 async_llm_engine.py:111] Finished request cmpl-b8c7b3b2eb7a4de488ef870004648708. ``` This is the command I use to start the model: ``` python -m vllm.entrypoints.openai.api_server --model TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ --quantization gptq --dtype float16 --max-model-len 4096 --gpu-memory-utilization 0.99 ``` The model starts with: ``` INFO 12-19 10:20:40 api_server.py:719] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], block_size=16, chat_template=None, disable_log_requests=False, disable_log_stats=False, download_dir=None, dtype='float16', enforce_eager=False, engine_use_ray=False, gpu_memory_utilization=0.99, host=None, load_format='auto', max_context_len_to_capture=8192, max_log_len=None, max_model_len=4096, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, max_parallel_loading_workers=None,...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: nts.openai.api_server --model TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ --quantization gptq --dtype float16 --max-model-len 4096 --gpu-memory-utilization 0.99 ``` The model starts with: ``` INFO 12-19 10:20:40 api_server...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 3b2eb7a4de488ef870004648708. ``` This is the command I use to start the model: ``` python -m vllm.entrypoints.openai.api_server --model TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ --quantization gptq --dtype float16 --max-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: . However, longer prompts lead to the error: ``` WARNING 12-19 10:21:05 scheduler.py:161] Input prompt (1217 tokens) is too long and exceeds the capacity of block_manager INFO 12-19 10:21:05 async_llm_engine.py:111] Fin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Mixtral GPTQ Long Prompts exceed capacity of block_manager I loaded Mixtral TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ in VLLM successfully. Everything works for short prompts. However, longer prompts lead to the error: `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: WARNING 12-19 10:20:40 config.py:191] gptq does not support CUDA graph yet. Disabling CUDA graph. INFO 12-19 10:20:40 llm_engine.py:73] Initializing an LLM engine with c

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
