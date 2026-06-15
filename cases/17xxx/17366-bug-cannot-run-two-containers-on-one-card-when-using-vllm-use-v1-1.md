# vllm-project/vllm#17366: [Bug]: Cannot run two containers on one card when using VLLM_USE_V1=1

| 字段 | 值 |
| --- | --- |
| Issue | [#17366](https://github.com/vllm-project/vllm/issues/17366) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot run two containers on one card when using VLLM_USE_V1=1

### Issue 正文摘录

### Your current environment I started two docker containers on a card on an A100(80G) machine to run the w8w8 quantized qwen2.5 14B model, limiting gpu-memory-utilization to 0.3 respectively. The first service can be loaded normally, but the second service fails to start. The GPU memory is sufficient. It can be reproduced in v0.8.* versions, In addition, it runs normally when using VLLM_USE_V1=0. ### 🐛 Describe the bug # the first container ```shell docker run -itd --gpus='"device=0"' --name vllm_qwen_first -e VLLM_USE_V1=1 \ --shm-size 10g -v /data/model/qwen2_5_14b_w8a8/:/data/model/ --network=host \ vllm/vllm-openai:v0.8.5 \ --model /data/model/ --max-model-len 4096 --gpu-memory-utilization 0.3 --port 8900 ``` ![Image](https://github.com/user-attachments/assets/dc03bdb8-4dcb-45f6-b36b-ff5a2bf16723) The service runs normally, and there were no other services on the card before. # the second container ```shell docker run -itd --gpus='"device=0"' --name vllm_qwen_second -e VLLM_USE_V1=1 \ --shm-size 10g -v /data/model/qwen2_5_14b_w8a8/:/data/model/ --network=host \ vllm/vllm-openai:v0.8.5 \ --model /data/model/ --max-model-len 4096 --gpu-memory-utilization 0.3 --port 8901 ``` The...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: two docker containers on a card on an A100(80G) machine to run the w8w8 quantized qwen2.5 14B model, limiting gpu-memory-utilization to 0.3 respectively. The first service can be loaded normally, but the second service...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: when using VLLM_USE_V1=1 bug ### Your current environment I started two docker containers on a card on an A100(80G) machine to run the w8w8 quantized qwen2.5 14B model, limiting gpu-memory-utilization to 0.3 respectivel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: r containers on a card on an A100(80G) machine to run the w8w8 quantized qwen2.5 14B model, limiting gpu-memory-utilization to 0.3 respectively. The first service can be loaded normally, but the second service fails to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: True, config_format= , dtype='auto', max_model_len=4096, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='/data/model/', task='auto', tokenize...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
