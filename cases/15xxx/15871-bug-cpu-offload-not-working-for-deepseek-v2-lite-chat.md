# vllm-project/vllm#15871: [Bug]: CPU offload not working for DeepSeek-V2-Lite-Chat

| 字段 | 值 |
| --- | --- |
| Issue | [#15871](https://github.com/vllm-project/vllm/issues/15871) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU offload not working for DeepSeek-V2-Lite-Chat

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running this script on my machine with 32GB RAM and a 3090. My vllm is 0.8.2. I am trying to offload 15GB to CPU RAM but it crashes complaining tensors can't be on different devices. Does that mean DeepSeek-V2-Lite-Chat is not supported for CPU offloading? This is the script vc.py I ran: ``` from vllm import LLM, SamplingParams import sys # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model=sys.argv[1], trust_remote_code=True, max_model_len=32768, cpu_offload_gb=15) # Generate texts from the prompts. The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` #python3 vc.py deepseek-ai/DeepSeek-V2-Lite-Chat/ INFO 04-01 16:42:54 [__init...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: CPU offload not working for DeepSeek-V2-Lite-Chat bug;stale ### Your current environment ### 🐛 Describe the bug I am running this script on my machine with 32GB RAM and a 3090. My vllm is 0.8.2. I am trying to of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rted for CPU offloading? This is the script vc.py I ran: ``` from vllm import LLM, SamplingParams import sys # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of Fr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ne, tokenizer='/home/user/DeepSeek-V2-Lite-Chat/', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model=sys.argv[1], trust_remote_code=True, max_model_len=32768, cpu_offload_gb=15) # Generate texts from the prompts. The output is a list of Reques...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
