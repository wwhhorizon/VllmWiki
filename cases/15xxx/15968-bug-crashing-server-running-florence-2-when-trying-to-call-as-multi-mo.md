# vllm-project/vllm#15968: [Bug]: Crashing server running Florence-2 when trying to call as multi modal

| 字段 | 值 |
| --- | --- |
| Issue | [#15968](https://github.com/vllm-project/vllm/issues/15968) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;operator;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crashing server running Florence-2 when trying to call as multi modal

### Issue 正文摘录

### Your current environment ok ### 🐛 Describe the bug running vLLM as follows: ``` export HF_HOME=path export MODEL_ID=microsoft/Florence-2-large export HUGGING_FACE_HUB_TOKEN=token docker run \ --runtime nvidia \ -e VLLM_USE_V1=0 \ --gpus 0 \ --ipc=host \ -p "8000:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}" \ -v "${HF_HOME}:/root/.cache/huggingface" \ vllm/vllm-openai:latest \ --tensor-parallel-size 1 \ --model ${MODEL_ID} \ --tokenizer facebook/bart-large \ --max-model-len 4096 \ --gpu-memory-utilization 0.2 \ --dtype float16 \ --trust-remote-code \ --max-num-seqs 8 ``` when trying to call it via curl ``` # Step 1: Create the base64 encoded image data base64 -w 0 "fuca.png" > image_data.txt # Step 2: Create a JSON file with the request payload cat > request.json ", "multi_modal_data": { "image": "data:image/png;base64,$(cat image_data.txt)" }, "max_tokens": 50, "temperature": 0.5 } EOF # Step 3: Send the request using the JSON file curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d @request.json ``` the server crashes ``` INFO: 172.17.0.1:50586 - "POST /v1/completions HTTP/1.1" 400 Bad Request WARNING 04-02 12:48:54 [protoc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: MODEL_ID=microsoft/Florence-2-large export HUGGING_FACE_HUB_TOKEN=token docker run \ --runtime nvidia \ -e VLLM_USE_V1=0 \ --gpus 0 \ --ipc=host \ -p "8000:8000" \ --env "HUGGING_FACE_HUB_TOKEN=${HUGGING_FACE_HUB_TOKEN}...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: -w 0 "fuca.png" > image_data.txt # Step 2: Create a JSON file with the request payload cat > request.json ", "multi_modal_data": { "image": "data:image/png;base64,$(cat image_data.txt)" }, "max_tokens": 50, "temperature...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment ok ### 🐛 Describe the bug running vLLM as follows: ``` export HF_HOME=path export MODEL_ID=microsoft/Florence-2-large export HUGGING_FACE_HUB_TOKEN=token docker run \ --runtime nvidia \ -e VLLM_USE_V1=0 \ --gpus 0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ook/bart-large \ --max-model-len 4096 \ --gpu-memory-utilization 0.2 \ --dtype float16 \ --trust-remote-code \ --max-num-seqs 8 ``` when trying to call it via curl ``` # Step 1: Create the base64 encoded image data base...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e.py:160] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/flash_attn.py", line 783, in forward ERROR 04-02 12:48:54 [engine.py:160] key = key[:num_prefill_kv_tokens] ERROR 04-02 12:48:54 [engine.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
