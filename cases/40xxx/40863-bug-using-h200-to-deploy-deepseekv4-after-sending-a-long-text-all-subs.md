# vllm-project/vllm#40863: [Bug]: Using H200 to deploy DeepSeekV4, after sending a long text, all subsequent requests are blocked.

| 字段 | 值 |
| --- | --- |
| Issue | [#40863](https://github.com/vllm-project/vllm/issues/40863) |
| 状态 | closed |
| 标签 | bug;DSv4 |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using H200 to deploy DeepSeekV4, after sending a long text, all subsequent requests are blocked.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1.deploy the model on H200： docker run --gpus all \ --privileged --ipc=host -p 8000:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \ vllm/vllm-openai:deepseekv4-cu129 deepseek-ai/DeepSeek-V4-Pro \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 8 \ --max-model-len 800000 \ --gpu-memory-utilization 0.95 \ --max-num-seqs 512 \ --max-num-batched-tokens 512 \ --no-enable-flashinfer-autotune \ --compilation-config '{"mode": 0, "cudagraph_mode": "FULL_DECODE_ONLY"}' \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 2. Send a 64k long request using the benchmark script： vllm bench serve --backend vllm --model /mnt/ssd1/modelscope/DeepSeek-V4-Pro --endpoint /v1/completions --dataset-name random --random-input 64000 --random-output 512 --max-concurrency 1 --num-prompt 5 --ignore-eos --percentile-metrics "ttft,tpot,itl,e2el" --port 8000 --seed 43021 3.Long text requests remain stuck in the waiting queue without actually running, and any subsequent requests...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ing H200 to deploy DeepSeekV4, after sending a long text, all subsequent requests are blocked. bug;DSv4 ### Your current environment ### 🐛 Describe the bug 1.deploy the model on H200： docker run --gpus all \ --privilege...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rent environment ### 🐛 Describe the bug 1.deploy the model on H200： docker run --gpus all \ --privileged --ipc=host -p 8000:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: \ --max-num-seqs 512 \ --max-num-batched-tokens 512 \ --no-enable-flashinfer-autotune \ --compilation-config '{"mode": 0, "cudagraph_mode": "FULL_DECODE_ONLY"}' \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cu129 deepseek-ai/DeepSeek-V4-Pro \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 8 \ --max-model-len 800000 \ --gpu-memory-utilization 0.95 \ --max-num-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: v4 ### Your current environment ### 🐛 Describe the bug 1.deploy the model on H200： docker run --gpus all \ --privileged --ipc=host -p 8000:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -e VLLM_ENGINE_READY_T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
