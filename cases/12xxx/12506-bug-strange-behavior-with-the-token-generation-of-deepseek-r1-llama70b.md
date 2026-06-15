# vllm-project/vllm#12506: [Bug]: Strange behavior with the token generation of DeepSeek-R1-LLama70B in v0.7.0

| 字段 | 值 |
| --- | --- |
| Issue | [#12506](https://github.com/vllm-project/vllm/issues/12506) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Strange behavior with the token generation of DeepSeek-R1-LLama70B in v0.7.0

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I use vLLM v0.7.0 with the new V1 architecture to load `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`. With the v0.6.6.post1, everything is working fine. But the v0.7.0 with the V1 architecture, the model outputs random tokens. Here is the command I used: ```sh docker run --rm -it --runtime nvidia --gpus all \ -e CUDA_VISIBLE_DEVICES=0,1,2,3 \ -e NVIDIA_VISIBLE_DEVICES=0,1,2,3 \ -e VLLM_ATTENTION_BACKEND=FLASHINFER \ -e VLLM_USE_V1=1 \ -p 8090:8000 \ -v /data/models/deepseek/deepseek-r1-distill-llama-70b:/root/data/models/deepseek/deepseek-r1-distill-llama-70b \ -v /data/vllm/huggingface:/root/vllm/huggingface \ --ipc=host \ --name deepseek-r1 \ vllm/vllm-openai:v0.7.0 \ --host 0.0.0.0 \ --model /root/data/models/deepseek/deepseek-r1-distill-llama-70b \ --task auto \ --trust-remote-code \ --load-format safetensors \ --dtype bfloat16 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 32768 \ --guided-decoding-backend xgrammar \ --distributed-executor-backend mp \ --tensor-parallel-size 4 \ --enable-prefix-caching \ --gpu-memory-utilization 0.95 \ --max-num-seqs 16 \ --disable-custom-all-reduce \ --e...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Strange behavior with the token generation of DeepSeek-R1-LLama70B in v0.7.0 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi, I use vLLM v0.7.0 with the new V1 archi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: re, the model outputs random tokens. Here is the command I used: ```sh docker run --rm -it --runtime nvidia --gpus all \ -e CUDA_VISIBLE_DEVICES=0,1,2,3 \ -e NVIDIA_VISIBLE_DEVICES=0,1,2,3 \ -e VLLM_ATTENTION_BACKEND=FL...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: -70b \ --task auto \ --trust-remote-code \ --load-format safetensors \ --dtype bfloat16 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 32768 \ --guided-decoding-backend xgrammar \ --distributed-executor-backend mp \ --te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _DEVICES=0,1,2,3 \ -e NVIDIA_VISIBLE_DEVICES=0,1,2,3 \ -e VLLM_ATTENTION_BACKEND=FLASHINFER \ -e VLLM_USE_V1=1 \ -p 8090:8000 \ -v /data/models/deepseek/deepseek-r1-distill-llama-70b:/root/data/models/deepseek/deepseek-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: .95 \ --max-num-seqs 16 \ --disable-custom-all-reduce \ --enable-chunked-prefill \ --compilation-config 3 \ --enable-sleep-mode ``` Output: ```text INFO 01-28 00:40:19 logger.py:37] Received request chatcmpl-c690572d9b0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
