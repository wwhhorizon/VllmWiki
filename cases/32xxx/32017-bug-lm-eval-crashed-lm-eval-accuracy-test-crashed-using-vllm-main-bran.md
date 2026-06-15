# vllm-project/vllm#32017: [Bug]: [lm_eval crashed] lm eval accuracy test crashed using VLLM MAIN branch but v0.14.0rc0 works

| 字段 | 值 |
| --- | --- |
| Issue | [#32017](https://github.com/vllm-project/vllm/issues/32017) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [lm_eval crashed] lm eval accuracy test crashed using VLLM MAIN branch but v0.14.0rc0 works

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to run lm_eval accuracy test based on 1/9/2026 vllm using gptoss on AMD MI355X(though **I think this issue is HW-agnositic, it can be reproduced on NV GPU I believe**), and **v0.14.0rc0 branch does not have this issue** ### issue desc after I served a gptoss model, and I run lm_eval cli cmd to run acc test the client showed ``` 2026-01-09:03:44:17,044 WARNING [task.py:799] [Task: wikitext] metric word_perplexity is defined, but aggregation is not. using default aggregation=weighted_perplexity 2026-01-09:03:44:17,045 WARNING [task.py:811] [Task: wikitext] metric word_perplexity is defined, but higher_is_better is not. using default higher_is_better=False 2026-01-09:03:44:17,045 WARNING [task.py:799] [Task: wikitext] metric byte_perplexity is defined, but aggregation is not. using default aggregation=weighted_perplexity 2026-01-09:03:44:17,045 WARNING [task.py:811] [Task: wikitext] metric byte_perplexity is defined, but higher_is_better is not. using default higher_is_better=False 2026-01-09:03:44:17,045 WARNING [task.py:799] [Task: wikitext] metric bits_per_byte is defined, but aggregation is not. using default aggregation=b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: is an intended behavior. 2026-01-09:03:44:36,393 INFO [task.py:415] Building contexts for wikitext on rank 0... 100%|██████████| 167/167 [00:00 /tmp/vllm_config.yaml << 'EOF' compilation-config: '{"compile_sizes":[1,2,4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ranch does not have this issue** ### issue desc after I served a gptoss model, and I run lm_eval cli cmd to run acc test the client showed ``` 2026-01-09:03:44:17,044 WARNING [task.py:799] [Task: wikitext] metric word_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: al accuracy test crashed using VLLM MAIN branch but v0.14.0rc0 works bug;rocm ### Your current environment ### 🐛 Describe the bug I try to run lm_eval accuracy test based on 1/9/2026 vllm using gptoss on AMD MI355X(thou...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: s defined, but higher_is_better is not. using default higher_is_better=False 2026-01-09:03:44:17,045 WARNING [task.py:799] [Task: wikitext] metric byte_perplexity is defined, but aggregation is not. using default aggreg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: \ --block-size=$BLOCK_SIZE \ --no-enable-prefix-caching \ --disable-log-requests \ --async-scheduling set +x ``` ### step5: acc test install the lm_eval ``` git clone https://github.com/baberabb/lm-evaluation-harness.gi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
