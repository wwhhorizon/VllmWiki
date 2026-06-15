# vllm-project/vllm#13579: [Bug]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

| 字段 | 值 |
| --- | --- |
| Issue | [#13579](https://github.com/vllm-project/vllm/issues/13579) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

### Issue 正文摘录

### Your current environment root@node15:/disk2/qwen-2.5-vl-72b-4bit# docker images|grep vllm vllm/vllm-openai v0.6.5 56aa649484bf 2 months ago 10.1GB root@node15:/disk2/qwen-2.5-vl-72b-4bit# ll total 41333976 drwxr-xr-x 2 root root 4096 2月 20 10:44 ./ drwxr-xr-x 16 root root 4096 2月 20 10:04 ../ -rw-r--r-- 1 root root 605 2月 19 09:46 added_tokens.json -rw-r--r-- 1 root root 1050 2月 19 09:46 chat_template.json -rw-r--r-- 1 root root 1660 2月 19 09:46 config.json -rw-r--r-- 1 root root 76 2月 19 09:46 configuration.json -rw-r--r-- 1 root root 725 2月 20 10:44 docker-compose.yml -rw-r--r-- 1 root root 2122 2月 19 09:46 .gitattributes -rw-r--r-- 1 root root 1671853 2月 19 09:46 merges.txt -rw-r--r-- 1 root root 5293545214 2月 19 13:06 model-00001-of-00008.safetensors -rw-r--r-- 1 root root 5294882403 2月 19 13:06 model-00002-of-00008.safetensors -rw-r--r-- 1 root root 5346175170 2月 19 13:07 model-00003-of-00008.safetensors -rw-r--r-- 1 root root 5294849486 2月 19 13:06 model-00004-of-00008.safetensors -rw-r--r-- 1 root root 5294882430 2月 19 13:05 model-00005-of-00008.safetensors -rw-r--r-- 1 root root 5294882523 2月 19 13:24 model-00006-of-00008.safetensors -rw-r--r-- 1 root root 5346175172 2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: . This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. bug ### Your current environment root@node15:/disk2/qwen-2.5-vl-72b-4bit# docker images|grep vllm vllm/vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: The checkpoint you are trying to load has model type `qwen2_5_vl` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: e, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', num_scheduler_steps=1, multi_step_stream_outputs=True, scheduler_delay_factor=0.0, enable_chunked_prefill=None, speculative_model=None, speculative_mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: model /models/qwen-2.5-vl-72b-4bit --tokenizer_mode="auto" --dtype=bfloat16 --tensor_parallel_size=2 --gpu-memory-utilization=0.85 --max-model-len=8192 --served-model-name=Qwen2.5-VL-72B-Instruct-4bit deploy: resources:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
