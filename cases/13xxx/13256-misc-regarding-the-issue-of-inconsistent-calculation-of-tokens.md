# vllm-project/vllm#13256: [Misc]: Regarding the issue of inconsistent calculation of tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#13256](https://github.com/vllm-project/vllm/issues/13256) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Regarding the issue of inconsistent calculation of tokens

### Issue 正文摘录

### Anything you want to discuss about vllm. Hello, I am using vllm to deploy the inference service. The usage.prompt_tokens data returned by the calling interface is inconsistent with the token obtained using transformers.AutoTokenizer. The following is the test process: vllm startup command: ``` docker run -itd \ --name deepseek-awq \ --network host \ --shm-size=1024m \ --gpus all \ -v $(pwd):/app \ --entrypoint "bash" \ docker.1ms.run/vllm/vllm-openai:v0.7.2 \ -c " python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8000 --enable_prefix_caching --max-model-len 65536 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-util 0.97 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-awq --enable-chunked-prefill --model /app/cognitivecomputations/DeepSeek-R1-awq" ``` ``` curl --request POST \ --url http://10.1.30.59:8000/v1/chat/completions \ --header 'Authorization: Bearer sk-ddddddddddddddd' \ --header 'Content-Type: application/json' \ --data '{ "messages": [ { "role": "user", "content": "what is you name" } ], "stream": false, // "stream_options":{ // "include_usage": true // }, "model": "deepseek-awq", "temp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: oTokenizer. The following is the test process: vllm startup command: ``` docker run -itd \ --name deepseek-awq \ --network host \ --shm-size=1024m \ --gpus all \ -v $(pwd):/app \ --entrypoint "bash" \ docker.1ms.run/vll...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ng --max-model-len 65536 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-util 0.97 --kv-cache-dtype fp8_e5m2 --calculate-kv-scales --served-model-name deepseek-awq --enable-chunked-pre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nai.api_server --host 0.0.0.0 --port 8000 --enable_prefix_caching --max-model-len 65536 --trust-remote-code --tensor-parallel-size 8 --quantization moe_wna16 --gpu-memory-util 0.97 --kv-cache-dtype fp8_e5m2 --calculate-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Misc]: Regarding the issue of inconsistent calculation of tokens stale ### Anything you want to discuss about vllm. Hello, I am using vllm to deploy the inference service. The usage.prompt_tokens data returned by the c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ) result = tokenizer.encode("what is you name") print(result) root@A100-GPU-59:/app/cognitivecomputations/DeepSeek-R1-awq# python3 deepseek_tokenizer.py [0, 9602, 344, 440, 2329] ``` They use the same tokenizer configur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
