# vllm-project/vllm#39415: [New Model]: Cuda 13 wheels for Blackwell GPUs, Linux-aarm64 and Linux-aamd64 Please

| 字段 | 值 |
| --- | --- |
| Issue | [#39415](https://github.com/vllm-project/vllm/issues/39415) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: Cuda 13 wheels for Blackwell GPUs, Linux-aarm64 and Linux-aamd64 Please

### Issue 正文摘录

### The model to consider. We have been purchasing newer hardware leveraging the Blackwell GPU and find we need to manually build VLLM to run on this environment. This has become a barrier for adoption on these platforms. It would be wonderful if you could provide pypi installable runtimes for these environments. Thank you in advance for your consideration. ### The closest model vllm already supports. None -- has to be built manually. ### What's your difficulty of supporting the model you want? _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [New Model]: Cuda 13 wheels for Blackwell GPUs, Linux-aarm64 and Linux-aamd64 Please ### The model to consider. We have been purchasing newer hardware leveraging the Blackwell GPU and find we need to manually build VLLM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [New Model]: Cuda 13 wheels for Blackwell GPUs, Linux-aarm64 and Linux-aamd64 Please ### The model to consider. We have been purchasing newer hardware leveraging the Blackwell GPU and find we need to manually build VLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: Cuda 13 wheels for Blackwell GPUs, Linux-aarm64 and Linux-aamd64 Please ### The model to consider. We have been purchasing newer hardware leveraging the Blackwell GPU and find we need to manually build VLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error The model to con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
