# vllm-project/vllm#16740: [Bug]: vllm v0.8.4 serve glm-4-32b-0414 error

| 字段 | 值 |
| --- | --- |
| Issue | [#16740](https://github.com/vllm-project/vllm/issues/16740) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm v0.8.4 serve glm-4-32b-0414 error

### Issue 正文摘录

### Your current environment CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=0 vllm serve /home/lc/work/models/GLM-4-32B-0414 --port 8000 --trust-remote-code --max-model-len 32768 --tensor-parallel-size 2 --gpu_memory_utilization 0.8 --served-model-name "glm4" --enable-auto-tool-choice --tool-call-parser pythonic --trust-remote-code got error ，vllm == 0.8.4 , transformers == 4.51.3 , 2x H100 80Gb ### 🐛 Describe the bug ``` (llm) (base) lc@ai-h100:~/work/vllm$ CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=0 vllm serve /home/lc/work/models/GLM-4-32B-0414 --port 8000 --trust-remote-code --max-model-len 32768 --tensor-parallel-size 2 --gpu_memory_utilization 0.8 --s erved-model-name "glm4" --enable-auto-tool-choice --tool-call-parser pythonic --trust-remote-code INFO 04-17 02:04:28 [__init__.py:239] Automatically detected platform cuda. WARNING 04-17 02:04:28 [cuda.py:409] Detected different devices in the system: NVIDIA H100 80GB HBM3, NVIDIA H100. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. INFO 04-17 02:04:30 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-17 02:04:30 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='/home/lc/work/mo...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=True, tool_call_parser='pythonic', tool_parser_plugin='', model='/home/lc/work/models/GLM-4-32B-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: H100 80GB HBM3, NVIDIA H100. Please make sure to set `CUDA_DEVICE_ORDER=PCI_BUS_ID` to avoid unexpected behavior. INFO 04-17 02:04:30 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-17 02:04:30 [api_server.py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: model_loader_extra_config=None, use_tqdm_on_load=True, config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=32768, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: vllm v0.8.4 serve glm-4-32b-0414 error bug ### Your current environment CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=0 vllm serve /home/lc/work/models/GLM-4-32B-0414 --port 8000 --trust-remote-code --max-model-len 32768 --tenso...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ronment CUDA_VISIBLE_DEVICES=0,1 VLLM_USE_V1=0 vllm serve /home/lc/work/models/GLM-4-32B-0414 --port 8000 --trust-remote-code --max-model-len 32768 --tensor-parallel-size 2 --gpu_memory_utilization 0.8 --served-model-na...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
