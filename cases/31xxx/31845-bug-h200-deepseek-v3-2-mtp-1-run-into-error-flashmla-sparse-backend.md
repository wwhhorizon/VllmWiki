# vllm-project/vllm#31845: [Bug]: [H200] DeepSeek V3.2 MTP > 1 run into error (FLASHMLA_SPARSE backend)

| 字段 | 值 |
| --- | --- |
| Issue | [#31845](https://github.com/vllm-project/vllm/issues/31845) |
| 状态 | closed |
| 标签 | bug;speculative-decoding;deepseek |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [H200] DeepSeek V3.2 MTP > 1 run into error (FLASHMLA_SPARSE backend)

### Issue 正文摘录

### 🐛 Describe the bug When serving DeepSeek-V3.2 with MTP = 3, the server launched, but failed when any request is sent. ``` VLLM_USE_DEEP_GEMM=1,VLLM_MOE_USE_DEEP_GEMM=0,VLLM_USE_DEEP_GEMM_E8M0=1 \ vllm serve deepseek-ai/DeepSeek-V3.2 \ --max-num-seqs 512 \ --max-num-batched-tokens 4096 \ --max-model-len 4096 \ --host 0.0.0.0 \ --port 8001 \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.9 \ --async-scheduling \ --no-enable-prefix-caching \ --speculative-config {"method": "deepseek_mtp", "num_speculative_tokens": 3} \ > $LOGDIR/out.log & ``` ``` [0;36m(Worker_TP2 pid=145446)[0;0m ERROR 01-06 12:59:32 [multiproc_executor.py:824] File "/home/dev_user/.local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl [0;36m(Worker_TP2 pid=145446)[0;0m ERROR 01-06 12:59:32 [multiproc_executor.py:824] return forward_call(*args, **kwargs) [0;36m(Worker_TP2 pid=145446)[0;0m ERROR 01-06 12:59:32 [multiproc_executor.py:824] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [0;36m(Worker_TP2 pid=145446)[0;0m ERROR 01-06 12:59:32 [multiproc_executor.py:824] File " .1256", line 5, in forward [0;36m(Worker_TP2 pid=145446)[0;0m ERROR 01-06 12:59:32 [multiproc_executor.py:8...

## 现有链接修复摘要

#31644 [Bugfix] Add missing extra_tensors arg to DeviceCommunicatorBase.disp…

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: questions. ### Your current environment correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding attentio...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: server launched, but failed when any request is sent. ``` VLLM_USE_DEEP_GEMM=1,VLLM_MOE_USE_DEEP_GEMM=0,VLLM_USE_DEEP_GEMM_E8M0=1 \ vllm serve deepseek-ai/DeepSeek-V3.2 \ --max-num-seqs 512 \ --max-num-batched-tokens 40...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: H200] DeepSeek V3.2 MTP > 1 run into error (FLASHMLA_SPARSE backend) bug;speculative-decoding;deepseek ### 🐛 Describe the bug When serving DeepSeek-V3.2 with MTP = 3, the server launched, but failed when any request is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: [H200] DeepSeek V3.2 MTP > 1 run into error (FLASHMLA_SPARSE backend) bug;speculative-decoding;deepseek ### 🐛 Describe the bug When serving DeepSeek-V3.2 with MTP = 3, the server launched, but failed when any req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31644](https://github.com/vllm-project/vllm/pull/31644) | mentioned | 0.45 | [Bugfix] Add missing extra_tensors arg to DeviceCommunicatorBase.disp… | ugfix] add missing extra_tensors arg to devicecommunicatorbase.disp… (#31644) signed-off-by: kunzh <zhikun.wu@outlook.com> ``` ### before submitting a new issue... - [x] make sur |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
