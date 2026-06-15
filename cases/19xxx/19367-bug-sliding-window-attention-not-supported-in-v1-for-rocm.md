# vllm-project/vllm#19367: [Bug]: Sliding Window Attention not supported in V1 for ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#19367](https://github.com/vllm-project/vllm/issues/19367) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Sliding Window Attention not supported in V1 for ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Multiple architectures, such as Qwen2, use Sliding Window Attention. However, there is no option in V1 to run Sliding Window Attention on ROCm. Sending a request to the server crashes, for: ```bash MODEL_NAME="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" export VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --port 8080 --model $MODEL_NAME --served-model-name $MODEL_NAME --gpu-memory-utilization 0.95 --disable-custom-all-reduce --tensor-parallel-size 1 --enable-chunked-prefill --disable-log-requests --enable-reasoning --reasoning-parser deepseek_r1 ``` This is because it uses Triton Flash Attention, which not support Sliding Window Attention. As a result, sending a request to the server crashes vLLM: **Request:** ```bash curl -iX POST "http://localhost:8080/v1/chat/completions" -H "Content-Type: application/json" -d '{ "model": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", "messages": [{ "role": "user", "content": "Hello, how are you?"}], "stream": false }' ``` **Resulting logs from crash:** ``` Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/triton/language/core.py", line 34, in wrapper...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e/core.py", line 1281, in arange return semantic.arange(start, end, _builder) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/triton/language/semantic.py", line 610, in arange raise V...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: re is no option in V1 to run Sliding Window Attention on ROCm. Sending a request to the server crashes, for: ```bash MODEL_NAME="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" export VLLM_USE_V1=1 python3 -m vllm.entrypoint...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e-reasoning --reasoning-parser deepseek_r1 ``` This is because it uses Triton Flash Attention, which not support Sliding Window Attention. As a result, sending a request to the server crashes vLLM: **Request:** ```bash...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: == (-1, -1)) and (qtype == torch.half or qtype == torch.bfloat16) and (head_size == 64 or head_size == 128) and (block_size == 16 or block_size == 32) and (gqa_ratio >= 1 and gqa_ratio = 3 and gqa_ratio <= 16) a
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Sliding Window Attention not supported in V1 for ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug Multiple architectures, such as Qwen2, use Sliding Window Attention. However, there is no option...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
