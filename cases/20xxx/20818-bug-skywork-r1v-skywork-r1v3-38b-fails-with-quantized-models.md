# vllm-project/vllm#20818: [Bug]: Skywork R1V (Skywork-R1V3-38B) fails with Quantized models

| 字段 | 值 |
| --- | --- |
| Issue | [#20818](https://github.com/vllm-project/vllm/issues/20818) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Skywork R1V (Skywork-R1V3-38B) fails with Quantized models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The mlp1 layer in the SkyworkR1VChatModel for Skywork-R1V3-38B, does not support quantization on the linear layers, and causes failures when loading quantized models (FP8, BNB, etc). `mlp1.1.weight_scale not supported/recognized` https://github.com/vllm-project/vllm/blob/b4f0b5f9aaa8b93a335c12b7f412f44f17d704e0/vllm/model_executor/models/skyworkr1v.py#L736-L749 This can be fixed by swapping out the `ReplicatedLinear` layers for ``` mlp_in_dim = vit_hidden_size * int(1 / self.downsample_ratio)**2 return nn.Sequential( nn.LayerNorm(mlp_in_dim), ColumnParallelLinear(mlp_in_dim, <---- llm_hidden_size, bias=True, quant_config=quant_config, return_bias=False), nn.GELU(), RowParallelLinear(llm_hidden_size, <---- llm_hidden_size, bias=True, quant_config=quant_config, return_bias=False), ) ``` ColumnParallelLinear and RowParallelLinear, which support quantized weight_scale values @pengyuange @skydownacai is this a change that would play well with the earlier SkyworkR1V models? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [docum...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Skywork R1V (Skywork-R1V3-38B) fails with Quantized models bug;stale ### Your current environment ### 🐛 Describe the bug The mlp1 layer in the SkyworkR1VChatModel for Skywork-R1V3-38B, does not support quantizati...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n answer lots of frequently asked questions. correctness activation_norm;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding activation;cuda;fp8;ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ls? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Skywork R1V (Skywork-R1V3-38B) fails with Quantized models bug;stale ### Your current environment ### 🐛 Describe the bug The mlp1 layer in the SkyworkR1VChatModel for Skywork-R1V3-38B, does not support quantizati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Skywork R1V (Skywork-R1V3-38B) fails with Quantized models bug;stale ### Your current environment ### 🐛 Describe the bug The mlp1 layer in the SkyworkR1VChatModel for Skywork-R1V3-38B, does not support quantizati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
