# vllm-project/vllm#17513: [Bug]: [V1][Spec Dec] EAGLE TP > 1 leads to errors when using --enforce_eager

| 字段 | 值 |
| --- | --- |
| Issue | [#17513](https://github.com/vllm-project/vllm/issues/17513) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale;needs reproduction |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1][Spec Dec] EAGLE TP > 1 leads to errors when using --enforce_eager

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I specify TP > 1 and `--enforce_eager` at the same time, vLLM raises some torch dynamo error. IIUC, under eager mode, torch.compile should not be involved. To reproduce the error, run `VLLM_USE_V1=1 python examples/offline_inference/eagle.py --enforce_eager --draft_tp 8 --tp 8` I was suspecting my [PR](https://github.com/vllm-project/vllm/pull/17211) that applies torch.compile & cuda graph caused this error but it seems to be not the case. vLLM already suffers from the error before the PR was merged. One can verify this by checking out the parent commit [here](https://github.com/vllm-project/vllm/commit/c9c1b59e59a35d5004e3914e23015617fc330b31). The command seems to work fine with this [PR](https://github.com/vllm-project/vllm/pull/16035). So basically something in-between messed things up. cc @WoosukKwon @LiuXiaoxuanPKU ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: c Dec] EAGLE TP > 1 leads to errors when using --enforce_eager bug;torch.compile;stale;needs reproduction ### Your current environment ### 🐛 Describe the bug When I specify TP > 1 and `--enforce_eager` at the same time,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: AGLE TP > 1 leads to errors when using --enforce_eager bug;torch.compile;stale;needs reproduction ### Your current environment ### 🐛 Describe the bug When I specify TP > 1 and `--enforce_eager` at the same time, vLLM ra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ://github.com/vllm-project/vllm/pull/17211) that applies torch.compile & cuda graph caused this error but it seems to be not the case. vLLM already suffers from the error before the PR was merged. One can verify this by...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: error. IIUC, under eager mode, torch.compile should not be involved. To reproduce the error, run `VLLM_USE_V1=1 python examples/offline_inference/eagle.py --enforce_eager --draft_tp 8 --tp 8` I was suspecting my [PR](ht...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
