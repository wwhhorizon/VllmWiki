# vllm-project/vllm#13508: [Usage]: how to optimize my deployment?

| 字段 | 值 |
| --- | --- |
| Issue | [#13508](https://github.com/vllm-project/vllm/issues/13508) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to optimize my deployment?

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/42daf185-f093-4a40-845a-8f5374ddc075) According to above snapshot, the deployment indicates low GPU KV cache usage, low runing request and high pending requests. so there must some unreasonable setting for my deployment, could you give me some suggestions on hyper-params optimization? device: 4*4090 image: vllm 0.6.3 model: qwen2.5-72B-AWQ launch command: ``` args: - '--model' - /models/Qwen2.5-72B-Instruct-AWQ - '--port' - '9066' - '--gpu-memory-utilization' - '0.8' - '--served-model-name' - Qwen1.5-72B-Chat-AWQ - '--max-model-len' - '32768' - '--max-num-seqs' - '64' - '--enable-prefix-caching' - '--dtype' - bfloat16 - '--tensor-parallel-size' - '4' - '--enable-chunked-prefill' - '--max-num-batched-tokens' - '4096' - '--enable-auto-tool-choice' - '--tool-call-parser' - hermes ``` ### How would you like to use vllm I want to know optimal hyper-param setting ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: - '64' - '--enable-prefix-caching' - '--dtype' - bfloat16 - '--tensor-parallel-size' - '4' - '--enable-chunked-prefill' - '--max-num-batched-tokens' - '4096' - '--enable-auto-t
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: how to optimize my deployment? usage;stale ### Your current environment ![Image](https://github.com/user-attachments/assets/42daf185-f093-4a40-845a-8f5374ddc075) According to above snapshot, the deployment indi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: gestions on hyper-params optimization? device: 4*4090 image: vllm 0.6.3 model: qwen2.5-72B-AWQ launch command: ``` args: - '--model' - /models/Qwen2.5-72B-Instruct-AWQ - '--port' - '9066' - '--gpu-memory-utilization' - '
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ing ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 74ddc075) According to above snapshot, the deployment indicates low GPU KV cache usage, low runing request and high pending requests. so there must some unreasonable setting for my deployment, could you give me some sug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
