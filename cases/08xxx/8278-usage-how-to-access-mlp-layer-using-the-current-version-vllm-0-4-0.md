# vllm-project/vllm#8278: [Usage]: How to access mlp layer using the current version vllm(0.4.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#8278](https://github.com/vllm-project/vllm/issues/8278) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;model_support |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to access mlp layer using the current version vllm(0.4.0)

### Issue 正文摘录

### Your current environment --- **Description:** I am currently updating code that was written based on an older version of `vllm` (version 0.2.7). In the previous implementation, I accessed the `mlp` layer using the following code snippet: ```python obj = model.llm_engine.driver_worker.model_runner.model.model.layers[i].mlp ``` However, after updating to the latest version of `vllm`, this line now raises the following error: ```bash AttributeError: 'LLMEngine' object has no attribute 'driver_worker' ``` It seems that the architecture of `vllm` has changed in the newer version, and I am unsure how to access the `mlp` layer now. Below is the relevant part of the code where I use this method: ```python from vllm import LLM, SamplingParams model = LLM(model=args.model, tensor_parallel_size=torch.cuda.device_count(), enforce_eager=True) if args.activation_mask: activation_masks = torch.load(args.activation_mask) for activation_mask, mask_lang in zip(activation_masks, mask_langs): if activation_mask: def factory(mask): def llama_forward(self, x): gate_up, _ = self.gate_up_proj(x) i = gate_up.size(-1) activation = F.silu(gate_up[:, :, : i // 2]) activation.index_fill_(2, mask, 0) x = a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: How to access mlp layer using the current version vllm(0.4.0) usage ### Your current environment --- **Description:** I am currently updating code that was written based on an older version of `vllm` (version 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: LMEngine' object has no attribute 'driver_worker' ``` It seems that the architecture of `vllm` has changed in the newer version, and I am unsure how to access the `mlp` layer now. Below is the relevant part of the code...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: essed the `mlp` layer using the following code snippet: ```python obj = model.llm_engine.driver_worker.model_runner.model.model.layers[i].mlp ``` However, after updating to the latest version of `vllm`, this line now ra...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: r.model_runner.model.transformer.h[i].mlp obj.forward = MethodType(factory(layer_mask.to('cuda')), obj) for lang in langs: texts, sampling_params, = load_dataset(lang, sampling_params) outputs = model.generate(texts, sa...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: x, _ = self.down_proj(x) return x def bloom_forward(self, x: torch.Tensor): x, _ = self.dense_h_to_4h(x) x = self.gelu_impl(x) x.index_fill_(2, mask, 0) x, _ = self.dense_4h_to_h(x)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
