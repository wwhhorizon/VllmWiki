# vllm-project/vllm#42475: [Doc]: Integration Issue: Qwen3.6-27B-FP8 with Codex via vLLM Server

| 字段 | 值 |
| --- | --- |
| Issue | [#42475](https://github.com/vllm-project/vllm/issues/42475) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Integration Issue: Qwen3.6-27B-FP8 with Codex via vLLM Server

### Issue 正文摘录

### 📚 The doc issue Issue Description: I followed the tutorial in the codex.mddocumentation to integrate the Qwen3.6-27B model into Codex. The vLLM server configuration is as follows: ``` bash #!/bin/bash set -e MODEL_PATH="/home/user/vllm-server/models/Qwen3.6-27B-FP8" MODEL_NAME=$(basename "$MODEL_PATH" | tr '[:upper:]' '[:lower:]') export CUDA_VISIBLE_DEVICES=0,1 export NCCL_P2P_DISABLE=0 export NCCL_IB_DISABLE=1 export NCCL_SHM_DISABLE=0 export NCCL_DEBUG=WARN export CUDA_DEVICE_MAX_CONNECTIONS=1 source ~/miniconda3/etc/profile.d/conda.sh conda activate vllm exec vllm serve "$MODEL_PATH" \ --tensor-parallel-size 2 \ --kv-cache-dtype fp8 \ --max-model-len 204800 \ --max-num-seqs 8 \ --gpu-memory-utilization 0.92 \ --disable-custom-all-reduce \ --trust-remote-code \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --chat-template-content-format openai \ --enable-chunked-prefill \ --host 0.0.0.0 \ --port 8001 \ --served-model-name "$MODEL_NAME" ``` After issuing a command in Codex, the following error occurred: ``` {"error":{"message":"18 validation errors:\n {'type': 'literal_error', 'loc': ('body', 'tools', 11, 'FunctionTool', 'type'), 'msg': \"Input should be 'func...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Doc]: Integration Issue: Qwen3.6-27B-FP8 with Codex via vLLM Server documentation ### 📚 The doc issue Issue Description: I followed the tutorial in the codex.mddocumentation to integrate the Qwen3.6-27B model into Code...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Doc]: Integration Issue: Qwen3.6-27B-FP8 with Codex via vLLM Server documentation ### 📚 The doc issue Issue Description: I followed the tutorial in the codex.mddocumentation to integrate the Qwen3.6-27B model into Code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ODEL_NAME=$(basename "$MODEL_PATH" | tr '[:upper:]' '[:lower:]') export CUDA_VISIBLE_DEVICES=0,1 export NCCL_P2P_DISABLE=0 export NCCL_IB_DISABLE=1 export NCCL_SHM_DISABLE=0 export NCCL_DEBUG=WARN export CUDA_DEVICE_MAX...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en3_coder \ --chat-template-content-format openai \ --enable-chunked-prefill \ --host 0.0.0.0 \ --port 8001 \ --served-model-name "$MODEL_NAME" ``` After issuing a command in Codex, the following error occurred: ``` {"e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: DEBUG=WARN export CUDA_DEVICE_MAX_CONNECTIONS=1 source ~/miniconda3/etc/profile.d/conda.sh conda activate vllm exec vllm serve "$MODEL_PATH" \ --tensor-parallel-size 2 \ --kv-cache-dtype fp8 \ --max-model-len 204800 \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
