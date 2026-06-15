# vllm-project/vllm#17236: [Bug]: GLM-4-32B-0414 model output is empty

| 字段 | 值 |
| --- | --- |
| Issue | [#17236](https://github.com/vllm-project/vllm/issues/17236) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4-32B-0414 model output is empty

### Issue 正文摘录

### Your current environment vllm version: 0.8.4 GPU： one node，A40 x 2，48G per GPU At the same time, I have replaced the `glm4.py` file in the latest code. ### 🐛 Describe the bug Startup Command： vllm serve --host 0.0.0.0 --port 8000 ZhipuAI/GLM-4-32B-0414 --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.97 --served-model-name "glm4" Console Output： (vllm) xxx@xxx:/data/vLLM_model$ vllm serve --host 0.0.0.0 --port 8000 ZhipuAI/GLM-4-32B-0414 --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.97 --served-model-name "glm4" --trust-remote-code INFO 04-27 09:20:20 [__init__.py:239] Automatically detected platform cuda. INFO 04-27 09:20:22 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-27 09:20:22 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='ZhipuAI/GLM-4-32B-0414', config='', host='0.0.0.0', port=8000, uvicorn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=No...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='ZhipuAI/GLM-4-32B-0414', task='auto'...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: -4-32B-0414 model output is empty bug ### Your current environment vllm version: 0.8.4 GPU： one node，A40 x 2，48G per GPU At the same time, I have replaced the `glm4.py` file in the latest code. ### 🐛 Describe the bug St...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distrib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: escribe the bug Startup Command： vllm serve --host 0.0.0.0 --port 8000 ZhipuAI/GLM-4-32B-0414 --tensor-parallel-size 2 --max-model-len 32768 --gpu-memory-utilization 0.97 --served-model-name "glm4" Console Output： (vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GLM-4-32B-0414 model output is empty bug ### Your current environment vllm version: 0.8.4 GPU： one node，A40 x 2，48G per GPU At the same time, I have replaced the `glm4.py` file in the latest code. ### 🐛 Describe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
