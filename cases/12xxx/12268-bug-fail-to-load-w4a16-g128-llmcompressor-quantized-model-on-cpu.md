# vllm-project/vllm#12268: [Bug]: Fail to load W4A16-G128 (llmcompressor) quantized model on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#12268](https://github.com/vllm-project/vllm/issues/12268) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fail to load W4A16-G128 (llmcompressor) quantized model on CPU

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting error (TypeError: 'NoneType' object is not subscriptable) on loading a W4A16-G128 (llmcompressor) quantized model on vllm 0.6.5 with ipex 2.5.0 on CPU ```python from vllm import LLM, SamplingParams import pandas as pd import csv def run_inference(model_path: str =None): # Initialize the model explicitly for CPU with adjusted settings llm = LLM( model=model_path, # Replace with the path to your model tokenizer=model_path, # Replace with the path to your tokenizer device="cpu", # Explicitly use CPU max_model_len=8124 ) tokenizer = llm.get_tokenizer() sampling_params = SamplingParams( temperature=0.0, max_tokens=750, top_k=1, # top_p=0.95, stop_token_ids=[tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids(" ")], # stop=EOS ) if __name__ == "__main__": #take the model path as input argument from terminal import sys model_path=sys.argv[1] # print(model_path) run_inference(model_path) ``` ``` warnings.warn(f"Warning: Cannot load xpu CCL. CCL doesn't work for XPU device due to {e}") INFO 01-21 08:56:15 config.py:478] This model supports multiple tasks: {'embed', 'classify', 'reward', 'sco...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: uantized model on vllm 0.6.5 with ipex 2.5.0 on CPU ```python from vllm import LLM, SamplingParams import pandas as pd import csv def run_inference(model_path: str =None): # Initialize the model explicitly for CPU with...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Fail to load W4A16-G128 (llmcompressor) quantized model on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting error (TypeError: 'NoneType' object is not...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Fail to load W4A16-G128 (llmcompressor) quantized model on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting error (TypeError: 'NoneType' object is not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Bug]: Fail to load W4A16-G128 (llmcompressor) quantized model on CPU bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Getting error (TypeError: 'NoneType' object is not s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ARNING 01-21 08:56:15 _logger.py:72] CUDA graph is not supported on CPU, fallback to the eager mode. WARNING 01-21 08:56:15 _logger.py:72] Environment variable VLLM_CPU_KVCACHE_SPACE (GB) for CPU backend is not set, usi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
