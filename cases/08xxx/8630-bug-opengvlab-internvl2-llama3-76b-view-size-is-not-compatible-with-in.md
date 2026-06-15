# vllm-project/vllm#8630: [Bug]: OpenGVLab/InternVL2-Llama3-76B: view size is not compatible with input tensor's size and stride

| 字段 | 值 |
| --- | --- |
| Issue | [#8630](https://github.com/vllm-project/vllm/issues/8630) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenGVLab/InternVL2-Llama3-76B: view size is not compatible with input tensor's size and stride

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20240919-094504.pkl.zip](https://github.com/user-attachments/files/17057110/err_execute_model_input_20240919-094504.pkl.zip) ### 🐛 Describe the bug When I start the model via: ```vllm serve OpenGVLab/InternVL2-Llama3-76B --tensor-parallel-size 8 --max-model-len 8000``` I get: ```Traceback (most recent call last): File "/vllm-workspace/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) File "/vllm-workspace/vllm/worker/model_runner.py", line 1590, in execute_model hidden_or_intermediate_states = model_executable( File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1735, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1746, in _call_impl return forward_call(*args, **kwargs) File "/vllm-workspace/vllm/model_executor/models/internvl.py", line 488, in forward vision_embeddings = self._process_image_input(image_input) File "/vllm-workspace/vllm/model_executor/models/internvl.py", line 471, in _process_image_input image_embeds = self.ext...

## 现有链接修复摘要

#8880 [Bugfix] fix #8630

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: OpenGVLab/InternVL2-Llama3-76B: view size is not compatible with input tensor's size and stride bug;rocm;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20240919-094504.pkl.zip](...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: VL2-Llama3-76B: view size is not compatible with input tensor's size and stride bug;rocm;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20240919-094504.pkl.zip](https://github.com/user...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oss two contiguous subspaces). Use .reshape(...) instead.``` correctness ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 76B: view size is not compatible with input tensor's size and stride bug;rocm;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20240919-094504.pkl.zip](https://github.com/user-attachment...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: view size is not compatible with input tensor's size and stride bug;rocm;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20240919-094504.pkl.zip](https://github.com/user-attachments/fil...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8880](https://github.com/vllm-project/vllm/pull/8880) | closes_keyword | 0.95 | [Bugfix] fix #8630 | FIX #8630 After transpose, the tensor becomes discontinuous, then calling `view` will cause the bug in #8630. cc @WoosukKwon @youkaichao **BEFORE SUBMITTING, PLEASE READ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
