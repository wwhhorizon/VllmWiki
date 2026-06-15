# vllm-project/vllm#10710: [Bug]: Unsloth bitsandbytes quantized model cannot be run due to: `KeyError: 'layers.42.mlp.down_proj.weight.absmax`

| 字段 | 值 |
| --- | --- |
| Issue | [#10710](https://github.com/vllm-project/vllm/issues/10710) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Unsloth bitsandbytes quantized model cannot be run due to: `KeyError: 'layers.42.mlp.down_proj.weight.absmax`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I would like to run [unsloth/Meta-Llama-3.1-70B-bnb-4bit](https://huggingface.co/unsloth/Meta-Llama-3.1-70B-bnb-4bit) using the `AsyncLLMEngine` in the following way: ```python return AsyncLLMEngineWithLoRA( async_llm_engine=AsyncLLMEngine.from_engine_args( AsyncEngineArgs( model=base_model_config.model_name, enable_lora=finetuned_model_config is not None, max_loras=1, device=device, trust_remote_code=True, # max_model_len=121296 ) ), lora_request=lora_request, ) ``` Please note that `lora_request` is `None` and `enable_lora` is False in this case. I get: ``` ank0]: Traceback (most recent call last): [rank0]: File " ", line 198, in _run_module_as_main [rank0]: File " ", line 88, in _run_code [rank0]: File "/home/kerem/miniconda3/envs/webservice-local-llm-inference/lib/python3.11/site-packages/uvicorn/__main__.py", line 4, in [rank0]: uvicorn.main() [rank0]: File "/home/kerem/miniconda3/envs/webservice-local-llm-inference/lib/python3.11/site-packages/click/core.py", line 1157, in __call__ [rank0]: return self.main(*args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/k...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ite-packages/uvicorn/server.py", line 62, in run [rank0]: return asyncio.run(self.serve(sockets=sockets)) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/kerem/miniconda3/envs/webservice-local-llm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unsloth bitsandbytes quantized model cannot be run due to: `KeyError: 'layers.42.mlp.down_proj.weight.absmax` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hell...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: model cannot be run due to: `KeyError: 'layers.42.mlp.down_proj.weight.absmax` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I would like to run [unsloth/Meta-L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ot be run due to: `KeyError: 'layers.42.mlp.down_proj.weight.absmax` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hello, I would like to run [unsloth/Meta-Llama-3.1-7...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: Unsloth bitsandbytes quantized model cannot be run due to: `KeyError: 'layers.42.mlp.down_proj.weight.absmax` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hell...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
