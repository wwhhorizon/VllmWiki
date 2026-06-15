# vllm-project/vllm#21045: [Doc]: qwen2.5-vl-72B-AWQ -speed

| 字段 | 值 |
| --- | --- |
| Issue | [#21045](https://github.com/vllm-project/vllm/issues/21045) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: qwen2.5-vl-72B-AWQ -speed

### Issue 正文摘录

### 📚 The doc issue Why is the inference speed of the qwen2.5-vl-72B-AWQ model I deployed with vllm similar to that of the qwen2.5-vl-72B model? Shouldn't the AWQ model be faster? Here is my deployment command. Could you please help answer this? CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve "Qwen2.5-VL-72B-Instruct-AWQ" --port 8080 --dtype float16 --tensor-parallel-size 8 --cpu-offload-gb 0 --gpu-memory-utilization 0.80 --max-model-len 128000 --api-key abc123 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser hermes --trust-remote-code CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve "Qwen2.5-VL-72B-Instruct" --port 8080 --dtype bfloat16 --tensor-parallel-size 8 --cpu-offload-gb 0 --gpu-memory-utilization 0.80 --max-model-len 128000 --api-key abc123 --enable-prefix-caching --enable-auto-tool-choice --tool-call-parser hermes --trust-remote-code ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: S=0,1,2,3,4,5,6,7 vllm serve "Qwen2.5-VL-72B-Instruct-AWQ" --port 8080 --dtype float16 --tensor-parallel-size 8 --cpu-offload-gb 0 --gpu-memory-utilization 0.80 --max-model-len 128000 --api-key abc123 --enable-prefix-ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ster? Here is my deployment command. Could you please help answer this? CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve "Qwen2.5-VL-72B-Instruct-AWQ" --port 8080 --dtype float16 --tensor-parallel-size 8 --cpu-offload-gb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Doc]: qwen2.5-vl-72B-AWQ -speed documentation;stale ### 📚 The doc issue Why is the inference speed of the qwen2.5-vl-72B-AWQ model I deployed with vllm similar to that of the qwen2.5-vl-72B model? Shouldn't the AWQ mod...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: Instruct-AWQ" --port 8080 --dtype float16 --tensor-parallel-size 8 --cpu-offload-gb 0 --gpu-memory-utilization 0.80 --max-model-len 128000 --api-key abc123 --enable-prefix-caching --enable-auto-tool-choice --tool-call-p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: qwen2.5-vl-72B-AWQ -speed documentation;stale ### 📚 The doc issue Why is the inference speed of the qwen2.5-vl-72B-AWQ model I deployed with vllm similar to that of the qwen2.5-vl-72B model? Shouldn't the AWQ mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
