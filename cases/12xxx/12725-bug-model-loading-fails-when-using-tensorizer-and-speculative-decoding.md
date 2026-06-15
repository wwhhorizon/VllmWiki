# vllm-project/vllm#12725: [Bug]: Model loading fails when using tensorizer and speculative decoding with local draft model

| 字段 | 值 |
| --- | --- |
| Issue | [#12725](https://github.com/vllm-project/vllm/issues/12725) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model loading fails when using tensorizer and speculative decoding with local draft model

### Issue 正文摘录

### Your current environment `vllm[tensorizer]~=0.6.4post1` `Python 3.10` `Linux Debian` ### 🐛 Describe the bug When loading a model with tensorizer (for example Llama) and enabling speculative decoding with a draft model where the model weights are on local disk `vllm` wrongly re-uses the `TensorizerConfig` supplied via the `model_loader_extra_config` field. This causes the following error: ``` File "/vllm/worker/model_runner.py", line 1074, in load_model self.model = get_model(vllm_config=self.vllm_config) │ │ │ └ VllmConfig(model_config= , cache_config= │ └ └ File "vllm/model_executor/model_loader/__init__.py", line 12, in get_model return loader.load_model(vllm_config=vllm_config) │ │ └ VllmConfig(model_config= , cache_config= └ File "/vllm/model_executor/model_loader/loader.py", line 475, in load_model if is_vllm_tensorized(self.tensorizer_config): │ │ └ TensorizerConfig(tensorizer_uris=['s3://...-... │ └ └ File "vllm/model_executor/model_loader/tensorizer.py", line 423, in is_vllm_tensorized deserializer = TensorDeserializer(open_stream( │ └ └ File "tensorizer/stream_io.py", line 1329, in open_stream scheme, *location = path_uri.split("://", maxsplit=1) └ None ``` We could f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Model loading fails when using tensorizer and speculative decoding with local draft model bug;stale ### Your current environment `vllm[tensorizer]~=0.6.4post1` `Python 3.10` `Linux Debian` ### 🐛 Describe the bug...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Model loading fails when using tensorizer and speculative decoding with local draft model bug;stale ### Your current environment `vllm[tensorizer]~=0.6.4post1` `Python 3.10` `Linux Debian` ### 🐛 Describe the bug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s not fully loaded to the `target_device` so we also had to make an explicit call for that. ``` diff --git a/vllm/model_executor/model_loader/loader.py b/vllm/model_executor/model_loader/loader.py index aa2ccd3f..a5c648...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: to target_device explicitly as we otherwise get an error when computing CUDA graphs + # that not all tensors/parameters are on the same device. + model = model.to(target_device) return model.eval() diff --git a/vllm/spe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e device. + model = model.to(target_device) return model.eval() diff --git a/vllm/spec_decode/draft_model_runner.py b/vllm/spec_decode/draft_model_runner.py index cd4d7eb0..68ceda99 100644 --- a/vllm/spec_decode/draft_m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
