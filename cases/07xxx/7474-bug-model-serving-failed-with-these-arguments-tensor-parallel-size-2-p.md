# vllm-project/vllm#7474: [Bug]: Model serving failed with these arguments --tensor-parallel-size 2 --pipeline-parallel-size 2

| 字段 | 值 |
| --- | --- |
| Issue | [#7474](https://github.com/vllm-project/vllm/issues/7474) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model serving failed with these arguments --tensor-parallel-size 2 --pipeline-parallel-size 2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to serve mixtral 7x8 awq model with 4 gpu node and wanted to publish two instances of that same model. in that node. My understanding from the documnets was we can use --tensor-parallel-size 2 --pipeline-parallel-size 2 to distribute these. My expectation was from this was that it will have two instances of this model using two gpu each but its throwing me this error. (VllmWorkerProcess pid=138) INFO 08-13 15:22:51 model_runner.py:732] Loading model weights took 11.4953 GB (VllmWorkerProcess pid=137) INFO 08-13 15:22:51 model_runner.py:732] Loading model weights took 11.4953 GB (VllmWorkerProcess pid=139) INFO 08-13 15:22:52 model_runner.py:732] Loading model weights took 11.4953 GB INFO 08-13 15:22:52 model_runner.py:732] Loading model weights took 11.4953 GB (VllmWorkerProcess pid=139) ERROR 08-13 15:22:52 multiproc_worker_utils.py:226] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks: 'MixtralForCausalLM' object has no attribute 'make_empty_intermediate_tensors', Traceback (most recent call last): (VllmWorkerProcess pid=139) ERROR 08-13 15:22:52 multiproc_worker_utils.py:226]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n warnings.warn('resource_tracker: There appear to be %d ' correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantizati...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: worker VllmWorkerProcess while processing method determine_num_available_blocks: 'MixtralForCausalLM' object has no attribute 'make_empty_intermediate_tensors', Traceback (most recent call last): (VllmWorkerProcess pid=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: these arguments --tensor-parallel-size 2 --pipeline-parallel-size 2 bug;stale ### Your current environment ### 🐛 Describe the bug Trying to serve mixtral 7x8 awq model with 4 gpu node and wanted to publish two instances...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: pt/conda/lib/python3.11/site-packages/vllm/model_executor/models/mixtral_quant.py", line 361, in forward (VllmWorkerProcess pid=137) ERROR 08-13 15:23:05 multiproc_worker_utils.py:226] hidden_states = self.model(input_i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
