# vllm-project/vllm#561: Unable to load the configuration of 'MPTForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#561](https://github.com/vllm-project/vllm/issues/561) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;gemm_linear;model_support |
| 子分类 |  |
| Operator 关键词 | activation;cuda;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Unable to load the configuration of 'MPTForCausalLM

### Issue 正文摘录

When I run this, my error is OSError: Can't load the configuration of 'MPTForCausalLM even though I don't have a local directory. `import torch import transformers from torch import cuda, bfloat16 name = 'mosaicml/mpt-7b' config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True) #config.attn_config['attn_impl'] = 'triton' config.init_device = 'cuda:5' # For fast initialization directly on GPU! torch.cuda.empty_cache() model = transformers.AutoModelForCausalLM.from_pretrained( 'mosaicml/mpt-7b', config=config, trust_remote_code=True, torch_dtype=bfloat16 ) from vllm import LLM torch.cuda.empty_cache() llm = LLM(model=model)` `OSError: Can't load the configuration of 'MPTForCausalLM( (transformer): MPTModel( (wte): SharedEmbedding(50432, 4096) (emb_drop): Dropout(p=0, inplace=False) (blocks): ModuleList( (0-31): 32 x MPTBlock( (norm_1): LPLayerNorm((4096,), eps=1e-05, elementwise_affine=True) (attn): MultiheadAttention( (Wqkv): Linear(in_features=4096, out_features=12288, bias=False) (out_proj): Linear(in_features=4096, out_features=4096, bias=False) ) (norm_2): LPLayerNorm((4096,), eps=1e-05, elementwise_affine=True) (ffn): MPTMLP( (up_proj): Linear(in_features...

## 现有链接修复摘要

#18886 Fa upstream3 (#561)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ory. `import torch import transformers from torch import cuda, bfloat16 name = 'mosaicml/mpt-7b' config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True) #config.attn_config['attn_impl'] = 'triton'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Unable to load the configuration of 'MPTForCausalLM When I run this, my error is OSError: Can't load the configuration of 'MPTForCausalLM even though I don't have a local directory. `import torch import transformers fro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: f 'MPTForCausalLM even though I don't have a local directory. `import torch import transformers from torch import cuda, bfloat16 name = 'mosaicml/mpt-7b' config = transformers.AutoConfig.from_pretrained(name, trust_remo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: directory. `import torch import transformers from torch import cuda, bfloat16 name = 'mosaicml/mpt-7b' config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True) #config.attn_config['attn_impl'] = 't...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: te): SharedEmbedding(50432, 4096) (emb_drop): Dropout(p=0, inplace=False) (blocks): ModuleList( (0-31): 32 x MPTBlock( (norm_1): LPLayerNorm((4096,), eps=1e-05, elementwise_affine=True) (attn): MultiheadAttention( (Wqkv...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18886](https://github.com/vllm-project/vllm/pull/18886) | mentioned | 0.6 | Fa upstream3 (#561) | Fa upstream3 (#561) * integrate aiter * add env variable * rename function * optimize kernels with small query lens |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
