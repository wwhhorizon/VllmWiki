# vllm-project/vllm#34850: [Bug]: MiniMax M2.5 MI355 compile error

| 字段 | 值 |
| --- | --- |
| Issue | [#34850](https://github.com/vllm-project/vllm/issues/34850) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | debug |
| Operator 关键词 | attention;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax M2.5 MI355 compile error

### Issue 正文摘录

hi @powderluv @chunfangamd @andyluo7 ## Reprod using 0.15.1 rocm vllm image following @andyluo7's linkedin recipe https://www.linkedin.com/posts/andyluo77_day-0-support-of-minimax-25-on-amd-gpu-activity-7428151527309025280-hXR8 using `VLLM_ROCM_USE_AITER=1` https://github.com/SemiAnalysisAI/InferenceX/pull/755/changes#diff-119a77d9e36f224115a110d7ced653f45bdd04fcf2e5ac1c72c50289df124243 Can you take a look, please let me know if i am doing something wrong or when an version with an bug fix will occur ### trace log full error log here https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22160107761/job/64074423272?pr=755 ``` Worker_TP0 pid=2546205) ERROR 02-18 22:49:39 [multiproc_executor.py:852] return forward_call(*args, **kwargs) (Worker_TP0 pid=2546205) ERROR 02-18 22:49:39 [multiproc_executor.py:852] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=2546205) ERROR 02-18 22:49:39 [multiproc_executor.py:852] File " .2", line 5, in forward (Worker_TP0 pid=2546205) ERROR 02-18 22:49:39 [multiproc_executor.py:852] unified_attention_with_output = torch.ops.vllm.unified_attention_with_output(query_2, key_2, value, output_5, 'model.layers.0.self_attn.attn', kv_cache_dummy_dep = None)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: MiniMax M2.5 MI355 compile error bug;rocm hi @powderluv @chunfangamd @andyluo7 ## Reprod using 0.15.1 rocm vllm image following @andyluo7's linkedin recipe https://www.linkedin.com/posts/andyluo77_day-0-support-o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: max-25-on-amd-gpu-activity-7428151527309025280-hXR8 using `VLLM_ROCM_USE_AITER=1` https://github.com/SemiAnalysisAI/InferenceX/pull/755/changes#diff-119a77d9e36f224115a110d7ced653f45bdd04fcf2e5ac1c72c50289df124243 Can y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: MiniMax M2.5 MI355 compile error bug;rocm hi @powderluv @chunfangamd @andyluo7 ## Reprod using 0.15.1 rocm vllm image following @andyluo7's linkedin recipe https://www.linkedin.com/posts/andyluo77_day-0-support-o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ops.vllm.unified_attention_with_output(query_2, key_2, value, output_5, 'model.layers.0.self_attn.attn', kv_cache_dummy_dep = None); query_2 = key_2 = value = output_5 = unified_attention_with_output = None (Worker_TP0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build;hardware_porting;model_support attention;oper...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
