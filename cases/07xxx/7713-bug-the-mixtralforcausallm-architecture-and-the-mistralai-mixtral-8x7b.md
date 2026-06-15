# vllm-project/vllm#7713: [Bug]: The MixtralForCausalLM architecture and the mistralai/Mixtral-8x7B-Instruct-v0.1 model are stated to be supported by vLLM, but an error occurs during model loading.

| 字段 | 值 |
| --- | --- |
| Issue | [#7713](https://github.com/vllm-project/vllm/issues/7713) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: The MixtralForCausalLM architecture and the mistralai/Mixtral-8x7B-Instruct-v0.1 model are stated to be supported by vLLM, but an error occurs during model loading.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The MixtralForCausalLM architecture and the mistralai/Mixtral-8x7B-Instruct-v0.1 model with LoRA are stated to be supported by vLLM ([reference](https://docs.vllm.ai/en/latest/models/supported_models.html)), but an error occurs during model loading. I tested it for vllm versions [v0.5.4] [v0.5.3.post1], and [v0.5.3]. ![image](https://github.com/user-attachments/assets/f0303c3e-2beb-4600-aa39-a8d2aef7a056) ``` #Sample code from vllm import LLM model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1" llm = LLM(model = model_id, enable_lora = True, max_lora_rank = 16, quantization = "bitsandbytes", load_format = "bitsandbytes", enforce_eager = True) ``` ``` #ErrorMessage vllm version: 0.5.4 WARNING 08-21 00:27:46 config.py:254] bitsandbytes quantization is not fully optimized yet. The speed can be slower than non-quantized models. WARNING 08-21 00:27:46 config.py:1342] bitsandbytes quantization is not tested with LoRA yet. INFO 08-21 00:27:46 llm_engine.py:174] Initializing an LLM engine (v0.5.4) with config: model='mistralai/Mixtral-8x7B-Instruct-v0.1', speculative_config=None, tokenizer='mistralai/Mixtral-8x7B-Instruct-v0.1', skip_tokeni...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s.html)), but an error occurs during model loading. I tested it for vllm versions [v0.5.4] [v0.5.3.post1], and [v0.5.3]. ![image](https://github.com/user-attachments/assets/f0303c3e-2beb-4600-aa39-a8d2aef7a056) ``` #Sam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ralForCausalLM architecture and the mistralai/Mixtral-8x7B-Instruct-v0.1 model are stated to be supported by vLLM, but an error occurs during model loading. bug;stale ### Your current environment ### 🐛 Describe the bug...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 0.1" llm = LLM(model = model_id, enable_lora = True, max_lora_rank = 16, quantization = "bitsandbytes", load_format = "bitsandbytes", enforce_eager = True) ``` ``` #ErrorMessage vllm version: 0.5.4 WARNING 08-21 00:27:4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: d to be supported by vLLM, but an error occurs during model loading. bug;stale ### Your current environment ### 🐛 Describe the bug The MixtralForCausalLM architecture and the mistralai/Mixtral-8x7B-Instruct-v0.1 model w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: The MixtralForCausalLM architecture and the mistralai/Mixtral-8x7B-Instruct-v0.1 model are stated to be supported by vLLM, but an error occurs during model loading. bug;stale ### Your current environment ### 🐛 De...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
