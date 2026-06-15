# vllm-project/vllm#8712: [Feature] compile triton kernels ahead of time 

| 字段 | 值 |
| --- | --- |
| Issue | [#8712](https://github.com/vllm-project/vllm/issues/8712) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature] compile triton kernels ahead of time 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi vllm specialists, I just found that Prefix Caching triton kernels may have a bad e2e performance **at the first time running** . After using nsys, it showed that the first compiling for different input shapes( [grid size: (batch, head, triton.cdiv(max_input_len, BLOCK))](https://github.com/vllm-project/vllm/blob/8ca5051b9afb6f8d2b3ae1b71d45d84e5d1c6f57/vllm/attention/ops/prefix_prefill.py#L751C9-L751C80) ) takes a lot of time. Is there a way to compile these triton kernels of different grid sizes before the inference progress, so that the compiling time won't be involved in the e2e overhead ? here're some methods i found that may work under nvidia environment: - triton's AOT [(link)](https://github.com/triton-lang/triton/blob/main/python/triton/tools/compile.py). There're not documents showing that how to use it. - cuda grpah. But It seems that cuda_graph is disabled in the prefill/chunked prefill? https://github.com/vllm-project/vllm/blob/8ca5051b9afb6f8d2b3ae1b71d45d84e5d1c6f57/vllm/attention/backends/flash_attn.py#L601 So is there any other available solution? BTW i just noticed that in this [PR](https://github.com/vllm-project/vllm/pu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature] compile triton kernels ahead of time feature request ### 🚀 The feature, motivation and pitch Hi vllm specialists, I just found that Prefix Caching triton kernels may have a bad e2e performance **at the first t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Feature] compile triton kernels ahead of time feature request ### 🚀 The feature, motivation and pitch Hi vllm specialists, I just found that Prefix Caching triton kernels may have a bad e2e performance **at the first t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: /tools/compile.py). There're not documents showing that how to use it. - cuda grpah. But It seems that cuda_graph is disabled in the prefill/chunked prefill? https://github.com/vllm-project/vllm/blob/8ca5051b9afb6f8d2b3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: erent input shapes( [grid size: (batch, head, triton.cdiv(max_input_len, BLOCK))](https://github.com/vllm-project/vllm/blob/8ca5051b9afb6f8d2b3ae1b71d45d84e5d1c6f57/vllm/attention/ops/prefix_prefill.py#L751C9-L751C80) )...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature] compile triton kernels ahead of time feature request ### 🚀 The feature, motivation and pitch Hi vllm specialists, I just found that Prefix Caching triton kernels may have a bad e2e performance **at the first t...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
