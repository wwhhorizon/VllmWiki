# vllm-project/vllm#4902: [Feature]: Support for Falcon-11B model (Falcon 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#4902](https://github.com/vllm-project/vllm/issues/4902) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Falcon-11B model (Falcon 2)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [Falcon-11B](https://huggingface.co/tiiuae/falcon-11B) is trained on multilingual data. There is a lot of potential to serve this model where these languages are preferred. Functional, working inference in fp16 would be a great addition in my opinion. ### Additional context The tokenizer has been consistent, however the architecture has been changed from: ```{ "model_type": "falcon", "architectures": [ "FalconForCausalLM" ], "pre_weights": [ { "name": "transformer.word_embeddings.weight", "is_embed": true } ], "post_weights": [ { "name": "transformer.ln_f.weight" }, { "name": "transformer.ln_f.bias" }, { "name": "lm_head.weight", "is_embed": true } ], "num_layers_config_key": "num_hidden_layers", "layer_templates": { "weights": [ { "name": "transformer.h.${layer_index}.ln_attn.bias" }, { "name": "transformer.h.${layer_index}.ln_attn.weight" }, { "name": "transformer.h.${layer_index}.ln_mlp.bias" }, { "name": "transformer.h.${layer_index}.ln_mlp.weight" }, { "name": "transformer.h.${layer_index}.mlp.dense_4h_to_h.weight" }, { "name": "transformer.h.${layer_index}.mlp.dense_h_to_4h.weight" }, { "name": "transformer.h.${layer_index}.self_attent...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Support for Falcon-11B model (Falcon 2) feature request ### 🚀 The feature, motivation and pitch [Falcon-11B](https://huggingface.co/tiiuae/falcon-11B) is trained on multilingual data. There is a lot of potent...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: -00005.safetensors: 100%|████| 4.98G/4.98G [18:21 [rank0]: sys.exit(benchmark()) [rank0]: File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1157, in __call__ [rank0]: return self.main(*args, **kwargs) [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Additional context The tokenizer has been consistent, however the architecture has been changed from: ```{ "model_type": "falcon", "architectures": [ "FalconForCausalLM" ], "pre_weights": [ { "name": "transformer.wo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: al/benchmarker.py", line 720, in _benchmark_single [rank0]: results, metadata_dict, model, tokenizer = dataset( [rank0]: File "/usr/local/lib/python3.10/dist-packages/scandeval/benchmark_dataset.py", line 601, in __call...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support for Falcon-11B model (Falcon 2) feature request ### 🚀 The feature, motivation and pitch [Falcon-11B](https://huggingface.co/tiiuae/falcon-11B) is trained on multilingual data. There is a lot of potent...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
