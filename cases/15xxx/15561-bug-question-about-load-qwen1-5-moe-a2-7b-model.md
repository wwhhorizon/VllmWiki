# vllm-project/vllm#15561: [Bug]:Question about load Qwen1.5-MoE-A2.7B model

| 字段 | 值 |
| --- | --- |
| Issue | [#15561](https://github.com/vllm-project/vllm/issues/15561) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Question about load Qwen1.5-MoE-A2.7B model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to run Qwen1.5-MoE-A2.7B model from load checkpoint. ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="/root/nfs/codespace/llm-models/Qwen1.5-MoE-A2.7B") print(llm) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ``` (vllm) root@54f5f1ac14f8:~/nfs/codespace/SLMoE# python test_qwen.py INFO 03-27 01:24:16 [__init__.py:256] Automatically detected platform cuda. WARNING 03-27 01:24:16 [cuda.py:394] Detected different devices in the system: NVIDIA GeForce RTX 4090, NVIDIA GeForce RTX 4090, NVIDIA A100-PCIE-40GB, NVIDIA A100-PCIE-40GB, Quadro P600....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: t to run Qwen1.5-MoE-A2.7B model from load checkpoint. ``` from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "Th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: y INFO 03-27 01:24:16 [__init__.py:256] Automatically detected platform cuda. WARNING 03-27 01:24:16 [cuda.py:394] Detected different devices in the system: NVIDIA GeForce RTX 4090, NVIDIA GeForce RTX 4090, NVIDIA A100-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]:Question about load Qwen1.5-MoE-A2.7B model bug ### Your current environment ### 🐛 Describe the bug I want to run Qwen1.5-MoE-A2.7B model from load checkpoint. ``` from vllm import LLM, SamplingParams # Sample pro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
