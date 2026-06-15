# vllm-project/vllm#15779: [Bug]: Disagreement and misalignment between supported models in documentation and actual testing

| 字段 | 值 |
| --- | --- |
| Issue | [#15779](https://github.com/vllm-project/vllm/issues/15779) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Disagreement and misalignment between supported models in documentation and actual testing

### Issue 正文摘录

### Your current environment Tested under VLLM ==0.7.3 and 0.8.2 ### 🐛 Describe the bug I am using this model (after quantizing it to 4 bits): **nvidia/Llama-3_3-Nemotron-Super-49B-v1** https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1 and according to the documentation here: https://docs.vllm.ai/en/latest/models/supported_models.html (This is the summary of the related section in the above website: `To determine whether a given model is natively supported, you can check the config.json file inside the HF repository. If the "architectures" field contains a model architecture listed below, then it should be natively supported.` ) The **nvidia/Llama-3_3-Nemotron-Super-49B-v1** model architecture according to the HF is **DeciLMForCausalLM** and according to the documentation above, **DeciLMForCausalLM** is listed as one of the supported architectures hence it should be natively supported. However loading the above model create these issues: ![Image](https://github.com/user-attachments/assets/2cb8e815-2169-462d-a7a6-6903f81a81e8) 1- Under VLLM ==0.7.3 I get this error: DeciLMConfig object has no attribute 'num_key_value_heads_per_layer' 2- Under VLLM==0.8.2 I get OOM and t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Disagreement and misalignment between supported models in documentation and actual testing bug ### Your current environment Tested under VLLM ==0.7.3 and 0.8.2 ### 🐛 Describe the bug I am using this model (after...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _3-Nemotron-Super-49B-v1** model architecture according to the HF is **DeciLMForCausalLM** and according to the documentation above, **DeciLMForCausalLM** is listed as one of the supported architectures hence it should...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ==0.7.3 and 0.8.2 ### 🐛 Describe the bug I am using this model (after quantizing it to 4 bits): **nvidia/Llama-3_3-Nemotron-Super-49B-v1** https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1 and according to t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed, you can check the config.json file inside the HF repository. If the "architectures" field contains a model architecture listed below, then it should be natively supported.` ) The **nvidia/Llama-3_3-Nemotron-Super-49...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: no attribute 'num_key_value_heads_per_layer' 2- Under VLLM==0.8.2 I get OOM and this error together. Can someone explain if I am doing anything wrong, or if I am interpreting anything wrong. ### Before submitting a new...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
