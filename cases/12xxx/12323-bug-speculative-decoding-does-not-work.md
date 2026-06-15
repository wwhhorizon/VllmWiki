# vllm-project/vllm#12323: [Bug]: Speculative decoding does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#12323](https://github.com/vllm-project/vllm/issues/12323) |
| 状态 | closed |
| 标签 | bug;speculative-decoding;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding does not work

### Issue 正文摘录

Here is a script: ``` docker run --gpus '"device=0,1"' --rm -d --net host \ --name vllm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /home/thinclient/llm-server/weights:/mnt/weights \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "TORCH_USE_CUDA_DSA=1" \ --env "CUDA_LAUNCH_BLOCKING=1" \ --env "VLLM_RPC_TIMEOUT=100000" \ --shm-size=15g \ --ipc host \ vllm/vllm-openai:latest \ --model jakiAJK/DeepSeek-R1-Distill-Qwen-7B_GPTQ-int4 \ --speculative-model Qwen/Qwen2.5-0.5B-Instruct-GPTQ-Int4 \ --num-speculative-tokens 5 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --gpu-memory-utilization 0.98 \ --max_model_len 1000 \ --enable-prefix-caching \ docker logs -f vllm ``` And logs: ``` INFO 01-22 09:01:26 api_server.py:651] vLLM API server version 0.6.5 INFO 01-22 09:01:26 api_server.py:652] args: Namespace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=None, chat_template_content_format='auto', response_role='assistant', ssl_keyfile=None, ssl_certfile=None, ssl_ca_certs=None, ssl_cert_reqs=0, root_path=None, mi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Speculative decoding does not work bug;speculative-decoding;stale Here is a script: ``` docker run --gpus '"device=0,1"' --rm -d --net host \ --name vllm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: oding does not work bug;speculative-decoding;stale Here is a script: ``` docker run --gpus '"device=0,1"' --rm -d --net host \ --name vllm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /home/thinclient/llm-ser...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: us '"device=0,1"' --rm -d --net host \ --name vllm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /home/thinclient/llm-server/weights:/mnt/weights \ --env "HUGGING_FACE_HUB_TOKEN= " \ --env "TORCH_USE_CUDA_DSA=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: llm-openai:latest \ --model jakiAJK/DeepSeek-R1-Distill-Qwen-7B_GPTQ-int4 \ --speculative-model Qwen/Qwen2.5-0.5B-Instruct-GPTQ-Int4 \ --num-speculative-tokens 5 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: HUB_TOKEN= " \ --env "TORCH_USE_CUDA_DSA=1" \ --env "CUDA_LAUNCH_BLOCKING=1" \ --env "VLLM_RPC_TIMEOUT=100000" \ --shm-size=15g \ --ipc host \ vllm/vllm-openai:latest \ --model jakiAJK/DeepSeek-R1-Distill-Qwen-7B_GPTQ-i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
