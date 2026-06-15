# vllm-project/vllm#44290: [Feature]: Improving NVFP4 Quantization via Fast and Accurate Sweep on FP8 Block Scale

| 字段 | 值 |
| --- | --- |
| Issue | [#44290](https://github.com/vllm-project/vllm/issues/44290) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;kernel;operator;quantization;triton |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Improving NVFP4 Quantization via Fast and Accurate Sweep on FP8 Block Scale

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I propose ScaleSweep to improve NVFP4 quantization by selecting a better FP8 block scale with a fast and accurate sweep method. In NVFP4 quantization, the FP8 block scale directly affects FP4 reconstruction error. Based on our analysis, we obtain bounded FP8 scale ranges for the MSE and weighted MSE objectives. ScaleSweep then sweeps the possible FP8 scales within these bounds and selects the scale that minimizes the corresponding reconstruction error. ### Alternatives A preliminary implementation and corresponding tests are available here: https://github.com/efsotr/nvfp4quant_test On an NVIDIA RTX PRO 6000 Blackwell GPU, `ScaleSweep_MSE_round` shows comparable speed to the current vLLM default operator `vllm._custom_ops.scaled_fp4_quant` on an 8192×8192 speed test: about `1.0064×` latency. In a preliminary error test on Gaussian-distributed inputs, it reduces MSE from `0.0171616` to `0.0135951`. Currently, I only have preliminary Triton implementations of the `ScaleSweep*` kernels, and the tests have only been run on an NVIDIA RTX PRO 6000 Blackwell GPU. I would appreciate further help from the vLLM community to refine these kernels and int...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Feature]: Improving NVFP4 Quantization via Fast and Accurate Sweep on FP8 Block Scale feature request ### 🚀 The feature, motivation and pitch I propose ScaleSweep to improve NVFP4 quantization by selecting a better FP8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: available here: https://github.com/efsotr/nvfp4quant_test On an NVIDIA RTX PRO 6000 Blackwell GPU, `ScaleSweep_MSE_round` shows comparable speed to the current vLLM default operator `vllm._custom_ops.scaled_fp4_quant` o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: eature]: Improving NVFP4 Quantization via Fast and Accurate Sweep on FP8 Block Scale feature request ### 🚀 The feature, motivation and pitch I propose ScaleSweep to improve NVFP4 quantization by selecting a better FP8 b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: error. ### Alternatives A preliminary implementation and corresponding tests are available here: https://github.com/efsotr/nvfp4quant_test On an NVIDIA RTX PRO 6000 Blackwell GPU, `ScaleSweep_MSE_round` shows comparable...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: MSE from `0.0171616` to `0.0135951`. Currently, I only have preliminary Triton implementations of the `ScaleSweep*` kernels, and the tests have only been run on an NVIDIA RTX PRO 6000 Blackwell GPU. I would appreciate f...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
