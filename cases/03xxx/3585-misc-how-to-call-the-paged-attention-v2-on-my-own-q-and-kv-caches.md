# vllm-project/vllm#3585: [Misc]: How to call the paged_attention_v2 on my own q and kv caches?

| 字段 | 值 |
| --- | --- |
| Issue | [#3585](https://github.com/vllm-project/vllm/issues/3585) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: How to call the paged_attention_v2 on my own q and kv caches?

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi, I am trying to use the `paged_attention_v2` function on my own data, qkv. However, I find it is not giving the correct result. I test with the following script: ``` from typing import Optional import argparse import random import time import torch from flash_attn import flash_attn_func from vllm._C import ops, cache_ops from vllm.utils import create_kv_caches_with_random NUM_BLOCKS = 1024 BLOCK_SIZE = 32 PARTITION_SIZE = 512 torch.set_default_device('cuda:0') torch.set_default_dtype(torch.float16) def expand_heads(tensor, num_heads=32, num_heads_kv=8): assert tensor.dim() == 3 _, length, dim_head = tensor.shape num_group = num_heads // num_heads_kv tensor = tensor.view((num_heads_kv, 1, length, dim_head)) tensor = tensor.expand((num_heads_kv, num_group, length, dim_head)).reshape((num_heads, length, dim_head)) return tensor def make_qkv(len_k, num_head, num_head_kv, head_dim): q = torch.randn(num_head, 1, head_dim) k = torch.randn(num_head_kv, len_k, head_dim) v = torch.randn(num_head_kv, len_k, head_dim) return q, k, v def ref_attention(q, k, v): head_dim = q.shape[2] scale = float(1.0 / (head_dim**0.5)) k, v = expand_heads(k), exp...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: RTITION_SIZE = 512 torch.set_default_device('cuda:0') torch.set_default_dtype(torch.float16) def expand_heads(tensor, num_heads=32, num_heads_kv=8): assert tensor.dim() == 3 _, length, dim_head = tensor.shape num_group...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g the correct result. I test with the following script: ``` from typing import Optional import argparse import random import time import torch from flash_attn import flash_attn_func from vllm._C import ops, cache_ops fr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ops, cache_ops from vllm.utils import create_kv_caches_with_random NUM_BLOCKS = 1024 BLOCK_SIZE = 32 PARTITION_SIZE = 512 torch.set_default_device('cuda:0') torch.set_default_dtype(torch.float16) def expand_heads(tensor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: S = 1024 BLOCK_SIZE = 32 PARTITION_SIZE = 512 torch.set_default_device('cuda:0') torch.set_default_dtype(torch.float16) def expand_heads(tensor, num_heads=32, num_heads_kv=8): assert tensor.dim() == 3 _, length, dim_hea...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ged_attention(q, k, v) print('Vanilla attention:') print(o_ref) print('\nFlash attention:') print(o_fa) print('\nPaged attention:') print(o_pa, o_pa.shape) ``` In my above code, I set the length of `kv` to be `10`, and...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
