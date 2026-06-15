# vllm-project/vllm#43141: [Bug]: Deepseek v4 ImportError: cannot import name 'Arch' from 'cutlass.base_dsl'

| 字段 | 值 |
| --- | --- |
| Issue | [#43141](https://github.com/vllm-project/vllm/issues/43141) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;gemm_linear |
| 子分类 |  |
| Operator 关键词 | activation;attention;cuda;operator |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deepseek v4 ImportError: cannot import name 'Arch' from 'cutlass.base_dsl'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running on top-of-tree main: ``` (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] File "/vllm/vllm/models/deepseek_v4/attention.py", line 1179, in forward (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] q_quant, weights = fused_indexer_q_rope_quant( (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] File "/vllm/vllm/models/deepseek_v4/common/ops/fused_indexer_q.py", line 349, in fused_indexer_q_rope_quant (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] from vllm.models.deepseek_v4.nvidia.ops.fused_indexer_q_cutedsl import ( (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] File "/vllm/vllm/models/deepseek_v4/nvidia/ops/fused_indexer_q_cutedsl.py", line 10, in (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] from quack.compile_utils import make_fake_tensor (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] File "/vllm/.venv/lib/python3.12/site-pa...

## 现有链接修复摘要

#43146 [Bugfix] Fix DeepSeek V4 ImportError when cutlass/quack versions are incompatible

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Deepseek v4 ImportError: cannot import name 'Arch' from 'cutlass.base_dsl' bug ### Your current environment ### 🐛 Describe the bug Running on top-of-tree main: ``` (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Deepseek v4 ImportError: cannot import name 'Arch' from 'cutlass.base_dsl' bug ### Your current environment ### 🐛 Describe the bug Running on top-of-tree main: ``` (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Deepseek v4 ImportError: cannot import name 'Arch' from 'cutlass.base_dsl' bug ### Your current environment ### 🐛 Describe the bug Running on top-of-tree main: ``` (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: P2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] q_quant, weights = fused_indexer_q_rope_quant( (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] File "/vllm/vllm/models/deepseek_v4/attention.py", line 1179, in forward (Worker_DP2_EP2 pid=26757) ERROR 05-19 13:32:24 [multiproc_executor.py:962] q_quant, weights...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43146](https://github.com/vllm-project/vllm/pull/43146) | closes_keyword | 0.95 | [Bugfix] Fix    DeepSeek V4 ImportError when cutlass/quack versions are              incompatible | Fixes #43141 EOF |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
