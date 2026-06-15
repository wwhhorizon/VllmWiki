# vllm-project/vllm#35644: [Feature]: AMD MXFP4 MiniMax M2.5 Checkpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#35644](https://github.com/vllm-project/vllm/issues/35644) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: AMD MXFP4 MiniMax M2.5 Checkpoint

### Issue 正文摘录

### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 AMD only have MXFP4 checkpoints of MiniMax M2.1 but doesnt have MXFP4 checkpoints of the latest MiniMax M2.5 model MiniMax M2.5 is the same architecture as MiniMax M2.1 but different weights. It would be great to have an MXFP4 ckpt of MiniMax M2.5 since M2.5 is way more popularity used than M2.1 We see great performance boost from MXFP4 compared to FP8 on the MiniMax architecture ### Alternatives use fp8 and get worse perf ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Feature]: AMD MXFP4 MiniMax M2.5 Checkpoint feature request;rocm ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 AMD only have MXFP4 checkpoints of MiniMax M2.1 but doesnt have MXFP4 checkp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: AMD MXFP4 MiniMax M2.5 Checkpoint feature request;rocm ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 AMD only have MXFP4 checkpoints of MiniMax M2.1 but doesnt have MXFP4 checkp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: iniMax M2.1 but doesnt have MXFP4 checkpoints of the latest MiniMax M2.5 model MiniMax M2.5 is the same architecture as MiniMax M2.1 but different weights. It would be great to have an MXFP4 ckpt of MiniMax M2.5 since M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: AMD MXFP4 MiniMax M2.5 Checkpoint feature request;rocm ### 🚀 The feature, motivation and pitch hi @powderluv @chunfangamd @andyluo7 AMD only have MXFP4 checkpoints of MiniMax M2.1 but doesnt have MXFP4 checkp...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 4 checkpoints of MiniMax M2.1 but doesnt have MXFP4 checkpoints of the latest MiniMax M2.5 model MiniMax M2.5 is the same architecture as MiniMax M2.1 but different weights. It would be great to have an MXFP4 ckpt of Mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
