# vllm-project/vllm#8275: [Bug]: RuntimeError: shape mismatch: value tensor of shape [3328, 7168] cannot be broadcast to indexing result of shape [3328] for OpenGVLab/InternVL2-40B

| 字段 | 值 |
| --- | --- |
| Issue | [#8275](https://github.com/vllm-project/vllm/issues/8275) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: shape mismatch: value tensor of shape [3328, 7168] cannot be broadcast to indexing result of shape [3328] for OpenGVLab/InternVL2-40B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While serving the **OpenGVLab/InternVL2-40B** using Multi-Node Multi-GPU (tensor parallel plus pipeline parallel inference) facing these issue **RuntimeError: shape mismatch: value tensor of shape [3328, 7168] cannot be broadcast to indexing result of shape [3328]** But I don't face these issue while serving the **OpenGVLab/InternVL2-8B** and **OpenGVLab/InternVL2-26B** Command: **vllm serve OpenGVLab/InternVL2-40B --tensor-parallel-size 1 --pipeline-parallel-size 4 --dtype bfloat16 --gpu-memory-utilization 0.9 --max-model-len 6000 --enforce-eager --trust-remo te-code --tokenizer-mode "auto"** Log: ``` INFO 09-08 10:17:29 api_server.py:495] vLLM API server version 0.6.0 INFO 09-08 10:17:29 api_server.py:496] args: Namespace(model_tag='OpenGVLab/InternVL2-40B', config='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_meth ods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, ro ot_path=None, middleware=[], return_tokens_a...

## 现有链接修复摘要

#8299 [Bugfix] Fix InternVL2 vision embeddings process with pipeline parallel

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 68] cannot be broadcast to indexing result of shape [3328] for OpenGVLab/InternVL2-40B bug ### Your current environment ### 🐛 Describe the bug While serving the **OpenGVLab/InternVL2-40B** using Multi-Node Multi-GPU (te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_model_q uantization=None, num_spec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ulti-Node Multi-GPU (tensor parallel plus pipeline parallel inference) facing these issue **RuntimeError: shape mismatch: value tensor of shape [3328, 7168] cannot be broadcast to indexing result of shape [3328]** But I...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: VLab/InternVL2-40B --tensor-parallel-size 1 --pipeline-parallel-size 4 --dtype bfloat16 --gpu-memory-utilization 0.9 --max-model-len 6000 --enforce-eager --trust-remo te-code --tokenizer-mode "auto"** Log: ``` INFO 09-0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=6000, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=4, tensor_parallel_size=1 , max_parallel_loadi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8299](https://github.com/vllm-project/vllm/pull/8299) | closes_keyword | 0.95 | [Bugfix] Fix InternVL2 vision embeddings process with pipeline parallel | FIX #8275 - For InternVL2 with PP, we only need to process image input on first rank. - This PR fixed the error raised by image input processing on other ranks **BEFORE SUBMI |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
