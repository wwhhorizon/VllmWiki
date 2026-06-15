# vllm-project/vllm#20946: [Bug]: How to imporve the TTFT for Qwen3 model

| 字段 | 值 |
| --- | --- |
| Issue | [#20946](https://github.com/vllm-project/vllm/issues/20946) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | moe;quantization |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: How to imporve the TTFT for Qwen3 model

### Issue 正文摘录

### Your current environment vllm==0.9.0.1 ### 🐛 Describe the bug I experience a slow Time to first token regarding the following command to run Qwen3-GPTQ `QuantTrio/Qwen3-235B-A22B-GPTQ-Int8 ` - Hardwarre: 8 x H100 GPUs I tried to use `enable-expert-parallel` but it didn't help to speed up the TTFT. vllm serve \ QuantTrio/Qwen3-235B-A22B-GPTQ-Int8 \ --served-model-name Qwen3-235B-A22B-GPTQ-Int8 \ --max-model-len 32768 \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --distributed-backend mp Any idea how to imporve the TTFT? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: w Time to first token regarding the following command to run Qwen3-GPTQ `QuantTrio/Qwen3-235B-A22B-GPTQ-Int8 ` - Hardwarre: 8 x H100 GPUs I tried to use `enable-expert-parallel` but it didn't help to speed up the TTFT....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o run Qwen3-GPTQ `QuantTrio/Qwen3-235B-A22B-GPTQ-Int8 ` - Hardwarre: 8 x H100 GPUs I tried to use `enable-expert-parallel` but it didn't help to speed up the TTFT. vllm serve \ QuantTrio/Qwen3-235B-A22B-GPTQ-Int8 \ --se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: How to imporve the TTFT for Qwen3 model bug;stale ### Your current environment vllm==0.9.0.1 ### 🐛 Describe the bug I experience a slow Time to first token regarding the following command to run Qwen3-GPTQ `Quant...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 235B-A22B-GPTQ-Int8 ` - Hardwarre: 8 x H100 GPUs I tried to use `enable-expert-parallel` but it didn't help to speed up the TTFT. vllm serve \ QuantTrio/Qwen3-235B-A22B-GPTQ-Int8 \ --served-model-name Qwen3-235B-A22B-GP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ensor-parallel-size 8 \ --enable-expert-parallel \ --distributed-backend mp Any idea how to imporve the TTFT? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
