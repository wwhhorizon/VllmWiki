# vllm-project/vllm#10945: [Performance]: V1 CudaGrpah

| 字段 | 值 |
| --- | --- |
| Issue | [#10945](https://github.com/vllm-project/vllm/issues/10945) |
| 状态 | closed |
| 标签 | performance;torch.compile;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | activation;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: V1 CudaGrpah

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have ported the vllm code to my TTS model, using llama for autoregressive token generation, and I am using version v0.2.7. I noticed that during the decode step, using the `torch.cuda.CUDAGraph().replay()` method, my inference speed has increased to 6 times the original. I observed that version V1 does not use `torch.cuda.CUDAGraph()`, and upon testing, I found that setting `VLLM_TORCH_COMPILE_LEVEL=3` not only fails to achieve a 6-fold increase in inference speed but also slows down the process, with a significant increase in the time taken by RMSNorm. Are there any suggestions to help me modify the code? ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Performance]: V1 CudaGrpah performance;torch.compile;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have ported the vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: V1 CudaGrpah performance;torch.compile;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have ported the vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## Misc discussion on performance I have ported the vllm code to my TTS model, using llama for autoregressive token generation, and I am using version v0.2.7. I noticed that during the decode step, using the `torch.cuda...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: V1 CudaGrpah performance;torch.compile;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have ported the vllm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I have ported the vllm code to my TTS model, using llama for autoregressive token genera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
