# vllm-project/vllm#6312: [Feature]: control over llm_engine placement when multiple gpus are available.

| 字段 | 值 |
| --- | --- |
| Issue | [#6312](https://github.com/vllm-project/vllm/issues/6312) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: control over llm_engine placement when multiple gpus are available.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I need a way to specify which gpu exactly should vllm use when multiple gpus are available. Currently, it automatically occupies all available gpus (https://docs.vllm.ai/en/latest/serving/distributed_serving.html). For example, something like this: `vllm.LLM(model_path, device="cuda:N")` #691 is exactly the same question but they end up agreeing that they can use Ray. I'm asking for a simpler solution that would not require spending time on extra engineering. ### Alternatives My use-case doesn't allow me to use CUDA_VISIBLE_DEVICES to specify which gpu to use. That's because i train a model on multiple gpus in a DDP-like fashion where each vllm instance generates data for a model on its device, then gradients are synchronized and so on. So I cannot set CUDA_VISIBLE_DEVICES to some specific device as that would turn multiple-gpu training in a single-gpu training. Also, I cannot just avoid this problem by running a vllm-server on a separate gpu because I need to substitute model weights (loras) on-the-fly and currently this is not available (#3446). ### Additional context So I either need a way to specify which gpu to use, or have the #3446 PR...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: trol over llm_engine placement when multiple gpus are available. feature request;stale ### 🚀 The feature, motivation and pitch I need a way to specify which gpu exactly should vllm use when multiple gpus are available....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: equest;stale ### 🚀 The feature, motivation and pitch I need a way to specify which gpu exactly should vllm use when multiple gpus are available. Currently, it automatically occupies all available gpus (https://docs.vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .html). For example, something like this: `vllm.LLM(model_path, device="cuda:N")` #691 is exactly the same question but they end up agreeing that they can use Ray. I'm asking for a simpler solution that would not requir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /distributed_serving.html). For example, something like this: `vllm.LLM(model_path, device="cuda:N")` #691 is exactly the same question but they end up agreeing that they can use Ray. I'm asking for a simpler solution t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: it automatically occupies all available gpus (https://docs.vllm.ai/en/latest/serving/distributed_serving.html). For example, something like this: `vllm.LLM(model_path, device="cuda:N")` #691 is exactly the same question...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
