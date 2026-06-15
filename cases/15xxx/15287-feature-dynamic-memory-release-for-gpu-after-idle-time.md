# vllm-project/vllm#15287: [Feature]: Dynamic Memory Release for GPU after idle time

| 字段 | 值 |
| --- | --- |
| Issue | [#15287](https://github.com/vllm-project/vllm/issues/15287) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Dynamic Memory Release for GPU after idle time

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm running sparse experiments using vLLM and need dynamic memory management. It would be beneficial to have a feature that automatically releases GPU memory when idle and reallocates it when a new experiment starts. ### Proposed Solution: Dynamic Memory Release: Automatically release GPU memory when no experiments are active. Memory Reallocation: Efficiently reallocate GPU memory when a new experiment begins. Configuration Options: Allow setting idle timeout and memory utilization thresholds. Use Case: This feature would optimize GPU memory usage and improve performance for users running sparse experiments, reducing memory footprint during idle periods. ```bash vllm serve \ --host \ --port \ --max-model-len \ --api-key \ --quantization= \ --load-format= \ --gpu-memory-utilization= \ --enable-dynamic-memory-release # <--- this would be great ``` This feature would greatly enhance the usability and efficiency of vLLM for many users , during experimental procedures. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the cha...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ocation: Efficiently reallocate GPU memory when a new experiment begins. Configuration Options: Allow setting idle timeout and memory utilization thresholds. Use Case: This feature would optimize GPU memory usage and im...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Dynamic Memory Release for GPU after idle time feature request;stale ### 🚀 The feature, motivation and pitch I'm running sparse experiments using vLLM and need dynamic memory management. It would be beneficia...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: riments using vLLM and need dynamic memory management. It would be beneficial to have a feature that automatically releases GPU memory when idle and reallocates it when a new experiment starts. ### Proposed Solution: Dy...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: e \ --host \ --port \ --max-model-len \ --api-key \ --quantization= \ --load-format= \ --gpu-memory-utilization= \ --enable-dynamic-memory-release # <--- this would be great ``` This feature would greatly enhance the us...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
