# vllm-project/vllm#33519: [Bug]: GLM4.7-flash cannot load lora adapters

| 字段 | 值 |
| --- | --- |
| Issue | [#33519](https://github.com/vllm-project/vllm/issues/33519) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM4.7-flash cannot load lora adapters

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I trained a lora adapter using unsloth and now trying to load it for inference using vllm however I get this error MoE model detected. Using fused MoE LoRA implementation. ... File "/opt/conda/lib/python3.11/site-packages/vllm/lora/model_manager.py", line 890, in create_lora_manager lora_manager = lora_manager_cls( File "/opt/conda/lib/python3.11/site-packages/vllm/lora/model_manager.py", line 802, in __init super().__init__( File "/opt/conda/lib/python3.11/site-packages/vllm/lora/model_manager.py", line 100, in __init_ self.packed_modules_mapping = process_packed_modules_mapping(self.model) File "/opt/conda/lib/python3.11/site-packages/vllm/lora/utils.py", line 267, in process_packed_modules_mapping if moe_packed_mapping := get_moe_expert_mapping(model): File "/opt/conda/lib/python3.11/site-packages/vllm/model_executor/utils.py", line 107, in get_moe_expert_mapping return parent_map() File "/opt/conda/lib/python3.11/site-packages/vllm/model_executor/models/glm4_moe_lite.py", line 619, in get_expert_mapping return SharedFusedMoE.make_expert_params_mapping( TypeError: FusedMoE.make_expert_params_mapping() missing 1 required positi...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: environment ### 🐛 Describe the bug I trained a lora adapter using unsloth and now trying to load it for inference using vllm however I get this error MoE model detected. Using fused MoE LoRA implementation. ... File "/o...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: now trying to load it for inference using vllm however I get this error MoE model detected. Using fused MoE LoRA implementation. ... File "/opt/conda/lib/python3.11/site-packages/vllm/lora/model_manager.py", line 890, i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: trying to load it for inference using vllm however I get this error MoE model detected. Using fused MoE LoRA implementation. ... File "/opt/conda/lib/python3.11/site-packages/vllm/lora/model_manager.py", line 890, in cr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
