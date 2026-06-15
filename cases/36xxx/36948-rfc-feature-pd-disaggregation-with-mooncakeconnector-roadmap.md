# vllm-project/vllm#36948: [RFC] [Feature]: PD Disaggregation with MooncakeConnector Roadmap

| 字段 | 值 |
| --- | --- |
| Issue | [#36948](https://github.com/vllm-project/vllm/issues/36948) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] [Feature]: PD Disaggregation with MooncakeConnector Roadmap

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Following the successful initial integration of Mooncake Transfer Engine into vLLM (#24718 #31034), this RFC proposes a feature roadmap to unlock more advanced capabilities, enhance performance, and improve flexibility. The foundational work allows for basic KV cache offloading, but to fully leverage the potential of Mooncake and support more complex, large-scale inference scenarios, we need to implement more sophisticated parallelism strategies and optimizations. Core Features: - [ ] Mooncake store integration (#38474 #40900) - [x] Heterogeneous TP support (#36869) - [ ] PP support - [ ] Layer-wise Transfer - [ ] Cross-Layer KV Support (#41093) - [ ] PCP/DCP Support - [ ] hybrid attention - Other improvements and fixes - [ ] better error handling - [ ] physical block != config block - [ ] different hidden size per layer - [ ] HND-NHD transfer - [x] kv events & stats (#40414) Related issue #33702 cc @NickLucche @LCAIZJ ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: le inference scenarios, we need to implement more sophisticated parallelism strategies and optimizations. Core Features: - [ ] Mooncake store integration (#38474 #40900) - [x] Heterogeneous TP support (#36869) - [ ] PP...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ormance, and improve flexibility. The foundational work allows for basic KV cache offloading, but to fully leverage the potential of Mooncake and support more complex, large-scale inference scenarios, we need to impleme...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: fully leverage the potential of Mooncake and support more complex, large-scale inference scenarios, we need to implement more sophisticated parallelism strategies and optimizations. Core Features: - [ ] Mooncake store i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: er improvements and fixes - [ ] better error handling - [ ] physical block != config block - [ ] different hidden size per layer - [ ] HND-NHD transfer - [x] kv events & stats (#40414) Related issue #33702 cc @NickLucch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ements and fixes - [ ] better error handling - [ ] physical block != config block - [ ] different hidden size per layer - [ ] HND-NHD transfer - [x] kv events & stats (#40414) Related issue #33702 cc @NickLucche @LCAIZJ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
