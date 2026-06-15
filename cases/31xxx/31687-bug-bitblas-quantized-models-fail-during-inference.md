# vllm-project/vllm#31687: [Bug]: BitBlas quantized models fail during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#31687](https://github.com/vllm-project/vllm/issues/31687) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: BitBlas quantized models fail during inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to quantize a LLama-3.1-1B model using [GPTQModel](https://github.com/ModelCloud/GPTQModel) to 4 bits with BitBlast as the quantization backend. I ended up with the following quantization config: ```json { "bits": 4, "group_size": 128, "desc_act": false, "sym": true, "lm_head": false, "quant_method": "gptq", "checkpoint_format": "gptq", "pack_dtype": "int32", "meta": { "quantizer": [ "gptqmodel:5.6.12" ], "uri": "https://github.com/modelcloud/gptqmodel", "damp_percent": 0.05, "damp_auto_increment": 0.01, "static_groups": false, "true_sequential": true, "mse": 0.0, "gptaq": false, "gptaq_alpha": 0.25, "act_group_aware": true }, "pack_impl": "cpu", "format": "gptq" } ``` I try to run a vLLM server as follows (with the vllm docker container v0.13.0): ``` [docker setup commands] /path/to/quantized/model --quantization bitblas --dtype float16 ``` I could not post the full output of the server startup command due to length contraints, but here is the critical traceback: ``` Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mat": "gptq" } ``` I try to run a vLLM server as follows (with the vllm docker container v0.13.0): ``` [docker setup commands] /path/to/quantized/model --quantization bitblas --dtype float16 ``` I could not post the ful...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: BitBlas quantized models fail during inference bug;stale ### Your current environment ### 🐛 Describe the bug I tried to quantize a LLama-3.1-1B model using [GPTQModel](https://github.com/ModelCloud/GPTQModel) to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: BitBlas quantized models fail during inference bug;stale ### Your current environment ### 🐛 Describe the bug I tried to quantize a LLama-3.1-1B model using [GPTQModel](https://github.com/ModelCloud/GPTQModel) to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ub.com/ModelCloud/GPTQModel) to 4 bits with BitBlast as the quantization backend. I ended up with the following quantization config: ```json { "bits": 4, "group_size": 128, "desc_act": false, "sym": true, "lm_head": fal...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: B). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
