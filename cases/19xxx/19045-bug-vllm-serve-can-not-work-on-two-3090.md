# vllm-project/vllm#19045: [Bug]: vllm serve can not work on two 3090

| 字段 | 值 |
| --- | --- |
| Issue | [#19045](https://github.com/vllm-project/vllm/issues/19045) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm serve can not work on two 3090

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug root@ai66:/workspace# CUDA_VISIBLE_DEVICES=0,1 vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-1.5B-Instruct --disable-log-requests --tensor-parallel-size 2 --port 45526 --max-model-len 100 --gpu_memory_utilization 0.9 INFO 06-03 01:55:23 [__init__.py:239] Automatically detected platform cuda. WARNING 06-03 01:55:23 [cuda.py:409] Detected different devices in the system: NVIDIA GeForce RTX 3090, NVIDIA GeForce RTX 3090, NVIDIA GeForce GTX 1080 Ti, NVIDIA GeForce GTX 1080 Ti, NVIDIA GeForce GTX 1080 Ti. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. INFO 06-03 01:55:32 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 06-03 01:55:32 [api_server.py:1044] args: Namespace(subparser='serve', model_tag='/root/.cache/modelscope/hub/models/Qwen/Qwen2.5-1.5B-Instruct', config='', host=None, port=45526, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: root@ai66:/workspace# CUDA_VISIBLE_DEVICES=0,1 vllm serve /root/.cache/modelscope/hub/models/Qwen/Qwen2.5-1.5B-Instruct --disable-log-requests --tensor-parallel-size 2 --port 45526 --max-model-len 100 --gpu_memory_utili...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: NVIDIA GeForce GTX 1080 Ti. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. INFO 06-03 01:55:32 [api_server.py:1043] vLLM API server version 0.8.5.post1 INFO 06-03 01:55:32 [api_serv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e, model_loader_extra_config={}, use_tqdm_on_load=True, config_format= , dtype='auto', max_model_len=100, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distribu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ot/.cache/modelscope/hub/models/Qwen/Qwen2.5-1.5B-Instruct --disable-log-requests --tensor-parallel-size 2 --port 45526 --max-model-len 100 --gpu_memory_utilization 0.9 INFO 06-03 01:55:23 [__init__.py:239] Automaticall...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: =True, config_format= , dtype='auto', max_model_len=100, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
