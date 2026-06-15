# vllm-project/vllm#5010: [New Model]: tiiuae/falcon-11B

| 字段 | 值 |
| --- | --- |
| Issue | [#5010](https://github.com/vllm-project/vllm/issues/5010) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: tiiuae/falcon-11B

### Issue 正文摘录

### The model to consider. https://huggingface.co/tiiuae/falcon-11B ### The closest model vllm already supports. tiiuae/falcon-7b tiiuae/falcon-40b ### What's your difficulty of supporting the model you want? ### 🚀 The feature, motivation and pitch [Falcon-11B](https://huggingface.co/tiiuae/falcon-11B) is trained on multilingual data. There is a lot of potential to serve this model where these languages are preferred. Functional, working inference in fp16 would be a great addition in my opinion. ### Additional context The main architectural changes between the two configurations of the Falcon model are: 1. New Decoder Architecture: - Falcon-7B has `new_decoder_architecture: false`, which means it uses the original or a previous version of the decoder architecture. - Falcon-11B specifies `new_decoder_architecture: true`, indicating a newer version of the decoder architecture. 2. Number of Attention Heads: - Falcon-7B uses `num_attention_heads: 71`. - With Falcon-11B this number is significantly decreased to `num_attention_heads: 32`. 3. Number of Hidden Layers: - Falcon-11B has `num_hidden_layers: 60`, which is almost double the number in Falcon-7B, which has `num_hidden_layers: 32...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: tiiuae/falcon-11B new-model ### The model to consider. https://huggingface.co/tiiuae/falcon-11B ### The closest model vllm already supports. tiiuae/falcon-7b tiiuae/falcon-40b ### What's your difficulty of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: der_architecture: false`, which means it uses the original or a previous version of the decoder architecture. - Falcon-11B specifies `new_decoder_architecture: true`, indicating a newer version of the decoder architectu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ew Decoder Architecture: - Falcon-7B has `new_decoder_architecture: false`, which means it uses the original or a previous version of the decoder architecture. - Falcon-11B specifies `new_decoder_architecture: true`, in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: -00005.safetensors: 100%|████| 4.98G/4.98G [18:21 [rank0]: sys.exit(benchmark()) [rank0]: File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1157, in __call__ [rank0]: return self.main(*args, **kwargs) [...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: uld be a great addition in my opinion. ### Additional context The main architectural changes between the two configurations of the Falcon model are: 1. New Decoder Architecture: - Falcon-7B has `new_decoder_architecture...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
