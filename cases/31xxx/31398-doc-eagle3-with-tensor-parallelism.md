# vllm-project/vllm#31398: [Doc]: Eagle3 with tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#31398](https://github.com/vllm-project/vllm/issues/31398) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Eagle3 with tensor parallelism

### Issue 正文摘录

### 📚 The doc issue According to https://docs.vllm.ai/en/latest/features/spec_decode/#speculating-using-eagle-based-draft-models: > The EAGLE based draft models need to be run without tensor parallelism (i.e. draft_tensor_parallel_size is set to 1 in speculative_config), although it is possible to run the main model using tensor parallelism (see example above). But there's no explanation for why the draft tpsize could only be set to 1, so I checked the code and found: https://github.com/vllm-project/vllm/blob/52bf0665168c539d2d061a664ad62b18a12e80bb/vllm/config/speculative.py#L441-L447 and https://github.com/vllm-project/vllm/blob/52bf0665168c539d2d061a664ad62b18a12e80bb/vllm/config/speculative.py#L563-L571 I did not find any explicit restriction that enforces the draft model to run without tensor parallelism. So I guess the `draft_tensor_parallel_size` should be set to **either** 1 **or** the same value as the target_model. And also I tried doing so, and found that the tensor parallelism seems worked correctly. Is it possible that this functionality has already been implemented, but the documentation has not been updated accordingly? ### Suggest a potential alternative/fix Just c...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Doc]: Eagle3 with tensor parallelism documentation;stale ### 📚 The doc issue According to https://docs.vllm.ai/en/latest/features/spec_decode/#speculating-using-eagle-based-draft-models: > The EAGLE based draft models...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Doc]: Eagle3 with tensor parallelism documentation;stale ### 📚 The doc issue According to https://docs.vllm.ai/en/latest/features/spec_decode/#speculating-using-eagle-based-draft-models: > The EAGLE based draft models...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m.ai/en/latest/features/spec_decode/#speculating-using-eagle-based-draft-models: > The EAGLE based draft models need to be run without tensor parallelism (i.e. draft_tensor_parallel_size is set to 1 in speculative_confi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 18a12e80bb/vllm/config/speculative.py#L563-L571 I did not find any explicit restriction that enforces the draft model to run without tensor parallelism. So I guess the `draft_tensor_parallel_size` should be set to **eit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tation;stale ### 📚 The doc issue According to https://docs.vllm.ai/en/latest/features/spec_decode/#speculating-using-eagle-based-draft-models: > The EAGLE based draft models need to be run without tensor parallelism (i....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
