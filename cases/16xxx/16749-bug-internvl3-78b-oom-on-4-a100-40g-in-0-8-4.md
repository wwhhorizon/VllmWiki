# vllm-project/vllm#16749: [Bug]: InternVL3-78B OOM on 4 A100 40G in 0.8.4

| 字段 | 值 |
| --- | --- |
| Issue | [#16749](https://github.com/vllm-project/vllm/issues/16749) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;gemm;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: InternVL3-78B OOM on 4 A100 40G in 0.8.4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, I have tried using transfromers on 4 a100 and it can describe the image but the vllm is OOM Below is my logs. I have added --eager-mode, but can not deal the problem ``` CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve /data/ps/pretrained_model/OpenGVLab/InternVL3-78B/ --dtype bfloat16 --port 8009 --trust-remote-c ode --served-model-name qwen2vl --tensor-parallel-size 4 --gpu-memory-utilization 0.95 --max-num-seqs 2 --max-model-len 4096 --limit-mm-per-prompt image=1,video=0 --mm_processo r_kwargs '{"max_pixels":1024}' --enforce-eager INFO 04-17 09:40:27 [__init__.py:239] Automatically detected platform cuda. INFO 04-17 09:40:29 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-17 09:40:29 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='/data/ps/pretrained_model/OpenGVLab/InternVL3-78B/', config='', host=None, port=8009, uvi corn_log_level='info', disable_uvicorn_access_log=False, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_module s=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: InternVL3-78B OOM on 4 A100 40G in 0.8.4 bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I have tried using transfromers on 4 a100 and it can describe the image but the vllm is OOM Below is my l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: InternVL3-78B OOM on 4 A100 40G in 0.8.4 bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I have tried using transfromers on 4 a100 and it can describe the image but the vllm is OOM Below is my l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: platform cuda. INFO 04-17 09:40:29 [api_server.py:1034] vLLM API server version 0.8.4 INFO 04-17 09:40:29 [api_server.py:1035] args: Namespace(subparser='serve', model_tag='/data/ps/pretrained_model/OpenGVLab/InternVL3-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =4,5,6,7 vllm serve /data/ps/pretrained_model/OpenGVLab/InternVL3-78B/ --dtype bfloat16 --port 8009 --trust-remote-c ode --served-model-name qwen2vl --tensor-parallel-size 4 --gpu-memory-utilization 0.95 --max-num-seqs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: InternVL3-78B OOM on 4 A100 40G in 0.8.4 bug;stale ### Your current environment ### 🐛 Describe the bug Hi, I have tried using transfromers on 4 a100 and it can describe the image but the vllm is OOM Below is my l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
