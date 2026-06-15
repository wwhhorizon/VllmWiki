# vllm-project/vllm#25903: [MM]: Optimize encoder cache memory consumption by storing encoder outputs only

| 字段 | 值 |
| --- | --- |
| Issue | [#25903](https://github.com/vllm-project/vllm/issues/25903) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [MM]: Optimize encoder cache memory consumption by storing encoder outputs only

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the encoder embedding cache stores the embeddings that encoder outputs are scattered into. https://github.com/vllm-project/vllm/blob/c42ff4f4fdc4a4d48ccef18b8067995f6c19e6ec/vllm/v1/worker/gpu_model_runner.py#L1624-L1629 This is because very often the representation of a multimodal item in the token sequence can include special tokens other than embedding placeholder tokens (such as break token, image start token, image end token, etc). For example, in Pixtral we have the following: Storing embeddings after scattering eases the logic for scheduling, since the scheduler doesn't need to be aware of whether a token is an embedding or not, and will just grab the sequence it needs to be merged into text embedding depending on the `mm_position` information. Because of this design, we also had to reserve for the space for the embeddings after scattering in the encoder cache during profiling run, which was addressed in https://github.com/vllm-project/vllm/pull/25810. https://github.com/vllm-project/vllm/blob/c42ff4f4fdc4a4d48ccef18b8067995f6c19e6ec/vllm/v1/worker/gpu_model_runner.py#L3441-L3454 However, the Qwen3-VL release introduces a ch...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ct/vllm/blob/c42ff4f4fdc4a4d48ccef18b8067995f6c19e6ec/vllm/v1/worker/gpu_model_runner.py#L1624-L1629 This is because very often the representation of a multimodal item in the token sequence can include special tokens ot...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: encoder cache memory consumption by storing encoder outputs only feature request ### 🚀 The feature, motivation and pitch Currently the encoder embedding cache stores the embeddings that encoder outputs are scattered int...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: he space for the embeddings after scattering in the encoder cache during profiling run, which was addressed in https://github.com/vllm-project/vllm/pull/25810. https://github.com/vllm-project/vllm/blob/c42ff4f4fdc4a4d48...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: representation of a multimodal item in the token sequence can include special tokens other than embedding placeholder tokens (such as break token, image start token, image end token, etc). For example, in Pixtral we hav...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
