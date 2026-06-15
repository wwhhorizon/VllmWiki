# vllm-project/vllm#9937: [Bug]: Phi-3 cannot be used with bitsandbytes

| 字段 | 值 |
| --- | --- |
| Issue | [#9937](https://github.com/vllm-project/vllm/issues/9937) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi-3 cannot be used with bitsandbytes

### Issue 正文摘录

### Your current environment vllm version `0.6.3.post1` ### Model Input Dumps _No response_ ### 🐛 Describe the bug here is the testing script: ```python llm = LLM(model= llm_name, dtype='float16', tensor_parallel_size=4, gpu_memory_utilization= 0.96, #seed=None, trust_remote_code=True, quantization="bitsandbytes", load_format="bitsandbytes", enforce_eager=True, enable_lora=False, cpu_offload_gb = 48 #tokenizer_mode= "mistral" if args.llm_name.startswith('mistralai') else 'auto' ) ``` when `llm_name` is `microsoft/Phi-3.5-mini-instruct`, or `microsoft/Phi-3-mini-128k-instruct` or other models under the same series, inference causes error `[rank0]: KeyError: 'layers.21.mlp.gate_up_proj.weight'` full error message: > INFO 11-01 17:09:41 model_runner.py:1056] Starting to load model microsoft/Phi-3-mini-128k-instruct... > INFO 11-01 17:09:41 selector.py:224] Cannot use FlashAttention-2 backend for Volta and Turing GPUs. > INFO 11-01 17:09:41 selector.py:115] Using XFormers backend. > INFO 11-01 17:09:42 loader.py:1051] Loading weights with BitsAndBytes quantization. May take a while ... > INFO 11-01 17:09:42 weight_utils.py:243] Using model weights format ['*.safetensors'] > model-0000...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: dbytes bug ### Your current environment vllm version `0.6.3.post1` ### Model Input Dumps _No response_ ### 🐛 Describe the bug here is the testing script: ```python llm = LLM(model= llm_name, dtype='float16', tensor_para...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: he bug here is the testing script: ```python llm = LLM(model= llm_name, dtype='float16', tensor_parallel_size=4, gpu_memory_utilization= 0.96, #seed=None, trust_remote_code=True, quantization="bitsandbytes", load_format...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -mini-128k-instruct... > INFO 11-01 17:09:41 selector.py:224] Cannot use FlashAttention-2 backend for Volta and Turing GPUs. > INFO 11-01 17:09:41 selector.py:115] Using XFormers backend. > INFO 11-01 17:09:42 loader.py...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cannot be used with bitsandbytes bug ### Your current environment vllm version `0.6.3.post1` ### Model Input Dumps _No response_ ### 🐛 Describe the bug here is the testing script: ```python llm = LLM(model= llm_name, dt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: /s] ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
