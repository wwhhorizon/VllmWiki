# vllm-project/vllm#16551: [Bug]: Severe OOM in 0.8.3 （ok in 0.7.2）

| 字段 | 值 |
| --- | --- |
| Issue | [#16551](https://github.com/vllm-project/vllm/issues/16551) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 25; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Severe OOM in 0.8.3 （ok in 0.7.2）

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used to serve Qwen-QwQ-32b, Qwen2.5-vl-32b-awq and qwen2.5-vl-7b in vllm 0.7.2，both of them can load successfully. when I upgraded vllm to 0.8.3 I found only QwQ can load successfully and qwen2.5-vl all go OOM.even after I reduced max-model-len, for example for the 7b model, I reduced max-model-len from 26000 to 16384, still OOM. I tried both increase and decrease gpu-memory-utilization, also not working. so I think this is a bug with vllm. hope will be fixed in 0.8.4 or further, this is really a big bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#16704 [Doc] Improve OOM troubleshooting

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### Your current environment ### 🐛 Describe the bug I used to serve Qwen-QwQ-32b, Qwen2.5-vl-32b-awq and qwen2.5-vl-7b in vllm 0.7.2，both of them can load successfully. when I upgraded vllm to 0.8.3 I found only QwQ can...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf;oom env_dependency #16704 [Doc] Improve OOM troubleshooting Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf;oom env_dependency #16704 [Doc] I...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16704](https://github.com/vllm-project/vllm/pull/16704) | closes_keyword | 0.95 | [Doc] Improve OOM troubleshooting | FIX #16551 FIX #16570 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
