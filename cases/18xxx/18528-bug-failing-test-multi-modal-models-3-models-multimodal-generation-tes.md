# vllm-project/vllm#18528: [Bug][Failing Test]: Multi-Modal Models 3 - models/multimodal/generation/test_common.py

| 字段 | 值 |
| --- | --- |
| Issue | [#18528](https://github.com/vllm-project/vllm/issues/18528) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Failing Test]: Multi-Modal Models 3 - models/multimodal/generation/test_common.py

### Issue 正文摘录

### Your current environment N/A ### 🐛 Describe the bug `models/multimodal/generation/test_common.py::test_single_image_models[gemma3-test_case91]` is failing on main. It is another illegal memory access error. https://buildkite.com/vllm/ci/builds/20503/steps?jid=0196f626-d4d6-4af6-b10f-da8c3145ddfc Stack: ``` [2025-05-22T05:33:18Z] ERROR 05-21 22:33:18 [dump_input.py:68] Dumping input data --- Logging error --- [2025-05-22T05:33:18Z] Traceback (most recent call last): [2025-05-22T05:33:18Z] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 207, in execute_model [2025-05-22T05:33:18Z] return self.model_executor.execute_model(scheduler_output) [2025-05-22T05:33:18Z] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-22T05:33:18Z] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/abstract.py", line 86, in execute_model [2025-05-22T05:33:18Z] output = self.collective_rpc("execute_model", [2025-05-22T05:33:18Z] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-22T05:33:18Z] File "/usr/local/lib/python3.12/dist-packages/vllm/executor/uniproc_executor.py", line 56, in collective_rpc [2025-05-22T05:33:18Z] answer = run_method(self.driver_worke...

## 现有链接修复摘要

#18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug][Failing Test]: Multi-Modal Models 3 - models/multimodal/generation/test_common.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug `models/multimodal/generation/test_common.py::test_single_im...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : Multi-Modal Models 3 - models/multimodal/generation/test_common.py bug;ci-failure ### Your current environment N/A ### 🐛 Describe the bug `models/multimodal/generation/test_common.py::test_single_image_models[gemma3-t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y_(self.block_table_cpu[:num_reqs], [2025-05-22T05:33:18Z] RuntimeError: CUDA error: an illegal memory access was encountered [2025-05-22T05:33:18Z] CUDA kernel errors might be asynchronously reported at some other API...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: line 528, in _prepare_inputs [2025-05-22T05:33:18Z] self.input_batch.block_table.commit(num_reqs) [2025-05-22T05:33:18Z] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/block_table.py", line 81, in commit [...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: odel [2025-05-22T05:33:18Z] return self.model_executor.execute_model(scheduler_output) [2025-05-22T05:33:18Z] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [2025-05-22T05:33:18Z] File "/usr/local/lib/python3.12/di...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | mentioned | 0.6 | [Bugfix] Use random hidden states in dummy sampler run | ot affect any actual model behavior. **Note:** The error reported in #18528 may still occur, as expected, but it will no longer result in illegal memory access due to the fix intr… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
