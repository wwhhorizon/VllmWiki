# vllm-project/vllm#36999: [Bug]: CPU offloading produces gibberish output with flashinfer autotuner

| 字段 | 值 |
| --- | --- |
| Issue | [#36999](https://github.com/vllm-project/vllm/issues/36999) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU offloading produces gibberish output with flashinfer autotuner

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running Kimi K2 on GB300 with offloading produces garbage output: ``` VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY=1 vllm serve \ --model nvidia/Kimi-K2.5-NVFP4 \ --trust-remote-code \ --cpu-offload-gb 350 \ --cpu-offload-params w13_weight w2_weight ``` After investigation, the problem seems to be associated with flashinfer autotuner. Disabling autotuner resolves the issue. ``` VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY=1 vllm serve \ --model nvidia/Kimi-K2.5-NVFP4 \ --trust-remote-code \ --cpu-offload-gb 350 \ --cpu-offload-params w13_weight w2_weight \ --kernel_config '{"enable_flashinfer_autotune": false}' ``` Note: cpu offloading seems broken on current main. https://github.com/vllm-project/vllm/pull/36461 gets around the error to reproduce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: T_OFFLOADING_DISABLE_PIN_MEMORY=1 vllm serve \ --model nvidia/Kimi-K2.5-NVFP4 \ --trust-remote-code \ --cpu-offload-gb 350 \ --cpu-offload-params w13_weight w2_weight ``` After investigation, the problem seems to be ass...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: output: ``` VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY=1 vllm serve \ --model nvidia/Kimi-K2.5-NVFP4 \ --trust-remote-code \ --cpu-offload-gb 350 \ --cpu-offload-params w13_weight w2_weight ``` After investigation, the p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: CPU offloading produces gibberish output with flashinfer autotuner bug ### Your current environment ### 🐛 Describe the bug Running Kimi K2 on GB300 with offloading produces garbage output: ``` VLLM_WEIGHT_OFFLOAD...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: https://github.com/vllm-project/vllm/pull/36461 gets around the error to reproduce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bott...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 3_weight w2_weight ``` After investigation, the problem seems to be associated with flashinfer autotuner. Disabling autotuner resolves the issue. ``` VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY=1 vllm serve \ --model nvid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
