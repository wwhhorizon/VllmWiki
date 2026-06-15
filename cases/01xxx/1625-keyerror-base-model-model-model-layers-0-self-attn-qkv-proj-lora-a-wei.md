# vllm-project/vllm#1625: KeyError: 'base_model.model.model.layers.0.self_attn.qkv_proj.lora_A.weight'

| 字段 | 值 |
| --- | --- |
| Issue | [#1625](https://github.com/vllm-project/vllm/issues/1625) |
| 状态 | closed |
| 标签 |  |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KeyError: 'base_model.model.model.layers.0.self_attn.qkv_proj.lora_A.weight'

### Issue 正文摘录

When I try to inference my finetuned code llama model using vllm, getting this error ` File "/usr/local/lib/python3.9/dist-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, **kwargs) File "/usr/local/lib/python3.9/dist-packages/vllm/worker/worker.py", line 70, in init_model self.model = get_model(self.model_config) File "/usr/local/lib/python3.9/dist-packages/vllm/model_executor/model_loader.py", line 103, in get_model model.load_weights(model_config.model, model_config.download_dir, File "/usr/local/lib/python3.9/dist-packages/vllm/model_executor/models/llama.py", line 367, in load_weights param = state_dict[name.replace(weight_name, "qkv_proj")] KeyError: 'base_model.model.model.layers.0.self_attn.qkv_proj.lora_A.weight'` ![vllm](https://github.com/vllm-project/vllm/assets/102607452/9d0c6d78-f658-47ec-bd3a-f06b46ff6c7d) Some Shape Of my models ` model.layers.0.input_layernorm.weight | [4096] | BF16 -- | -- | -- model.layers.0.mlp.down_proj.weight | [4096,11008] | BF16 model.layers.0.mlp.gate_proj.weight | [11008,4096] | BF16 model.layers.0.mlp.up_proj.weight | [11008,4096] | BF16 model.layers.0.post_attention_layernorm.weight | [4096] | BF16 m...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: KeyError: 'base_model.model.model.layers.0.self_attn.qkv_proj.lora_A.weight' When I try to inference my finetuned code llama model using vllm, getting this error ` File "/usr/local/lib/python3.9/dist-packages/vllm/engin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ight | [4096,4096] | BF16 ` Any Suggestion or help is highly appreciated.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: pe Of my models ` model.layers.0.input_layernorm.weight | [4096] | BF16 -- | -- | -- model.layers.0.mlp.down_proj.weight | [4096,11008] | BF16 model.layers.0.mlp.gate_proj.weight | [11008,4096] | BF16 model.layers.0.mlp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
