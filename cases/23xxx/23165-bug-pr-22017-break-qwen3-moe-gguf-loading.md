# vllm-project/vllm#23165: [Bug]: PR #22017 break Qwen3 MoE GGUF loading.

| 字段 | 值 |
| --- | --- |
| Issue | [#23165](https://github.com/vllm-project/vllm/issues/23165) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PR #22017 break Qwen3 MoE GGUF loading.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Recent PR https://github.com/vllm-project/vllm/pull/22017 introduced a quantization config for the `mlp.gate` layer. ``` python self.gate = ReplicatedLinear(config.hidden_size, config.num_experts, bias=False, quant_config=quant_config, prefix=f"{prefix}.gate") ``` After this modification, the weight layout of `mlp.gate` changed from: ``` "layers.0.mlp.gate.weight" ``` to: ``` "layers.0.mlp.gate.qweight" "layers.0.mlp.gate.qweight_type" ``` However, the GGUF weights iterator doesn't load an F32 layer as a qweight/qweight_type layout since it's not quantized. https://github.com/vllm-project/vllm/blob/v0.10.1/vllm/model_executor/model_loader/weight_utils.py#L568 ``` python def gguf_quant_weights_iterator( gguf_file: str, gguf_to_hf_name_map: dict[str, str] ) -> Generator[tuple[str, torch.Tensor], None, None]: """ Iterate over the quant weights in the model gguf files and convert them to torch tensors """ reader = gguf.GGUFReader(gguf_file) for tensor in reader.tensors: if tensor.name in gguf_to_hf_name_map: weight_type = tensor.tensor_type name = gguf_to_hf_name_map[tensor.name] if weight_type.name != "F32": weight_type_name = name....

## 现有链接修复摘要

#23188 [Quantization] Allow GGUF quantization to skip unquantized layer

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: PR #22017 break Qwen3 MoE GGUF loading. bug ### Your current environment ### 🐛 Describe the bug Recent PR https://github.com/vllm-project/vllm/pull/22017 introduced a quantization config for the `mlp.gate` layer....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits cuda;moe;operator;quantization;sampling;triton build...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: config.num_experts, bias=False, quant_config=quant_config, prefix=f"{prefix}.gate") ``` After this modification, the weight layout of `mlp.gate` changed from: ``` "laye
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Recent PR https://github.com/vllm-project/vllm/pull/22017 introduced a quantization config for the `mlp.gate` layer. ``` python self.gate = ReplicatedLinear(config.hidden_size, config.num_experts, bias=False
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ch? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23188](https://github.com/vllm-project/vllm/pull/23188) | closes_keyword | 0.95 | [Quantization] Allow GGUF quantization to skip unquantized layer | Fix #23165 - Add `unquantized_modules` to `GGUFConfig` to avoid creating quantized weights for unquantized layer. ## Test Plan ``` $ python examples/offline_inference/basic/gener |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
