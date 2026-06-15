# vllm-project/vllm#14412: [Performance]:

| 字段 | 值 |
| --- | --- |
| Issue | [#14412](https://github.com/vllm-project/vllm/issues/14412) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:

### Issue 正文摘录

### Proposal to improve performance ![Image](https://github.com/user-attachments/assets/bf5559b5-31c9-4c73-8010-ac095a7ad8b7) I use vllm as backend to test the perdormance my question is : 1. when GPU kv cache useage is 100% , waiting reqseq should increase? and runing reqseq should descrease 2. why only two request , kv cache is 100% ? 3. what reasones decide gpu kv cache size? --------------------------------------------------- GPU:单张L40 48G Model:Qwq 32B FP8 vLLM=1.0 模式 start cmd: vllm serve /aixunlian/weight/hub/Qwen/QwQ-32B-FP8-Dynamic --port 28081 --dtype auto --max-num-seqs 20 --served-model-name q32fp8 --enable-reasoning --reasoning-parser deepseek_r1 --max_model_len 32000 --gpu-memory-utilization 0.95 when server startd ,GPU memory is 44.13 ![Image](https://github.com/user-attachments/assets/057d2db6-bb8a-4c69-8bb5-b1796b004e5e) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: performance;stale ### Proposal to improve performance ![Image](https://github.com/user-attachments/assets/bf5559b5-31c9-4c73-8010-ac095a7ad8b7) I use vllm as backend to test the perdormance my question is...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ------------------------------------------ GPU:单张L40 48G Model:Qwq 32B FP8 vLLM=1.0 模式 start cmd: vllm serve /aixunlian/weight/hub/Qwen/QwQ-32B-FP8-Dynamic --port 28081 --dtype auto --max-num-seqs 20 --served-model-name...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: se vllm as backend to test the perdormance my question is : 1. when GPU kv cache useage is 100% , waiting reqseq should increase? and runing reqseq should descrease 2. why only two request , kv cache is 100% ? 3. what r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: --------------------------------------------------- GPU:单张L40 48G Model:Qwq 32B FP8 vLLM=1.0 模式 start cmd: vllm serve /aixunlian/weight/hub/Qwen/QwQ-32B-FP8-Dynamic --port 28081 --dtype auto --max-num-seqs 20 --served-m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: s/assets/bf5559b5-31c9-4c73-8010-ac095a7ad8b7) I use vllm as backend to test the perdormance my question is : 1. when GPU kv cache useage is 100% , waiting reqseq should increase? and runing reqseq should descrease 2. w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
