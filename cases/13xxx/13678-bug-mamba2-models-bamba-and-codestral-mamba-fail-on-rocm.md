# vllm-project/vllm#13678: [Bug]: Mamba2 models (Bamba and Codestral Mamba) fail on RoCM

| 字段 | 值 |
| --- | --- |
| Issue | [#13678](https://github.com/vllm-project/vllm/issues/13678) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 | crash;import_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mamba2 models (Bamba and Codestral Mamba) fail on RoCM

### Issue 正文摘录

### Your current environment Via @hackey: >I am using: ROCM (Dual AMD 7900 xtx) Ubuntu 24.04 ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/issues/6479#issuecomment-2674292711 Specifically this part: ``` registry.py:321] from vllm.attention.backends.flash_attn import FlashAttentionMetadata ERROR 02-21 11:17:10 registry.py:321] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/flash_attn.py", line 25, in ERROR 02-21 11:17:10 registry.py:321] from vllm.vllm_flash_attn import (flash_attn_varlen_func, ERROR 02-21 11:17:10 registry.py:321] ImportError: cannot import name 'flash_attn_varlen_func' from 'vllm.vllm_flash_attn' (unknown location) ERROR 02-21 11:17:10 registry.py:321] Traceback (most recent call last): File "/usr/local/bin/vllm", line 8, in sys.exit(main()) ^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/main.py", line 73, in main ``` It looks like the problem is caused by importing FlashAttentionMetadata in MambaMixer2, which pulls in vllm_flash_attn, which is unsupported on RoCM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bo...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 11 Specifically this part: ``` registry.py:321] from vllm.attention.backends.flash_attn import FlashAttentionMetadata ERROR 02-21 11:17:10 registry.py:321] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/ba...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s://github.com/vllm-project/vllm/issues/6479#issuecomment-2674292711 Specifically this part: ``` registry.py:321] from vllm.attention.backends.flash_attn import FlashAttentionMetadata ERROR 02-21 11:17:10 registry.py:32...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mamba2 models (Bamba and Codestral Mamba) fail on RoCM bug;stale ### Your current environment Via @hackey: >I am using: ROCM (Dual AMD 7900 xtx) Ubuntu 24.04 ### 🐛 Describe the bug See https://github.com/vllm-pro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: py:321] from vllm.attention.backends.flash_attn import FlashAttentionMetadata ERROR 02-21 11:17:10 registry.py:321] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/flash_attn.py", line 25, in ERROR...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Mamba2 models (Bamba and Codestral Mamba) fail on RoCM bug;stale ### Your current environment Via @hackey: >I am using: ROCM (Dual AMD 7900 xtx) Ubuntu 24.04 ### 🐛 Describe the bug See https://github.com/vllm-pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
