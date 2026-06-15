# vllm-project/vllm#25437: [Bug][Qwen3-Next][DP]: Assert when serving Qwen3-Next using DP

| 字段 | 值 |
| --- | --- |
| Issue | [#25437](https://github.com/vllm-project/vllm/issues/25437) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Qwen3-Next][DP]: Assert when serving Qwen3-Next using DP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running: ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -dp 4 --enable-expert-parallel --port 8192 --gpu-memory-utilization 0.75 ``` and then ``` lm_eval --model local-completions --tasks gsm8k \ --model_args model=Qwen/Qwen3-Next-80B-A3B-Instruct,base_url=http://localhost:8192/v1/completions,num_concurrent=50,max_retries=3,tokenized_requests=False \ --limit 100 ``` vLLM crashes while serving requests, with the following log. ``` (EngineCore_DP3 pid=1012497) ERROR 09-23 01:31:45 [v1/engine/core.py:710] File " .2", line 5, in forward (EngineCore_DP3 pid=1012497) ERROR 09-23 01:31:45 [v1/engine/core.py:710] gdn_attention = torch.ops.vllm.gdn_attention(x_3, self_attention_output, 'model.layers.0.linear_attn'); x_3 = self_attention_output = gdn_attention = None (EngineCore_DP3 pid=1012497) ERROR 09-23 01:31:45 [v1/engine/core.py:710] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP3 pid=1012497) ERROR 09-23 01:31:45 [v1/engine/core.py:710] File "/home/tms/vllm/.venv/lib/python3.12/site-packages/torch/_ops.py", line 1243, in __call__ (EngineCore_DP3 pid=1012497) ERROR 09-23 01:31:4...

## 现有链接修复摘要

#24982 [Bugfix][WideEP] Apply TP Attn + EP MoE fix to other models

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;moe;operator;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: on 0.75 ``` and then ``` lm_eval --model local-completions --tasks gsm8k \ --model_args model=Qwen/Qwen3-Next-80B-A3B-Instruct,base_url=http://localhost:8192/v1/completions,num_concurrent=50,max_retries=3,tokenized_requ...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug][Qwen3-Next][DP]: Assert when serving Qwen3-Next using DP bug;stale ### Your current environment ### 🐛 Describe the bug Running: ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -dp 4 --enable-expert-parallel --port...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][Qwen3-Next][DP]: Assert when serving Qwen3-Next using DP bug;stale ### Your current environment ### 🐛 Describe the bug Running: ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -dp 4 --enable-expert-parallel --port
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: unning: ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -dp 4 --enable-expert-parallel --port 8192 --gpu-memory-utilization 0.75 ``` and then ``` lm_eval --model local-completions --tasks gsm8k \ --model_args model=Qwen...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24982](https://github.com/vllm-project/vllm/pull/24982) | mentioned | 0.6 | [Bugfix][WideEP] Apply TP Attn + EP MoE fix to other models | `` `Qwen/Qwen3-Next-80B-A3B-Instruct` (with `--enforce-eager` due to #25437): ``` \|Tasks\|Version\| Filter \|n-shot\| Metric \| \|Value\| \|Stderr\| \|-----\|------:\|--------------- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
