# vllm-project/vllm#6987: [Bug]: 导入default_dump_dir报错

| 字段 | 值 |
| --- | --- |
| Issue | [#6987](https://github.com/vllm-project/vllm/issues/6987) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 导入default_dump_dir报错

### Issue 正文摘录

### Your current environment ubuntu Ubuntu 22.04.4 LTS cuda 12.2 vllm 0.5.3.post1 /home/gtlm/ai/zhangyr/vllm vllm-flash-attn 2.5.9.post1 ### 🐛 Describe the bug 运行vllm server 报错： vllm/vllm/triton_utils/custom_cache_manager.py", line 3, in from triton.runtime.cache import (FileCacheManager, default_cache_dir, ImportError: cannot import name 'default_dump_dir' from 'triton.runtime.cache'

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2.5.9.post1 ### 🐛 Describe the bug 运行vllm server 报错： vllm/vllm/triton_utils/custom_cache_manager.py", line 3, in from triton.runtime.cache import (FileCacheManager, default_cache_dir, ImportError: cannot import name 'de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ils/custom_cache_manager.py", line 3, in from triton.runtime.cache import (FileCacheManager, default_cache_dir, ImportError: cannot import name 'default_dump_dir' from 'triton.runtime.cache' development attention_kv_cac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _dir报错 bug;stale ### Your current environment ubuntu Ubuntu 22.04.4 LTS cuda 12.2 vllm 0.5.3.post1 /home/gtlm/ai/zhangyr/vllm vllm-flash-attn 2.5.9.post1 ### 🐛 Describe the bug 运行vllm server 报错： vllm/vllm/tr
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: 导入default_dump_dir报错 bug;stale ### Your current environment ubuntu Ubuntu 22.04.4 LTS cuda 12.2 vllm 0.5.3.post1 /home/gtlm/ai/zhangyr/vllm vllm-flash-attn 2.5.9

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
