# vllm-project/vllm#16658: [Bug]: V0 engines gives incorrect output for Moonlight model

| 字段 | 值 |
| --- | --- |
| Issue | [#16658](https://github.com/vllm-project/vllm/issues/16658) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V0 engines gives incorrect output for Moonlight model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the [moonlight model](https://huggingface.co/moonshotai/Moonlight-16B-A3B-Instruct) with the V0 and V1 engines gives different outputs. I launched the service using the following command: ```bash python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8888 \ --served-model-name moonlight \ --trust-remote-code \ --model /dev/shm/moonshotai--Moonlight-16B-A3B-Instruct \ --tensor-parallel-size 1 \ --max-model-len 8192 \ --max-num-batched-tokens 8192 \ --max-seq-len-to-capture 8192 \ --swap-space 0 \ --max-num-seq 2048 ``` and I use curl to query the service: ```bash curl ... \ # Link to the service -H "Content-Type: application/json" \ -d '{ "model": "moonlight", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who are you? "} ], "max_tokens": 100, "temperature": 0 }' ``` The outputs are V0: "Hello! I'm here to assist you. How can I help you?" V1: "I am an AI developed by a team of talented scientists and developers. I am here to assist you with any questions or tasks you may have. How can I help you today?" ### Root Cause The reason for this issue is t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: m-seq 2048 ``` and I use curl to query the service: ```bash curl ... \ # Link to the service -H "Content-Type: application/json" \ -d '{ "model": "moonlight", "messages": [ {"role": "system", "content": "You are a helpf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eason for this issue is that the V0 engine's MLA backend doesn't support cuda-native RoPE embeddings. In https://github.com/vllm-project/vllm/blob/main/vllm/attention/backends/mla/common.py#L1382-1393, `prefill_q_pe` an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: roject/vllm/blob/main/vllm/attention/backends/mla/common.py#L1382-1393, `prefill_q_pe` and `decode_q_pe` are split from a big tensor along the second dimension, so they are not contiguous. V0 engine attempts to compute...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: " ### Root Cause The reason for this issue is that the V0 engine's MLA backend doesn't support cuda-native RoPE embeddings. In https://github.com/vllm-project/vllm/blob/main/vllm/attention/backends/mla/common.py#L1382-1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: /moonshotai/Moonlight-16B-A3B-Instruct) with the V0 and V1 engines gives different outputs. I launched the service using the following command: ```bash python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
