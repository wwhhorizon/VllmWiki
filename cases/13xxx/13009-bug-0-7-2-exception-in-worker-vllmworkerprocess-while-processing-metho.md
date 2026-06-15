# vllm-project/vllm#13009: [Bug]:  [0.7.2] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks  in 8H100

| 字段 | 值 |
| --- | --- |
| Issue | [#13009](https://github.com/vllm-project/vllm/issues/13009) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  [0.7.2] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks  in 8H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Descrition We want to deploy multi-modal models and vLLM fails to processing the method `determine_num_available_blocks` in **vLLM 0.7.2** but it works in **vLLM 0.6.3.post1** ### Info Model: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct vLLM version: 0.7.2 vLLM Engine Args: ``` limit_mm_per_prompt = {'image': 8} max_model_len = 65536 max_num_seqs = 2 num_scheduler_steps = 1 tensor_parallel_size = 8 ``` ### Error stack trace ``` Traceback (most recent call last): [1;36m(VllmWorkerProcess pid=924)[0;0m ERROR 02-10 05:41:10 multiproc_worker_utils.py:242] File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/output_graph.py", line 1446, in _call_user_compiler [1;36m(VllmWorkerProcess pid=924)[0;0m ERROR 02-10 05:41:10 multiproc_worker_utils.py:242] compiled_fn = compiler_fn(gm, self.example_inputs()) [1;36m(VllmWorkerProcess pid=924)[0;0m ERROR 02-10 05:41:10 multiproc_worker_utils.py:242] File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/repro/after_dynamo.py", line 129, in __call__ [1;36m(VllmWorkerProcess pid=924)[0;0m ERROR 02-10 05:41:10 multiproc_worker_utils.py:242] compiled_gm =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l: https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct vLLM version: 0.7.2 vLLM Engine Args: ``` limit_mm_per_prompt = {'image': 8} max_model_len = 65536 max_num_seqs = 2 num_scheduler_steps = 1 tensor_paral...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug ### Descrition We want to deploy multi-modal models and vLLM fails to processing the method `determine_num_available_blocks` in **vLLM 0.7.2** but it works in **vLLM 0.6.3.post1** ### Info Model:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ls.py:242] File "/usr/local/lib/python3.10/dist-packages/torch/_dynamo/backends/common.py", line 72, in __call__ [1;36m(VllmWorkerProcess pid=924)[0;0m ERROR 02-10 05:41:10 multiproc_worker_utils.py:242] cg = aot_modu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: orkerProcess while processing method determine_num_available_blocks in 8H100 bug;stale ### Your current environment ### 🐛 Describe the bug ### Descrition We want to deploy multi-modal models and vLLM fails to processing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ess while processing method determine_num_available_blocks in 8H100 bug;stale ### Your current environment ### 🐛 Describe the bug ### Descrition We want to deploy multi-modal models and vLLM fails to processing the meth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
