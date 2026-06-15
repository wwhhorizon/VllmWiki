# vllm-project/vllm#14683: [Feature]: Data parallel inference in offline mode(based on Ray)

| 字段 | 值 |
| --- | --- |
| Issue | [#14683](https://github.com/vllm-project/vllm/issues/14683) |
| 状态 | closed |
| 标签 | feature request;ray;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Data parallel inference in offline mode(based on Ray)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I've been building model evaluation datasets using offline inference as outlined in the [documentation](https://docs.vllm.ai/en/stable/serving/offline_inference.html#offline-inference), and I noticed that it’s challenging to fully leverage all available GPUs—when the model fits on a single GPU. To overcome this, I implemented a feature that distributes model replicas across different GPUs, allowing prompt data to be processed concurrently. For large datasets, this approach achieves nearly linear speedup, significantly enhancing performance for both my team and me. It’s important to note that offline inference also plays a crucial role in model training and evaluation. By enabling efficient and scalable processing of evaluation data, offline inference helps in thoroughly benchmarking models and fine-tuning them during the development cycle. Interestingly, this feature has been discussed before (see [issue #1237](https://github.com/vllm-project/vllm/issues/1237)), yet there hasn't been any implementation so far. I’m curious if others still find this feature useful for offline inference, as it would eliminate the need to launch a multi-k8s-pod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ure request;ray;stale ### 🚀 The feature, motivation and pitch I've been building model evaluation datasets using offline inference as outlined in the [documentation](https://docs.vllm.ai/en/stable/serving/offline_infere...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ;stale ### 🚀 The feature, motivation and pitch I've been building model evaluation datasets using offline inference as outlined in the [documentation](https://docs.vllm.ai/en/stable/serving/offline_inference.html#offlin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Data parallel inference in offline mode(based on Ray) feature request;ray;stale ### 🚀 The feature, motivation and pitch I've been building model evaluation datasets using offline inference as outlined in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st;ray;stale ### 🚀 The feature, motivation and pitch I've been building model evaluation datasets using offline inference as outlined in the [documentation](https://docs.vllm.ai/en/stable/serving/offline_inference.html#...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
