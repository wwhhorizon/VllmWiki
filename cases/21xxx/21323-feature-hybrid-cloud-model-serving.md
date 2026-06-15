# vllm-project/vllm#21323: [Feature]: Hybrid Cloud Model Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#21323](https://github.com/vllm-project/vllm/issues/21323) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Hybrid Cloud Model Serving

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm interested in supporting the SLED approach, where a draft model interacts with the validator remotely. I've created a use case for a near-edge device (GPU-enabled) communicating with a validator model within the cloud. I understand that vLLM has a shared kv-cache for this, so anything with speculative decoding happens in one instance. What would it take to implement this? If someone could point me in the right direction, I wouldn't mind rolling up my sleeves and seeing if I could contribute to something like this if possible. **Here's some research articles where I learned about the concept** https://arxiv.org/abs/2507.00605 https://arxiv.org/abs/2506.09397 **A diagram of a hypothetical implementation of this approach** ![Image](https://github.com/user-attachments/assets/e8e4a9b0-bfa3-468f-991f-3e013050d538) **An outline of the benefits of a approach I put together** _Hybrid model serving unlocks a new class of deployment strategies where latency, bandwidth, and cost considerations can be balanced without sacrificing model performance. By dividing the workload across edge and cloud infrastructure, organizations can meet demanding SLAs an...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Hybrid Cloud Model Serving feature request;stale ### 🚀 The feature, motivation and pitch I'm interested in supporting the SLED approach, where a draft model interacts with the validator remotely. I've created...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: _Hybrid model serving unlocks a new class of deployment strategies where latency, bandwidth, and cost considerations can be balanced without sacrificing model performance. By dividing the workload across edge and cloud...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e payload exchanged with the cloud. * **Energy-Aware Deployments:** Use quantized draft models on low-power devices for initial speculation, offloading only high-confidence continuation to the cloud to save energy. * **...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: could contribute to something like this if possible. **Here's some research articles where I learned about the concept** https://arxiv.org/abs/2507.00605 https://arxiv.org/abs/2506.09397 **A diagram of a hypothetical im...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: a validator model within the cloud. I understand that vLLM has a shared kv-cache for this, so anything with speculative decoding happens in one instance. What would it take to implement this? If someone could point me i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
