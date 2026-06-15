# vllm-project/vllm#9376: [Bug]: KeyError: 'layers.60.mlp.gate_up_proj.weight' mistral large bitsandbytes

| 字段 | 值 |
| --- | --- |
| Issue | [#9376](https://github.com/vllm-project/vllm/issues/9376) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'layers.60.mlp.gate_up_proj.weight' mistral large bitsandbytes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug while trying to deploy mistral-large with bitsandbytes in-flight quantization on 2 H100 80GB, I came across this error. ``` [rank0]: KeyError: 'layers.60.mlp.gate_up_proj.weight' ``` minimal code to reproduce it: ```python from vllm import LLM, SamplingParams import torch model_id = "mistralai/Mistral-Large-Instruct-2407" llm = LLM(model=model_id, dtype=torch.bfloat16, trust_remote_code=True, \ quantization="bitsandbytes", load_format="bitsandbytes", tensor_parallel_size = 2) ``` Other persons mentioned it: posted by @figuernd in https://github.com/vllm-project/vllm/issues/4198#issuecomment-2412149718_ this is related to the packed module here: https://github.com/vllm-project/vllm/blob/v0.6.2/vllm/model_executor/models/llama.py#L354 we have gate and up layers referenced in the safetensor index, but somewhat the packing does not happen. https://huggingface.co/mistralai/Mistral-Large-Instruct-2407/blob/main/model.safetensors.index.json#L523 might be linked to these issues: https://github.com/vllm-project/vllm/issues/4198 https://github.com/vllm-project/vllm/issues/9316 ### Before submitting a new issue... - [X] Make sure you alread...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: up_proj.weight' ``` minimal code to reproduce it: ```python from vllm import LLM, SamplingParams import torch model_id = "mistralai/Mistral-Large-Instruct-2407" llm = LLM(model=model_id, dtype=torch.bfloat16, trust_remo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: he bug while trying to deploy mistral-large with bitsandbytes in-flight quantization on 2 H100 80GB, I came across this error. ``` [rank0]: KeyError: 'layers.60.mlp.gate_up_proj.weight' ``` minimal code to reproduce it:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: roduce it: ```python from vllm import LLM, SamplingParams import torch model_id = "mistralai/Mistral-Large-Instruct-2407" llm = LLM(model=model_id, dtype=torch.bfloat16, trust_remote_code=True, \ quantization="bitsandby...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ng to deploy mistral-large with bitsandbytes in-flight quantization on 2 H100 80GB, I came across this error. ``` [rank0]: KeyError: 'layers.60.mlp.gate_up_proj.weight' ``` minimal code to reproduce it: ```python from v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rror: 'layers.60.mlp.gate_up_proj.weight' mistral large bitsandbytes bug;stale ### Your current environment ### 🐛 Describe the bug while trying to deploy mistral-large with bitsandbytes in-flight quantization on 2 H100...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
