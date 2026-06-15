# vllm-project/vllm#34377: [Bug]: FP8 speed regression in version 0.16.0rc2.dev87+g0b20469c6 (latest nightly)

| 字段 | 值 |
| --- | --- |
| Issue | [#34377](https://github.com/vllm-project/vllm/issues/34377) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 speed regression in version 0.16.0rc2.dev87+g0b20469c6 (latest nightly)

### Issue 正文摘录

### Your current environment vllm/vllm-openai:nightly Commit-tagged alias: nightly-0b20469c627e94060d1015170b186d19de1db583 ### 🐛 Describe the bug Substantial drop in speed on FP8 images on: vllm/vllm-openai:nightly Commit-tagged alias: nightly-0b20469c627e94060d1015170b186d19de1db583 Currently on RTX PRO 6000's All FP8 models have dropped substantially in inference speed. Qwen Coder Next FP8 in TP went from 100+ TPS to 38 TPS Stepfun3.5 FP8 using PP 66 TPS -> 18 TPS `` vllm/vllm-openai:nightly \ --model /models/step35flash \ --served-model-name step3p5-flash \ --host 0.0.0.0 \ --port 5000 \ --max-model-len 170000 \ --pipeline-parallel-size 3 \ --gpu-memory-utilization 0.97 \ --max-num-seqs 2 \ --tool-call-parser step3p5 \ --reasoning-parser step3p5 \ --enable-auto-tool-choice \ --enable-prefix-caching \ --optimization-level 3 \ --trust-remote-code \ --disable-cascade-attn \ --quantization fp8 `` No changes in the launch commands, substantially slower. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lo...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 speed regression in version 0.16.0rc2.dev87+g0b20469c6 (latest nightly) bug;stale ### Your current environment vllm/vllm-openai:nightly Commit-tagged alias: nightly-0b20469c627e94060d1015170b186d19de1db583 ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed alias: nightly-0b20469c627e94060d1015170b186d19de1db583 Currently on RTX PRO 6000's All FP8 models have dropped substantially in inference speed. Qwen Coder Next FP8 in TP went from 100+ TPS to 38 TPS Stepfun3.5 FP8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 9c627e94060d1015170b186d19de1db583 Currently on RTX PRO 6000's All FP8 models have dropped substantially in inference speed. Qwen Coder Next FP8 in TP went from 100+ TPS to 38 TPS Stepfun3.5 FP8 using PP 66 TPS -> 18 TP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: FP8 speed regression in version 0.16.0rc2.dev87+g0b20469c6 (latest nightly) bug;stale ### Your current environment vllm/vllm-openai:nightly Commit-tagged alias: nightly-0b20469c627e94060d1015170b186d19de1db583 ##...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: FP8 speed regression in version 0.16.0rc2.dev87+g0b20469c6 (latest nightly) bug;stale ### Your current environment vllm/vllm-openai:nightly Commit-tagged alias: nightly-0b20469c627e94060d1015170b186d19de1db583 ##...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
