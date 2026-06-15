# vllm-project/vllm#8141: [Bug]: Met a error when deploying an AWQ model on H20. 

| 字段 | 值 |
| --- | --- |
| Issue | [#8141](https://github.com/vllm-project/vllm/issues/8141) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Met a error when deploying an AWQ model on H20. 

### Issue 正文摘录

### Your current environment ### Describe the bug I want to deploy a AWQ model on H20. But I met some errors when I curl it. I use `export VLLM_LOGGING_LEVEL=DEBUG ` to show traceback, but it seems that useless info is printed. The phenomenon is that the gpu memory is released to 0. I think there is a coredump. ### Reproduction ``` CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server /data/model/Yi-1.5-34B-Chat-AWQ --server-port 8081 --model-name yi --cache-max-entry-count 0.7 --tp 1 --session-len 4096 --enable-prefix-caching --model-format awq --log-level DEBUG ``` Yi-1.5-34B-Chat-AWQ from: https://huggingface.co/modelscope/Yi-1.5-34B-Chat-AWQ. ``` curl --request POST \ --url http://127.0.0.1:8081/v1/chat/completions \ --header 'content-type: application/json' \ --data '{ "model": "yi", "temperature": 0.7, "top_p": 0.8, "messages": [ { "role": "user", "content": "你是谁" } ], "max_tokens": 1024, "repetition_penalty": 1.0 }' ``` ### Error traceback ``` INFO: Uvicorn running on http://0.0.0.0:8082 (Press CTRL+C to quit) INFO 09-04 11:39:56 metrics.py:351] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _tokens=1024, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [6, 2942, 144, 59568, 13961, 60638, 7, 144,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ry is released to 0. I think there is a coredump. ### Reproduction ``` CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server /data/model/Yi-1.5-34B-Chat-AWQ --server-port 8081 --model-name yi --cache-max-entry-count 0.7 --tp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Met a error when deploying an AWQ model on H20. bug;stale ### Your current environment ### Describe the bug I want to deploy a AWQ model on H20. But I met some errors when I curl it. I use `export VLLM_LOGGING_LE...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Met a error when deploying an AWQ model on H20. bug;stale ### Your current environment ### Describe the bug I want to deploy a AWQ model on H20. But I met some errors when I curl it. I use `export VLLM_LOGGING_LE...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: k, but it seems that useless info is printed. The phenomenon is that the gpu memory is released to 0. I think there is a coredump. ### Reproduction ``` CUDA_VISIBLE_DEVICES=0 lmdeploy serve api_server /data/model/Yi-1.5...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
