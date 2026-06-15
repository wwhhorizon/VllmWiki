# vllm-project/vllm#13954: [Bug]: vllm crash when enable prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#13954](https://github.com/vllm-project/vllm/issues/13954) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm crash when enable prefix caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug base on docker image intelanalytics/ipex-llm-serving-xpu:latest. ``` docker image ls REPOSITORY TAG IMAGE ID CREATED SIZE intelanalytics/ipex-llm-serving-xpu latest 17b300a22da2 14 hours ago 23.6GB ``` ``` export DOCKER_IMAGE=intelanalytics/ipex-llm-serving-xpu:latest export CONTAINER_NAME=ipex-llm-serving-xpu-container sudo docker run -itd \ --privileged \ --net=host \ --device=/dev/dri \ -v /home/ubuntu/.cache/huggingface/hub:/llm/models \ -e no_proxy=localhost,127.0.0.1 \ --memory="32G" \ --name=$CONTAINER_NAME \ --shm-size="16g" \ $DOCKER_IMAGE docker start $CONTAINER_NAME docker exec -it $CONTAINER_NAME /bin/bash ``` ``` vim /llm/start-vllm-service.sh #changed: model="/llm/models/Qwen2.5-7B-Instruct" served_model_name="Qwen2.5-7B-Instruct" # enable prefix caching for vllm # insert "--enable_prefix_caching \" to line 34 #save it bash /llm/start-vllm-service.sh ``` open another console, then send 2 request to test. The first request is fine, but the second one return nothing. ``` ubuntu@ubuntu:~$ time curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen2.5-7B-Instruct", "m...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: g;stale ### Your current environment ### 🐛 Describe the bug base on docker image intelanalytics/ipex-llm-serving-xpu:latest. ``` docker image ls REPOSITORY TAG IMAGE ID CREATED SIZE intelanalytics/ipex-llm-serving-xpu l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: vllm crash when enable prefix caching bug;stale ### Your current environment ### 🐛 Describe the bug base on docker image intelanalytics/ipex-llm-serving-xpu:latest. ``` docker image ls REPOSITORY TAG IMAGE ID
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: --net=host \ --device=/dev/dri \ -v /home/ubuntu/.cache/huggingface/hub:/llm/models \ -e no_proxy=localhost,127.0.0.1 \ --memory="32G" \ --name=$CONTAINER_NAME \ --shm-size="16g" \ $DOCKER_IMAGE docker start $CONTAINER_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='float16', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=2048, guided_decoding_backend='xgrammar', logits_processor_pat...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: _v2_block_manager=True, num_lookahead_slots=0, seed=0, swap_space=4, cpu_offload_gb=0, gpu_memory_utilization=0.95, num_gpu_blocks_override=None, max_num_batched_tokens=4000, max_num_seqs=256, max_logprobs=20, disable_l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
